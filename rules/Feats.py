from rules import Abilities, Bonuses, Spells
from rules.Enums import Languages
from rules.CommonFunctions import ordinal, validate_string


class Feat:
    """A feature that defines special rules for a character."""

    _name: str
    _description: str
    _level: int | None
    _prerequisite: str
    _repeatable: str
    _abilities: Abilities.Abilities
    _bonuses: Bonuses.Bonuses
    _spells: list[Spells.Spell]

    def __init__(self,
                 name: str,
                 description: str,
                 level: int = None,
                 prerequisite: str = "None",
                 repeatable: str = "No",
                 abilities: Abilities.Abilities = Abilities.Abilities(),
                 bonuses: Bonuses.Bonuses = Bonuses.Bonuses(),
                 spells: list[Spells.Spell] = None):
        if level not in [None, 1, 4, 20]:
            raise Exception("Invalid Feat level")

        self._name = validate_string(name)
        self._description = validate_string(description)
        self._level = level
        self._prerequisite = validate_string(prerequisite)
        self._repeatable = validate_string(repeatable)
        self._abilities = abilities
        self._bonuses = bonuses
        self._spells = spells

    def get_abilities(self) -> Abilities.Abilities:
        return self._abilities

    def get_level(self) -> int:
        return self._level

    def get_name(self) -> str:
        return self._name

    def summary(self) -> str:
        return f"{self._name}. {self._description}"

    def __str__(self) -> str:
        """Print the Feat as it would be seen in a feat description."""

        output = f"{self._name}\n"

        if self._level is not None:
            output += f"{ordinal(self._level)}-Level Feat\n"

            output += f"Prerequisite: {self._prerequisite}\n"

            output += f"Repeatable: {self._repeatable}\n"

        output += f"{self._description}"

        return output
