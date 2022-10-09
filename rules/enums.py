"""
A list of enums for common options.
"""

from __future__ import annotations

import math
from enum import Enum


class AbilityNames(Enum):
    """
    The 6 standard ability scores.
    """

    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"


class Alignments(Enum):
    """
    The 9 standard alignments.
    """

    LAWFUL_GOOD = "Lawful Good"
    LAWFUL_NEUTRAL = "Lawful Neutral"
    LAWFUL_EVIL = "Lawful Evil"
    NEUTRAL_GOOD = "Neutral Good"
    NEUTRAL = "Neutral"
    NEUTRAL_EVIL = "Neutral Evil"
    CHAOTIC_GOOD = "Chaotic Good"
    CHAOTIC_NEUTRAL = "Chaotic Neutral"
    CHAOTIC_EVIL = "Chaotic Evil"


class ArmorTraining(Enum):
    """
    The 4 types of armor.
    """

    LIGHT = "Light Armor"
    MEDIUM = "Medium Armor"
    HEAVY = "Heavy Armor"
    SHIELD = "Shield"


class ArtisansTools(Enum):
    """
    The tools of the 'Artisan's Tools' type.
    """

    ALCHEMISTS_SUPPLIES = "Alchemist's Supplies"
    BREWERS_SUPPLIES = "Brewer's Supplies"
    CALLIGRAPHERS_SUPPLIES = "Calligrapher's Supplies"
    CARPENTERS_TOOLS = "Carpenter's Tools"
    CARTOGRAPHERS_TOOLS = "Cartographer's Tools"
    COBBLERS_TOOLS = "Cobbler's Tools"
    COOKS_UTENSILS = "Cook's Utensils"
    GLASSBLOWERS_TOOLS = "Glassblower's Tools"
    JEWELERS_TOOLS = "Jeweler's Tools"
    LEATHERWORKERS_TOOLS = "Leatherworker's Tools"
    MASONS_TOOLS = "Mason's Tools"
    PAINTERS_SUPPLIES = "Painter's Supplies"
    POTTERS_TOOLS = "Potter's Tools"
    SMITHS_TOOLS = "Smith's Tools"
    TINKERS_TOOLS = "Tinker's Tools"
    WEAVERS_TOOLS = "Weaver's Tools"
    WOODCARVERS_TOOLS = "Woodcarver's Tools"


class ClassGroups(Enum):
    """
    The 4 types of character class.
    """

    EXPERT = "Expert"
    MAGE = "Mage"
    PRIEST = "Priest"
    WARRIOR = "Warrior"


class CreatureTypes(Enum):
    """
    The special types a character or creature can be.
    """

    ABERRATION = "Aberration"
    BEAST = "Beast"
    CELESTIAL = "Celestial"
    CONSTRUCT = "Construct"
    DRAGON = "Dragon"
    ELEMENTAL = "Elemental"
    FEY = "Fey"
    FIEND = "Fiend"
    GIANT = "Giant"
    HUMANOID = "Humanoid"
    MONSTROSITY = "Monstrosity"
    OOZE = "Ooze"
    PLANT = "Plant"
    UNDEAD = "Undead"


class DamageTypes(Enum):
    """
    The types of damage a character can deal or take.
    """

    ACID = "Acid"
    BLUDGEONING = "Bludgeoning"
    COLD = "Cold"
    FIRE = "Fire"
    FORCE = "Force"
    LIGHTNING = "Lightning"
    NECROTIC = "Necrotic"
    PIERCING = "Piercing"
    POISON = "Poison"
    PSYCHIC = "Psychic"
    RADIANT = "Radiant"
    SLASHING = "Slashing"
    THUNDER = "Thunder"


class GamingSets(Enum):
    """
    The tools of the 'Gaming Sets' type.
    """

    DICE_SET = "Dice Set"
    DRAGONCHESS_SET = "Dragonchess Set"
    PLAYING_CARD_SET = "Playing Card Set"
    THREE_DRAGON_ANTE_SET = "Three-Dragon Ante Set"


class ProficiencyLevels(Enum):
    """
    The different levels a character can be proficient in a skill, tool, or weapon.
    """
    NONE = 0
    HALF = 0.5
    PROFICIENT = 1
    EXPERT = 2

    def __lt__(self, other) -> bool:
        return self.value < other

    def __gt__(self, other) -> bool:
        return self.value > other

    def __mul__(self, other) -> int:
        return math.floor(self.value * other)


class Skills(Enum):
    """
    The skills a character can be proficient in.
    """

    ACROBATICS = "Acrobatics"
    ANIMAL_HANDLING = "Animal Handling"
    ARCANA = "Arcana"
    ATHLETICS = "Athletics"
    DECEPTION = "Deception"
    HISTORY = "History"
    INSIGHT = "Insight"
    INTIMIDATION = "Intimidation"
    INVESTIGATION = "Investigation"
    MEDICINE = "Medicine"
    NATURE = "Nature"
    PERCEPTION = "Perception"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"
    RELIGION = "Religion"
    SLEIGHT_OF_HAND = "Sleight of Hand"
    STEALTH = "Stealth"
    SURVIVAL = "Survival"


class Languages(Enum):
    """
    The languages a character can know.
    """

    COMMON = "Common"
    COMMON_SIGN_LANGUAGE = "Common Sign Language"
    DWARVISH = "Dwarvish"
    ELVISH = "Elvish"
    GIANT = "Giant"
    GNOMISH = "Gnomish"
    GOBLIN = "Goblin"
    HALFLING = "Halfling"
    ORC = "Orc"
    ABYSSAL = "Abyssal"
    CELESTIAL = "Celestial"
    DEEP_SPEECH = "Deep Speech"
    DRACONIC = "Draconic"
    DRUIDIC = "Druidic"
    INFERNAL = "Infernal"
    PRIMORDIAL = "Primordial"
    AQUAN = "Aquan"
    AURAN = "Auran"
    IGNAN = "Ignan"
    TERRAN = "Terran"
    SYLVAN = "Sylvan"
    THIEVES_CANT = "Thieves' Cant"
    UNDERCOMMON = "Undercommon"


class MusicalInstruments(Enum):
    """
    The tools of the 'Musical Instrument' type.
    """

    BAGPIPES = "Bagpipes"
    DRUM = "Drum"
    DULCIMER = "Dulcimer"
    FLUTE = "Flute"
    HORN = "Horn"
    LUTE = "Lute"
    LYRE = "Lyre"
    PAN_FLUTE = "Pan Flute"
    SHAWM = "Shawm"
    VIOL = "Viol"


class Sizes(Enum):
    """
    The sizes of characters or creatures.
    """

    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    HUGE = "Huge"
    GARGANTUAN = "Gargantuan"


class SpellLists(Enum):
    """
    The types of magic a character can know.
    """

    ARCANE = "Arcane"
    DIVINE = "Divine"
    PRIMAL = "Primal"


class SpellSchools(Enum):
    """
    The schools of magic that describe what effect the spell creates.
    """

    ABJURATION = "Abjuration"
    CONJURATION = "Conjuration"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    EVOCATION = "Evocation"
    ILLUSION = "Illusion"
    NECROMANCY = "Necromancy"
    TRANSMUTATION = "Transmutation"


class Tools(Enum):
    """
    The tools of the no specific tool type.
    """

    DISGUISE_KIT = "Disguise Kit"
    FORGERY_KIT = "Forgery Kit"
    HERBALISM_KIT = "Herbalism Kit"
    NAVIGATORS_TOOLS = "Navigator's Tools"
    POISONERS_KIT = "Poisoner's Kit"
    THIEVES_TOOLS = "Thieves' Tools"
