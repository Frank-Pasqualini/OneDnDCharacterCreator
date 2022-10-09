"""
All the information about a character.
"""

# TODO a lot of this file

import math

import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject

from rules import abilities, armors, backgrounds, bonuses, classes, feats, races
from rules.enums import AbilityNames, Alignments, Languages, Skills


class Character:
    """
    All the information about a character.
    """

    _name: str
    _player_name: str
    _alignment: Alignments
    _classes: list[classes.CharacterClass]
    _race: races.Race
    _background: backgrounds.Background
    _abilities: abilities.Abilities
    _language: Languages
    _xp: int
    _milestone: bool
    _armor: armors.Armor | None
    _shield: armors.Armor | None
    _appearance_image: str | None
    _age: str
    _height: str
    _weight: str
    _eyes: str
    _skin: str
    _hair: str
    _faction: str
    _faction_image: str | None

    def __init__(self,
                 name: str,
                 character_class: classes.CharacterClass,
                 race: races.Race,
                 background: backgrounds.Background,
                 starting_abilities: dict[AbilityNames, int],
                 alignment: Alignments,
                 language: Languages,
                 player_name: str = "",
                 milestone: bool = True,
                 armor: armors.Armor = None,
                 shield: armors.Armor = None,
                 appearance_image: str = None,
                 age: str = "",
                 height: str = "",
                 weight: str = "",
                 eyes: str = "",
                 skin: str = "",
                 hair: str = "",
                 faction: str = "",
                 faction_image: str = None):
        # TODO add some validation

        self._name = name
        self._player_name = player_name
        self._alignment = alignment

        self._classes = [character_class]
        self._race = race
        self._background = background
        self._abilities = abilities.Abilities(
            strength=starting_abilities.get(AbilityNames.STRENGTH, 0),
            dexterity=starting_abilities.get(AbilityNames.DEXTERITY, 0),
            constitution=starting_abilities.get(AbilityNames.CONSTITUTION, 0),
            intelligence=starting_abilities.get(AbilityNames.INTELLIGENCE, 0),
            wisdom=starting_abilities.get(AbilityNames.WISDOM, 0),
            charisma=starting_abilities.get(AbilityNames.CHARISMA, 0),
        )
        self._language = language

        self._xp = 0
        self._milestone = milestone

        self._armor = armor
        self._shield = shield

        self._appearance_image = appearance_image
        self._age = age
        self._height = height
        self._weight = weight
        self._eyes = eyes
        self._skin = skin
        self._hair = hair
        self._faction = faction
        self._faction_image = faction_image

    def _get_abilities(self) -> abilities.Abilities:
        return sum([feature.get_abilities() for feature in self._get_features()],
                   self._abilities + self._background.get_abilities())

    def _get_armor_class(self) -> int:
        dex_mod = self._get_abilities().get_dexterity_mod()
        return (dex_mod + 10 if self._armor is None else self._armor.get_armor_class(dex_mod)) + (
            0 if self._shield is None else self._shield.get_armor_class())

    def _get_bonuses(self) -> bonuses.Bonuses:
        class_bonuses = bonuses.Bonuses()
        class_bonuses_list = [character_class.get_bonuses()
                              for character_class in self._classes]
        for item in class_bonuses_list:
            class_bonuses += item

        return self._background.get_bonuses() + class_bonuses + bonuses.Bonuses(languages=[self._language,
                                                                                           Languages.COMMON])

    def _get_character_level(self) -> int:
        return sum(character_class.get_level() for character_class in self._classes)

    def _get_class_levels(self) -> str:
        return ", ".join([str(character_class) for character_class in self._classes])

    def _get_features(self) -> list[feats.Feat]:
        return self._race.get_features() + [self._background.get_feat()] + [
            feature for features in [character_class.get_features() for character_class in self._classes]
            for feature in features]

    def _get_max_hit_dice(self) -> str:
        return "+".join([f"{character_class.get_level()}d{character_class.get_hit_die()}" for
                         character_class in self._classes])

    def _get_max_hp(self) -> int:
        return sum(sum(character_class.get_rolled_hit_dice()) for character_class in self._classes) + (
            self._get_character_level() *
            (self._get_abilities().get_constitution_mod() + self._get_bonuses().get_hp_bonus()))

    def _get_proficiency_bonus(self) -> int:
        return math.ceil(self._get_character_level() / 4) + 1

    def _get_speed(self) -> int:
        return self._race.get_speed()

    def get_name(self) -> str:
        return self._name

    def level_up(self, character_class: int, **kwargs):
        self._classes[character_class].level_up(**kwargs)

    def write_character_sheet(self, filepath: str):
        """
        Writes out a 5e character sheet from this character
        :param filepath: The pdf file to write to
        :type filepath: str
        """

        reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
        writer = PdfWriter()

        writer.add_page(reader.pages[0])

        compiled_abilities = self._get_abilities()
        compiled_features = self._get_features()
        compiled_bonuses = self._get_bonuses()
        prof_bonus = self._get_proficiency_bonus()

        str_mod = compiled_abilities.get_strength_mod()
        dex_mod = compiled_abilities.get_dexterity_mod()
        con_mod = compiled_abilities.get_constitution_mod()
        int_mod = compiled_abilities.get_intelligence_mod()
        wis_mod = compiled_abilities.get_wisdom_mod()
        chr_mod = compiled_abilities.get_charisma_mod()

        skills = compiled_bonuses.get_skills()
        s_throws = compiled_bonuses.get_saving_throws()

        writer.update_page_form_field_values(
            writer.pages[0], {
                "AC": self._get_armor_class(),
                "Acrobatics": f"{dex_mod + (skills.get(Skills.ACROBATICS, 0) * prof_bonus):+g}",
                "Alignment": self._alignment.value,
                "Animal": f"{wis_mod + (skills.get(Skills.ANIMAL_HANDLING, 0) * prof_bonus):+g}",
                "Arcana": f"{int_mod + (skills.get(Skills.ARCANA, 0) * prof_bonus):+g}",
                "Athletics": f"{str_mod + (skills.get(Skills.ATHLETICS, 0) * prof_bonus):+g}",
                "AttacksSpellcasting": "TODO",
                "Background": self._background.get_name(),
                "Bonds": str(self._background.get_bonds()),
                "CHA": compiled_abilities.get_charisma(),
                "CHamod": f"{chr_mod:+g}",
                "CharacterName": self._name,
                "ClassLevel": self._get_class_levels(),
                "CON": compiled_abilities.get_constitution(),
                "CONmod": f"{con_mod:+g}",
                "CP": "",
                "Deception ": f"{chr_mod + (skills.get(Skills.DECEPTION, 0) * prof_bonus):+g}",
                "DEX": compiled_abilities.get_dexterity(),
                "DEXmod ": f"{dex_mod:+g}",
                "EP": "",
                "Equipment": "TODO",
                "Features and Traits": "\n\n".join(feature.summary() for feature in compiled_features),
                "Flaws": str(self._background.get_flaws()),
                "GP": "",
                "HD": "",
                "HDTotal": self._get_max_hit_dice(),
                "History ": f"{int_mod + (skills.get(Skills.HISTORY, 0) * prof_bonus):+g}",
                "HPCurrent": "",
                "HPMax": self._get_max_hp(),
                "HPTemp": "",
                "Ideals": str(self._background.get_ideals()),
                "Initiative": f"{dex_mod + (compiled_bonuses.get_initiative() * prof_bonus):+g}",
                "Insight": f"{wis_mod + (skills.get(Skills.INSIGHT, 0) * prof_bonus):+g}",
                "Inspiration": "",
                "INT": compiled_abilities.get_intelligence(),
                "INTmod": f"{int_mod:+g}",
                "Intimidation": f"{chr_mod + (skills.get(Skills.INTIMIDATION, 0) * prof_bonus):+g}",
                "Investigation ": f"{int_mod + (skills.get(Skills.INVESTIGATION, 0) * prof_bonus):+g}",
                "Medicine": f"{wis_mod + (skills.get(Skills.MEDICINE, 0) * prof_bonus):+g}",
                "Nature": f"{int_mod + (skills.get(Skills.NATURE, 0) * prof_bonus):+g}",
                "Passive": wis_mod + (skills.get(Skills.PERCEPTION, 0) * prof_bonus) + 10,
                "PersonalityTraits ": str(self._background.get_personality_traits()),
                "Perception ": f"{wis_mod + (skills.get(Skills.PERCEPTION, 0) * prof_bonus):+g}",
                "Performance": f"{chr_mod + (skills.get(Skills.PERFORMANCE, 0) * prof_bonus):+g}",
                "Persuasion": f"{chr_mod + (skills.get(Skills.PERSUASION, 0) * prof_bonus):+g}",
                "PlayerName": self._player_name,
                "PP": "",
                "ProfBonus": f"{prof_bonus:+g}",
                "ProficienciesLang": compiled_bonuses.summary(),
                "Race ": str(self._race.get_name()),
                "Religion": f"{int_mod + (skills.get(Skills.RELIGION, 0) * prof_bonus):+g}",
                "SleightofHand": f"{dex_mod + (skills.get(Skills.SLEIGHT_OF_HAND, 0) * prof_bonus):+g}",
                "SP": "",
                "Speed": str(self._get_speed()) + " ft.",
                "ST Strength": f"{str_mod + (s_throws.get(AbilityNames.STRENGTH, 0) * prof_bonus):+g}",
                "ST Dexterity": f"{dex_mod + (s_throws.get(AbilityNames.DEXTERITY, 0) * prof_bonus):+g}",
                "ST Constitution": f"{con_mod + (s_throws.get(AbilityNames.CONSTITUTION, 0) * prof_bonus):+g}",
                "ST Intelligence": f"{int_mod + (s_throws.get(AbilityNames.INTELLIGENCE, 0) * prof_bonus):+g}",
                "ST Wisdom": f"{wis_mod + (s_throws.get(AbilityNames.WISDOM, 0) * prof_bonus):+g}",
                "ST Charisma": f"{chr_mod + (s_throws.get(AbilityNames.CHARISMA, 0) * prof_bonus):+g}",
                "Stealth ": f"{dex_mod + (skills.get(Skills.STEALTH, 0) * prof_bonus):+g}",
                "STR": compiled_abilities.get_strength(),
                "STRmod": f"{str_mod:+g}",
                "Survival": f"{wis_mod + (skills.get(Skills.SURVIVAL, 0) * prof_bonus):+g}",
                "Wpn Name": "TODO",
                "Wpn Name 2": "TODO",
                "Wpn Name 3": "TODO",
                "Wpn1 AtkBonus": "TODO",
                "Wpn1 Damage": "TODO",
                "Wpn2 AtkBonus ": "TODO",
                "Wpn2 Damage ": "TODO",
                "Wpn3 AtkBonus  ": "TODO",
                "Wpn3 Damage ": "TODO",
                "WIS": compiled_abilities.get_wisdom(),
                "WISmod": f"{wis_mod:+g}",
                "XP": self._xp if not self._milestone else "N/A"
            }
        )

        checkboxes = {
            "Check Box 11": "/Yes" if s_throws.get(AbilityNames.STRENGTH, None) is not None else "/No",
            "Check Box 18": "/Yes" if s_throws.get(AbilityNames.DEXTERITY, None) is not None else "/No",
            "Check Box 19": "/Yes" if s_throws.get(AbilityNames.CONSTITUTION, None) is not None else "/No",
            "Check Box 20": "/Yes" if s_throws.get(AbilityNames.INTELLIGENCE, None) is not None else "/No",
            "Check Box 21": "/Yes" if s_throws.get(AbilityNames.WISDOM, None) is not None else "/No",
            "Check Box 22": "/Yes" if s_throws.get(AbilityNames.CHARISMA, None) is not None else "/No",
            "Check Box 23": "/Yes" if skills.get(Skills.ACROBATICS, None) is not None else "/No",
            "Check Box 24": "/Yes" if skills.get(Skills.ANIMAL_HANDLING, None) is not None else "/No",
            "Check Box 25": "/Yes" if skills.get(Skills.ARCANA, None) is not None else "/No",
            "Check Box 26": "/Yes" if skills.get(Skills.ATHLETICS, None) is not None else "/No",
            "Check Box 27": "/Yes" if skills.get(Skills.DECEPTION, None) is not None else "/No",
            "Check Box 28": "/Yes" if skills.get(Skills.HISTORY, None) is not None else "/No",
            "Check Box 29": "/Yes" if skills.get(Skills.INSIGHT, None) is not None else "/No",
            "Check Box 30": "/Yes" if skills.get(Skills.INTIMIDATION, None) is not None else "/No",
            "Check Box 31": "/Yes" if skills.get(Skills.INVESTIGATION, None) is not None else "/No",
            "Check Box 32": "/Yes" if skills.get(Skills.MEDICINE, None) is not None else "/No",
            "Check Box 33": "/Yes" if skills.get(Skills.NATURE, None) is not None else "/No",
            "Check Box 34": "/Yes" if skills.get(Skills.PERCEPTION, None) is not None else "/No",
            "Check Box 35": "/Yes" if skills.get(Skills.PERFORMANCE, None) is not None else "/No",
            "Check Box 36": "/Yes" if skills.get(Skills.PERSUASION, None) is not None else "/No",
            "Check Box 37": "/Yes" if skills.get(Skills.RELIGION, None) is not None else "/No",
            "Check Box 38": "/Yes" if skills.get(Skills.SLEIGHT_OF_HAND, None) is not None else "/No",
            "Check Box 39": "/Yes" if skills.get(Skills.STEALTH, None) is not None else "/No",
            "Check Box 40": "/Yes" if skills.get(Skills.SURVIVAL, None) is not None else "/No",
            "Check Box 12": "/No",
            "Check Box 13": "/No",
            "Check Box 14": "/No",
            "Check Box 15": "/No",
            "Check Box 16": "/No",
            "Check Box 17": "/No",
        }

        # noinspection PyTypeChecker
        for j in range(0, len(writer.pages[0]["/Annots"])):
            writer_annot = writer.pages[0]["/Annots"][j].getObject()
            for checkbox, value in checkboxes.items():
                if writer_annot.get("/T") == checkbox:
                    writer_annot.update({
                        NameObject("/V"): NameObject(value),
                        NameObject("/AS"): NameObject(value)
                    })

        writer.add_page(reader.pages[1])

        writer.update_page_form_field_values(
            writer.pages[1], {
                "Age": self._age,
                "Allies": "TODO",
                "Backstory": self._background.get_description(),
                "CharacterName 2": self._name,
                "Eyes": self._eyes,
                "FactionName": self._faction,
                "Feat+Traits": "TODO",
                "Hair": self._hair,
                "Height": self._height,
                "Skin": self._skin,
                "Treasure": "TODO",
                "Weight": self._weight,
            }
        )

        appearance_file = None
        if self._appearance_image is not None:
            # pylint: disable-next=consider-using-with
            appearance_file = open(self._appearance_image, "rb")
            image = PyPDF2.PdfFileReader(appearance_file)
            # pylint: disable-next=no-member
            writer.pages[1].mergeScaledTranslatedPage(
                image.getPage(0), scale=0.235, tx=47, ty=480)

        faction_file = None
        if self._faction_image is not None:
            # pylint: disable-next=consider-using-with
            faction_file = open(self._faction_image, "rb")
            image = PyPDF2.PdfFileReader(faction_file)
            # pylint: disable-next=no-member
            writer.pages[1].mergeScaledTranslatedPage(
                image.getPage(0), scale=0.137, tx=435, ty=530)

        writer.write(filepath)

        if appearance_file is not None:
            appearance_file.close()

        if faction_file is not None:
            faction_file.close()
