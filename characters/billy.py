"""
Billy "Dragonblood" Kekali. From the Baldur's Gate: Descent into Avernus campaign that I am running with my friends.
"""

from rules import abilities, character, bonuses, magicitem
from rules.enums import AbilityNames, Alignments, GamingSets, Languages, ProficiencyLevels, Skills


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
            constitution=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.INSIGHT: ProficiencyLevels.PROFICIENT,
                Skills.PERSUASION: ProficiencyLevels.PROFICIENT,
            },
            tools={
                GamingSets.DICE_SET: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.GIANT],
        ),
        feat=content["Feats"]["Alert"](),
        personality_traits="I take great pains to always look my best and follow the latest fashions.\n"
                           "I don't like to get my hands dirty, and I won't be caught dead in unsuitable "
                           "accommodations.",
        ideals="Noble Obligation. It is my duty to protect and care for the people beneath me. (Good)",
        bonds="I will face any challenge to win the approval of my family.",
        flaws="By my words and actions, I often bring shame to my family.")

    billy = character.Character(
        name="Billy Dragonblood Kekali",
        character_class=content["Classes"]["Samurai Fighter"](skill1=Skills.ACROBATICS,
                                                              skill2=Skills.ATHLETICS,
                                                              fighting_style=content["Feats"][
                                                                  "Fighting Style: Dueling"]()),
        character_species=content["Species"]["Cloud Goliath"](),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 15,
            AbilityNames.DEXTERITY: 16,
            AbilityNames.CONSTITUTION: 13,
            AbilityNames.INTELLIGENCE: 9,
            AbilityNames.WISDOM: 14,
            AbilityNames.CHARISMA: 6,
        },
        alignment=Alignments.NEUTRAL,
        player_name="Roman",
        language=Languages.GOBLIN,
        age="15",
        height="5'7\"",
        weight="215 lb.",
        eyes="Blue",
        skin="Gray",
        hair="Black",
        faction="Order of the Companions",
        appearance_image="characters/images/billy.pdf",
        faction_image="characters/images/companions.pdf"
    )

    billy.level_up(0, hit_roll=9)
    billy.level_up(0, hit_roll=8, skill=Skills.HISTORY)
    billy.level_up(0, hit_roll=8, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.STRENGTH,
        ability2=AbilityNames.CONSTITUTION
    ))
    billy.level_up(0, hit_roll=8)
    billy.level_up(0, hit_roll=10, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.STRENGTH,
        ability2=AbilityNames.STRENGTH
    ))

    billy.set_armor(content["Armors"]["Breastplate"]())
    billy.set_shield(content["Armors"]["Shield"](
        name="Shield of the Hidden Lord", ac_bonus=2))
    billy.set_weapons([
        content["Weapons"]["Mace"](
            attack_bonus=1, damage_bonus=1, magical=True),
        content["Weapons"]["Longbow"](),
        content["Weapons"]["Handaxe"](silvered=True),
    ])

    billy.set_magic_items(magic_items=[  # TODO better magic items
        magicitem.MagicItem(name="Holy Mace",
                            description="The head of the mace sheds bright light in a 5-foot-radius and dim light for "
                                        "an additional 5 feet. The wielder of the mace and extinguish or ignite its "
                                        "light as an action."),
        magicitem.MagicItem(name="Shield of the Hidden Lord",
                            description="The Shield of the Hidden Lord is of celestial origin and serves as a prison "
                                        "for the pit fiend Gargauth, whose mortal followers revere it as a god. Over "
                                        "time, Gargauth's evil has warped the shield's appearance, so that its "
                                        "celestial motif and designs have become twisted into a fiendish face that "
                                        "subtly moves in disturbing ways.\n"
                                        "While holding this shield, you gain a +2 bonus to AC and resistance to fire "
                                        "damage.\n"
                                        "Sentience. The Shield of the Hidden Lord is sentient as long as it imprisons "
                                        "Gargauth. While sentient, the shield has the following properties:\n"
                                        "• The shield has an Intelligence of 22, a Wisdom of 18, and a Charisma of "
                                        "24, as well as hearing and truesight out to a range of 120 feet.\n"
                                        "• The shield can speak, read, and understand Common and Infernal, and it can "
                                        "communicate telepathically with any creature it can sense within 120 feet of "
                                        "it. Its voice is a deep, hollow whisper.\n"
                                        "• The shield has 3 charges. You can use an action to expend 1 charge to cast "
                                        "Fireball or 2 charges to cast Wall of Fire from the shield (save DC 21 for "
                                        "each). The wall of fire spell lasts for 1 minute (no concentration "
                                        "required). The shield regains all expended charges daily at dawn.")
    ])

    return billy
