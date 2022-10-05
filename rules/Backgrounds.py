from rules import Abilities, Feats, Bonuses
from rules.CommonFunctions import validate_string
from rules.Enums import AbilityNames, Languages, ProficiencyLevels


class Background:
    """A Background for a character."""

    _name: str
    _abilities: Abilities.Abilities
    _bonuses: Bonuses.Bonuses
    _language: Languages
    _feat: Feats.Feat
    _equipment: any  # TODO
    _description: str
    _personality_traits: str
    _ideals: str
    _bonds: str
    _flaws: str

    def __init__(self,
                 name: str,
                 abilities: Abilities.Abilities,
                 bonuses: Bonuses.Bonuses,
                 language: Languages,
                 feat: Feats.Feat,
                 equipment: any,
                 description: str = "",
                 personality_traits: str = "",
                 ideals: str = "",
                 bonds: str = "",
                 flaws: str = ""):
        abilities_list = [abilities.get_strength(), abilities.get_dexterity(), abilities.get_constitution(),
                          abilities.get_intelligence(), abilities.get_wisdom(), abilities.get_charisma()]
        if sum(abilities_list) != 3 or min(abilities_list) != 0 or max(abilities_list) > 2:
            raise Exception("A Background must give either 3 +1s or a +1 and a +2")

        if len(bonuses.get_saving_throws()) != 0 or \
                len(bonuses.get_skills()) != 2 or \
                (len(bonuses.get_artisans_tools()) + len(bonuses.get_gaming_sets()) +
                 len(bonuses.get_musical_instruments()) + len(bonuses.get_tools())) != 1 or \
                bonuses.get_initiative() != ProficiencyLevels.NONE or bonuses.get_hp_bonus():
            raise Exception("A Background must contain exactly 2 skills and one tool")

        if language == Languages.COMMON:
            raise Exception("A Background must contain a language other than Common")

        if feat.get_level() != 1:
            raise Exception("Only a first level Feat can be part of a Background")

        self._name = validate_string(name)
        self._abilities = abilities
        self._bonuses = bonuses
        self._language = language
        self._feat = feat
        self._equipment = equipment
        self._description = description
        self._personality_traits = personality_traits
        self._ideals = ideals
        self._bonds = bonds
        self._flaws = flaws

    def __str__(self) -> str:
        """Print the Background as it would be seen in a background description."""

        output = f"{self._name}\n"

        abilities_dict = {
            AbilityNames.STRENGTH.value: self._abilities.get_strength(),
            AbilityNames.DEXTERITY.value: self._abilities.get_dexterity(),
            AbilityNames.CONSTITUTION.value: self._abilities.get_constitution(),
            AbilityNames.INTELLIGENCE.value: self._abilities.get_intelligence(),
            AbilityNames.WISDOM.value: self._abilities.get_wisdom(),
            AbilityNames.CHARISMA.value: self._abilities.get_charisma()
        }
        abilities_dict = [f"+{v} {k}" for k, v in
                          sorted(abilities_dict.items(), key=lambda item: item[1], reverse=True)
                          if v > 0]
        output += f"Ability Scores: {', '.join(abilities_dict)}\n"

        skills = [str(skill.value) for skill in self._bonuses.get_skills().keys()]
        output += f"Skill Proficiencies: {', '.join(skills)}\n"

        tools = [str(tool.value) for tool in self._bonuses.get_artisans_tools().keys()] + \
                [str(tool.value) for tool in self._bonuses.get_gaming_sets().keys()] + \
                [str(tool.value) for tool in self._bonuses.get_musical_instruments().keys()] + \
                [str(tool.value) for tool in self._bonuses.get_tools().keys()]
        output += f"Tool Proficiencies: {tools[0]}\n"

        output += f"Language: {self._language.value}\n"

        output += f"Feat: {self._feat.get_name()}\n"

        output += f"{self._description}\n"

        output += f"Equipment\nTODO"

        return output
