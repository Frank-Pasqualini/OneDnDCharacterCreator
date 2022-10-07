from rules import abilities, character
from rules.enums import Alignments, Languages, Skills


def create(content) -> character.Character:
    return character.Character(
        name="Example Character",
        character_class=content['Classes']['Thief Rogue'](),
        race=content['Races']['Human'](skill=Skills.INVESTIGATION,
                                       versatile=content['Feats']['Lucky']()),
        background=content['Backgrounds']['Criminal'](),
        starting_abilities=abilities.Abilities(
            strength=8,
            dexterity=15,
            constitution=12,
            intelligence=14,
            wisdom=10,
            charisma=13,
        ),
        alignment=Alignments.CHAOTIC_NEUTRAL,
        player_name="Example Player",
        language=Languages.ELVISH
    )
