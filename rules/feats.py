from rules import abilities, bonuses, spells
from rules.common import ordinal, validate_string


class Feat:
    """A feature that defines special rules for a character."""

    _name: str
    _description: str
    _level: int | None
    _prerequisite: str
    _repeatable: str
    _abilities: abilities.Abilities
    _bonuses: bonuses.Bonuses
    _spells: list[spells.Spell]

    def __init__(self,
                 name: str,
                 description: str,
                 level: int = None,
                 prerequisite: str = "None",
                 repeatable: str = "No",
                 feat_abilities: abilities.Abilities = abilities.Abilities(),
                 feat_bonuses: bonuses.Bonuses = bonuses.Bonuses(),
                 feat_spells: list[spells.Spell] = None):
        if level not in [None, 1, 4, 20]:
            raise Exception("Invalid Feat level")

        self._name = validate_string(name)
        self._description = validate_string(description)
        self._level = level
        self._prerequisite = validate_string(prerequisite)
        self._repeatable = validate_string(repeatable)
        self._abilities = feat_abilities
        self._bonuses = feat_bonuses
        self._spells = feat_spells

    def get_abilities(self) -> abilities.Abilities:
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
