"""
A weapon that deals damage.
"""

from abc import ABC

from rules.common import validate_string, mod
from rules.enums import DamageTypes, WeaponTypes


class Weapon(ABC):
    """
    A weapon that deals damage.
    """

    _name: str
    _weapon_type: WeaponTypes
    _damage_dice: str
    _damage_type: DamageTypes
    _range = tuple[int, int]
    _ammunition: bool
    _finesse: bool
    _heavy: bool
    _light: bool
    _loading: bool
    _reach: bool
    _thrown: bool
    _two_handed: bool
    _versatile: str | None
    _special: str | None
    _attack_bonus: int
    _damage_bonus: int
    _silvered: bool
    _magical: bool

    def __init__(self,
                 name: str,
                 weapon_type: WeaponTypes,
                 damage_dice: str,
                 damage_type: DamageTypes,
                 attack_range: tuple[int, int] = (0, 0),
                 ammunition: bool = False,
                 finesse: bool = False,
                 heavy: bool = False,
                 light: bool = False,
                 loading: bool = False,
                 reach: bool = False,
                 thrown: bool = False,
                 two_handed: bool = False,
                 versatile: str = None,
                 special: str = None,
                 attack_bonus: int = 0,
                 damage_bonus: int = 0,
                 silvered: bool = False,
                 magical: bool = False):
        if thrown and attack_range == (0, 0):
            raise Exception("A thrown weapon must have a range")

        if heavy and light:
            raise Exception("A weapon cannot be both heavy and light")

        self._name = validate_string(name)
        self._weapon_type = weapon_type
        self._damage_dice = validate_string(damage_dice)
        self._damage_type = damage_type
        self._range = attack_range
        self._ammunition = ammunition
        self._finesse = finesse
        self._heavy = heavy
        self._light = light
        self._loading = loading
        self._reach = reach
        self._thrown = thrown
        self._two_handed = two_handed
        self._versatile = versatile
        self._special = special
        self._attack_bonus = attack_bonus
        self._damage_bonus = damage_bonus
        self._silvered = silvered
        self._magical = magical

    def get_attack_bonus(self, str_mod: int, dex_mod: int, prof_mod: int, weapon_profs: list[WeaponTypes]) -> int:
        """
        Returns the attack bonus of a weapon for a user
        :param str_mod: Strength modifier
        :type str_mod: int
        :param dex_mod: Dexterity modifier
        :type dex_mod: int
        :param prof_mod: Proficiency modifier
        :type prof_mod: int
        :param weapon_profs: List of weapon proficiencies
        :type weapon_profs: list[WeaponTypes]
        :return: Attack modifier
        :rtype: int
        """

        if self._finesse:
            base = max(str_mod, dex_mod) + self._attack_bonus
        elif self._range == (0, 0) or self._thrown:
            base = str_mod + self._attack_bonus
        else:
            base = dex_mod + self._attack_bonus

        if (self._weapon_type in weapon_profs) or (self._weapon_type == WeaponTypes.MARTIAL and self._finesse and
                                                   WeaponTypes.MARTIAL_FINESSE in weapon_profs):
            return base + prof_mod

        return base

    def get_damage(self, str_mod: int, dex_mod: int) -> str:
        """
        Returns the damage of a weapon for a user
        :param str_mod: Strength modifier
        :type str_mod: int
        :param dex_mod: Dexterity modifier
        :type dex_mod: int
        :return: The damage
        :rtype: int
        """

        if self._finesse:
            return self._damage_dice + mod(max(str_mod, dex_mod) + self._damage_bonus)

        if self._range == (0, 0) or self._thrown:
            return self._damage_dice + mod(str_mod + self._damage_bonus)

        return self._damage_dice + mod(dex_mod + self._damage_bonus)

    def summary(self) -> str:
        """
        Returns a summary of a weapon
        :return: Summary of a weapon
        :rtype: str
        """

        output = f"{self._name}. {self._damage_dice}{mod(self._damage_bonus) if self._damage_bonus != 0 else ''}"
        output += f" {'Magical ' if self._magical else 'Silvered ' if self._silvered else ''}{self._damage_type.value}"
        output += f"{' ' + mod(self._attack_bonus) + ' to hit' if self._attack_bonus != 0 else ''}"

        properties = []

        if self._ammunition:
            if self._range != (0, 0) and not self._thrown:
                properties.append(
                    f"Ammunition (range {self._range[0]}/{self._range[1]})")
            else:
                properties.append("Ammunition")

        if self._finesse:
            properties.append("Finesse")

        if self._heavy:
            properties.append("Heavy")

        if self._light:
            properties.append("Light")

        if self._loading:
            properties.append("Loading")

        if self._reach:
            properties.append("Reach")

        if self._thrown:
            if self._range != (0, 0) and not self._ammunition:
                properties.append(
                    f"Thrown (range {self._range[0]}/{self._range[1]})")
            else:
                properties.append("Thrown")

        if self._two_handed:
            properties.append("Two-Handed")

        if self._versatile:
            properties.append(f"Versatile {self._versatile}")

        if self._range != (0, 0) and not self._ammunition and not self._thrown:
            properties.append(f"(range {self._range[0]}/{self._range[1]})")

        if self._special:
            properties.append(self._special)

        if len(properties) > 0:
            output += ": " + ", ".join(properties)

        return output
