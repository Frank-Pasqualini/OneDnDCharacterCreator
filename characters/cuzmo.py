"""
Cuzmo Mountainbeast Elanithino. From the Baldur's Gate: Descent into Avernus campaign that I am running with my family.
"""

from rules import abilities, character, bonuses
from rules.enums import AbilityNames, Alignments, Languages, ProficiencyLevels, Skills, Tools


def create(content: dict[str, dict[str, any]]) -> character.Character:
    """
    A method that creates and returns a character. For now this is the method of saving character configurations
    :param content: The compiled content of the source files
    :type content: dict[str, dict[str, any]]
    :return: The created character.
    :rtype: character.Character
    """

    custom_background = content["Backgrounds"]["Custom"](
        name="Outlander",
        background_abilities=abilities.Abilities(
            strength=2,
            constitution=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.INVESTIGATION: ProficiencyLevels.PROFICIENT,
                Skills.PERCEPTION: ProficiencyLevels.PROFICIENT,
            },
            tools={
                Tools.NAVIGATORS_TOOLS: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.GIANT],
        ),
        feat=content["Feats"]["Tough"](),
        description="You grew up in the wilds, far from civilization and the comforts of town and technology. You've "
                    "witnessed the migration of herds larger than forests, survived weather more extreme than any "
                    "city-dweller could comprehend, and enjoyed the solitude of being the only thinking creature for "
                    "miles in any direction. The wilds are in your blood, whether you were a nomad, an explorer, "
                    "a recluse, a hunter-gatherer, or even a marauder. Even in places where you don't know the "
                    "specific features of the terrain, you know the ways of the wild.",
        personality_traits="I have a lesson for every situation, drawn from observing nature.\n"
                           "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from "
                           "a hungry owlbear.",
        ideals="Glory. I must earn glory in battle, for myself and my clan.",
        bonds="I will bring terrible wrath down on the evildoers who destroyed my homeland.",
        flaws="I am slow to trust members of other species, tribes, and societies.")

    cuzmo = character.Character(
        name="Cuzmo Mountainbeast Elanithino",
        character_class=content["Classes"]["Champion Fighter"](skill1=Skills.INTIMIDATION,
                                                               skill2=Skills.SURVIVAL,
                                                               fighting_style=content["Feats"][
                                                                   "Fighting Style: Great Weapon Fighting"]()),
        character_species=content["Species"]["Stone Goliath"](),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 15,
            AbilityNames.DEXTERITY: 13,
            AbilityNames.CONSTITUTION: 14,
            AbilityNames.INTELLIGENCE: 12,
            AbilityNames.WISDOM: 10,
            AbilityNames.CHARISMA: 8,
        },
        alignment=Alignments.LAWFUL_GOOD,
        player_name="Dad",
        language=Languages.INFERNAL,
        age="50",
        height="7'10\"",
        weight="440 lb.",
        eyes="Gray",
        skin="Gray",
        hair="None",
        appearance_image="characters/images/cuzmo.pdf",
    )

    cuzmo.level_up(0, hit_roll=6)
    cuzmo.level_up(0, hit_roll=6)
    cuzmo.level_up(0, hit_roll=6, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.STRENGTH,
        ability2=AbilityNames.CONSTITUTION
    ))
    cuzmo.level_up(0, hit_roll=6)
    cuzmo.level_up(0, hit_roll=6, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.STRENGTH,
        ability2=AbilityNames.STRENGTH
    ))
    cuzmo.level_up(0, hit_roll=6)
    cuzmo.level_up(0, hit_roll=6, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.CONSTITUTION,
        ability2=AbilityNames.CONSTITUTION
    ))
    cuzmo.level_up(0, hit_roll=6)
    cuzmo.level_up(
        0, hit_roll=7, fighting_style=content["Feats"]["Fighting Style: Blind Fighting"]())
    cuzmo.level_up(0, hit_roll=4)
    cuzmo.level_up(0, hit_roll=6, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.CONSTITUTION,
        ability2=AbilityNames.CONSTITUTION
    ))
    cuzmo.level_up(0, hit_roll=3)

    cuzmo.set_armor(content["Armors"]["Splint"]())
    cuzmo.set_weapons([
        content["Weapons"]["Maul"](attack_bonus=1, damage_bonus=1, magical=True),
        content["Weapons"]["Boomerang"](silvered=True),
        content["Weapons"]["Handaxe"](silvered=True),
    ])

    return cuzmo
