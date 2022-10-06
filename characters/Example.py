from rules import Abilities, Character
from rules.Enums import Alignments, Languages, Skills


def create(content) -> Character.Character:
    return Character.Character(
        name="Example Character",
        character_class=content['Classes']['Rogue'](),
        race=content['Races']['Human'](skill=Skills.INVESTIGATION,
                                       versatile=content['Feats']['Lucky']()),
        background=content['Backgrounds']['Criminal'](),
        abilities=Abilities.Abilities(
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
