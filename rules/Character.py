import json
import math

from PyPDF2 import PdfReader, PdfWriter

from rules import Abilities, Backgrounds, CharacterClasses, Races
from rules.Enums import Alignments, Languages

# TODO IN NEED OF CLEANUP AND COMPLETION
def int_mod(score: int):
    return math.floor((score - 10) / 2)


def str_mod(mod: int):
    return ("" if mod < 0 else "+") + str(mod)


class Character:
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

        self._classes = [character_class]
        self._race = race
        self._background = background
        self._alignment = alignment
        self._abilities = abilities
        self._language = language

        self._xp = 0
        self._milestone = milestone

        self._inspiration = False
        self._current_hp = 0
        self._temp_hp = 0
        self._inventory = {}

    def get_abilities(self):
        return sum([feature._abilities for feature in self.get_features()],
                   self._abilities + self.get_background()._abilities)

    def get_alignment(self):
        return self._alignment.value

    def get_armor_class(self):
        return 10 + self.get_dexterity_mod()

    def get_background(self):
        return self._background

    def get_character_level(self):
        return sum([character_class.level for character_class in self._classes])

    def get_charisma(self):
        return self.get_abilities()._charisma

    def get_charisma_mod(self):
        return int_mod(self.get_charisma())

    def get_classes(self):
        return self._classes

    def get_class_level(self):
        return ", ".join([str(character_class) for character_class in self._classes])

    def get_constitution(self):
        return self.get_abilities()._constitution

    def get_constitution_mod(self):
        return int_mod(self.get_constitution())

    def get_dexterity(self):
        return self.get_abilities()._dexterity

    def get_dexterity_mod(self):
        return int_mod(self.get_dexterity())

    def get_features(self):
        return self.get_race()._features + \
               [self.get_background()._feat] + \
               [feature for features in [character_class.features for character_class in self.get_classes()]
                for feature in features]

    def get_initiative_mod(self):
        return self.get_dexterity_mod()

    def get_inspiration(self):
        return self._inspiration

    def get_intelligence(self):
        return self.get_abilities()._intelligence

    def get_intelligence_mod(self):
        return int_mod(self.get_intelligence())

    def get_max_hit_dice(self):
        return "1d8"  # TODO

    def get_max_hp(self):
        return 0  # TODO

    def get_milestone(self):
        return self._milestone

    def get_name(self):
        return self._name

    def get_player_name(self):
        return self._player_name

    def get_proficiency_bonus(self):
        return math.ceil(self.get_character_level() / 4) + 1

    def get_race(self):
        return self._race

    def get_speed(self):
        return self._race._speed

    def get_strength(self):
        return self.get_abilities()._strength

    def get_strength_mod(self):
        return int_mod(self.get_strength())

    def get_wisdom(self):
        return self.get_abilities()._wisdom

    def get_wisdom_mod(self):
        return int_mod(self.get_wisdom())

    def get_xp(self):
        return self._xp

    def dump(self, filepath):
        return json.dump({
            "name": self.get_name(),
            "player_name": self.get_player_name(),
        }, filepath)

    def write_character_sheet(self, filepath):
        reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
        writer = PdfWriter()

        writer.add_page(reader.pages[0])
        writer.add_page(reader.pages[1])
        writer.add_page(reader.pages[2])

        writer.update_page_form_field_values(
            writer.pages[0], {
                "AC": str(self.get_armor_class()),
                "Alignment": str(self.get_alignment()),
                "Background": str(self.get_background()),
                "Bonds": str(self.get_background()._bonds),
                "CHA": str(self.get_charisma()),
                "CHamod": str_mod(self.get_charisma_mod()),
                "CharacterName": str(self.get_name()),
                "ClassLevel": str(self.get_class_level()),
                "CON": str(self.get_constitution()),
                "CONmod": str_mod(self.get_constitution_mod()),
                "DEX": str(self.get_dexterity()),
                "DEXmod ": str_mod(self.get_dexterity_mod()),
                "Features and Traits": "\n\n".join(str(feature) for feature in self.get_features()),
                "Flaws": str(self.get_background()._flaws),
                "HDTotal": str(self.get_max_hit_dice()),
                "HPMax": str(self.get_max_hp()),
                "Ideals": str(self.get_background()._ideals),
                "Initiative": str_mod(self.get_initiative_mod()),
                "Inspiration": "X" if self.get_inspiration() else "",
                "INT": str(self.get_intelligence()),
                "INTmod": str_mod(self.get_intelligence_mod()),
                "PersonalityTraits ": str(self.get_background()._personality_traits),
                "PlayerName": self.get_player_name(),
                "ProfBonus": str_mod(self.get_proficiency_bonus()),
                "Race ": str(self._race),
                "Speed": str(self.get_speed()) + " ft.",
                "STR": str(self.get_strength()),
                "STRmod": str_mod(self.get_strength_mod()),
                "WIS": str(self.get_wisdom()),
                "WISmod": str_mod(self.get_wisdom_mod()),
                "XP": self.get_xp() if not self.get_milestone() else "N/A"
            }
        )

        writer.write(filepath)
