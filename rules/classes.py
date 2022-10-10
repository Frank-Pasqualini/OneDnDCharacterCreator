"""
A specialization a character can have.
"""
import logging
from abc import ABC, abstractmethod

from rules import abilities, bonuses, feats
from rules.common import validate_string
from rules.enums import AbilityNames, ArmorTraining, ClassGroups, Languages, ProficiencyLevels, Skills, Tools
from rules.enums import WeaponTypes


# TODO a lot of this file.


class CharacterClass(ABC):
    """
    A specialization a character can have.
    """

    _name: str
    _class_group: ClassGroups
    _primary_ability: AbilityNames
    _features: list[feats.Feat]
    _hit_die: int
    _bonuses: bonuses.Bonuses
    _level: int
    _rolled_hit_dice: list[int]

    def __init__(self,
                 name: str,
                 class_group: ClassGroups,
                 primary_ability: AbilityNames,
                 features: list[feats.Feat],
                 hit_die: int,
                 class_bonuses: bonuses.Bonuses):
        self._name = validate_string(name)
        self._class_group = class_group
        self._primary_ability = primary_ability
        self._features = features
        self._hit_die = hit_die
        self._bonuses = class_bonuses

        self._level = 1
        self._rolled_hit_dice = [hit_die]

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

    def get_abilities(self) -> abilities.Abilities:
        """
        Sums the abilities of all features
        :return: A summed up Abilities.
        :rtype: abilities.Abilities
        """

        feat_abilities = abilities.Abilities()
        feat_abilities_list = [feat.get_abilities() for feat in self._features]

        for item in feat_abilities_list:
            feat_abilities += item

        return feat_abilities

    def get_bonuses(self) -> bonuses.Bonuses:
        """
        Sums the bonuses of all features
        :return: A summed up Bonuses.
        :rtype: bonuses.Bonuses
        """

        feat_bonuses = bonuses.Bonuses()
        feat_bonuses_list = [feat.get_bonuses() for feat in self._features]

        for item in feat_bonuses_list:
            feat_bonuses += item

        return self._bonuses + feat_bonuses

    def get_features(self) -> list[feats.Feat]:
        return self._features

    def get_hit_die(self) -> int:
        return self._hit_die

    def get_level(self) -> int:
        return self._level

    def get_rolled_hit_dice(self) -> list[int]:
        return self._rolled_hit_dice

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
                         primary_ability=AbilityNames.DEXTERITY,
                         features=[
                             feats.Feat(name="Expertise",
                                        description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
                                        feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                                             expertise2: ProficiencyLevels.EXPERT})),
                             feats.Feat(name="Sneak Attack",
                                        description="You know how to turn a subtle attack into a deadly one. Once on "
                                                    "each of your turns when you take the Attack Action, you can deal "
                                                    "extra damage to one creature you hit with an Attack Roll if "
                                                    "you’re attacking with a Finesse Weapon or a Ranged Weapon and if "
                                                    "at least one of the following requirements is met:\n"
                                                    "Advantage. You have Advantage on the Attack Roll.\n"
                                                    "Ally Adjacent to Target. At least one of your allies is within 5 "
                                                    "feet of the target, the ally isn’t Incapacitated, "
                                                    "and you don’t have Disadvantage on the Attack Roll.\n"
                                                    "To determine the extra damage, roll a number of d6s equal to "
                                                    "half your Rogue level(round up), and add the dice together. The "
                                                    "extra damage’s type is the same as the weapon’s Damage Type."),
                             feats.Feat(name="Thieves' Cant",
                                        description="You picked up various languages in the communities where you "
                                                    "plied your roguish talents. You know Thieves’ Cant and "
                                                    f"{language.value}.",
                                        feat_bonuses=bonuses.Bonuses(languages=[Languages.THIEVES_CANT, language]))
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
                                                     "you can use your Reaction to halve the attack’s damage against "
                                                     "you (round down)."))

    def _level_up_7(self, expertise1: Skills, expertise2: Skills):
        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        self._features.append(feats.Feat(
            name="Expertise",
            description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
            feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                 expertise2: ProficiencyLevels.EXPERT})))

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
                                                     "damage if you fail. You can’t use this feature if you’re "
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
                                         description="When you attack, you know how to exploit a target’s "
                                                     "distraction. You have Advantage on any Attack Roll that targets "
                                                     "a creature that is within 5 feet of at least one of your allies "
                                                     "who isn’t Incapacitated."))

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Slippery Mind",
                                         description="Your cunning mind is exceptionally difficult to control. You "
                                                     "gain Proficiency in Wisdom and Charisma Saving Throws.",
                                         feat_bonuses=bonuses.Bonuses(
                                             saving_throws={AbilityNames.WISDOM: ProficiencyLevels.PROFICIENT,
                                                            AbilityNames.CHARISMA: ProficiencyLevels.PROFICIENT})))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        self._features.append(feats.Feat(name="Elusive",
                                         description="You are so evasive that attackers rarely gain the upper hand "
                                                     "against you. No Attack Roll has Advantage against you while you "
                                                     "aren’t Incapacitated."))

    def _level_up_18(self, **kwargs):
        self._features.append(feats.Feat(name="Stroke of Luck",
                                         description="You have an uncanny knack for succeeding when you need to. If "
                                                     "you fail a d20 Test,you can turn the roll into a 20.\n"
                                                     "Once you use this feature, you can’t use it again until you "
                                                     "finish a Short Rest or a Long Rest."))

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)
