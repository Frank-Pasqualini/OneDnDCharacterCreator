import math

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject

from rules import Abilities, Backgrounds, Bonuses, CharacterClasses, Feats, Races
from rules.Enums import AbilityNames, Alignments, Languages, Skills


class Character:
    _name: str
    _player_name: str
    _alignment: Alignments
    _classes: list[CharacterClasses.CharacterClass]
    _race: Races.Race
    _background: Backgrounds.Background
    _abilities: Abilities.Abilities
    _language: Languages
    _xp: int
    _milestone: bool
    _inventory: any

    def __init__(self,
                 name: str,
                 character_class: CharacterClasses.CharacterClass,
                 race: Races.Race,
                 background: Backgrounds.Background,
                 abilities: Abilities.Abilities,
                 alignment: Alignments,
                 language: Languages,
                 player_name: str = "",
                 milestone: bool = True):
        self._name = name
        self._player_name = player_name
        self._alignment = alignment

        self._classes = [character_class]
        self._race = race
        self._background = background
        self._abilities = abilities
        self._language = language

        self._xp = 0
        self._milestone = milestone

        self._inventory = {}

    def get_abilities(self) -> Abilities.Abilities:
        return sum([feature.get_abilities() for feature in self.get_features()],
                   self._abilities + self._background.get_abilities())

    def get_armor_class(self) -> int:
        return 10

    def get_bonuses(self) -> Bonuses.Bonuses:
        return self._background.get_bonuses()

    def get_character_level(self) -> int:
        return sum([character_class.level for character_class in self._classes])

    def get_class_levels(self) -> str:
        return ", ".join([str(character_class) for character_class in self._classes])

    def get_features(self) -> list[Feats.Feat]:
        return self._race.get_features() + \
               [self._background.get_feat()] + \
               [feature for features in [character_class.features for character_class in self._classes]
                for feature in features]

    def get_max_hit_dice(self) -> str:
        return "1d8"  # TODO

    def get_max_hp(self) -> int:
        return 8  # TODO

    def get_name(self) -> str:
        return self._name

    def get_proficiency_bonus(self) -> int:
        return math.ceil(self.get_character_level() / 4) + 1

    def get_speed(self) -> int:
        return self._race.get_speed()

    def write_character_sheet(self, filepath):
        reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
        writer = PdfWriter()

        writer.add_page(reader.pages[0])

        abilities = self.get_abilities()
        features = self.get_features()
        bonuses = self.get_bonuses()
        prof_bonus = self.get_proficiency_bonus()

        str_mod = abilities.get_strength_mod()
        dex_mod = abilities.get_dexterity_mod()
        con_mod = abilities.get_constitution_mod()
        int_mod = abilities.get_intelligence_mod()
        wis_mod = abilities.get_wisdom_mod()
        chr_mod = abilities.get_charisma_mod()

        skills = bonuses.get_skills()
        s_throws = bonuses.get_saving_throws()

        writer.update_page_form_field_values(
            writer.pages[0], {
                "AC": self.get_armor_class(),
                "Acrobatics": f"{dex_mod + (skills.get(Skills.ACROBATICS, 0) * prof_bonus):+g}",
                "Alignment": self._alignment.value,
                "Animal": f"{wis_mod + (skills.get(Skills.ANIMAL_HANDLING, 0) * prof_bonus):+g}",
                "Arcana": f"{int_mod + (skills.get(Skills.ARCANA, 0) * prof_bonus):+g}",
                "Athletics": f"{str_mod + (skills.get(Skills.ATHLETICS, 0) * prof_bonus):+g}",
                "AttacksSpellcasting": "",
                "Background": self._background.get_name(),
                "Bonds": str(self._background.get_bonds()),
                "CHA": abilities.get_charisma(),
                "CHamod": f"{chr_mod:+g}",
                "CharacterName": self._name,
                "ClassLevel": self.get_class_levels(),
                "CON": abilities.get_constitution(),
                "CONmod": f"{con_mod:+g}",
                "CP": "",
                "Deception ": f"{chr_mod + (skills.get(Skills.DECEPTION, 0) * prof_bonus):+g}",
                "DEX": abilities.get_dexterity(),
                "DEXmod ": f"{dex_mod:+g}",
                "EP": "",
                "Equipment": "TODO",
                "Features and Traits": "\n\n".join(feature.summary() for feature in features),
                "Flaws": str(self._background.get_flaws()),
                "GP": "",
                "HD": "",
                "HDTotal": self.get_max_hit_dice(),
                "History ": f"{int_mod + (skills.get(Skills.HISTORY, 0) * prof_bonus):+g}",
                "HPCurrent": "",
                "HPMax": self.get_max_hp(),
                "HPTemp": "",
                "Ideals": str(self._background.get_ideals()),
                "Initiative": f"{dex_mod + (bonuses.get_initiative() * prof_bonus):+g}",
                "Insight": f"{wis_mod + (skills.get(Skills.INSIGHT, 0) * prof_bonus):+g}",
                "Inspiration": "",
                "INT": abilities.get_intelligence(),
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
                "ProficienciesLang": bonuses.summary(),
                "Race ": str(self._race.get_name()),
                "Religion": f"{int_mod + (skills.get(Skills.RELIGION, 0) * prof_bonus):+g}",
                "SleightofHand": f"{dex_mod + (skills.get(Skills.SLEIGHT_OF_HAND, 0) * prof_bonus):+g}",
                "SP": "",
                "Speed": str(self.get_speed()) + " ft.",
                "ST Strength": f"{str_mod + (s_throws.get(AbilityNames.STRENGTH, 0) * prof_bonus):+g}",
                "ST Dexterity": f"{dex_mod + (s_throws.get(AbilityNames.DEXTERITY, 0) * prof_bonus):+g}",
                "ST Constitution": f"{con_mod + (s_throws.get(AbilityNames.CONSTITUTION, 0) * prof_bonus):+g}",
                "ST Intelligence": f"{int_mod + (s_throws.get(AbilityNames.INTELLIGENCE, 0) * prof_bonus):+g}",
                "ST Wisdom": f"{wis_mod + (s_throws.get(AbilityNames.WISDOM, 0) * prof_bonus):+g}",
                "ST Charisma": f"{chr_mod + (s_throws.get(AbilityNames.CHARISMA, 0) * prof_bonus):+g}",
                "Stealth ": f"{dex_mod + (skills.get(Skills.STEALTH, 0) * prof_bonus):+g}",
                "STR": abilities.get_strength(),
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
                "WIS": abilities.get_wisdom(),
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

        for j in range(0, len(writer.pages[0]['/Annots'])):
            writer_annot = writer.pages[0]['/Annots'][j].getObject()
            for checkbox in checkboxes:
                if writer_annot.get('/T') == checkbox:
                    writer_annot.update({
                        NameObject("/V"): NameObject(checkboxes[checkbox]),
                        NameObject("/AS"): NameObject(checkboxes[checkbox])
                    })

        writer.add_page(reader.pages[1])

        writer.update_page_form_field_values(
            writer.pages[0], {
                "CharacterName 2": self._name,
            }
        )

        writer.write(filepath)
