from rules import bonuses, feats
from rules.common import validate_string
from rules.enums import AbilityNames, ClassGroups, ProficiencyLevels, Skills, Tools


class CharacterClass:
    _name: str
    _class_group: ClassGroups
    _primary_ability: AbilityNames
    _features: dict[int, list[feats.Feat]]
    _hit_die: int
    _bonuses: bonuses.Bonuses
    _level: int
    _rolled_hit_dice: list[int]

    def __init__(self,
                 name: str,
                 class_group: ClassGroups,
                 primary_ability: AbilityNames,
                 features: dict[int, list[feats.Feat]],
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

    def get_bonuses(self) -> bonuses.Bonuses:
        return self._bonuses

    def get_hit_die(self) -> int:
        return self._hit_die

    def get_level(self) -> int:
        return self._level

    def get_rolled_hit_dice(self) -> list[int]:
        return self._rolled_hit_dice

    def __str__(self):
        return f"{self._name} {self._level}"


class Rogue(CharacterClass):
    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills,
                 skill4: Skills):
        allowable_skills = [Skills.ACROBATICS, Skills.ATHLETICS, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION,
                            Skills.INVESTIGATION, Skills.PERCEPTION, Skills.PERSUASION, Skills.SLEIGHT_OF_HAND,
                            Skills.STEALTH]
        if skill1 not in allowable_skills or skill2 not in allowable_skills or \
                skill3 not in allowable_skills or skill4 not in allowable_skills or \
                skill1 == skill2 or skill1 == skill3 or skill1 == skill4 or skill2 == skill3 or skill2 == skill4 or \
                skill3 == skill4:
            raise Exception(
                "All 4 skills must be in the approved skill list and none may be duplicates.")

        super().__init__(name=name,
                         class_group=ClassGroups.EXPERT,
                         primary_ability=AbilityNames.DEXTERITY,
                         features={},
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
                                 skill4: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.THIEVES_TOOLS: ProficiencyLevels.PROFICIENT
                             }
                         ))
