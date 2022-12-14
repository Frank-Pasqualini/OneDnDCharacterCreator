"""
Fena. From the Baldur's Gate: Descent into Avernus campaign that I am running with my family.
"""

from rules import abilities, character, bonuses, magicitem
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
        name="Outcast",
        background_abilities=abilities.Abilities(
            dexterity=2,
            intelligence=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.INVESTIGATION: ProficiencyLevels.PROFICIENT,
                Skills.SURVIVAL: ProficiencyLevels.PROFICIENT,
            },
            tools={
                Tools.NAVIGATORS_TOOLS: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.ELVISH],
        ),
        feat=content["Feats"]["Tough"](),
        description="You grew up in the wilds, far from civilization and the comforts of town and technology. You've "
                    "witnessed the migration of herds larger than forests, survived weather more extreme than any "
                    "city-dweller could comprehend, and enjoyed the solitude of being the only thinking creature for "
                    "miles in any direction. The wilds are in your blood, whether you were a nomad, an explorer, "
                    "a recluse, a hunter-gatherer, or even a marauder. Even in places where you don't know the "
                    "specific features of the terrain, you know the ways of the wild.",
        personality_traits="I watch over my friends as if they were a litter of newborn pups.\n"
                           "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from "
                           "a hungry owlbear.",
        ideals="Greater Good. It is each person's responsibility to make the most happiness for the whole tribe. "
               "(Good)",
        bonds="My friends are the most important thing in my life, even when they are far from me.",
        flaws="I am slow to trust members of other species, tribes, and societies.")

    tarquin = character.Character(
        name="Tarquin Shadow",
        character_class=content["Classes"]["Order of the Mutant Bloodhunter"](
            skill1=Skills.ACROBATICS,
            skill2=Skills.ARCANA,
            skill3=Skills.ATHLETICS,
            hemocraft_ability=AbilityNames.INTELLIGENCE,
            blood_curse=content["Blood Curses"]["Blood Curse of Binding"]()
        ),
        character_species=content["Species"]["Drow"](
            content, AbilityNames.CHARISMA),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 15,
            AbilityNames.DEXTERITY: 16,
            AbilityNames.CONSTITUTION: 12,
            AbilityNames.INTELLIGENCE: 13,
            AbilityNames.WISDOM: 10,
            AbilityNames.CHARISMA: 13,
        },
        alignment=Alignments.LAWFUL_GOOD,
        player_name="Levi",
        language=Languages.COMMON_SIGN_LANGUAGE,
        age="101",
        height="5'6\"",
        weight="155 lb.",
        eyes="Red",
        skin="Charcoal",
        hair="Pale Yellow",
        faction="Elturel",
        appearance_image="characters/images/tarquin.pdf",
        faction_image="characters/images/elturel.pdf",
    )

    tarquin.level_up(0, hit_roll=7, fighting_style=content["Feats"]["Fighting Style: Dueling"](),
                     crimson_rite=content["Crimson Rites"]["Rite of the Frozen"]())
    tarquin.level_up(0, hit_roll=7, mutagen1=content["Mutagens"]["Mutagen: Embers"](),
                     mutagen2=content["Mutagens"]["Mutagen: Mobility"](),
                     mutagen3=content["Mutagens"]["Mutagen: Percipient"](),
                     mutagen4=content["Mutagens"]["Mutagen: Potency"]())
    tarquin.level_up(0, hit_roll=7, feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.DEXTERITY,
                                                                                       ability2=AbilityNames.DEXTERITY))
    tarquin.level_up(0, hit_roll=7)
    tarquin.level_up(
        0, hit_roll=7, blood_curse=content["Blood Curses"]["Blood Curse of Bloated Agony"]())
    tarquin.level_up(0, hit_roll=7, mutagen=content["Mutagens"]["Mutagen: Rapidity"](),
                     crimson_rite=content["Crimson Rites"]["Rite of the Storm"]())
    tarquin.level_up(0, hit_roll=7, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.INTELLIGENCE,
        ability2=AbilityNames.INTELLIGENCE))
    tarquin.level_up(0, hit_roll=6)
    tarquin.level_up(
        0, hit_roll=6, blood_curse=content["Blood Curses"]["Blood Curse of the Fallen Puppet"]())
    tarquin.level_up(
        0, hit_roll=10, mutagen=content["Mutagens"]["Mutagen: Reconstruction"]())
    tarquin.level_up(
        0, hit_roll=4, feat=content["Feats"]["Drow High Magic"](content=content))
    tarquin.level_up(0, hit_roll=3)

    tarquin.set_armor(content["Armors"]["Studded Leather"]())
    tarquin.set_shield(content["Armors"]["Shield"]())
    tarquin.set_weapons([
        content["Weapons"]["Shortsword"](
            name="Hellfire Shortsword", magical=True),
        content["Weapons"]["Scimitar"](),
    ])

    tarquin.set_magic_items([  # TODO better magic items
        magicitem.MagicItem(name="Hellfire Weapon",
                            description="This weapon is fashioned from infernal iron and traced with veins of "
                                        "hellfire that shed dim light in a 5-foot-radius.\n"
                                        "Any humanoid killed by an attack made with this weapon has its soul "
                                        "funneled into the River Styx, where it's reborn instantly as a lemure "
                                        "devil."),
        magicitem.MagicItem(name="Horn of Valhalla",
                            description="You can use an Action to blow this horn. In response, 3d4 + 3 Warrior "
                                        "spirits from the Valhalla appear within 60 feet of you. They use the "
                                        "Statistics of a Berserker. They Return to Valhalla after 1 hour or when they "
                                        "drop to 0 Hit Points. Once you use the horn, it can't be used again until 7 "
                                        "days have passed."),
    ])

    return tarquin
