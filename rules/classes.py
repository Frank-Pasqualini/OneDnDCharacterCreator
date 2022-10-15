"""
A specialization a character can have.
"""
import logging
from abc import ABC, abstractmethod

from rules import bonuses, feats, spells
from rules.common import validate_string
from rules.enums import AbilityNames, ArmorTraining, ClassGroups, Languages, ProficiencyLevels, Skills, SpellLists
from rules.enums import SpellSchools, Tools, WeaponTypes


class CharacterClass(ABC):
    """
    A specialization a character can have.
    """

    _name: str
    _class_group: ClassGroups
    _primary_abilities: list[AbilityNames]
    _features: list[feats.Feat]
    _hit_die: int
    _bonuses: bonuses.Bonuses
    _level: int
    _rolled_hit_dice: list[int]
    _known_spells: list[spells.Spell]
    _spellcasting_ability: AbilityNames | None

    def __init__(self,
                 name: str,
                 class_group: ClassGroups,
                 primary_abilities: list[AbilityNames],
                 features: list[feats.Feat],
                 hit_die: int,
                 class_bonuses: bonuses.Bonuses,
                 spellcasting_ability: AbilityNames = None):
        if hit_die not in [6, 8, 10, 12]:
            raise Exception("Invalid hit die")

        self._name = validate_string(name)
        self._class_group = class_group
        self._primary_abilities = primary_abilities
        self._features = features
        self._hit_die = hit_die
        self._bonuses = class_bonuses
        self._spellcasting_ability = spellcasting_ability

        self._level = 1
        self._rolled_hit_dice = [hit_die]
        self._known_spells = []

    @abstractmethod
    def _level_up_2(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_3(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_4(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_5(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_6(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_7(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_8(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_9(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_10(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_11(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_12(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_13(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_14(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_15(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_16(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_17(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_18(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_19(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_20(self, **kwargs):
        pass

    def _level_up_past_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_bonuses(self) -> bonuses.Bonuses:
        return self._bonuses

    def get_features(self) -> list[feats.Feat]:
        return self._features

    def get_hit_die(self) -> int:
        return self._hit_die

    def get_known_spells(self) -> list[spells.Spell]:
        return self._known_spells

    def get_level(self) -> int:
        return self._level

    def get_rolled_hit_dice(self) -> list[int]:
        return self._rolled_hit_dice

    def get_spellcasting_ability(self) -> AbilityNames | None:
        return self._spellcasting_ability

    @abstractmethod
    def get_spellcasting_class(self) -> str | None:
        pass

    @abstractmethod
    def get_spellcasting_level(self) -> float:
        pass

    def level_up(self, hit_roll: int = -1, **kwargs):
        """
        Level up a class.
        """

        if hit_roll < 1 or hit_roll > self._hit_die:
            if hit_roll != -1:
                logging.warning("Invalid hit roll entered")
            hit_roll = (self._hit_die + 2) / 2

        level_up_n = {
            1: self._level_up_2,
            2: self._level_up_3,
            3: self._level_up_4,
            4: self._level_up_5,
            5: self._level_up_6,
            6: self._level_up_7,
            7: self._level_up_8,
            8: self._level_up_9,
            9: self._level_up_10,
            10: self._level_up_11,
            11: self._level_up_12,
            12: self._level_up_13,
            13: self._level_up_14,
            14: self._level_up_15,
            15: self._level_up_16,
            16: self._level_up_17,
            17: self._level_up_18,
            18: self._level_up_19,
            19: self._level_up_20,
        }

        if self._level >= 20:
            self._level_up_past_20(**kwargs)
        else:
            # noinspection PyArgumentList
            level_up_n[self._level](**kwargs)
            self._level += 1
            self._rolled_hit_dice.append(hit_roll)

    def __str__(self):
        return f"{self._name} {self._level}"


class Ranger(CharacterClass, ABC):
    """
    The Rogue class.
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 name: str,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills,
                 expertise1: Skills,
                 expertise2: Skills):
        allowable_skills = [Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INSIGHT, Skills.INVESTIGATION,
                            Skills.NATURE, Skills.PERCEPTION, Skills.STEALTH, Skills.SURVIVAL]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills) or (skill3 not in allowable_skills):
            raise Exception(
                "All 3 skills must be in the approved skill list")

        if (skill1 == skill2) or (skill1 == skill3) or (skill2 == skill3):
            raise Exception("All 3 skills must be unique")

        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.EXPERT,
                         primary_abilities=[
                             AbilityNames.DEXTERITY, AbilityNames.WISDOM],
                         features=[
                             feats.Feat(name="Expertise",
                                        description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
                                        feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                                             expertise2: ProficiencyLevels.EXPERT}),
                                        visible=False),
                             feats.Feat(name="Favored Enemy",
                                        description="You are adept at focusing your ire on a single foe. You always "
                                                    "have the Hunter's Mark Spell prepared, and it doesn't count "
                                                    "against the number of Spells you can prepare. Moreover, "
                                                    "you don't have to concentrate on the Spell once you cast it; it "
                                                    "lasts for its full duration, until you end it as a Bonus Action, "
                                                    "or until you are Incapacitated.",
                                        feat_spells=[
                                            content["Spells"]["Hunter's Mark"]()],
                                        spellcasting_ability=AbilityNames.WISDOM),
                             feats.Feat(name="Spellcasting",
                                        description="Spell Preparation. Any Spell you prepare for this Class must be "
                                                    "a Primal Spell, and it can be from any School of Magic except "
                                                    "Evocation.\n"
                                                    "Whenever you finish a Long Rest, you can commune with nature and "
                                                    "replace any Spell you have prepared for this Class with another "
                                                    "Primal Spell of the same level that isn't an Evocation.\n"
                                                    "Your spell slots determine the number of different Spells you "
                                                    "can prepare of each level.\n"
                                                    "Spellcasting Ability. Wisdom is your Spellcasting Ability for "
                                                    "your Ranger Spells.\n"
                                                    "Spellcasting Focus. You can use a Druidic Focus as a "
                                                    "Spellcasting Focus for the Spells you prepare for this Class.")
                         ],
                         hit_die=10,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.STRENGTH: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.DEXTERITY: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                                 skill3: ProficiencyLevels.PROFICIENT,
                             },
                             armor_training=[
                                 ArmorTraining.LIGHT, ArmorTraining.MEDIUM, ArmorTraining.SHIELD],
                             weapon_types=[WeaponTypes.SIMPLE,
                                           WeaponTypes.MARTIAL]
                         ),
                         spellcasting_ability=AbilityNames.WISDOM)

        self._known_spells = [spell() for spell in content["Spells"].values() if
                              spell().get_level() in [0, 1] and
                              SpellLists.PRIMAL in spell().get_spell_lists() and
                              spell().get_school() != SpellSchools.EVOCATION]

    def _level_up_2(self, fighting_style: feats.FightingStyle):
        if fighting_style.get_level() > 2:
            raise Exception("Invalid fighting style level. Must be 2 or lower")

        if "Fighting Style" not in fighting_style.get_name():
            raise Exception("This is not a fighting style")

        self._features.append(fighting_style)

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Extra Attack",
                                         description="You can attack twice, instead of once, whenever you take the "
                                                     "Attack Action on your turn."))

        self._known_spells = [spell() for spell in content["Spells"].values() if
                              spell().get_level() in [0, 1, 2] and
                              SpellLists.PRIMAL in spell().get_spell_lists() and
                              spell().get_school() != SpellSchools.EVOCATION]

    def _level_up_7(self):
        self._features.append(feats.Feat(
            name="Roving",
            description="Your Speed increases by 10 feet while you aren't wearing Heavy Armor. You also have a Climb "
                        "Speed and a Swim Speed equal to your Speed."))  # TODO

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self, content: dict[str, dict[str, any]], expertise1: Skills, expertise2: Skills):
        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        self._features.append(feats.Feat(
            name="Expertise",
            description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
            feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                 expertise2: ProficiencyLevels.EXPERT}),
            visible=False))

        self._known_spells = [spell() for spell in content["Spells"].values() if
                              spell().get_level() in [0, 1, 2, 3] and
                              SpellLists.PRIMAL in spell().get_spell_lists() and
                              spell().get_school() != SpellSchools.EVOCATION]

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Tireless",
                                         description="Primal forces now help fuel you on your journeys,granting you "
                                                     "the following benefits:\n"
                                                     "Temporary Hit Points. Whenever you finish a Short Rest or a "
                                                     "Long Rest,you can give yourself a number of Temporary Hit "
                                                     "Points equal to 1d8 plus your Proficiency Bonus.\n"
                                                     "Decrease Exhaustion. If you are Exhausted when you finish a "
                                                     "Short Rest,your level of exhaustion decreases by 1."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Nature's Veil",
                                         description="You invoke spirits of nature to magically hide yourself from "
                                                     "view. As a Bonus Action, you can expend a Spell Slot and become "
                                                     "Invisible until the end of your next turn."))

        self._known_spells = [spell() for spell in content["Spells"].values() if
                              spell().get_level() in [0, 1, 2, 3, 4] and
                              SpellLists.PRIMAL in spell().get_spell_lists() and
                              spell().get_school() != SpellSchools.EVOCATION]

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Feral Senses",
                                         description="Your connection to the forces of nature grants you Blindsight "
                                                     "with a range of 30 feet."))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self, content: dict[str, dict[str, any]]):
        self._known_spells = [spell() for spell in content["Spells"].values() if
                              spell().get_level() in [0, 1, 2, 3, 4, 5] and
                              SpellLists.PRIMAL in spell().get_spell_lists() and
                              spell().get_school() != SpellSchools.EVOCATION]

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Foe Slayer",
                                         description="Your Hunter's Mark now deals an extra 1d10 damage to its "
                                                     "target, rather than an extra 1d6."))

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_spellcasting_class(self) -> str | None:
        return "Ranger"

    def get_spellcasting_level(self) -> float:
        return self._level / 2


class Rogue(CharacterClass, ABC):
    """
    The Rogue class.
    """

    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills,
                 skill4: Skills,
                 expertise1: Skills,
                 expertise2: Skills,
                 language: Languages):
        allowable_skills = [Skills.ACROBATICS, Skills.ATHLETICS, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION,
                            Skills.INVESTIGATION, Skills.PERCEPTION, Skills.PERSUASION, Skills.SLEIGHT_OF_HAND,
                            Skills.STEALTH]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills) or (skill3 not in allowable_skills) or (
                skill4 not in allowable_skills):
            raise Exception(
                "All 4 skills must be in the approved skill list")

        if (skill1 == skill2) or (skill1 == skill3) or (skill1 == skill4) or (skill2 == skill3) or (
                skill2 == skill4) or (skill3 == skill4):
            raise Exception("All 4 skills must be unique")

        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.EXPERT,
                         primary_abilities=[AbilityNames.DEXTERITY],
                         features=[
                             feats.Feat(name="Expertise",
                                        description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
                                        feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                                             expertise2: ProficiencyLevels.EXPERT}),
                                        visible=False),
                             feats.Feat(name="Sneak Attack",
                                        description="You know how to turn a subtle attack into a deadly one. Once on "
                                                    "each of your turns when you take the Attack Action, you can deal "
                                                    "extra damage to one creature you hit with an Attack Roll if "
                                                    "you're attacking with a Finesse Weapon or a Ranged Weapon and if "
                                                    "at least one of the following requirements is met:\n"
                                                    "Advantage. You have Advantage on the Attack Roll.\n"
                                                    "Ally Adjacent to Target. At least one of your allies is within 5 "
                                                    "feet of the target, the ally isn't Incapacitated, "
                                                    "and you don't have Disadvantage on the Attack Roll.\n"
                                                    "To determine the extra damage, roll a number of d6s equal to "
                                                    "half your Rogue level(round up), and add the dice together. The "
                                                    "extra damage's type is the same as the weapon's Damage Type."),
                             feats.Feat(name="Thieves' Cant",
                                        description="You picked up various languages in the communities where you "
                                                    "plied your roguish talents. You know Thieves' Cant and "
                                                    f"{language.value}.",
                                        feat_bonuses=bonuses.Bonuses(
                                            languages=[Languages.THIEVES_CANT, language]),
                                        visible=False)
                         ],
                         hit_die=8,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.DEXTERITY: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.INTELLIGENCE: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                                 skill3: ProficiencyLevels.PROFICIENT,
                                 skill4: ProficiencyLevels.PROFICIENT
                             },
                             tools={
                                 Tools.THIEVES_TOOLS: ProficiencyLevels.PROFICIENT
                             },
                             armor_training=[ArmorTraining.LIGHT],
                             weapon_types=[WeaponTypes.SIMPLE,
                                           WeaponTypes.MARTIAL_FINESSE]
                         ))

    def _level_up_2(self):
        self._features.append(feats.Feat(name="Cunning Action",
                                         description="Your quick thinking and agility allow you to move and act "
                                                     "quickly. On your turn, you can take one of the following "
                                                     "Actions as a Bonus Action: Dash, Disengage, or Hide."))

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Uncanny Dodge",
                                         description="When an attacker that you can see hits you with an Attack Roll, "
                                                     "you can use your Reaction to halve the attack's damage against "
                                                     "you (round down)."))

    def _level_up_7(self, expertise1: Skills, expertise2: Skills):
        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        self._features.append(feats.Feat(
            name="Expertise",
            description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
            feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                 expertise2: ProficiencyLevels.EXPERT}),
            visible=False))

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self):
        self._features.append(feats.Feat(name="Evasion",
                                         description="You can nimbly dodge out of the way of certain dangers. When "
                                                     "you are subjected to an effect that allows you to make a "
                                                     "Dexterity Saving Throw to take only half damage, you instead "
                                                     "take no damage if you succeed on the Saving Throw and only half "
                                                     "damage if you fail. You can't use this feature if you're "
                                                     "Incapacitated."))

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Reliable Talent",
                                         description="You have refined your talents until they approach perfection. "
                                                     "Whenever you make an Ability Check that uses one of your Skill "
                                                     "or Tool Proficiencies,you can treat a d20 roll of 9 or lower as "
                                                     "a 10."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        self._features.append(feats.Feat(name="Subtle Strikes",
                                         description="When you attack, you know how to exploit a target's "
                                                     "distraction. You have Advantage on any Attack Roll that targets "
                                                     "a creature that is within 5 feet of at least one of your allies "
                                                     "who isn't Incapacitated."))

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Slippery Mind",
                                         description="Your cunning mind is exceptionally difficult to control. You "
                                                     "gain Proficiency in Wisdom and Charisma Saving Throws.",
                                         feat_bonuses=bonuses.Bonuses(
                                             saving_throws={AbilityNames.WISDOM: ProficiencyLevels.PROFICIENT,
                                                            AbilityNames.CHARISMA: ProficiencyLevels.PROFICIENT}),
                                         visible=False))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        self._features.append(feats.Feat(name="Elusive",
                                         description="You are so evasive that attackers rarely gain the upper hand "
                                                     "against you. No Attack Roll has Advantage against you while you "
                                                     "aren't Incapacitated."))

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Stroke of Luck",
                                         description="You have an uncanny knack for succeeding when you need to. If "
                                                     "you fail a d20 Test,you can turn the roll into a 20.\n"
                                                     "Once you use this feature, you can't use it again until you "
                                                     "finish a Short Rest or a Long Rest."))

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_spellcasting_class(self) -> str | None:
        return None

    def get_spellcasting_level(self) -> float:
        return 0
