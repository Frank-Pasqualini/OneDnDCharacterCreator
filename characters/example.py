"""
An example character. A Human Thief Rogue.
"""

from rules import character
from rules.enums import AbilityNames, Alignments, Languages, Skills


def create(content: dict[str, dict[str, any]]) -> character.Character:
    """
    A method that creates and returns a character. For now this is the method of saving character configurations
    :param content: The compiled content of the source files
    :type content: dict[str, dict[str, any]]
    :return: The created character.
    :rtype: character.Character
    """

    return character.Character(
        name="Example Character",
        character_class=content["Classes"]["Thief Rogue"](skill1=Skills.ACROBATICS,
                                                          skill2=Skills.ATHLETICS,
                                                          skill3=Skills.DECEPTION,
                                                          skill4=Skills.INSIGHT,
                                                          expertise1=Skills.STEALTH,
                                                          expertise2=Skills.SLEIGHT_OF_HAND,
                                                          language=Languages.COMMON_SIGN_LANGUAGE),
        race=content["Races"]["Human"](skill=Skills.INTIMIDATION,
                                       versatile=content["Feats"]["Skilled"](skill1=Skills.INVESTIGATION,
                                                                             skill2=Skills.PERCEPTION,
                                                                             skill3=Skills.PERSUASION)),
        background=content["Backgrounds"]["Criminal"](),
        starting_abilities={
            AbilityNames.STRENGTH: 8,
            AbilityNames.DEXTERITY: 15,
            AbilityNames.CONSTITUTION: 12,
            AbilityNames.INTELLIGENCE: 14,
            AbilityNames.WISDOM: 10,
            AbilityNames.CHARISMA: 13,
        },
        alignment=Alignments.CHAOTIC_NEUTRAL,
        player_name="Example Player",
        language=Languages.ELVISH
    )
