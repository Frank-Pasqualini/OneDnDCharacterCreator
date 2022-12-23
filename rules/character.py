"""
All the information about a character.
"""
import logging
import math
from typing import Tuple

import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject

from rules import abilities, armors, backgrounds, bonuses, classes, feats, magicitem, species, spells, weapons
from rules.common import validate_string, mod, WIDTHS
from rules.enums import AbilityNames, Alignments, ArmorTraining, Languages, Skills


class Character:
    """
    All the information about a character.
    """

    _name: str
    _player_name: str
    _alignment: Alignments
    _classes: list[classes.CharacterClass]
    _species: species.Species
    _background: backgrounds.Background
    _abilities: abilities.Abilities
    _language: Languages
    _xp: int
    _milestone: bool
    _weapons: list[weapons.Weapon]
    _magic_items: list[magicitem.MagicItem]
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
    _allies: str

    def __init__(self,
                 name: str,
                 character_class: classes.CharacterClass,
                 character_species: species.Species,
                 background: backgrounds.Background,
                 starting_abilities: dict[AbilityNames, int],
                 alignment: Alignments,
                 language: Languages,
                 player_name: str = "",
                 milestone: bool = True,
                 appearance_image: str = None,
                 age: str = "",
                 height: str = "",
                 weight: str = "",
                 eyes: str = "",
                 skin: str = "",
                 hair: str = "",
                 faction: str = "",
                 faction_image: str = None,
                 allies: str = ""):
        self._name = validate_string(name)
        self._player_name = player_name
        self._alignment = alignment

        self._classes = [character_class]
        self._species = character_species
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

        self._weapons = []
        self._magic_items = []
        self._armor = None
        self._shield = None

        self._appearance_image = appearance_image
        self._faction_image = faction_image

        self._age = age
        self._height = height
        self._weight = weight
        self._eyes = eyes
        self._skin = skin
        self._hair = hair
        self._faction = faction
        self._allies = allies

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

        feat_bonuses = bonuses.Bonuses()
        feat_bonuses_list = [feat.get_bonuses()
                             for feat in self._get_features()]
        for item in feat_bonuses_list:
            feat_bonuses += item

        return self._background.get_bonuses() + class_bonuses + feat_bonuses + bonuses.Bonuses(
            languages=[self._language, Languages.COMMON])

    def _get_character_level(self) -> int:
        return sum(character_class.get_level() for character_class in self._classes)

    def _get_class_levels(self) -> str:
        return ", ".join([str(character_class) for character_class in self._classes])

    def _get_features(self) -> list[feats.Feat]:
        return self._species.get_features() + [self._background.get_feat()] + [
            feature for features in [character_class.get_features() for character_class in self._classes]
            for feature in features]

    def _get_features_and_traits(self) -> Tuple[str, str]:
        compiled_features = self._get_features()

        feats_and_traits_1 = ""
        feats_and_traits_1_width = 0.0
        feats_and_traits_2 = ""

        for feature in compiled_features:
            if feature.summary() is not None:
                summary = feature.summary() + "\n\n"
                size = 0.0

                for char in summary:
                    size += WIDTHS[char]

                if feats_and_traits_2 == "" and feats_and_traits_1_width + size < 50000:
                    feats_and_traits_1 += summary
                    feats_and_traits_1_width += size
                else:
                    feats_and_traits_2 += summary

        return feats_and_traits_1, feats_and_traits_2  # TODO even more overflow

    def _get_known_spells(self, content: dict[str, dict[str, any]], ) -> list[spells.Spell]:
        spell_list = []
        for character_class in self._classes:
            spell_list += character_class.get_known_spells(content)

        return sorted(spell_list)

    def _get_max_hit_dice(self) -> str:
        return "+".join([f"{character_class.get_level()}d{character_class.get_hit_die()}" for
                         character_class in self._classes])

    def _get_max_hp(self) -> int:
        return sum(sum(character_class.get_rolled_hit_dice()) for character_class in self._classes
                   ) + (self._get_character_level() * (self._get_abilities().get_constitution_mod() +
                                                       self._get_bonuses().get_hp_bonus()))

    def _get_prepared_spells(self) -> list[spells.Spell]:
        spell_list = []
        for feat in self._get_features():
            spell_list += feat.get_spells()

        return sorted(spell_list)

    def _get_proficiency_bonus(self) -> int:
        return math.ceil(self._get_character_level() / 4) + 1

    def _get_speed(self) -> int:
        return self._species.get_speed()

    def _get_spell_slots(self) -> list[int]:
        spellcasting_level = math.ceil(
            sum(character_class.get_spellcasting_level() for character_class in self._classes))

        slots = {
            0: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            9: [4, 3, 3, 3, 1, 0, 0, 0, 0],
            10: [4, 3, 3, 3, 2, 0, 0, 0, 0],
            11: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            12: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            13: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            14: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            15: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            16: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
            18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
            19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
            20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
        }

        return slots[spellcasting_level]

    def _get_spellcasting_class(self) -> str:
        return ", ".join(character_class.get_spellcasting_class() for character_class in self._classes if
                         character_class.get_spellcasting_class() is not None)

    def _get_spellcasting_ability(self) -> AbilityNames | None:
        spellcasting_abilities = [character_class.get_spellcasting_ability() for character_class in self._classes if
                                  character_class.get_spellcasting_ability() is not None
                                  ] + [feat.get_spellcasting_ability() for feat in self._get_features() if
                                       feat.get_spellcasting_ability() is not None]
        if len(set(spellcasting_abilities)) != 1:
            logging.warning("Multiple spellcasting abilities detected")
        return spellcasting_abilities[0] if len(spellcasting_abilities) > 0 else None

    def _get_spellcasting_mod(self) -> int:
        ability_scores = self._get_abilities()
        ability = self._get_spellcasting_ability()
        return ability_scores.get_intelligence_mod() if ability == AbilityNames.INTELLIGENCE else (
            ability_scores.get_wisdom_mod() if ability == AbilityNames.WISDOM else (
                ability_scores.get_charisma_mod() if ability == AbilityNames.CHARISMA else 0))

    def get_name(self) -> str:
        return self._name

    def set_armor(self, armor: armors.Armor | None):
        if armor.get_type() == ArmorTraining.SHIELD:
            raise Exception("That is not armor")
        self._armor = armor

    def set_shield(self, shield: armors.Armor | None):
        if shield.get_type() != ArmorTraining.SHIELD:
            raise Exception("That is not a shield")
        self._shield = shield

    def set_magic_items(self, magic_items: list[magicitem.MagicItem]):
        self._magic_items = magic_items

    def set_weapons(self, equipped_weapons: list[weapons.Weapon]):
        self._weapons = equipped_weapons

    def level_up(self, character_class: int, **kwargs):
        self._classes[character_class].level_up(**kwargs)

    def write_character_sheet(self, content: dict[str, dict[str, any]], filepath: str):
        """
        Writes out a 5e character sheet from this character
        :param content: The content dictionary
        :type content: dict[str, dict[str, any]]
        :param filepath: The pdf file to write to
        :type filepath: str
        """

        reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
        writer = PdfWriter()

        writer.add_page(reader.pages[0])

        compiled_abilities = self._get_abilities()
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

        f_and_t_1, f_and_t_2 = self._get_features_and_traits()

        writer.update_page_form_field_values(
            writer.pages[0], {
                "AC": self._get_armor_class(),
                "Acrobatics": mod(dex_mod + (skills.get(Skills.ACROBATICS, 0) * prof_bonus)),
                "Alignment": self._alignment.value,
                "Animal": mod(wis_mod + (skills.get(Skills.ANIMAL_HANDLING, 0) * prof_bonus)),
                "Arcana": mod(int_mod + (skills.get(Skills.ARCANA, 0) * prof_bonus)),
                "Athletics": mod(str_mod + (skills.get(Skills.ATHLETICS, 0) * prof_bonus)),
                "AttacksSpellcasting": "\n\n".join(
                    [f"{index + 1}:  {weapon.summary()}" for index, weapon in enumerate(self._weapons)]),
                "Background": self._background.get_name(),
                "Bonds": str(self._background.get_bonds()),
                "CHA": compiled_abilities.get_charisma(),
                "CHamod": mod(chr_mod),
                "CharacterName": self._name,
                "ClassLevel": self._get_class_levels(),
                "CON": compiled_abilities.get_constitution(),
                "CONmod": mod(con_mod),
                "CP": "",
                "Deception ": mod(chr_mod + (skills.get(Skills.DECEPTION, 0) * prof_bonus)),
                "DEX": compiled_abilities.get_dexterity(),
                "DEXmod ": mod(dex_mod),
                "EP": "",
                "Equipment": "\n".join([self._armor.get_name() if self._armor is not None else ""] + [
                    self._shield.get_name() if self._shield is not None else ""]),
                "Features and Traits": f_and_t_1,
                "Flaws": str(self._background.get_flaws()),
                "GP": "",
                "HD": "",
                "HDTotal": self._get_max_hit_dice(),
                "History ": mod(int_mod + (skills.get(Skills.HISTORY, 0) * prof_bonus)),
                "HPCurrent": "",
                "HPMax": self._get_max_hp(),
                "HPTemp": "",
                "Ideals": str(self._background.get_ideals()),
                "Initiative": mod(dex_mod + (compiled_bonuses.get_initiative() * prof_bonus)),
                "Insight": mod(wis_mod + (skills.get(Skills.INSIGHT, 0) * prof_bonus)),
                "Inspiration": "",
                "INT": compiled_abilities.get_intelligence(),
                "INTmod": mod(int_mod),
                "Intimidation": mod(chr_mod + (skills.get(Skills.INTIMIDATION, 0) * prof_bonus)),
                "Investigation ": mod(int_mod + (skills.get(Skills.INVESTIGATION, 0) * prof_bonus)),
                "Medicine": mod(wis_mod + (skills.get(Skills.MEDICINE, 0) * prof_bonus)),
                "Nature": mod(int_mod + (skills.get(Skills.NATURE, 0) * prof_bonus)),
                "Passive": wis_mod + (skills.get(Skills.PERCEPTION, 0) * prof_bonus) + 10,
                "PersonalityTraits ": str(self._background.get_personality_traits()),
                "Perception ": mod(wis_mod + (skills.get(Skills.PERCEPTION, 0) * prof_bonus)),
                "Performance": mod(chr_mod + (skills.get(Skills.PERFORMANCE, 0) * prof_bonus)),
                "Persuasion": mod(chr_mod + (skills.get(Skills.PERSUASION, 0) * prof_bonus)),
                "PlayerName": self._player_name,
                "PP": "",
                "ProfBonus": mod(prof_bonus),
                "ProficienciesLang": compiled_bonuses.summary(),
                "Race ": str(self._species.get_name()),
                "Religion": mod(int_mod + (skills.get(Skills.RELIGION, 0) * prof_bonus)),
                "SleightofHand": mod(dex_mod + (skills.get(Skills.SLEIGHT_OF_HAND, 0) * prof_bonus)),
                "SP": "",
                "Speed": str(self._get_speed()) + " ft.",
                "ST Strength": mod(str_mod + (s_throws.get(AbilityNames.STRENGTH, 0) * prof_bonus)),
                "ST Dexterity": mod(dex_mod + (s_throws.get(AbilityNames.DEXTERITY, 0) * prof_bonus)),
                "ST Constitution": mod(con_mod + (s_throws.get(AbilityNames.CONSTITUTION, 0) * prof_bonus)),
                "ST Intelligence": mod(int_mod + (s_throws.get(AbilityNames.INTELLIGENCE, 0) * prof_bonus)),
                "ST Wisdom": mod(wis_mod + (s_throws.get(AbilityNames.WISDOM, 0) * prof_bonus)),
                "ST Charisma": mod(chr_mod + (s_throws.get(AbilityNames.CHARISMA, 0) * prof_bonus)),
                "Stealth ": mod(dex_mod + (skills.get(Skills.STEALTH, 0) * prof_bonus)),
                "STR": compiled_abilities.get_strength(),
                "STRmod": mod(str_mod),
                "Survival": mod(wis_mod + (skills.get(Skills.SURVIVAL, 0) * prof_bonus)),
                "Wpn Name": "Weapon 1" if len(self._weapons) >= 1 else "",
                "Wpn Name 2": "Weapon 2" if len(self._weapons) >= 2 else "",
                "Wpn Name 3": "Weapon 3" if len(self._weapons) >= 3 else "",
                "Wpn1 AtkBonus": mod(self._weapons[0].get_attack_bonus(
                    str_mod, dex_mod, prof_bonus, compiled_bonuses.get_weapon_types())) if len(
                    self._weapons) >= 1 else "",
                "Wpn1 Damage": self._weapons[0].get_damage(str_mod, dex_mod) if len(self._weapons) >= 1 else "",
                "Wpn2 AtkBonus ": mod(self._weapons[1].get_attack_bonus(
                    str_mod, dex_mod, prof_bonus, compiled_bonuses.get_weapon_types())) if len(
                    self._weapons) >= 2 else "",
                "Wpn2 Damage ": self._weapons[1].get_damage(str_mod, dex_mod) if len(self._weapons) >= 2 else "",
                "Wpn3 AtkBonus  ": mod(self._weapons[2].get_attack_bonus(
                    str_mod, dex_mod, prof_bonus, compiled_bonuses.get_weapon_types())) if len(
                    self._weapons) >= 3 else "",
                "Wpn3 Damage ": self._weapons[2].get_damage(str_mod, dex_mod) if len(self._weapons) >= 3 else "",
                "WIS": compiled_abilities.get_wisdom(),
                "WISmod": mod(wis_mod),
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
                "Allies": self._allies,
                "Backstory": self._background.get_description(),
                "CharacterName 2": self._name,
                "Eyes": self._eyes,
                "FactionName": self._faction,
                "Feat+Traits": f_and_t_2,
                "Hair": self._hair,
                "Height": self._height,
                "Skin": self._skin,
                "Treasure": "\n\n".join(str(magic_item) for magic_item in self._magic_items),
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

        prepared_spells = self._get_prepared_spells()
        known_spells = self._get_known_spells(content)
        all_spells = prepared_spells + sorted(
            list(set(known_spells) - set(prepared_spells)))
        if len(all_spells) > 0:
            writer.add_page(reader.pages[2])
            cantrips = [spell
                        for spell in all_spells if spell.get_level() == 0]
            first_level = [spell
                           for spell in all_spells if spell.get_level() == 1]
            second_level = [spell
                            for spell in all_spells if spell.get_level() == 2]
            third_level = [spell
                           for spell in all_spells if spell.get_level() == 3]
            fourth_level = [spell
                            for spell in all_spells if spell.get_level() == 4]
            fifth_level = [spell
                           for spell in all_spells if spell.get_level() == 5]
            sixth_level = [spell
                           for spell in all_spells if spell.get_level() == 6]
            seventh_level = [spell
                             for spell in all_spells if spell.get_level() == 7]
            eighth_level = [spell
                            for spell in all_spells if spell.get_level() == 8]
            ninth_level = [spell
                           for spell in all_spells if spell.get_level() == 9]

            def process_spells(sublist: list[spells.Spell | None], rows: int, prepared_count: int, cantrip=False):
                while len(sublist) % rows != 0:
                    sublist.append(None)

                columns = len(sublist) // rows

                processed = [""] * rows
                for i in range(rows):
                    for ii in range(columns):
                        spell = sublist[ii * rows + i]
                        if spell is not None and (ii != 0 or cantrip):
                            if prepared_count > ii * rows + i:
                                processed[i] += "● "
                            else:
                                processed[i] += "○ "
                        max_width = max(spells.calculate_spell_name_width(spell)
                                        for spell in sublist[ii * rows:ii * rows + rows])
                        item_width = spells.calculate_spell_name_width(spell)
                        space_width = 4.4453125
                        processed[i] += str(spell.summary() if spell is not None else ""
                                            ) + (" " * int((max_width - item_width) / space_width)) + " "

                return processed

            prepared_cantrips = len(
                [spell for spell in prepared_spells if spell.get_level() == 0])
            prepared_first = len(
                [spell for spell in prepared_spells if spell.get_level() == 1])
            prepared_second = len(
                [spell for spell in prepared_spells if spell.get_level() == 2])
            prepared_third = len(
                [spell for spell in prepared_spells if spell.get_level() == 3])
            prepared_fourth = len(
                [spell for spell in prepared_spells if spell.get_level() == 4])
            prepared_fifth = len(
                [spell for spell in prepared_spells if spell.get_level() == 5])
            prepared_sixth = len(
                [spell for spell in prepared_spells if spell.get_level() == 6])
            prepared_seventh = len(
                [spell for spell in prepared_spells if spell.get_level() == 7])
            prepared_eighth = len(
                [spell for spell in prepared_spells if spell.get_level() == 8])
            prepared_ninth = len(
                [spell for spell in prepared_spells if spell.get_level() == 9])

            cantrip_names = process_spells(
                cantrips, 8, prepared_cantrips, True)
            first_level_names = process_spells(first_level, 12, prepared_first)
            second_level_names = process_spells(
                second_level, 13, prepared_second)
            third_level_names = process_spells(third_level, 13, prepared_third)
            fourth_level_names = process_spells(
                fourth_level, 13, prepared_fourth)
            fifth_level_names = process_spells(fifth_level, 9, prepared_fifth)
            sixth_level_names = process_spells(sixth_level, 9, prepared_sixth)
            seventh_level_names = process_spells(
                seventh_level, 9, prepared_seventh)
            eighth_level_names = process_spells(
                eighth_level, 7, prepared_eighth)
            ninth_level_names = process_spells(ninth_level, 7, prepared_ninth)

            spell_slots = self._get_spell_slots()

            writer.update_page_form_field_values(
                writer.pages[2], {
                    "Spellcasting Class 2": self._get_spellcasting_class(),
                    "SpellcastingAbility 2": self._get_spellcasting_ability().value if
                    (self._get_spellcasting_ability() is not None) else "",
                    "SpellSaveDC  2": 8 + self._get_spellcasting_mod() + prof_bonus,
                    "SpellAtkBonus 2": mod(self._get_spellcasting_mod() + prof_bonus),
                    "SlotsTotal 19": spell_slots[0],
                    "SlotsTotal 20": spell_slots[1],
                    "SlotsTotal 21": spell_slots[2],
                    "SlotsTotal 22": spell_slots[3],
                    "SlotsTotal 23": spell_slots[4],
                    "SlotsTotal 24": spell_slots[5],
                    "SlotsTotal 25": spell_slots[6],
                    "SlotsTotal 26": spell_slots[7],
                    "SlotsTotal 27": spell_slots[8],
                    "SlotsRemaining 19": "",
                    "SlotsRemaining 20": "",
                    "SlotsRemaining 21": "",
                    "SlotsRemaining 22": "",
                    "SlotsRemaining 23": "",
                    "SlotsRemaining 24": "",
                    "SlotsRemaining 25": "",
                    "SlotsRemaining 26": "",
                    "SlotsRemaining 27": "",
                    "Spells 1014": cantrip_names[0],
                    "Spells 1016": cantrip_names[1],
                    "Spells 1017": cantrip_names[2],
                    "Spells 1018": cantrip_names[3],
                    "Spells 1019": cantrip_names[4],
                    "Spells 1020": cantrip_names[5],
                    "Spells 1021": cantrip_names[6],
                    "Spells 1022": cantrip_names[7],
                    "Spells 1015": first_level_names[0],
                    "Spells 1023": first_level_names[1],
                    "Spells 1024": first_level_names[2],
                    "Spells 1025": first_level_names[3],
                    "Spells 1026": first_level_names[4],
                    "Spells 1027": first_level_names[5],
                    "Spells 1028": first_level_names[6],
                    "Spells 1029": first_level_names[7],
                    "Spells 1030": first_level_names[8],
                    "Spells 1031": first_level_names[9],
                    "Spells 1032": first_level_names[10],
                    "Spells 1033": first_level_names[11],
                    "Spells 1046": second_level_names[0],
                    "Spells 1034": second_level_names[1],
                    "Spells 1035": second_level_names[2],
                    "Spells 1036": second_level_names[3],
                    "Spells 1037": second_level_names[4],
                    "Spells 1038": second_level_names[5],
                    "Spells 1039": second_level_names[6],
                    "Spells 1040": second_level_names[7],
                    "Spells 1041": second_level_names[8],
                    "Spells 1042": second_level_names[9],
                    "Spells 1043": second_level_names[10],
                    "Spells 1044": second_level_names[11],
                    "Spells 1045": second_level_names[12],
                    "Spells 1048": third_level_names[0],
                    "Spells 1047": third_level_names[1],
                    "Spells 1049": third_level_names[2],
                    "Spells 1050": third_level_names[3],
                    "Spells 1051": third_level_names[4],
                    "Spells 1052": third_level_names[5],
                    "Spells 1053": third_level_names[6],
                    "Spells 1054": third_level_names[7],
                    "Spells 1055": third_level_names[8],
                    "Spells 1056": third_level_names[9],
                    "Spells 1057": third_level_names[10],
                    "Spells 1058": third_level_names[11],
                    "Spells 1059": third_level_names[12],
                    "Spells 1061": fourth_level_names[0],
                    "Spells 1060": fourth_level_names[1],
                    "Spells 1062": fourth_level_names[2],
                    "Spells 1063": fourth_level_names[3],
                    "Spells 1064": fourth_level_names[4],
                    "Spells 1065": fourth_level_names[5],
                    "Spells 1066": fourth_level_names[6],
                    "Spells 1067": fourth_level_names[7],
                    "Spells 1068": fourth_level_names[8],
                    "Spells 1069": fourth_level_names[9],
                    "Spells 1070": fourth_level_names[10],
                    "Spells 1071": fourth_level_names[11],
                    "Spells 1072": fourth_level_names[12],
                    "Spells 1074": fifth_level_names[0],
                    "Spells 1073": fifth_level_names[1],
                    "Spells 1075": fifth_level_names[2],
                    "Spells 1076": fifth_level_names[3],
                    "Spells 1077": fifth_level_names[4],
                    "Spells 1078": fifth_level_names[5],
                    "Spells 1079": fifth_level_names[6],
                    "Spells 1080": fifth_level_names[7],
                    "Spells 1081": fifth_level_names[8],
                    "Spells 1083": sixth_level_names[0],
                    "Spells 1082": sixth_level_names[1],
                    "Spells 1084": sixth_level_names[2],
                    "Spells 1085": sixth_level_names[3],
                    "Spells 1086": sixth_level_names[4],
                    "Spells 1087": sixth_level_names[5],
                    "Spells 1088": sixth_level_names[6],
                    "Spells 1089": sixth_level_names[7],
                    "Spells 1090": sixth_level_names[8],
                    "Spells 1092": seventh_level_names[0],
                    "Spells 1091": seventh_level_names[1],
                    "Spells 1093": seventh_level_names[2],
                    "Spells 1094": seventh_level_names[3],
                    "Spells 1095": seventh_level_names[4],
                    "Spells 1096": seventh_level_names[5],
                    "Spells 1097": seventh_level_names[6],
                    "Spells 1098": seventh_level_names[7],
                    "Spells 1099": seventh_level_names[8],
                    "Spells 10101": eighth_level_names[0],
                    "Spells 10100": eighth_level_names[1],
                    "Spells 10102": eighth_level_names[2],
                    "Spells 10103": eighth_level_names[3],
                    "Spells 10104": eighth_level_names[4],
                    "Spells 10105": eighth_level_names[5],
                    "Spells 10106": eighth_level_names[6],
                    "Spells 10108": ninth_level_names[0],
                    "Spells 10107": ninth_level_names[1],
                    "Spells 10109": ninth_level_names[2],
                    "Spells 101010": ninth_level_names[3],
                    "Spells 101011": ninth_level_names[4],
                    "Spells 101012": ninth_level_names[5],
                    "Spells 101013": ninth_level_names[6],
                }
            )

            checkboxes = {
                "Check Box 251": "/Yes" if prepared_first > 0 else "/No",
                "Check Box 309": "/Yes" if prepared_first > 1 else "/No",
                "Check Box 3010": "/Yes" if prepared_first > 2 else "/No",
                "Check Box 3011": "/Yes" if prepared_first > 3 else "/No",
                "Check Box 3012": "/Yes" if prepared_first > 4 else "/No",
                "Check Box 3013": "/Yes" if prepared_first > 5 else "/No",
                "Check Box 3014": "/Yes" if prepared_first > 6 else "/No",
                "Check Box 3015": "/Yes" if prepared_first > 7 else "/No",
                "Check Box 3016": "/Yes" if prepared_first > 8 else "/No",
                "Check Box 3017": "/Yes" if prepared_first > 9 else "/No",
                "Check Box 3018": "/Yes" if prepared_first > 10 else "/No",
                "Check Box 3019": "/Yes" if prepared_first > 11 else "/No",
                "Check Box 313": "/Yes" if prepared_second > 0 else "/No",
                "Check Box 310": "/Yes" if prepared_second > 1 else "/No",
                "Check Box 3020": "/Yes" if prepared_second > 2 else "/No",
                "Check Box 3021": "/Yes" if prepared_second > 3 else "/No",
                "Check Box 3022": "/Yes" if prepared_second > 4 else "/No",
                "Check Box 3023": "/Yes" if prepared_second > 5 else "/No",
                "Check Box 3024": "/Yes" if prepared_second > 6 else "/No",
                "Check Box 3025": "/Yes" if prepared_second > 7 else "/No",
                "Check Box 3026": "/Yes" if prepared_second > 8 else "/No",
                "Check Box 3027": "/Yes" if prepared_second > 9 else "/No",
                "Check Box 3028": "/Yes" if prepared_second > 10 else "/No",
                "Check Box 3029": "/Yes" if prepared_second > 11 else "/No",
                "Check Box 3030": "/Yes" if prepared_second > 12 else "/No",
                "Check Box 315": "/Yes" if prepared_third > 0 else "/No",
                "Check Box 314": "/Yes" if prepared_third > 1 else "/No",
                "Check Box 3031": "/Yes" if prepared_third > 2 else "/No",
                "Check Box 3032": "/Yes" if prepared_third > 3 else "/No",
                "Check Box 3033": "/Yes" if prepared_third > 4 else "/No",
                "Check Box 3034": "/Yes" if prepared_third > 5 else "/No",
                "Check Box 3035": "/Yes" if prepared_third > 6 else "/No",
                "Check Box 3036": "/Yes" if prepared_third > 7 else "/No",
                "Check Box 3037": "/Yes" if prepared_third > 8 else "/No",
                "Check Box 3038": "/Yes" if prepared_third > 9 else "/No",
                "Check Box 3039": "/Yes" if prepared_third > 10 else "/No",
                "Check Box 3040": "/Yes" if prepared_third > 11 else "/No",
                "Check Box 3041": "/Yes" if prepared_third > 12 else "/No",
                "Check Box 317": "/Yes" if prepared_fourth > 0 else "/No",
                "Check Box 316": "/Yes" if prepared_fourth > 1 else "/No",
                "Check Box 3042": "/Yes" if prepared_fourth > 2 else "/No",
                "Check Box 3043": "/Yes" if prepared_fourth > 3 else "/No",
                "Check Box 3044": "/Yes" if prepared_fourth > 4 else "/No",
                "Check Box 3045": "/Yes" if prepared_fourth > 5 else "/No",
                "Check Box 3046": "/Yes" if prepared_fourth > 6 else "/No",
                "Check Box 3047": "/Yes" if prepared_fourth > 7 else "/No",
                "Check Box 3048": "/Yes" if prepared_fourth > 8 else "/No",
                "Check Box 3049": "/Yes" if prepared_fourth > 9 else "/No",
                "Check Box 3050": "/Yes" if prepared_fourth > 10 else "/No",
                "Check Box 3051": "/Yes" if prepared_fourth > 11 else "/No",
                "Check Box 3052": "/Yes" if prepared_fourth > 12 else "/No",
                "Check Box 319": "/Yes" if prepared_fifth > 0 else "/No",
                "Check Box 318": "/Yes" if prepared_fifth > 1 else "/No",
                "Check Box 3053": "/Yes" if prepared_fifth > 2 else "/No",
                "Check Box 3054": "/Yes" if prepared_fifth > 3 else "/No",
                "Check Box 3055": "/Yes" if prepared_fifth > 4 else "/No",
                "Check Box 3056": "/Yes" if prepared_fifth > 5 else "/No",
                "Check Box 3057": "/Yes" if prepared_fifth > 6 else "/No",
                "Check Box 3058": "/Yes" if prepared_fifth > 7 else "/No",
                "Check Box 3059": "/Yes" if prepared_fifth > 8 else "/No",
                "Check Box 321": "/Yes" if prepared_sixth > 0 else "/No",
                "Check Box 320": "/Yes" if prepared_sixth > 1 else "/No",
                "Check Box 3060": "/Yes" if prepared_sixth > 2 else "/No",
                "Check Box 3061": "/Yes" if prepared_sixth > 3 else "/No",
                "Check Box 3062": "/Yes" if prepared_sixth > 4 else "/No",
                "Check Box 3063": "/Yes" if prepared_sixth > 5 else "/No",
                "Check Box 3064": "/Yes" if prepared_sixth > 6 else "/No",
                "Check Box 3065": "/Yes" if prepared_sixth > 7 else "/No",
                "Check Box 3066": "/Yes" if prepared_sixth > 8 else "/No",
                "Check Box 323": "/Yes" if prepared_seventh > 0 else "/No",
                "Check Box 322": "/Yes" if prepared_seventh > 1 else "/No",
                "Check Box 3067": "/Yes" if prepared_seventh > 2 else "/No",
                "Check Box 3068": "/Yes" if prepared_seventh > 3 else "/No",
                "Check Box 3069": "/Yes" if prepared_seventh > 4 else "/No",
                "Check Box 3070": "/Yes" if prepared_seventh > 5 else "/No",
                "Check Box 3071": "/Yes" if prepared_seventh > 6 else "/No",
                "Check Box 3072": "/Yes" if prepared_seventh > 7 else "/No",
                "Check Box 3073": "/Yes" if prepared_seventh > 8 else "/No",
                "Check Box 325": "/Yes" if prepared_eighth > 0 else "/No",
                "Check Box 324": "/Yes" if prepared_eighth > 1 else "/No",
                "Check Box 3074": "/Yes" if prepared_eighth > 2 else "/No",
                "Check Box 3075": "/Yes" if prepared_eighth > 3 else "/No",
                "Check Box 3076": "/Yes" if prepared_eighth > 4 else "/No",
                "Check Box 3077": "/Yes" if prepared_eighth > 5 else "/No",
                "Check Box 3078": "/Yes" if prepared_eighth > 6 else "/No",
                "Check Box 327": "/Yes" if prepared_ninth > 0 else "/No",
                "Check Box 326": "/Yes" if prepared_ninth > 1 else "/No",
                "Check Box 3079": "/Yes" if prepared_ninth > 2 else "/No",
                "Check Box 3080": "/Yes" if prepared_ninth > 3 else "/No",
                "Check Box 3081": "/Yes" if prepared_ninth > 4 else "/No",
                "Check Box 3082": "/Yes" if prepared_ninth > 5 else "/No",
                "Check Box 3083": "/Yes" if prepared_ninth > 6 else "/No",
            }

            # noinspection PyTypeChecker
            for j in range(0, len(writer.pages[2]["/Annots"])):
                writer_annot = writer.pages[2]["/Annots"][j].getObject()
                for checkbox, value in checkboxes.items():
                    if writer_annot.get("/T") == checkbox:
                        writer_annot.update({
                            NameObject("/V"): NameObject(value),
                            NameObject("/AS"): NameObject(value)
                        })

            # TODO spellbook pages
            # spell_descriptions = [str(spell) for spell in cantrips + first_level + second_level + third_level +
            #                       fourth_level + fifth_level + sixth_level + seventh_level + eighth_level +
            #                       ninth_level if spell is not None]

        writer.write(filepath)

        if appearance_file is not None:
            appearance_file.close()

        if faction_file is not None:
            faction_file.close()
