"""
Content from the Dungeons and Dragons OneD&D Character Origins Unearthed Arcana.
https://media.dndbeyond.com/compendium-images/one-dnd/character-origins/CSWCVV0M4B6vX6E1/UA2022-CharacterOrigins.pdf
"""

from rules import abilities, backgrounds, bonuses, feats, species, spells
from rules.enums import AbilityNames, ArtisansTools, GamingSets, Languages, MusicalInstruments
from rules.enums import ProficiencyLevels, Sizes, Skills, SpellLists, Tools


class CustomBackground(backgrounds.Background):
    """
    A custom Background
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Acolyte(backgrounds.Background):
    """
    Acolyte example Background
    UA p. 11
    """

    def __init__(self,
                 cantrip1: spells.Spell,
                 cantrip2: spells.Spell,
                 spell: spells.Spell,
                 ability: AbilityNames):
        super().__init__(name="Acolyte",
                         background_abilities=abilities.Abilities(
                             wisdom=2, intelligence=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.INSIGHT: ProficiencyLevels.PROFICIENT,
                                 Skills.RELIGION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 ArtisansTools.CALLIGRAPHERS_SUPPLIES: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.CELESTIAL],
                         ),
                         feat=MagicInitiate(
                             SpellLists.DIVINE, cantrip1, cantrip2, spell, ability),
                         description="You devoted yourself to service in a temple, either nestled in a town or "
                                     "secluded in a sacred grove. There you performed hallowed rites in honor of a "
                                     "god or pantheon. You served under a priest and studied religion. Thanks to your "
                                     "priest's instruction and your own devotion, you also learned how to channel a "
                                     "modicum of divine power in service to your place of worship and the people "
                                     "who prayed there.")


class Artisan(backgrounds.Background):
    """
    Artisan example Background
    UA p. 12
    """

    def __init__(self,
                 tool1: ArtisansTools,
                 tool2: ArtisansTools,
                 tool3: ArtisansTools,
                 tool4: ArtisansTools):
        if tool1 in [tool2, tool3, tool4]:
            raise Exception("All tools should be unique")

        super().__init__(name="Artisan",
                         background_abilities=abilities.Abilities(
                             intelligence=2, charisma=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.INVESTIGATION: ProficiencyLevels.PROFICIENT,
                                 Skills.PERSUASION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 tool1: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.GNOMISH],
                         ),
                         feat=Crafter(tool2, tool3, tool4),
                         description="You began mopping floors and scrubbing counters in an artisan's workshop for a "
                                     "few coppers per day as soon as you were strong enough to carry a bucket. When "
                                     "you were finally old enough to apprentice, you learned to create basic crafts "
                                     "of your own, as well as how to sweet-talk the occasional demanding customer. As "
                                     "part of your studies,you picked up Gnomish, the tongue from which so many of "
                                     "the artisan's terms of art are derived.")


class Charlatan(backgrounds.Background):
    """
    Charlatan example Background
    UA p. 12
    """

    def __init__(self,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills):
        super().__init__(name="Charlatan",
                         background_abilities=abilities.Abilities(
                             charisma=2, dexterity=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.DECEPTION: ProficiencyLevels.PROFICIENT,
                                 Skills.SLEIGHT_OF_HAND: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.FORGERY_KIT: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.INFERNAL],
                         ),
                         feat=Skilled(skill1, skill2, skill3),
                         description="Soon after you were old enough to order an ale, you already had a favorite "
                                     "stool in every tavern within ten miles of where you were born. As you traveled "
                                     "the circuit from public house to watering hole, you learned to prey on the "
                                     "unfortunates who were in the market for a comforting lie or two-perhaps a sham "
                                     "potion or a forged 'treasure map.' You are fluent in Infernal,the ancient "
                                     "language of deception.")


class Criminal(backgrounds.Background):
    """
    Criminal example Background
    UA p. 12
    """

    def __init__(self):
        super().__init__(name="Criminal",
                         background_abilities=abilities.Abilities(
                             dexterity=2, intelligence=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.SLEIGHT_OF_HAND: ProficiencyLevels.PROFICIENT,
                                 Skills.STEALTH: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.THIEVES_TOOLS: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.THIEVES_CANT],
                         ),
                         feat=Alert(),
                         description="You learned to earn your coin in dark alleyways, cutting purses or burgling "
                                     "shops. Perhaps you were part of a small gang of like-minded wrongdoers, "
                                     "who looked out for each other. Or maybe you were a lone wolf, fending for "
                                     "yourself against the local thieves' guild and older, more fearsome lawbreakers.")


class Cultist(backgrounds.Background):
    """
    Cultist example Background
    UA p. 12
    """

    def __init__(self,
                 cantrip1: spells.Spell,
                 cantrip2: spells.Spell,
                 spell: spells.Spell,
                 ability: AbilityNames):
        super().__init__(name="Cultist",
                         background_abilities=abilities.Abilities(
                             intelligence=2, charisma=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ARCANA: ProficiencyLevels.PROFICIENT,
                                 Skills.RELIGION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.DISGUISE_KIT: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.ABYSSAL],
                         ),
                         feat=MagicInitiate(
                             SpellLists.ARCANE, cantrip1, cantrip2, spell, ability),
                         description="You scarcely recall what drove you into the service of the otherworldly "
                                     "being. Those memories were blotted out long ago by recurrent dreams of midnight "
                                     "gatherings round the obsidian pillar in the glade. By the light of each waning "
                                     "moon, the hierophants instructed you in the being's creed and the rudiments of "
                                     "the arcane arts. When you came of age, you were ordered to blend in among the "
                                     "nonbelievers and await whatever mission the Great One has in store for you.")


class Entertainer(backgrounds.Background):
    """
    Entertainer example Background
    UA p. 12-13
    """

    def __init__(self,
                 instrument1: MusicalInstruments,
                 instrument2: MusicalInstruments,
                 instrument3: MusicalInstruments,
                 instrument4: MusicalInstruments):
        if instrument1 in [instrument2, instrument3, instrument4]:
            raise Exception("All tools should be unique")

        super().__init__(name="Entertainer",
                         background_abilities=abilities.Abilities(
                             charisma=2, dexterity=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ACROBATICS: ProficiencyLevels.PROFICIENT,
                                 Skills.PERFORMANCE: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 instrument1: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.ELVISH],
                         ),
                         feat=Musician(instrument2, instrument3, instrument4),
                         description="You spent much of your youth following roving fairs and carnivals, performing "
                                     "odd jobs for musicians and acrobats in exchange for lessons. You may have "
                                     "learned how to walk a tightrope, how to double pick a lute, or how to recite "
                                     "Elvish poetry with the impeccable trills of an elf poet. To this day, "
                                     "you thrive on applause and long for the stage.")


class Farmer(backgrounds.Background):
    """
    Farmer example Background
    UA p. 13
    """

    def __init__(self):
        super().__init__(name="Farmer",
                         background_abilities=abilities.Abilities(
                             constitution=2, wisdom=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ANIMAL_HANDLING: ProficiencyLevels.PROFICIENT,
                                 Skills.NATURE: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 ArtisansTools.CARPENTERS_TOOLS: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.HALFLING],
                         ),
                         feat=Tough(),
                         description="You grew up close to the land. Years tending animals and cultivating the earth "
                                     "rewarded you with patience and good health. You have a keen appreciation for "
                                     "nature's bounty alongside a healthy respect for nature's wrath. Like many "
                                     "farmers, you made frequent use of the agricultural almanacs produced by the "
                                     "greatest halfling farmers.")


class Gladiator(backgrounds.Background):
    """
    Gladiator example Background
    UA p. 13
    """

    def __init__(self):
        super().__init__(name="Gladiator",
                         background_abilities=abilities.Abilities(
                             strength=2, charisma=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ATHLETICS: ProficiencyLevels.PROFICIENT,
                                 Skills.PERFORMANCE: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 ArtisansTools.SMITHS_TOOLS: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.ORC],
                         ),
                         feat=SavageAttacker(),
                         description="Your first few appearances in the gladiatorial pits led you to appreciate every "
                                     "one of the scars you carry from your instructors ands parring partners. Each "
                                     "scar was a lesson that taught you how to best your opponents and curry favor "
                                     "with the crowds your brawls entertained. Your time in the pits left you with a "
                                     "strong hand and a strong heart. You'll forever share a remarkable bond with the "
                                     "other pit fighters in your stable-humans, dragonborn, dwarves, "
                                     "and orcs-hardened warriors all.")


class Guard(backgrounds.Background):
    """
    Guard example Background
    UA p. 13
    """

    def __init__(self,
                 gaming_set: GamingSets):
        super().__init__(name="Guard",
                         background_abilities=abilities.Abilities(
                             strength=2, wisdom=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ATHLETICS: ProficiencyLevels.PROFICIENT,
                                 Skills.PERCEPTION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 gaming_set: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.DWARVISH],
                         ),
                         feat=Alert(),
                         description="Your feet begin to ache when you remember the countless hours you spent at your "
                                     "post in the tower. You were trained to keep one eye outside the wall, "
                                     "watching for marauders sweeping from the nearby forest, and your other eye "
                                     "inside the wall, searching for cutpurses and troublemakers. At the end of each "
                                     "shift, you bunked in the mayor's barracks alongside your fellow sentries and "
                                     "the dwarven smiths who kept your armor snug and your weapons sharp.")


class Guide(backgrounds.Background):
    """
    Guide example Background
    UA p. 13-14
    """

    def __init__(self,
                 cantrip1: spells.Spell,
                 cantrip2: spells.Spell,
                 spell: spells.Spell,
                 ability: AbilityNames
                 ):
        super().__init__(name="Guide",
                         background_abilities=abilities.Abilities(
                             wisdom=2, dexterity=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.STEALTH: ProficiencyLevels.PROFICIENT,
                                 Skills.SURVIVAL: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 ArtisansTools.CARTOGRAPHERS_TOOLS: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.GIANT],
                         ),
                         feat=MagicInitiate(spell_list=SpellLists.PRIMAL,
                                            cantrip1=cantrip1,
                                            cantrip2=cantrip2,
                                            spell=spell,
                                            ability=ability),
                         description="You came of age in the outdoors, far from settled lands. Your home? Any where "
                                     "you chose to unfurl your bedroll. There are wonders on the frontier-strange "
                                     "monsters, pristine forests and streams, overgrown ruins of great halls once "
                                     "trod by giants-and you learned to fend for yourself as you explored them. From "
                                     "time to time, you traveled with a pair of friendly druids who were kind enough "
                                     "to instruct you in the fundamentals of channeling the magic of the wild.")


class Hermit(backgrounds.Background):
    """
    Hermit example Background
    UA p. 14
    """

    def __init__(self,
                 cantrip1: spells.Spell,
                 cantrip2: spells.Spell,
                 spell: spells.Spell,
                 ability: AbilityNames
                 ):
        super().__init__(name="Hermit",
                         background_abilities=abilities.Abilities(
                             wisdom=2, constitution=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.MEDICINE: ProficiencyLevels.PROFICIENT,
                                 Skills.RELIGION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.HERBALISM_KIT: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.SYLVAN],
                         ),
                         feat=MagicInitiate(spell_list=SpellLists.PRIMAL,
                                            cantrip1=cantrip1,
                                            cantrip2=cantrip2,
                                            spell=spell,
                                            ability=ability),
                         description="You spent your early years secluded in a hut or monastery located well beyond "
                                     "the outskirts of the nearest settlement. In those days, your only companions "
                                     "were the creatures of the forest, who would occasionally visit to bring news of "
                                     "the outside world and supplies. The quiet and solitude you found in your time "
                                     "outside society allowed you to spend many hours pondering the mysteries of "
                                     "creation, attuning your mind to the magical energy flowing through the natural "
                                     "world.")


class Laborer(backgrounds.Background):
    """
    Laborer example Background
    UA p. 14
    """

    def __init__(self):
        super().__init__(name="Laborer",
                         background_abilities=abilities.Abilities(
                             constitution=2, strength=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ATHLETICS: ProficiencyLevels.PROFICIENT,
                                 Skills.SURVIVAL: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 ArtisansTools.MASONS_TOOLS: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.DWARVISH],
                         ),
                         feat=Tough(),
                         description="Your apprenticeship consumed the better part of your youth. First, you learned "
                                     "to cut and polish a stone. After several years of polishing stones, you learned "
                                     "how to cement those stones into a wall. After several years building walls, "
                                     "you learned to join your walls to form a structure. The structures you built "
                                     "were exceptionally durable. The masons who taught you were taught by even older "
                                     "masons who were taught by dwarf artisans of old.")


class Noble(backgrounds.Background):
    """
    Noble example Background
    UA p. 14
    """

    def __init__(self,
                 gaming_set: GamingSets,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills):
        super().__init__(name="Noble",
                         background_abilities=abilities.Abilities(
                             charisma=2, intelligence=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.HISTORY: ProficiencyLevels.PROFICIENT,
                                 Skills.PERSUASION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 gaming_set: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.DRACONIC],
                         ),
                         feat=Skilled(skill1, skill2, skill3),
                         description="You were raised in a castle as a creature of wealth, power, and privilege-none "
                                     "of it earned. Your family are minor aristocrats who saw to it that you received "
                                     "a first-class education, some of which you appreciated and some of which you "
                                     "resented. (Was it truly necessary to read all those ancient histories in their "
                                     "original Draconic?) Your time in the castle, especially the many hours you "
                                     "spent observing your family at court, also taught you a great deal about "
                                     "leadership.")


class Pilgrim(backgrounds.Background):
    """
    Pilgrim example Background
    UA p. 14-15
    """

    def __init__(self, instrument: MusicalInstruments):
        super().__init__(name="Pilgrim",
                         background_abilities=abilities.Abilities(
                             wisdom=2, constitution=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.RELIGION: ProficiencyLevels.PROFICIENT,
                                 Skills.SURVIVAL: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 instrument: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.HALFLING],
                         ),
                         feat=Healer(),
                         description="You and a group of like-minded believers-mostly humans and halflings-once "
                                     "endeavored to walk a thousand miles of road to reach a faraway shrine. Priests "
                                     "counseled at the outset that, long after your journey was complete, you'd come "
                                     "to realize that you found the key to your salvation not at your destination, "
                                     "but somewhere along the road that led there.")


class Sage(backgrounds.Background):
    """
    Sage example Background
    UA p. 15
    """

    def __init__(self,
                 cantrip1: spells.Spell,
                 cantrip2: spells.Spell,
                 spell: spells.Spell,
                 ability: AbilityNames
                 ):
        super().__init__(name="Sage",
                         background_abilities=abilities.Abilities(
                             intelligence=2, wisdom=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ARCANA: ProficiencyLevels.PROFICIENT,
                                 Skills.HISTORY: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 ArtisansTools.CALLIGRAPHERS_SUPPLIES: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.ELVISH],
                         ),
                         feat=MagicInitiate(spell_list=SpellLists.ARCANE,
                                            cantrip1=cantrip1,
                                            cantrip2=cantrip2,
                                            spell=spell,
                                            ability=ability),
                         description="You spent your formative years traveling between manors and monasteries, "
                                     "performing various odd jobs and services in exchange for access to their "
                                     "libraries. You wiled away many a long evening with your nose buried in books "
                                     "and scrolls, learning the lore of the multiverse-even the rudiments of "
                                     "magic-and your mind only yearns for more.")


class Sailor(backgrounds.Background):
    """
    Sailor example Background
    UA p. 15
    """

    def __init__(self):
        super().__init__(name="Sailor",
                         background_abilities=abilities.Abilities(
                             dexterity=2, wisdom=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ACROBATICS: ProficiencyLevels.PROFICIENT,
                                 Skills.PERCEPTION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.NAVIGATORS_TOOLS: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.PRIMORDIAL],
                         ),
                         feat=TavernBrawler(),
                         description="Thus far, you've spent most of your days living the life of a seafarer, "
                                     "wind at your back and decks swaying beneath your feet, as you sailed toward "
                                     "your next adventure. You've perched on barstools in more ports of call than you "
                                     "can remember, faced down mighty storms, and swapped stories with the folk who "
                                     "live beneath the waves.")


class Soldier(backgrounds.Background):
    """
    Soldier example Background
    UA p. 15
    """

    def __init__(self,
                 gaming_set: GamingSets):
        super().__init__(name="Soldier",
                         background_abilities=abilities.Abilities(
                             strength=2, constitution=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.ATHLETICS: ProficiencyLevels.PROFICIENT,
                                 Skills.INTIMIDATION: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 gaming_set: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.GOBLIN],
                         ),
                         feat=SavageAttacker(),
                         description="You began training for war at such an early age that you carry only a precious "
                                     "few memories of what life was like before you took up arms. Battle is in your "
                                     "blood. Sometimes you catch yourself reflexively performing the basic fighting "
                                     "exercises you learned as a youth. Eventually, you put that training to use on "
                                     "the battlefield, protecting the realm by waging war and studying the strategies "
                                     "of goblinoid generals.")


class Urchin(backgrounds.Background):
    """
    Urchin example Background
    UA p. 15
    """

    def __init__(self):
        super().__init__(name="Urchin",
                         background_abilities=abilities.Abilities(
                             dexterity=2, wisdom=1),
                         background_bonuses=bonuses.Bonuses(
                             skills={
                                 Skills.INSIGHT: ProficiencyLevels.PROFICIENT,
                                 Skills.STEALTH: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.THIEVES_TOOLS: ProficiencyLevels.PROFICIENT,
                             },
                             languages=[Languages.COMMON_SIGN_LANGUAGE],
                         ),
                         feat=Lucky(),
                         description="You grew up on the streets, surrounded by similarly ill-fated castoffs, "
                                     "a few of them friends and a few of them rivals. You slept where you could and "
                                     "did odd jobs for food. At times, when the hunger became unbearable, "
                                     "you resorted to theft. Still, you never lost your pride and never abandoned "
                                     "hope. Fate is not yet finished with you.")


class Alert(feats.Feat):
    """
    Alert Feat
    UA p. 16
    """

    def __init__(self):
        super().__init__(name="Alert",
                         level=1,
                         description="Always on the lookout for danger, you gain the following benefits:\n"
                                     "Initiative Proficiency. When you roll Initiative, you can add your Proficiency "
                                     "Bonus to the roll.\n"
                                     "Initiative Swap. Immediately after you roll Initiative, you can swap your "
                                     "Initiative with the Initiative of one willing ally in the same combat. You "
                                     "can't make this swap if you or the ally is Incapacitated.",
                         feat_bonuses=bonuses.Bonuses(initiative=ProficiencyLevels.PROFICIENT))


class Crafter(feats.Feat):
    """
    Crafter Feat
    UA p. 16
    """

    def __init__(self, tool1: ArtisansTools, tool2: ArtisansTools, tool3: ArtisansTools):
        if tool1 == tool2 or tool1 == tool3 or tool2 == tool3:
            raise Exception("All 3 tools should be unique")

        super().__init__(name="Crafter",
                         level=1,
                         description="You are adept at crafting things and bargaining with merchants, granting you "
                                     "the following benefits:\n"
                                     f"Tool Proficiency. You gain Tool Proficiency with {tool1.value}, {tool2.value}, "
                                     f"and {tool3.value}.\n"
                                     "Discount. Whenever you buy a nonmagical item, you receive a 20 percent discount "
                                     "on it.\n"
                                     "Faster Crafting. When you craft an item using a tool with which you have Tool "
                                     "Proficiency, the required crafting time is reduced by 20 percent.",
                         feat_bonuses=bonuses.Bonuses(tools={
                             tool1: ProficiencyLevels.PROFICIENT,
                             tool2: ProficiencyLevels.PROFICIENT,
                             tool3: ProficiencyLevels.PROFICIENT,
                         }))


class Healer(feats.Feat):
    """
    Healer Feat
    UA p. 16-17
    """

    def __init__(self):
        super().__init__(name="Healer",
                         level=1,
                         description="You have the training and intuition to administer first aid and other care "
                                     "effectively, granting you the following benefits:\n"
                                     "Battle Medic. If you have a Healer's Kit, you can expend one use of it and tend "
                                     "to a creature within 5 feet of you as an Action. That creature can expend one "
                                     "of its Hit Dice, and you then roll that die. The creature regains a number of "
                                     "Hit Points equal to the roll plus your Proficiency Bonus.\n"
                                     "Healing Rerolls. Whenever you roll a die to determine the number of Hit Points "
                                     "you restore with a spell or with this feat's Battle Medic benefit, you can "
                                     "reroll the die if it rolls a 1, and you must use the new roll.")


class Lucky(feats.Feat):
    """
    Lucky Feat
    UA p. 17
    """

    def __init__(self):
        super().__init__(name="Lucky",
                         level=1,
                         description="You have inexplicable luck that can kick in at just the right moment, granting "
                                     "you the following benefits:\n"
                                     "Luck Points. You have a number of Luck Points equal to your Proficiency Bonus. "
                                     "You can spend the points on the benefits below, and you regain your expended "
                                     "Luck Points when you finish a Long Rest.\n"
                                     "Advantage. Immediately after you roll a d20 for a d20 Test, you can spend 1 "
                                     "Luck Point to give yourself Advantage on the roll.\n"
                                     "Disadvantage. When a creature rolls a d20 for an attack roll against you, "
                                     "you can spend 1 Luck Point to impose Disadvantage on that roll.")


class MagicInitiate(feats.Feat):
    """
    Magic Initiate Feat
    UA p. 17
    """

    def __init__(self,
                 spell_list: SpellLists,
                 cantrip1: spells.Spell,
                 cantrip2: spells.Spell,
                 spell: spells.Spell,
                 ability: AbilityNames):

        if cantrip1.get_level() != 0 or cantrip2.get_level() != 0 or spell.get_level() != 1:
            raise Exception("Invalid spell levels")

        if spell_list not in cantrip1.get_spell_lists() or spell_list not in cantrip2.get_spell_lists():
            raise Exception("All cantrips must be in the proper Spell List")

        if spell_list not in spell.get_spell_lists():
            raise Exception("All spells must be in the proper Spell List")

        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception(
                "Spellcasting ability must be one of the mental abilities.")

        super().__init__(name="Magic Initiate",
                         level=1,
                         description=f"You have learned the basics of a the {spell_list.value} magical tradition. You "
                                     "gain the following benefits related to that choice:\n"
                                     f"Two Cantrips. You learn {cantrip1.get_name()} and {cantrip2.get_name()}.\n"
                                     f"1st-Level Spell. You learn {spell.get_name()}. You always have "
                                     f"{spell.get_name()} prepared. You can cast it once without a Spell Slot, "
                                     f"and you regain the ability to cast it in that way when you finish a Long Rest. "
                                     f"You can also cast {spell.get_name()} using any Spell Slots you have.\n"
                                     f"{ability.value} is your spellcasting ability for these Spells.\n"
                                     "Whenever you gain a new level, you can replace one of the Spells you chose for "
                                     "this Feat with a different Spell of the same level from the chosen Spell list.",
                         repeatable="Yes, but you must choose a different Spell List each time",
                         feat_spells=[cantrip1, cantrip2, spell],
                         spellcasting_ability=ability)


class Musician(feats.Feat):
    """
    Musician Feat
    UA p. 17
    """

    def __init__(self, instrument1: MusicalInstruments, instrument2: MusicalInstruments,
                 instrument3: MusicalInstruments):
        if instrument1 == instrument2 or instrument1 == instrument3 or instrument2 == instrument3:
            raise Exception("All 3 instruments should be unique")

        super().__init__(name="Musician",
                         level=1,
                         description="You are a practiced musician, granting you the following benefits:\n"
                                     f"Instrument Training. You gain Tool Proficiency with {instrument1.value}, "
                                     f"{instrument2.value}, and {instrument3.value}.\n"
                                     "Inspiring Song. As you finish a Short Rest or a Long Rest, you can play a song "
                                     "on a Musical Instrument with which you have Tool Proficiency and give "
                                     "Inspiration to allies who hear the song. The number of allies you can affect in "
                                     "this way equals your Proficiency Bonus.",
                         feat_bonuses=bonuses.Bonuses(tools={
                             instrument1: ProficiencyLevels.PROFICIENT,
                             instrument2: ProficiencyLevels.PROFICIENT,
                             instrument3: ProficiencyLevels.PROFICIENT,
                         }))


class SavageAttacker(feats.Feat):
    """
    Savage Attacker Feat
    UA p. 17
    """

    def __init__(self):
        super().__init__(name="Savage Attacker",
                         level=1,
                         description="You have trained to deal particularly damaging strikes. When you take the "
                                     "Attack Action and hit a target with a Weapon as part of that Action, "
                                     "you can roll the Weapon's damage dice twice and use either roll against the "
                                     "target. You can use this benefit only once per turn.")


class Skilled(feats.Feat):
    """
    Skilled Feat
    UA p. 17-18
    """

    def __init__(self, skill1: Skills, skill2: Skills, skill3: Skills):
        if skill1 == skill2 or skill1 == skill3 or skill2 == skill3:
            raise Exception("All 3 skills should be unique")

        super().__init__(name="Skilled",
                         level=1,
                         description=f"You have exceptionally broad learning. You gain Proficiency in {skill1.value}, "
                                     f"{skill2.value}, and {skill3.value}.",
                         repeatable="Yes",
                         feat_bonuses=bonuses.Bonuses(
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                                 skill3: ProficiencyLevels.PROFICIENT,
                             }),
                         visible=False)


class TavernBrawler(feats.Feat):
    """
    Tavern Brawler Feat
    UA p. 18
    """

    def __init__(self):
        super().__init__(name="Tavern Brawler",
                         level=1,
                         description="Accustomed to brawling, you gain the following benefits:\n"
                                     "Enhanced Unarmed Strike. When you hit with your Unarmed Strike and deal damage, "
                                     "you can deal Bludgeoning Damage equal to 1d4 + your Strength modifier, instead "
                                     "of the normal damage of an Unarmed Strike.\n"
                                     "Damage Rerolls. Whenever you roll a damage die for your Unarmed Strike, "
                                     "you can reroll the die if it rolls a 1, and you must use the new roll.\n"
                                     "Shove. When you hit a creature with an Unarmed Strike as part of the Attack "
                                     "Action on your turn, you can deal damage to the target and also push it 5 feet "
                                     "away. You can use this benefit only once per turn.\n"
                                     "Furniture as Weapons. You can wield furniture as a Weapon, using the rules of "
                                     "the Greatclub for Small or Medium furniture and the rules of the Club for Tiny "
                                     "furniture.")


class Tough(feats.Feat):
    """
    Tough Feat
    UA p. 18
    """

    def __init__(self):
        super().__init__(name="Tough",
                         level=1,
                         description="Your Hit Point Maximum increases by an amount equal to twice your character "
                                     "level when you gain this Feat. Whenever you gain a level thereafter, "
                                     "your Hit Point Maximum increases by an additional 2 Hit Points.",
                         feat_bonuses=bonuses.Bonuses(hp_bonus=True))


class Human(species.Species):
    """
    Human Species
    UA p. 2-3
    """

    def __init__(self,
                 skill: Skills,
                 versatile: feats.Feat,
                 size: Sizes = Sizes.MEDIUM):
        if size not in [Sizes.SMALL, Sizes.MEDIUM]:
            raise Exception("Invalid Size")

        if versatile.get_level() != 1:
            raise Exception("Humans can only start with a first level Feat")

        super().__init__(name="Human",
                         features=[
                             feats.Feat(name="Resourceful",
                                        description="You gain inspiration whenever you finish a Long Rest."),
                             feats.Feat(name="Skillful",
                                        description=f"You gain proficiency in {skill.value}",
                                        feat_bonuses=bonuses.Bonuses(
                                            skills={
                                                skill: ProficiencyLevels.PROFICIENT
                                            }),
                                        visible=False),
                             versatile,
                         ],
                         size=size,
                         life_span=80)


class Dwarf(species.Species):
    """
    Dwarf Species
    UA p. 5-6
    """

    def __init__(self, tool1: ArtisansTools, tool2: ArtisansTools):
        valid_tools = [ArtisansTools.JEWELERS_TOOLS, ArtisansTools.MASONS_TOOLS,
                       ArtisansTools.SMITHS_TOOLS, ArtisansTools.TINKERS_TOOLS]
        if tool1 not in valid_tools or tool2 not in valid_tools or tool1 == tool2:
            raise Exception("This tool selection is not valid")

        super().__init__(name="Dwarf",
                         features=[
                             feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             feats.Feat(
                                 name="Dwarven Resilience",
                                 description="You have Resistance to Poison Damage. You also have Advantage on saving "
                                             "throws you make to avoid or end the Poisoned Condition on yourself."
                             ),
                             feats.Feat(
                                 name="Dwarven Toughness",
                                 description="Your Hit Point Maximum increases by 1, and it increases by 1 again "
                                             "whenever you gain a level.",
                                 feat_bonuses=bonuses.Bonuses(hp_bonus=1)
                             ),
                             feats.Feat(
                                 name="Forge Wise",
                                 description="Your divine creator gave you an uncanny affinity for working with stone "
                                             f"or metal. You gain Tool Proficiency with {tool1.value} and "
                                             f"{tool2.value}.",
                                 visible=False,
                             ),
                             feats.Feat(
                                 name="Stonecunning",
                                 description="As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 "
                                             "minutes. You must be on a stone surface or touching such a surface to "
                                             "use this Tremorsense. The stone can be natural or worked.\n"
                                             "You can use this Bonus Action a number of times equal to your "
                                             "Proficiency Bonus, and you regain all expended uses when you finish a "
                                             "Long Rest."
                             )
                         ],
                         life_span=350)


class Elf(species.Species):
    """
    Elf Species
    UA p. 6-7
    """

    def __init__(self,
                 name: str,
                 lineage: feats.Feat,
                 ability: AbilityNames,
                 darkvision: feats.Feat = feats.Feat(
                     name="Darkvision",
                     description="You have Darkvision with a range of 60 feet."
                 ),
                 speed: int = 30):
        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception(
                "Spellcasting ability must be one of the mental abilities.")

        super().__init__(name=name,
                         features=[
                             darkvision,
                             lineage,
                             feats.Feat(
                                 name="Fey Ancestry",
                                 description="You have Advantage on saving throws you make to avoid or end the "
                                             "Charmed Condition on yourself."
                             ),
                             feats.Feat(
                                 name="Keen Senses",
                                 description="You have Proficiency in the Perception Skill.",
                                 feat_bonuses=bonuses.Bonuses(
                                     skills={Skills.PERCEPTION: ProficiencyLevels.PROFICIENT}),
                                 visible=False,
                             ),
                             feats.Feat(
                                 name="Trance",
                                 description="You don't need to sleep,and magic can't put you to sleep.You can finish "
                                             "a Long Rest in 4 hours if you spend those hours in a trancelike "
                                             "meditation, during which you retain consciousness."
                             )
                         ],
                         speed=speed,
                         life_span=750)


class Drow(Elf):
    """
    Elf Species
    UA p. 6-7
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames):
        super().__init__(name="Drow",
                         lineage=feats.Feat(
                             name="Elven Lineage",
                             description="You are part of an elven lineage that grants you supernatural abilities. "
                                         "Your Drow lineage is of the Underdark. You know the Dancing Lights cantrip.\n"
                                         "Starting at 3rd level and again at 5th level, you also gain the ability to "
                                         "cast a Spell with this trait, Faerie Fire and Darkness. Once you cast the "
                                         "Spell with this trait, you can't cast that Spell with it again until you "
                                         "finish a Long Rest; however, you can cast the Spell using any Spell Slots "
                                         "you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             feat_spells=[content["Spells"]["Dancing Lights"](),
                                          content["Spells"]["Faerie Fire"](),
                                          content["Spells"]["Darkness"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability,
                         darkvision=feats.Feat(
                             name="Darkvision",
                             description="You have Darkvision with a range of 120 feet."
                         ))


class HighElf(Elf):
    """
    Elf Species
    UA p. 6-7
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames):
        super().__init__(name="High Elf",
                         lineage=feats.Feat(
                             name="Elven Lineage",
                             description="You are part of an elven lineage that grants you supernatural abilities. "
                                         "Your High Elf lineage is of fey crossings and other magical locations. "
                                         "You know the Prestidigitation cantrip. Whenever you finish a Long Rest, "
                                         "you can replace that cantrip with a different cantrip from the Arcane Spell "
                                         "List.\n"
                                         "Starting at 3rd level and again at 5th level, you also gain the ability to "
                                         "cast a Spell with this trait, Detect Magic and Misty Step. Once you cast the "
                                         "Spell with this trait, you can't cast that Spell with it again until you "
                                         "finish a Long Rest; however, you can cast the Spell using any Spell Slots "
                                         "you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             feat_spells=[content["Spells"]["Poison Spray"](),
                                          content["Spells"]["Animal Friendship"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability)


class WoodElf(Elf):
    """
    Elf Species
    UA p. 6-7
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames):
        super().__init__(name="Wood Elf",
                         lineage=feats.Feat(
                             name="Elven Lineage",
                             description="You are part of an elven lineage that grants you supernatural abilities. "
                                         "Your Wood Elf lineage is of primeval forests. Your Speed increases to 35 "
                                         "feet. You know the Druidcraft cantrip.\n"
                                         "Starting at 3rd level and again at 5th level, you also gain the ability to "
                                         "cast a Spell with this trait, Longstrider and Pass Without Trace. Once you "
                                         "cast the Spell with this trait, you can't cast that Spell with it again "
                                         "until you finish a Long Rest; however, you can cast the Spell using any "
                                         "Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             feat_spells=[content["Spells"]["Druidcraft"](),
                                          content["Spells"]["Longstrider"](),
                                          content["Spells"]["Pass Without Trace"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability,
                         speed=35)


class Gnome(species.Species):
    """
    Gnome Species
    UA p. 7-8
    """

    def __init__(self,
                 name: str,
                 lineage: feats.Feat,
                 ability: AbilityNames):
        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception(
                "Spellcasting ability must be one of the mental abilities.")

        super().__init__(name=name,
                         features=[
                             feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             feats.Feat(
                                 name="Gnomish Cunning",
                                 description="You have Advantage on Intelligence, Wisdom, and Charisma saving throws."
                             ),
                             lineage
                         ],
                         size=Sizes.SMALL,
                         life_span=425)


class ForestGnome(Gnome):
    """
    Gnome Species
    UA p. 7-8
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames):
        super().__init__(name="Forest Gnome",
                         lineage=feats.Feat(
                             name="Gnomish Lineage",
                             description="You are part of a gnomish lineage that grants you supernatural abilities. "
                                         "Your Forest lineage is of magic-filled forests. You know the Minor Illusion "
                                         "cantrip.\n"
                                         "You can also cast the Speak with Animals Spell with this trait. You can "
                                         "cast it with the trait a number of times equal to your Proficiency Bonus, "
                                         "and you regain all expended uses when you finish a Long Rest. You can also "
                                         "use any Spell Slots you have to cast the Spell.",
                             feat_spells=[content["Spells"]["Minor Illusion"](),
                                          content["Spells"]["Speak with Animals"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability)


class RockGnome(Gnome):
    """
    Gnome Species
    UA p. 7-8
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames):
        super().__init__(name="Rock Gnome",
                         lineage=feats.Feat(
                             name="Gnomish Lineage",
                             description="You are part of a gnomish lineage that grants you supernatural abilities. "
                                         "Your Rock lineage is of primeval mountains. You know the Mending and "
                                         "Prestidigitation cantrips.\n"
                                         "In addition, you can spend 10 minutes casting Prestidigitation to create a "
                                         "Tiny clockwork device (AC 5, 1 HP), such as a toy, a fire starter, "
                                         "or a music box. Casting the Spell in this way consumes 10 GP worth of raw "
                                         "material (string, gears, and the like), which you provide during the "
                                         "casting.\n"
                                         "When you create the device, you determine its function by choosing one "
                                         "effect from Prestidigitation; the device produces that effect whenever you "
                                         "or another creature takes a Bonus Action to touch the device and activate "
                                         "it. If the chosen effect has options within it, you choose one of those "
                                         "options for the device when you create it. For example, if you choose the "
                                         "spell's ignite-extinguish effect, you determine whether the device ignites "
                                         "or extinguishes fire; the device doesn't do both.\n"
                                         "You can have three such devices in existence at a time, and each one "
                                         "dismantles itself 8 hours after its creation. You can also touch one of "
                                         "your devices and dismantle it as an Action. After a device is dismantled, "
                                         "the 10 GP of materials used to create it can be reclaimed.",
                             feat_spells=[content["Spells"]["Mending"](),
                                          content["Spells"]["Prestidigitation"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability)


class Halfling(species.Species):
    """
    Halfling Species
    UA p. 8-9
    """

    def __init__(self):
        super().__init__(name="Halfling",
                         features=[
                             feats.Feat(
                                 name="Brave",
                                 description="You have Advantage on saving throws you make to avoid or end the "
                                             "Frightened Condition on yourself."
                             ),
                             feats.Feat(
                                 name="Halfling Nimbleness",
                                 description="You can move through the space of any creature that is of a Size larger "
                                             "than yours, but you can't stop there."
                             ),
                             feats.Feat(
                                 name="Luck",
                                 description="When your oll a 1 on the d20 of a d20 Test, you can reroll the die, "
                                             "and you must use the new roll."
                             ),
                             feats.Feat(
                                 name="Naturally Stealthy",
                                 description="You have Proficiency in the Stealth Skill.",
                                 feat_bonuses=bonuses.Bonuses(
                                     skills={Skills.STEALTH: ProficiencyLevels.PROFICIENT}),
                                 visible=False,
                             )
                         ],
                         size=Sizes.SMALL,
                         life_span=150)


class Orc(species.Species):
    """
    Orc Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Orc",
                         features=[
                             feats.Feat(
                                 name="Adrenaline Rush",
                                 description="You can take the Dash Action as a Bonus Action. When you do so,you gain "
                                             "a number of Temporary Hit Points equal to your Proficiency Bonus.\n"
                                             "You can use this trait a number of times equal to your Proficiency "
                                             "Bonus, and you regain all expended uses when you finish a Long Rest."
                             ),
                             feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             feats.Feat(
                                 name="Powerful Build",
                                 description="You count as one Size larger when determining your carrying capacity "
                                             "and the weight you can push, drag, or lift."
                             ),
                             feats.Feat(
                                 name="Relentless Endurance",
                                 description="When you are reduced to 0 Hit Points but not killed outright, you can "
                                             "drop to 1 Hit Point instead. Once you use this trait,you can't do so "
                                             "again until you finish a Long Rest"
                             )
                         ],
                         life_span=80)


class Tiefling(species.Species):
    """
    Tiefling Species
    UA p. 9-10
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 name: str,
                 size: Sizes,
                 fiendish_legacy: feats.Feat,
                 ability: AbilityNames):
        if size not in [Sizes.SMALL, Sizes.MEDIUM]:
            raise Exception("Invalid Size")

        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception(
                "Spellcasting ability must be one of the mental abilities.")

        super().__init__(name=name,
                         features=[
                             feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             fiendish_legacy,
                             feats.Feat(
                                 name="Otherworldly Presence",
                                 description="You know the Thaumaturgy cantrip. When you cast it with this trait, "
                                             f"the Spell uses {ability.value}.",
                                 feat_spells=[
                                     content["Spells"]["Thaumaturgy"]()],
                                 spellcasting_ability=ability
                             )
                         ],
                         size=size)


class AbyssalTiefling(Tiefling):
    """
    Tiefling Species
    UA p. 9-10
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(content=content,
                         name="Abyssal Tiefling",
                         size=size,
                         fiendish_legacy=feats.Feat(
                             name="Fiendish Legacy",
                             description="You are the recipient of a fiendish legacy that grants you supernatural  "
                                         "abilities. Your Abyssal legacy is associated with Chaotic Evil planes. You "
                                         "gain the 1st-level benefit of the chosen legacy: the Poison Spray cantrip "
                                         "and resistance to Poison damage.\n"
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, Ray of Sickness and Hold Person. "
                                         "Once you cast the Spell with this trait, you can't cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             feat_spells=[content["Spells"]["Poison Spray"](),
                                          content["Spells"]["Ray of Sickness"](),
                                          content["Spells"]["Hold Person"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability)


class ChthonicTiefling(Tiefling):
    """
    Tiefling Species
    UA p. 9-10
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(content=content,
                         name="Chthonic Tiefling",
                         size=size,
                         fiendish_legacy=feats.Feat(
                             name="Fiendish Legacy",
                             description="You are the recipient of a fiendish legacy that grants you supernatural  "
                                         "abilities. Your Chthonic legacy is associated with Neutral Evil planes. You "
                                         "gain the 1st-level benefit of the chosen legacy: the Chill Touch cantrip "
                                         "and resistance to Necrotic damage.\n"
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, False Life and Ray of Enfeeblement. "
                                         "Once you cast the Spell with this trait, you can't cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             feat_spells=[content["Spells"]["Chill Touch"](),
                                          content["Spells"]["False Life"](),
                                          content["Spells"]["Ray of Enfeeblement"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability)


class InfernalTiefling(Tiefling):
    """
    Tiefling Species
    UA p. 9-10
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(content=content,
                         name="Infernal Tiefling",
                         size=size,
                         fiendish_legacy=feats.Feat(
                             name="Fiendish Legacy",
                             description="You are the recipient of a fiendish legacy that grants you supernatural  "
                                         "abilities. Your Infernal legacy is associated with Lawful Evil planes. You "
                                         "gain the 1st-level benefit of the chosen legacy: the Fire Bolt cantrip "
                                         "and resistance to Fire damage.\n"
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, Hellish Rebuke and Darkness. "
                                         "Once you cast the Spell with this trait, you can't cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             feat_spells=[content["Spells"]["Fire Bolt"](),
                                          content["Spells"]["Hellish Rebuke"](),
                                          content["Spells"]["Darkness"]()],
                             spellcasting_ability=ability
                         ),
                         ability=ability)


CONTENT = {
    "Backgrounds": {
        "Custom": CustomBackground,
        "Acolyte": Acolyte,
        "Artisan": Artisan,
        "Charlatan": Charlatan,
        "Criminal": Criminal,
        "Cultist": Cultist,
        "Entertainer": Entertainer,
        "Farmer": Farmer,
        "Gladiator": Gladiator,
        "Guard": Guard,
        "Guide": Guide,
        "Hermit": Hermit,
        "Laborer": Laborer,
        "Noble": Noble,
        "Pilgrim": Pilgrim,
        "Sage": Sage,
        "Sailor": Sailor,
        "Soldier": Soldier,
        "Urchin": Urchin,
    },
    "Feats": {
        "Alert": Alert,
        "Crafter": Crafter,
        "Healer": Healer,
        "Lucky": Lucky,
        "Magic Initiate": MagicInitiate,
        "Musician": Musician,
        "Savage Attacker": SavageAttacker,
        "Skilled": Skilled,
        "Tavern Brawler": TavernBrawler,
        "Tough": Tough,
    },
    "Species": {
        "Human": Human,
        "Black Dragonborn": "OBSOLETE",
        "Blue Dragonborn": "OBSOLETE",
        "Brass Dragonborn": "OBSOLETE",
        "Bronze Dragonborn": "OBSOLETE",
        "Copper Dragonborn": "OBSOLETE",
        "Gold Dragonborn": "OBSOLETE",
        "Green Dragonborn": "OBSOLETE",
        "Red Dragonborn": "OBSOLETE",
        "Silver Dragonborn": "OBSOLETE",
        "White Dragonborn": "OBSOLETE",
        "Dwarf": Dwarf,
        "Drow": Drow,
        "High Elf": HighElf,
        "Wood Elf": WoodElf,
        "Forest Gnome": ForestGnome,
        "Rock Gnome": RockGnome,
        "Halfling": Halfling,
        "Orc": Orc,
        "Abyssal Tiefling": AbyssalTiefling,
        "Chthonic Tiefling": ChthonicTiefling,
        "Infernal Tiefling": InfernalTiefling,
    },
}
