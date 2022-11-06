"""
Fena. From the Baldur's Gate: Descent into Avernus campaign that I am running with my family.
"""

from rules import abilities, character, bonuses
from rules.enums import AbilityNames, Alignments, ArtisansTools, Languages, ProficiencyLevels, Skills


def create(content: dict[str, dict[str, any]]) -> character.Character:
    """
    A method that creates and returns a character. For now this is the method of saving character configurations
    :param content: The compiled content of the source files
    :type content: dict[str, dict[str, any]]
    :return: The created character.
    :rtype: character.Character
    """

    custom_background = content["Backgrounds"]["Custom"](
        name="Knight of the Order of the Companion",
        background_abilities=abilities.Abilities(
            strength=2,
            charisma=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.INSIGHT: ProficiencyLevels.PROFICIENT,
                Skills.MEDICINE: ProficiencyLevels.PROFICIENT,
            },
            tools={
                ArtisansTools.ALCHEMISTS_SUPPLIES: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.ABYSSAL],
        ),
        feat=content["Feats"]["Savage Attacker"](),
        description="You belong to an order of knights who have sworn oaths to achieve a certain goal. The nature of "
                    "this goal depends on the order you serve, but in your eyes it is without question a vital and "
                    "honorable endeavor. Faerûn has a wide variety of knightly orders, all of which have a similar "
                    "outlook concerning their actions and responsibilities.\n"
                    "Though the term 'knight' conjures ideas of mounted, heavily armored warriors of noble blood, "
                    "most knightly orders in Faerûn don't restrict their membership to such individuals. The goals "
                    "and philosophies of the order are more important than the gear and fighting style of its "
                    "members, and so most of these orders aren't limited to fighting types, but are open to all sorts "
                    "of folk who are willing to battle and die for the order's cause.\n",
        personality_traits="I'm always polite and respectful.\n"
                           "I've lost too many friends, and I'm slow to make new ones.",
        ideals="Live and Let Live. Ideals aren't worth killing over or going to war for. (Neutral)",
        bonds="I fight for those who cannot fight for themselves.",
        flaws="I made a terrible mistake in battle that cost many lives – and I would do anything to keep that mistake "
              "secret.")

    fena = character.Character(
        name="Fena",
        character_class=content["Classes"]["Oath of the Watchers Paladin"](skill1=Skills.ATHLETICS,
                                                                           skill2=Skills.INTIMIDATION),
        race=content["Races"]["Copper Dragonborn"](),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 16,
            AbilityNames.DEXTERITY: 10,
            AbilityNames.CONSTITUTION: 16,
            AbilityNames.INTELLIGENCE: 12,
            AbilityNames.WISDOM: 13,
            AbilityNames.CHARISMA: 15,
        },
        alignment=Alignments.LAWFUL_GOOD,
        player_name="Mom",
        language=Languages.INFERNAL,
        age="30",
        height="6'9\"",
        weight="350 lb.",
        eyes="Turquoise",
        skin="Copper",
        hair="None",
        appearance_image="characters/images/cuzmo.pdf",  # TODO
    )

    fena.level_up(
        0, hit_roll=6, fighting_style=content["Feats"]["Fighting Style: Defense"]())
    fena.level_up(0, hit_roll=6, content=content)  # TODO
    fena.level_up(0, hit_roll=6)
    fena.level_up(0, hit_roll=6)
    fena.level_up(0, hit_roll=6)
    fena.level_up(0, hit_roll=6)
    fena.level_up(0, hit_roll=6)
    fena.level_up(0, hit_roll=6)
    fena.level_up(0, hit_roll=6)

    return fena
