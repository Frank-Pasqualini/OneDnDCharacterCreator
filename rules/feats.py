"""
A feature that defines special rules for a character.
"""

from abc import ABC

from rules import abilities, bonuses, spells
from rules.common import ordinal, validate_string
from rules.enums import AbilityNames


class Feat(ABC):
    """
    A feature that defines special rules for a character.
    """

    _name: str
    _description: str
    _level: int | None
    _prerequisite: str
    _repeatable: str
    _abilities: abilities.Abilities
    _bonuses: bonuses.Bonuses
    _spells: list[spells.Spell] | None
    _spellcasting_ability: AbilityNames | None
    _visible: bool

    def __init__(self,
                 name: str,
                 description: str,
                 level: int = None,
                 prerequisite: str = "None",
                 repeatable: str = "No",
                 feat_abilities: abilities.Abilities = abilities.Abilities(),
                 feat_bonuses: bonuses.Bonuses = bonuses.Bonuses(),
                 feat_spells: list[spells.Spell] = None,
                 spellcasting_ability: AbilityNames = None,
                 visible: bool = True):
        if level is not None and level not in range(1, 20):
            raise Exception("Invalid Feat level")

        if feat_spells is not None and spellcasting_ability is None:
            raise Exception(
                "If spells are added in a feat it must have an ability")

        self._name = validate_string(name)
        self._description = validate_string(description)
        self._level = level
        self._prerequisite = validate_string(prerequisite)
        self._repeatable = validate_string(repeatable)
        self._abilities = feat_abilities
        self._bonuses = feat_bonuses
        self._spells = feat_spells
        self._spellcasting_ability = spellcasting_ability
        self._visible = visible

    def get_abilities(self) -> abilities.Abilities:
        return self._abilities

    def get_bonuses(self) -> bonuses.Bonuses:
        return self._bonuses

    def get_level(self) -> int:
        return self._level

    def get_name(self) -> str:
        return self._name

    def get_spellcasting_ability(self) -> AbilityNames:
        return self._spellcasting_ability

    def get_spells(self) -> list[spells.Spell]:
        return self._spells if self._spells is not None else []

    def summary(self, visible_override: bool = False) -> str | None:
        return f"{self._name}. {self._description}" if self._visible or visible_override else None

    def __str__(self) -> str:
        output = f"{self._name}\n"

        if self._level is not None:
            output += f"{ordinal(self._level)}-Level Feat\n"

            output += f"Prerequisite: {self._prerequisite}\n"

            output += f"Repeatable: {self._repeatable}\n"

        output += f"{self._description}"

        return output


class FightingStyle(Feat, ABC):
    """
    A specific Fighting Style type of feat.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 level: int = None,
                 prerequisite: str = "None",
                 repeatable: str = "No",
                 feat_abilities: abilities.Abilities = abilities.Abilities(),
                 feat_bonuses: bonuses.Bonuses = bonuses.Bonuses(),
                 feat_spells: list[spells.Spell] = None,
                 visible: bool = True):
        super().__init__(name=name,
                         description=description,
                         level=level,
                         prerequisite=prerequisite,
                         repeatable=repeatable,
                         feat_abilities=feat_abilities,
                         feat_bonuses=feat_bonuses,
                         feat_spells=feat_spells,
                         visible=visible)
