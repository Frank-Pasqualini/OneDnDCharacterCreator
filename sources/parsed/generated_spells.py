
class AcidArrow(spells.Spell):
    """
    Acid Arrow Spell
    SRD p. 115
    Generated
    """

    def __init__(self):
        super().__init__(name="Acid Arrow",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="powdered rhubarb leaf and an adder's stomach",
                         duration="Instantaneous",
                         description="A shimmering green arrow streaks toward a target\nwithin range " +
                                    "and bursts in a spray of acid. Make a\nranged spell attack " +
                                    "against the target. On a hit, the\ntarget takes 4d4 acid " +
                                    "damage immediately and 2d4\nacid damage at the end of its next " +
                                    "turn. On a miss,\nthe arrow splashes the target with acid for " +
                                    "half as\nmuch of the initial damage and no damage at the " +
                                    "end\nof its next turn. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the damage (both\ninitial and later) increases by 1d4 " +
                                          "for each slot level\nabove 2nd. ")


class AcidSplash(spells.Spell):
    """
    Acid Splash Spell
    SRD p. 115
    Generated
    """

    def __init__(self):
        super().__init__(name="Acid Splash",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You hurl a bubble of acid. Choose one creature\nwithin range, " +
                                    "or choose two creatures within range\nthat are within 5 feet " +
                                    "of each other. A target must\nsucceed on a Dexterity saving " +
                                    "throw or take 1d6 acid\ndamage.\nThis spell's damage increases " +
                                    "by 1d6 when you\nreach 5th level (2d6), 11th level (3d6), and " +
                                    "17th\nlevel (4d6). ",
                         at_higher_levels="")


class Aid(spells.Spell):
    """
    Aid Spell
    SRD p. 115
    Generated
    """

    def __init__(self):
        super().__init__(name="Aid",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny strip of white cloth",
                         duration="8 hours",
                         description="Your spell bolsters your allies with toughness and\nresolve. " +
                                    "Choose up to three creatures within range.\nEach target's hit " +
                                    "point maximum and current hit\npoints increase by 5 for the " +
                                    "duration. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, a target's hit points\nincrease by an additional 5 for " +
                                          "each slot level above\n2nd. ")


class Alarm(spells.Spell):
    """
    Alarm Spell
    SRD p. 115
    Generated
    """

    def __init__(self):
        super().__init__(name="Alarm",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny bell and a piece of fine silver wire",
                         duration="8 hours",
                         description="You set an alarm against unwanted intrusion.\nChoose a door, a " +
                                    "window, or an area within range\nthat is no larger than a " +
                                    "20-foot cube. Until the spell\nends, an alarm alerts you " +
                                    "whenever a Tiny or larger\ncreature touches or enters the " +
                                    "warded area. When\nyou cast the spell, you can designate " +
                                    "creatures that\nwon't set off the alarm. You also choose " +
                                    "whether the\nalarm is mental or audible.\nA mental alarm " +
                                    "alerts you with a ping in your\nmind if you are within 1 mile " +
                                    "of the warded area.\nThis ping awakens you if you are " +
                                    "sleeping.\nAn audible alarm produces the sound of a hand\nbell " +
                                    "for 10 seconds within 60 feet. ",
                         at_higher_levels="")


class AlterSelf(spells.Spell):
    """
    Alter Self Spell
    SRD p. 115-116
    Generated
    """

    def __init__(self):
        super().__init__(name="Alter Self",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You assume a different form. When you cast the spell,\nchoose " +
                                    "one of the following options, the effects of\nwhich last for " +
                                    "the duration of the spell. While the\nspell lasts, you can end " +
                                    "one option as an action to\ngain the benefits of a different " +
                                    "one.\nAquatic Adaptation. You adapt your body to an\naquatic " +
                                    "environment, sprouting gills and growing\nwebbing between your " +
                                    "fingers. You can breathe\nunderwater and gain a swimming speed " +
                                    "equal to\nyour walking speed.\nChange Appearance. You " +
                                    "transform your\nappearance. You decide what you look like, " +
                                    "including\nyour height, weight, facial features, sound of " +
                                    "your\nvoice, hair length, coloration, and " +
                                    "distinguishing\ncharacteristics, if any. You can make yourself " +
                                    "appear\nas a member of another race, though none of " +
                                    "your\nstatistics change. You also can't appear as a " +
                                    "creature\nof a different size than you, and your basic " +
                                    "shape\nstays the same; if you're bipedal, you can't use " +
                                    "this\nspell to become quadrupedal, for instance. At any\ntime " +
                                    "for the duration of the spell, you can use your\naction to " +
                                    "change your appearance in this way again.\nNatural Weapons. " +
                                    "You grow claws, fangs, spines,\nhorns, or a different natural " +
                                    "weapon of your choice.\nYour unarmed strikes deal 1d6 " +
                                    "bludgeoning,\npiercing, or slashing damage, as appropriate to " +
                                    "the\nnatural weapon you chose, and you are proficient\nwith " +
                                    "your unarmed strikes. Finally, the natural\nweapon is magic " +
                                    "and you have a +1 bonus to the\nattack and damage rolls you " +
                                    "make using it. ",
                         at_higher_levels="")


class AnimalFriendship(spells.Spell):
    """
    Animal Friendship Spell
    SRD p. 116
    Generated
    """

    def __init__(self):
        super().__init__(name="Animal Friendship",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a morsel of food",
                         duration="24 hours",
                         description="This spell lets you convince a beast that you mean it\nno " +
                                    "harm. Choose a beast that you can see within\nrange. It must " +
                                    "see and hear you. If the beast's\nIntelligence is 4 or higher, " +
                                    "the spell fails. Otherwise,\nthe beast must succeed on a " +
                                    "Wisdom saving throw\nor be charmed by you for the spell's " +
                                    "duration. If you\nor one of your companions harms the target, " +
                                    "the\nspells ends. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you can affect one\nadditional beast t level above " +
                                          "1st. ")


class AnimalMessenger(spells.Spell):
    """
    Animal Messenger Spell
    SRD p. 116
    Generated
    """

    def __init__(self):
        super().__init__(name="Animal Messenger",
                         spell_lists=[SpellLists.PRIMAL],
                         ritual=True,
                         level=2,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a morsel of food",
                         duration="24 hours",
                         description="By means of this spell, you use an animal to deliver " +
                                    "a\nmessage. Choose a Tiny beast you can see within\nrange, " +
                                    "such as a squirrel, a blue jay, or a bat. You\nspecify a " +
                                    "location, which you must have visited, and\na recipient who " +
                                    "matches a general description, such\nas “a man or woman " +
                                    "dressed in the uniform of the\ntown guard” or “a red-haired " +
                                    "dwarf wearing a\npointed hat.” You also speak a message of up " +
                                    "to\ntwenty-five words. The target beast travels for " +
                                    "the\nduration of the spell toward the specified " +
                                    "location,\ncovering about 50 miles per 24 hours for a " +
                                    "flying\nmessenger, or 25 miles for other animals.\nWhen the " +
                                    "messenger arrives, it delivers your\nmessage to the creature " +
                                    "that you described,\nreplicating the sound of your voice. The " +
                                    "messenger\nspeaks only to a creature matching the " +
                                    "description\nyou gave. If the messenger doesn't reach " +
                                    "its\ndestination before the spell ends, the message is " +
                                    "lost,\nand the beast makes its way back to where you " +
                                    "cast\nthis spell. ",
                         at_higher_levels="If you cast this spell using a spell\nslot of 3nd level or " +
                                          "higher, the duration of the spell\nincreases by 48 hours for " +
                                          "each slot level above 2nd. ")


class AnimalShapes(spells.Spell):
    """
    Animal Shapes Spell
    SRD p. 116
    Generated
    """

    def __init__(self):
        super().__init__(name="Animal Shapes",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="24 hours",
                         description="Your magic turns others into beasts. Choose any\nnumber of " +
                                    "willing creatures that you can see within\nrange. You " +
                                    "transform each target into the form of a\nLarge or smaller " +
                                    "beast with a challenge rating of 4 or\nlower. On subsequent " +
                                    "turns, you can use your action\nto transform affected " +
                                    "creatures into new forms.\nThe transformation lasts for the " +
                                    "duration for each\ntarget, or until the target drops to 0 hit " +
                                    "points or dies.\nYou can choose a different form for each " +
                                    "target. A\ntarget's game statistics are replaced by the " +
                                    "statistics\nof the chosen beast, though the target retains " +
                                    "its\nalignment and Intelligence, Wisdom, and Charisma\nscores. " +
                                    "The target assumes the hit points of its new\nform, and when " +
                                    "it reverts to its normal form, it\nreturns to the number of " +
                                    "hit points it had before it\ntransformed. If it reverts as a " +
                                    "result of dropping to 0\nhit points, any excess damage carries " +
                                    "over to its\nnormal form. As long as the excess damage " +
                                    "doesn't\nreduce the creature's normal form to 0 hit points, " +
                                    "it\nisn't knocked unconscious. The creature is limited in\nthe " +
                                    "actions it can perform by the nature of its new\nform, and it " +
                                    "can't speak or cast spells.\nThe target's gear melds into the " +
                                    "new form. The\ntarget can't activate, wield, or otherwise " +
                                    "benefit\nfrom any of its equipment. ",
                         at_higher_levels="")


class AnimateDead(spells.Spell):
    """
    Animate Dead Spell
    SRD p. 116-117
    Generated
    """

    def __init__(self):
        super().__init__(name="Animate Dead",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.Necromancy,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of blood, a piece of flesh, and a pinch of bone dust",
                         duration="Instantaneous",
                         description="This spell creates an undead servant. Choose a pile\nof bones " +
                                    "or a corpse of a Medium or Small humanoid\nwithin range. Your " +
                                    "spell imbues the target with a\nfoul mimicry of life, raising " +
                                    "it as an undead creature.\nThe target becomes a skeleton if " +
                                    "you chose bones or\na zombie if you chose a corpse (the GM has " +
                                    "the\ncreature's game statistics).\nOn each of your turns, you " +
                                    "can use a bonus action\nto mentally command any creature you " +
                                    "made with\nthis spell if the creature is within 60 feet of you " +
                                    "(if\nyou control multiple creatures, you can command\nany or " +
                                    "all of them at the same time, issuing the same\ncommand to " +
                                    "each one). You decide what action the\ncreature will take and " +
                                    "where it will move during its\nnext turn, or you can issue a " +
                                    "general command, such\nas to guard a particular chamber or " +
                                    "corridor. If you\nissue no commands, the creature only defends " +
                                    "itself\nagainst hostile creatures. Once given an order, " +
                                    "the\ncreature continues to follow it until its task " +
                                    "is\ncomplete.\nThe creature is under your control for 24 " +
                                    "hours,\nafter which it stops obeying any command you've\ngiven " +
                                    "it. To maintain control of the creature for\nanother 24 hours, " +
                                    "you must cast this spell on the\ncreature again before the " +
                                    "current 24-hour period\nends. This use of the spell reasserts " +
                                    "your control\nover up to four creatures you have animated " +
                                    "with\nthis spell, rather than animating a new one. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, you animate or\nreassert control over two additional " +
                                          "undead\ncreatures for each slot level above 3rd. Each of " +
                                          "the\ncreatures must come from a different corpse or pile\nof " +
                                          "bones. ")


class AnimateObjects(spells.Spell):
    """
    Animate Objects Spell
    SRD p. 117
    Generated
    """

    def __init__(self):
        super().__init__(name="Animate Objects",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Transmutation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="Objects come to life at your command. Choose up to\nten " +
                                    "nonmagical objects within range that are not\nbeing worn or " +
                                    "carried. Medium targets count as two\nobjects, Large targets " +
                                    "count as four objects, Huge\ntargets count as eight objects. " +
                                    "You can't animate any\nobject larger than Huge. Each target " +
                                    "animates and\nbecomes a creature under your control until " +
                                    "the\nspell ends or until reduced to 0 hit points.\nAs a bonus " +
                                    "action, you can mentally command any\ncreature you made with " +
                                    "this spell if the creature is\nwithin 500 feet of you (if you " +
                                    "control multiple\ncreatures, you can command any or all of " +
                                    "them at the\nsame time, issuing the same command to each " +
                                    "one).\nYou decide what action the creature will take " +
                                    "and\nwhere it will move during its next turn, or you " +
                                    "can\nissue a general command, such as to guard a\nparticular " +
                                    "chamber or corridor. If you issue no\ncommands, the creature " +
                                    "only defends itself against\nhostile creatures. Once given an " +
                                    "order, the creature\ncontinues to follow it until its task is " +
                                    "complete.\nAnimated Object Statistics\nSize HP AC Attack Str " +
                                    "Dex\nTiny 20 18 +8 to hit, 1d4 + 4 damage 4 18\nSmall 25 16 +6 " +
                                    "to hit, 1d8 + 2 damage 6 14\nMedium 40 13 +5 to hit, 2d6 + 1 " +
                                    "damage 10 12\nLarge 50 10 +6 to hit, 2d10 + 2\ndamage\n14 " +
                                    "10\nHuge 80 10 +8 to hit, 2d12 + 4\ndamage\n18 6\nAn animated " +
                                    "object is a construct with AC, hit\npoints, attacks, Strength, " +
                                    "and Dexterity determined\nby its size. Its Constitution is 10 " +
                                    "and its Intelligence\nand Wisdom are 3, and its Charisma is 1. " +
                                    "Its speed is\n30 feet; if the object lacks legs or other " +
                                    "appendages it\ncan use for locomotion, it instead has a flying " +
                                    "speed\nof 30 feet and can hover. If the object is " +
                                    "securely\nattached to a surface or a larger object, such as " +
                                    "a\nchain bolted to a wall, its speed is 0. It has " +
                                    "blindsight\nwith a radius of 30 feet and is blind beyond " +
                                    "that\ndistance. When the animated object drops to 0 " +
                                    "hit\npoints, it reverts to its original object form, and " +
                                    "any\nremaining damage carries over to its original " +
                                    "object\nform.\nIf you command an object to attack, it can make " +
                                    "a\nsingle melee attack against a creature within 5 feet\nof " +
                                    "it. It makes a slam attack with an attack bonus " +
                                    "and\nbludgeoning damage determined by its size. The GM\nmight " +
                                    "rule that a specific object inflicts slashing or\npiercing " +
                                    "damage based on its form. ",
                         at_higher_levels="If you cast this spell using a spell\nslot of 6th level or " +
                                          "higher, you can animate two\nadditional objects for each slot " +
                                          "level above 5th. ")


class AntilifeShell(spells.Spell):
    """
    Antilife Shell Spell
    SRD p. 117-118
    Generated
    """

    def __init__(self):
        super().__init__(name="Antilife Shell",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Abjuration,
                         spell_range="Self (10-foot radius)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="A shimmering barrier extends out from you in a 10-\nfoot " +
                                    "radius and moves with you, remaining centered\non you and " +
                                    "hedging out creatures other than undead\nand constructs. The " +
                                    "barrier lasts for the duration.\nThe barrier prevents an " +
                                    "affected creature from\npassing or reaching through. An " +
                                    "affected creature\ncan cast spells or make attacks with ranged " +
                                    "or reach\nweapons through the barrier.\nIf you move so that an " +
                                    "affected creature is forced\nto pass through the barrier, the " +
                                    "spell ends. ",
                         at_higher_levels="")


class AntimagicField(spells.Spell):
    """
    Antimagic Field Spell
    SRD p. 118
    Generated
    """

    def __init__(self):
        super().__init__(name="Antimagic Field",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Abjuration,
                         spell_range="Self (10-foot-radius sphere)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of powdered iron or iron filings",
                         duration="1 hour",
                         description="A 10-foot-radius invisible sphere of antimagic\nsurrounds you. " +
                                    "This area is divorced from the\nmagical energy that suffuses " +
                                    "the multiverse. Within\nthe sphere, spells can't be cast, " +
                                    "summoned creatures\ndisappear, and even magic items become " +
                                    "mundane.\nUntil the spell ends, the sphere moves with " +
                                    "you,\ncentered on you.\nSpells and other magical effects, " +
                                    "except those\ncreated by an artifact or a deity, are " +
                                    "suppressed in\nthe sphere and can't protrude into it. A " +
                                    "slot\nexpended to cast a suppressed spell is consumed.\nWhile " +
                                    "an effect is suppressed, it doesn't function, but\nthe time it " +
                                    "spends suppressed counts against its\nduration.\nTargeted " +
                                    "Effects. Spells and other magical effects,\nsuch as magic " +
                                    "missile and charm person, that target a\ncreature or an object " +
                                    "in the sphere have no effect on\nthat target.\nAreas of Magic. " +
                                    "The area of another spell or\nmagical effect, such as " +
                                    "fireball, can't extend into the\nsphere. If the sphere " +
                                    "overlaps an area of magic, the\npart of the area that is " +
                                    "covered by the sphere is\nsuppressed. For example, the flames " +
                                    "created by a\nwall of fire are suppressed within the " +
                                    "sphere,\ncreating a gap in the wall if the overlap is " +
                                    "large\nenough.\nSpells. Any active spell or other magical " +
                                    "effect on a\ncreature or an object in the sphere is " +
                                    "suppressed\nwhile the creature or object is in it.\nMagic " +
                                    "Items. The properties and powers of magic\nitems are " +
                                    "suppressed in the sphere. For example, a\n+1 longsword in the " +
                                    "sphere functions as a\nnonmagical longsword.\nA magic weapon's " +
                                    "properties and powers are\nsuppressed if it is used against a " +
                                    "target in the sphere\nor wielded by an attacker in the sphere. " +
                                    "If a magic\nweapon or a piece of magic ammunition fully " +
                                    "leaves\nthe sphere (for example, if you fire a magic arrow " +
                                    "or\nthrow a magic spear at a target outside the sphere),\nthe " +
                                    "magic of the item ceases to be suppressed as\nsoon as it " +
                                    "exits.\nMagical Travel. Teleportation and planar travel\nfail " +
                                    "to work in the sphere, whether the sphere is the\ndestination " +
                                    "or the departure point for such magical\ntravel. A portal to " +
                                    "another location, world, or plane\nof existence, as well as an " +
                                    "opening to an\nextradimensional space such as that created by " +
                                    "the\nrope trick spell, temporarily closes while in " +
                                    "the\nsphere.\nCreatures and Objects. A creature or " +
                                    "object\nsummoned or created by magic temporarily winks\nout of " +
                                    "existence in the sphere. Such a creature\ninstantly reappears " +
                                    "once the space the creature\noccupied is no longer within the " +
                                    "sphere.\nDispel Magic. Spells and magical effects such " +
                                    "as\ndispel magic have no effect on the sphere. Likewise,\nthe " +
                                    "spheres created by different antimagic field\nspells don't " +
                                    "nullify each other. ",
                         at_higher_levels="")


class AntipathySympathy(spells.Spell):
    """
    Antipathy/Sympathy Spell
    SRD p. 118-119
    Generated
    """

    def __init__(self):
        super().__init__(name="Antipathy/Sympathy",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=8,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="either a lump of alum soaked in vinegar for the antipathy effect or a drop of honey for the sympathy effect",
                         duration="10 days",
                         description="This spell attracts or repels creatures of your choice.\nYou " +
                                    "target something within range, either a Huge or\nsmaller " +
                                    "object or creature or an area that is no larger\nthan a " +
                                    "200-foot cube. Then specify a kind of\nintelligent creature, " +
                                    "such as red dragons, goblins, or\nvampires. You invest the " +
                                    "target with an aura that\neither attracts or repels the " +
                                    "specified creatures for\nthe duration. Choose antipathy or " +
                                    "sympathy as the\naura's effect.\nAntipathy. The enchantment " +
                                    "causes creatures of\nthe kind you designated to feel an " +
                                    "intense urge to\nleave the area and avoid the target. When " +
                                    "such a\ncreature can see the target or comes within 60 " +
                                    "feet\nof it, the creature must succeed on a Wisdom " +
                                    "saving\nthrow or become frightened. The creature " +
                                    "remains\nfrightened while it can see the target or is within " +
                                    "60\nfeet of it. While frightened by the target, the " +
                                    "creature\nmust use its movement to move to the nearest " +
                                    "safe\nspot from which it can't see the target. If the " +
                                    "creature\nmoves more than 60 feet from the target and " +
                                    "can't\nsee it, the creature is no longer frightened, but " +
                                    "the\ncreature becomes frightened again if it regains sight\nof " +
                                    "the target or moves within 60 feet of it.\nSympathy. The " +
                                    "enchantment causes the specified\ncreatures to feel an intense " +
                                    "urge to approach the\ntarget while within 60 feet of it or " +
                                    "able to see it.\nWhen such a creature can see the target or " +
                                    "comes\nwithin 60 feet of it, the creature must succeed on " +
                                    "a\nWisdom saving throw or use its movement on each\nof its " +
                                    "turns to enter the area or move within reach of\nthe target. " +
                                    "When the creature has done so, it can't\nwillingly move away " +
                                    "from the target.\nIf the target damages or otherwise harms " +
                                    "an\naffected creature, the affected creature can make " +
                                    "a\nWisdom saving throw to end the effect, as " +
                                    "described\nbelow.\nEnding the Effect. If an affected creature " +
                                    "ends its\nturn while not within 60 feet of the target or able " +
                                    "to\nsee it, the creature makes a Wisdom saving throw.\nOn a " +
                                    "successful save, the creature is no longer\naffected by the " +
                                    "target and recognizes the feeling of\nrepugnance or attraction " +
                                    "as magical. In addition, a\ncreature affected by the spell is " +
                                    "allowed another\nWisdom saving throw every 24 hours while the " +
                                    "spell\npersists.\nA creature that successfully saves against " +
                                    "this\neffect is immune to it for 1 minute, after which " +
                                    "time\nit can be affected again. ",
                         at_higher_levels="")


class ArcaneEye(spells.Spell):
    """
    Arcane Eye Spell
    SRD p. 119
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Eye",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Divination,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of bat fur",
                         duration="1 hour",
                         description="You create an invisible, magical eye within range\nthat hovers " +
                                    "in the air for the duration.\nYou mentally receive visual " +
                                    "information from the\neye, which has normal vision and " +
                                    "darkvision out to\n30 feet. The eye can look in every " +
                                    "direction.\nAs an action, you can move the eye up to 30 feet " +
                                    "in\nany direction. There is no limit to how far away from\nyou " +
                                    "the eye can move, but it can't enter another\nplane of " +
                                    "existence. A solid barrier blocks the eye's\nmovement, but the " +
                                    "eye can pass through an opening\nas small as 1 inch in " +
                                    "diameter. ",
                         at_higher_levels="")


class ArcaneHand(spells.Spell):
    """
    Arcane Hand Spell
    SRD p. 119
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Hand",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an eggshell and a snakeskin glove",
                         duration="1 minute",
                         description="You create a Large hand of shimmering, translucent\nforce in " +
                                    "an unoccupied space that you can see within\nrange. The hand " +
                                    "lasts for the spell's duration, and it\nmoves at your command, " +
                                    "mimicking the movements\nof your own hand.\nThe hand is an " +
                                    "object that has AC 20 and hit points\nequal to your hit point " +
                                    "maximum. If it drops to 0 hit\npoints, the spell ends. It has " +
                                    "a Strength of 26 (+8)\nand a Dexterity of 10 (+0). The hand " +
                                    "doesn't fill its\nspace.\nWhen you cast the spell and as a " +
                                    "bonus action on\nyour subsequent turns, you can move the hand " +
                                    "up to\n60 feet and then cause one of the following " +
                                    "effects\nwith it.\nClenched Fist. The hand strikes one " +
                                    "creature or\nobject within 5 feet of it. Make a melee spell " +
                                    "attack\nfor the hand using your game statistics. On a hit, " +
                                    "the\ntarget takes 4d8 force damage.\nForceful Hand. The hand " +
                                    "attempts to push a\ncreature within 5 feet of it in a " +
                                    "direction you choose.\nMake a check with the hand's Strength " +
                                    "contested by\nthe Strength (Athletics) check of the target. If " +
                                    "the\ntarget is Medium or smaller, you have advantage on\nthe " +
                                    "check. If you succeed, the hand pushes the target\nup to 5 " +
                                    "feet plus a number of feet equal to five times\nyour " +
                                    "spellcasting ability modifier. The hand moves\nwith the target " +
                                    "to remain within 5 feet of it.\nGrasping Hand. The hand " +
                                    "attempts to grapple a\nHuge or smaller creature within 5 feet " +
                                    "of it. You use\nthe hand's Strength score to resolve the " +
                                    "grapple. If\nthe target is Medium or smaller, you have " +
                                    "advantage\non the check. While the hand is grappling the " +
                                    "target,\nyou can use a bonus action to have the hand crush " +
                                    "it.\nWhen you do so, the target takes bludgeoning\ndamage " +
                                    "equal to 2d6 + your spellcasting " +
                                    "ability\nmodifier.\nInterposing Hand. The hand interposes " +
                                    "itself\nbetween you and a creature you choose until you\ngive " +
                                    "the hand a different command. The hand moves\nto stay between " +
                                    "you and the target, providing you\nwith half cover against the " +
                                    "target. The target can't\nmove through the hand's space if its " +
                                    "Strength score\nis less than or equal to the hand's Strength " +
                                    "score. If\nits Strength score is higher than the hand's " +
                                    "Strength\nscore, the target can move toward you through " +
                                    "the\nhand's space, but that space is difficult terrain for " +
                                    "the\ntarget. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the damage from the\nclenched fist option increases by " +
                                          "2d8 and the\ndamage from the grasping hand increases by 2d6 " +
                                          "for\neach slot level above 5th. ")


class ArcaneLock(spells.Spell):
    """
    Arcane Lock Spell
    SRD p. 119-120
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Lock",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="gold dust worth at least 25 gp, which the spell consumes",
                         duration="Until dispelled",
                         description="You touch a closed door, window, gate, chest, or\nother " +
                                    "entryway, and it becomes locked for the\nduration. You and the " +
                                    "creatures you designate when\nyou cast this spell can open the " +
                                    "object normally. You\ncan also set a password that, when " +
                                    "spoken within 5\nfeet of the object, suppresses this spell for " +
                                    "1 minute.\nOtherwise, it is impassable until it is broken or " +
                                    "the\nspell is dispelled or suppressed. Casting knock on " +
                                    "the\nobject suppresses arcane lock for 10 minutes.\nWhile " +
                                    "affected by this spell, the object is more\ndifficult to break " +
                                    "or force open; the DC to break it or\npick any locks on it " +
                                    "increases by 10. ",
                         at_higher_levels="")


class ArcaneSword(spells.Spell):
    """
    Arcane Sword Spell
    SRD p. 120
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Sword",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=7,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a miniature platinum sword with a grip and pommel of copper and zinc, worth 250 gp",
                         duration="1 minute",
                         description="You create a sword-shaped plane of force that\nhovers within " +
                                    "range. It lasts for the duration.\nWhen the sword appears, you " +
                                    "make a melee spell\nattack against a target of your choice " +
                                    "within 5 feet of\nthe sword. On a hit, the target takes 3d10 " +
                                    "force\ndamage. Until the spell ends, you can use a " +
                                    "bonus\naction on each of your turns to move the sword up " +
                                    "to\n20 feet to a spot you can see and repeat this " +
                                    "attack\nagainst the same target or a different one. ",
                         at_higher_levels="")


class ArcanistsMagicAura(spells.Spell):
    """
    Arcanist's Magic Aura Spell
    SRD p. 120
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcanist's Magic Aura",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Illusion,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small square of silk",
                         duration="24 hours",
                         description="You place an illusion on a creature or an object you\ntouch so " +
                                    "that divination spells reveal false\ninformation about it. The " +
                                    "target can be a willing\ncreature or an object that isn't " +
                                    "being carried or worn\nby another creature.\nWhen you cast the " +
                                    "spell, choose one or both of the\nfollowing effects. The " +
                                    "effect lasts for the duration. If\nyou cast this spell on the " +
                                    "same creature or object\nevery day for 30 days, placing the " +
                                    "same effect on it\neach time, the illusion lasts until it is " +
                                    "dispelled.\nFalse Aura. You change the way the target\nappears " +
                                    "to spells and magical effects, such as detect\nmagic, that " +
                                    "detect magical auras. You can make a\nnonmagical object appear " +
                                    "magical, a magical object\nappear nonmagical, or change the " +
                                    "object's magical\naura so that it appears to belong to a " +
                                    "specific school\nof magic that you choose. When you use this " +
                                    "effect\non an object, you can make the false magic " +
                                    "apparent\nto any creature that handles the item.\nMask. You " +
                                    "change the way the target appears to\nspells and magical " +
                                    "effects that detect creature types,\nsuch as a paladin's " +
                                    "Divine Sense or the trigger of a\nsymbol spell. You choose a " +
                                    "creature type and other\nspells and magical effects treat the " +
                                    "target as if it\nwere a creature of that type or of that " +
                                    "alignment. ",
                         at_higher_levels="")


class AstralProjection(spells.Spell):
    """
    Astral Projection Spell
    SRD p. 120-121
    Generated
    """

    def __init__(self):
        super().__init__(name="Astral Projection",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=9,
                         school=SpellSchools.Necromancy,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="for each creature you affect with this spell, you must provide one jacinth worth at least 1,000 gp and one ornately carved bar of silver worth at least 100 gp, all of which the spell consumes",
                         duration="Special",
                         description="You and up to eight willing creatures within range\nproject " +
                                    "your astral bodies into the Astral Plane (the\nspell fails and " +
                                    "the casting is wasted if you are already\non that plane). The " +
                                    "material body you leave behind\nis unconscious and in a state " +
                                    "of suspended\nanimation; it doesn't need food or air and " +
                                    "doesn't\nage.\nYour astral body resembles your mortal form " +
                                    "in\nalmost every way, replicating your game statistics\nand " +
                                    "possessions. The principal difference is the\naddition of a " +
                                    "silvery cord that extends from between\nyour shoulder blades " +
                                    "and trails behind you, fading to\ninvisibility after 1 foot. " +
                                    "This cord is your tether to\nyour material body. As long as " +
                                    "the tether remains\nintact, you can find your way home. If the " +
                                    "cord is\ncut—something that can happen only when an " +
                                    "effect\nspecifically states that it does—your soul and " +
                                    "body\nare separated, killing you instantly.\nYour astral form " +
                                    "can freely travel through the\nAstral Plane and can pass " +
                                    "through portals there\nleading to any other plane. If you " +
                                    "enter a new plane\nor return to the plane you were on when " +
                                    "casting this\nspell, your body and possessions are " +
                                    "transported\nalong the silver cord, allowing you to re-enter " +
                                    "your\nbody as you enter the new plane. Your astral form is\na " +
                                    "separate incarnation. Any damage or other effects\nthat apply " +
                                    "to it have no effect on your physical body,\nnor do they " +
                                    "persist when you return to it.\nThe spell ends for you and " +
                                    "your companions when\nyou use your action to dismiss it. When " +
                                    "the spell\nends, the affected creature returns to its " +
                                    "physical\nbody, and it awakens.\nThe spell might also end " +
                                    "early for you or one of\nyour companions. A successful dispel " +
                                    "magic spell\nused against an astral or physical body ends the " +
                                    "spell\nfor that creature. If a creature's original body or " +
                                    "its\nastral form drops to 0 hit points, the spell ends " +
                                    "for\nthat creature. If the spell ends and the silver cord " +
                                    "is\nintact, the cord pulls the creature's astral form back\nto " +
                                    "its body, ending its state of suspended animation.\nIf you are " +
                                    "returned to your body prematurely,\nyour companions remain in " +
                                    "their astral forms and\nmust find their own way back to their " +
                                    "bodies, usually\nby dropping to 0 hit points. ",
                         at_higher_levels="")


class Augury(spells.Spell):
    """
    Augury Spell
    SRD p. 121
    Generated
    """

    def __init__(self):
        super().__init__(name="Augury",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         ritual=True,
                         level=2,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="specially marked sticks, bones, or similar tokens worth at least 25 gp",
                         duration="Instantaneous",
                         description="By casting gem-inlaid sticks, rolling dragon bones,\nlaying " +
                                    "out ornate cards, or employing some other\ndivining tool, you " +
                                    "receive an omen from an\notherworldly entity about the results " +
                                    "of a specific\ncourse of action that you plan to take within " +
                                    "the next\n30 minutes. The GM chooses from the " +
                                    "following\npossible omens:\n• Weal, for good results\n• Woe, " +
                                    "for bad results\n• Weal and woe, for both good and bad " +
                                    "results\n• Nothing, for results that aren't especially good " +
                                    "or\nbad\nThe spell doesn't take into account any " +
                                    "possible\ncircumstances that might change the outcome, " +
                                    "such\nas the casting of additional spells or the loss or " +
                                    "gain\nof a companion.\nIf you cast the spell two or more times " +
                                    "before\ncompleting your next long rest, there is a " +
                                    "cumulative\n25 percent chance for each casting after the first " +
                                    "that\nyou get a random reading. The GM makes this roll " +
                                    "in\nsecret. ",
                         at_higher_levels="")


class Awaken(spells.Spell):
    """
    Awaken Spell
    SRD p. 121
    Generated
    """

    def __init__(self):
        super().__init__(name="Awaken",
                         spell_lists=[SpellLists.PRIMAL],
                         level=5,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an agate worth at least 1,000 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="After spending the casting time tracing magical\npathways " +
                                    "within a precious gemstone, you touch a\nHuge or smaller beast " +
                                    "or plant. The target must have\neither no Intelligence score " +
                                    "or an Intelligence of 3 or\nless. The target gains an " +
                                    "Intelligence of 10. The\ntarget also gains the ability to " +
                                    "speak one language\nyou know. If the target is a plant, it " +
                                    "gains the ability\nto move its limbs, roots, vines, creepers, " +
                                    "and so forth,\nand it gains senses similar to a human's. Your " +
                                    "GM\nchooses statistics appropriate for the awakened\nplant, " +
                                    "such as the statistics for the awakened shrub\nor the awakened " +
                                    "tree.\nThe awakened beast or plant is charmed by you\nfor 30 " +
                                    "days or until you or your companions do\nanything harmful to " +
                                    "it. When the charmed condition\nends, the awakened creature " +
                                    "chooses whether to\nremain friendly to you, based on how you " +
                                    "treated it\nwhile it was charmed. ",
                         at_higher_levels="")


class Bane(spells.Spell):
    """
    Bane Spell
    SRD p. 121
    Generated
    """

    def __init__(self):
        super().__init__(name="Bane",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of blood",
                         duration="1 minute",
                         description="Up to three creatures of your choice that you can see\nwithin " +
                                    "range must make Charisma saving throws.\nWhenever a target " +
                                    "that fails this saving throw makes\nan attack roll or a saving " +
                                    "throw before the spell ends,\nthe target must roll a d4 and " +
                                    "subtract the number\nrolled from the attack roll or saving " +
                                    "throw. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 1st. ")


class Banishment(spells.Spell):
    """
    Banishment Spell
    SRD p. 121-122
    Generated
    """

    def __init__(self):
        super().__init__(name="Banishment",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Abjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an item distasteful to the target",
                         duration="1 minute",
                         description="You attempt to send one creature that you can see\nwithin " +
                                    "range to another plane of existence. The\ntarget must succeed " +
                                    "on a Charisma saving throw or\nbe banished.\nIf the target is " +
                                    "native to the plane of existence\nyou're on, you banish the " +
                                    "target to a harmless\ndemiplane. While there, the target is " +
                                    "incapacitated.\nThe target remains there until the spell ends, " +
                                    "at\nwhich point the target reappears in the space it left\nor " +
                                    "in the nearest unoccupied space if that space " +
                                    "is\noccupied.\nIf the target is native to a different plane " +
                                    "of\nexistence than the one you're on, the target is\nbanished " +
                                    "with a faint popping noise, returning to its\nhome plane. If " +
                                    "the spell ends before 1 minute has\npassed, the target " +
                                    "reappears in the space it left or in\nthe nearest unoccupied " +
                                    "space if that space is\noccupied. Otherwise, the target " +
                                    "doesn't return. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 5th level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 4th. ")


class Barkskin(spells.Spell):
    """
    Barkskin Spell
    SRD p. 122
    Generated
    """

    def __init__(self):
        super().__init__(name="Barkskin",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a handful of oak bark",
                         duration="1 hour",
                         description="You touch a willing creature. Until the spell ends, " +
                                    "the\ntarget's skin has a rough, bark-like appearance, and\nthe " +
                                    "target's AC can't be less than 16, regardless of\nwhat kind of " +
                                    "armor it is wearing. ",
                         at_higher_levels="")


class BeaconOfHope(spells.Spell):
    """
    Beacon of Hope Spell
    SRD p. 122
    Generated
    """

    def __init__(self):
        super().__init__(name="Beacon of Hope",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="This spell bestows hope and vitality. Choose any\nnumber of " +
                                    "creatures within range. For the duration,\neach target has " +
                                    "advantage on Wisdom saving throws\nand death saving throws, " +
                                    "and regains the maximum\nnumber of hit points possible from " +
                                    "any healing. ",
                         at_higher_levels="")


class BestowCurse(spells.Spell):
    """
    Bestow Curse Spell
    SRD p. 122
    Generated
    """

    def __init__(self):
        super().__init__(name="Bestow Curse",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You touch a creature, and that creature must\nsucceed on a " +
                                    "Wisdom saving throw or become\ncursed for the duration of the " +
                                    "spell. When you cast\nthis spell, choose the nature of the " +
                                    "curse from the\nfollowing options:\n• Choose one ability " +
                                    "score. While cursed, the target\nhas disadvantage on ability " +
                                    "checks and saving\nthrows made with that ability score.\n• " +
                                    "While cursed, the target has disadvantage on\nattack rolls " +
                                    "against you.\n• While cursed, the target must make a " +
                                    "Wisdom\nsaving throw at the start of each of its turns. If " +
                                    "it\nfails, it wastes its action that turn doing nothing.\n• " +
                                    "While the target is cursed, your attacks and spells\ndeal an " +
                                    "extra 1d8 necrotic damage to the target.\nA remove curse spell " +
                                    "ends this effect. At the GM's\noption, you may choose an " +
                                    "alternative curse effect,\nbut it should be no more powerful " +
                                    "than those\ndescribed above. The GM has final say on such " +
                                    "a\ncurse's effect. ",
                         at_higher_levels="If you cast this spell using a spell\nslot of 4th level or " +
                                          "higher, the duration is\nconcentration, up to 10 minutes. If " +
                                          "you use a spell\nslot of 5th level or higher, the duration is " +
                                          "8 hours. If\nyou use a spell slot of 7th level or higher, " +
                                          "the\nduration is 24 hours. If you use a 9th level spell " +
                                          "slot,\nthe spell lasts until it is dispelled. Using a spell " +
                                          "slot of\n5th level or higher grants a duration that " +
                                          "doesn't\nrequire concentration. ")


class BlackTentacles(spells.Spell):
    """
    Black Tentacles Spell
    SRD p. 122-123
    Generated
    """

    def __init__(self):
        super().__init__(name="Black Tentacles",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of tentacle from a giant octopus or a giant squid",
                         duration="1 minute",
                         description="Squirming, ebony tentacles fill a 20-foot square on\nground " +
                                    "that you can see within range. For the\nduration, these " +
                                    "tentacles turn the ground in the area\ninto difficult " +
                                    "terrain.\nWhen a creature enters the affected area for " +
                                    "the\nfirst time on a turn or starts its turn there, " +
                                    "the\ncreature must succeed on a Dexterity saving throw\nor " +
                                    "take 3d6 bludgeoning damage and be restrained\nby the " +
                                    "tentacles until the spell ends. A creature that\nstarts its " +
                                    "turn in the area and is already restrained\nby the tentacles " +
                                    "takes 3d6 bludgeoning damage.\nA creature restrained by the " +
                                    "tentacles can use its\naction to make a Strength or Dexterity " +
                                    "check (its\nchoice) against your spell save DC. On a success, " +
                                    "it\nfrees itself. ",
                         at_higher_levels="")


class BladeBarrier(spells.Spell):
    """
    Blade Barrier Spell
    SRD p. 123
    Generated
    """

    def __init__(self):
        super().__init__(name="Blade Barrier",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Evocation,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You create a vertical wall of whirling, razor-sharp\nblades " +
                                    "made of magical energy. The wall appears\nwithin range and " +
                                    "lasts for the duration. You can\nmake a straight wall up to " +
                                    "100 feet long, 20 feet high,\nand 5 feet thick, or a ringed " +
                                    "wall up to 60 feet in\ndiameter, 20 feet high, and 5 feet " +
                                    "thick. The wall\nprovides three-quarters cover to creatures " +
                                    "behind it,\nand its space is difficult terrain.\nWhen a " +
                                    "creature enters the wall's area for the first\ntime on a turn " +
                                    "or starts its turn there, the creature\nmust make a Dexterity " +
                                    "saving throw. On a failed save,\nthe creature takes 6d10 " +
                                    "slashing damage. On a\nsuccessful save, the creature takes " +
                                    "half as much\ndamage. ",
                         at_higher_levels="")


class Bless(spells.Spell):
    """
    Bless Spell
    SRD p. 123
    Generated
    """

    def __init__(self):
        super().__init__(name="Bless",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a sprinkling of holy water",
                         duration="1 minute",
                         description="You bless up to three creatures of your choice within\nrange. " +
                                    "Whenever a target makes an attack roll or a\nsaving throw " +
                                    "before the spell ends, the target can\nroll a d4 and add the " +
                                    "number rolled to the attack roll\nor saving throw. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 1st. ")


class Blight(spells.Spell):
    """
    Blight Spell
    SRD p. 123
    Generated
    """

    def __init__(self):
        super().__init__(name="Blight",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Necromancy,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Necromantic energy washes over a creature of your\nchoice that " +
                                    "you can see within range, draining\nmoisture and vitality from " +
                                    "it. The target must make a\nConstitution saving throw. The " +
                                    "target takes 8d8\nnecrotic damage on a failed save, or half as " +
                                    "much\ndamage on a successful one. This spell has no effect\non " +
                                    "undead or constructs.\nIf you target a plant creature or a " +
                                    "magical plant, it\nmakes the saving throw with disadvantage, " +
                                    "and the\nspell deals maximum damage to it.\nIf you target a " +
                                    "nonmagical plant that isn't a\ncreature, such as a tree or " +
                                    "shrub, it doesn't make a\nsaving throw; it simply withers and " +
                                    "dies. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 5th level or " +
                                          "higher, the damage increases\nby 1d8 for each slot level above " +
                                          "4th. ")


class BlindnessDeafness(spells.Spell):
    """
    Blindness/Deafness Spell
    SRD p. 123
    Generated
    """

    def __init__(self):
        super().__init__(name="Blindness/Deafness",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.Necromancy,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 minute",
                         description="You can blind or deafen a foe. Choose one creature\nthat you " +
                                    "can see within range to make a Constitution\nsaving throw. If " +
                                    "it fails, the target is either blinded or\ndeafened (your " +
                                    "choice) for the duration. At the end\nof each of its turns, " +
                                    "the target can make a\nConstitution saving throw. On a " +
                                    "success, the spell\nends. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 2nd. ")


class Blink(spells.Spell):
    """
    Blink Spell
    SRD p. 123-124
    Generated
    """

    def __init__(self):
        super().__init__(name="Blink",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="Roll a d20 at the end of each of your turns for the\nduration " +
                                    "of the spell. On a roll of 11 or higher, you\nvanish from your " +
                                    "current plane of existence and\nappear in the Ethereal Plane " +
                                    "(the spell fails and the\ncasting is wasted if you were " +
                                    "already on that plane).\nAt the start of your next turn, and " +
                                    "when the spell\nends if you are on the Ethereal Plane, you " +
                                    "return to\nan unoccupied space of your choice that you can " +
                                    "see\nwithin 10 feet of the space you vanished from. If " +
                                    "no\nunoccupied space is available within that range, " +
                                    "you\nappear in the nearest unoccupied space (chosen at\nrandom " +
                                    "if more than one space is equally near). You\ncan dismiss this " +
                                    "spell as an action.\nWhile on the Ethereal Plane, you can see " +
                                    "and hear\nthe plane you originated from, which is cast " +
                                    "in\nshades of gray, and you can't see anything there\nmore " +
                                    "than 60 feet away. You can only affect and be\naffected by " +
                                    "other creatures on the Ethereal Plane.\nCreatures that aren't " +
                                    "there can't perceive you or\ninteract with you, unless they " +
                                    "have the ability to do\nso. ",
                         at_higher_levels="")


class Blur(spells.Spell):
    """
    Blur Spell
    SRD p. 124
    Generated
    """

    def __init__(self):
        super().__init__(name="Blur",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Illusion,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 minute",
                         description="Your body becomes blurred, shifting and wavering\nto all who " +
                                    "can see you. For the duration, any\ncreature has disadvantage " +
                                    "on attack rolls against you.\nAn attacker is immune to this " +
                                    "effect if it doesn't rely\non sight, as with blindsight, or " +
                                    "can see through\nillusions, as with truesight. ",
                         at_higher_levels="")


class BrandingSmite(spells.Spell):
    """
    Branding Smite Spell
    SRD p. 124
    Generated
    """

    def __init__(self):
        super().__init__(name="Branding Smite",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 minute",
                         description="The next time you hit a creature with a weapon\nattack before " +
                                    "this spell ends, the weapon gleams\nwith astral radiance as " +
                                    "you strike. The attack deals\nan extra 2d6 radiant damage to " +
                                    "the target, which\nbecomes visible if it's invisible, and the " +
                                    "target sheds\ndim light in a 5-foot radius and can't " +
                                    "become\ninvisible until the spell ends. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the extra damage\nincreases by 1d6 for each slot level " +
                                          "above 2nd. ")


class BurningHands(spells.Spell):
    """
    Burning Hands Spell
    SRD p. 124
    Generated
    """

    def __init__(self):
        super().__init__(name="Burning Hands",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="Self (15-foot cone)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="As you hold your hands with thumbs touching and\nfingers " +
                                    "spread, a thin sheet of flames shoots forth\nfrom your " +
                                    "outstretched fingertips. Each creature in a\n15-foot cone must " +
                                    "make a Dexterity saving throw. A\ncreature takes 3d6 fire " +
                                    "damage on a failed save, or\nhalf as much damage on a " +
                                    "successful one.\nThe fire ignites any flammable objects in the " +
                                    "area\nthat aren't being worn or carried. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the damage\nincreases by 1d6 for each slot level above " +
                                          "1st. ")


class CallLightning(spells.Spell):
    """
    Call Lightning Spell
    SRD p. 124
    Generated
    """

    def __init__(self):
        super().__init__(name="Call Lightning",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Conjuration,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="A storm cloud appears in the shape of a cylinder that\nis 10 " +
                                    "feet tall with a 60-foot radius, centered on a\npoint you can " +
                                    "see 100 feet directly above you. The\nspell fails if you can't " +
                                    "see a point in the air where the\nstorm cloud could appear " +
                                    "(for example, if you are in\na room that can't accommodate the " +
                                    "cloud).\nWhen you cast the spell, choose a point you can\nsee " +
                                    "within range. A bolt of lightning flashes down\nfrom the cloud " +
                                    "to that point. Each creature within 5\nfeet of that point must " +
                                    "make a Dexterity saving\nthrow. A creature takes 3d10 " +
                                    "lightning damage on a\nfailed save, or half as much damage on " +
                                    "a successful\none. On each of your turns until the spell ends, " +
                                    "you\ncan use your action to call down lightning in this " +
                                    "way\nagain, targeting the same point or a different one.\nIf " +
                                    "you are outdoors in stormy conditions when you\ncast this " +
                                    "spell, the spell gives you control over the\nexisting storm " +
                                    "instead of creating a new one. Under\nsuch conditions, the " +
                                    "spell's damage increases by\n1d10. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th or higher " +
                                          "level, the damage increases\nby 1d10 for each slot level above " +
                                          "3rd. ")


class CalmEmotions(spells.Spell):
    """
    Calm Emotions Spell
    SRD p. 124-125
    Generated
    """

    def __init__(self):
        super().__init__(name="Calm Emotions",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You attempt to suppress strong emotions in a group\nof people. " +
                                    "Each humanoid in a 20-foot-radius sphere\ncentered on a point " +
                                    "you choose within range must\nmake a Charisma saving throw; a " +
                                    "creature can\nchoose to fail this saving throw if it wishes. " +
                                    "If a\ncreature fails its saving throw, choose one of " +
                                    "the\nfollowing two effects.\nYou can suppress any effect " +
                                    "causing a target to be\ncharmed or frightened. When this spell " +
                                    "ends, any\nsuppressed effect resumes, provided that " +
                                    "its\nduration has not expired in the meantime.\nAlternatively, " +
                                    "you can make a target indifferent\nabout creatures of your " +
                                    "choice that it is hostile\ntoward. This indifference ends if " +
                                    "the target is\nattacked or harmed by a spell or if it " +
                                    "witnesses any\nof its friends being harmed. When the spell " +
                                    "ends, the\ncreature becomes hostile again, unless the GM " +
                                    "rules\notherwise. ",
                         at_higher_levels="")


class ChainLightning(spells.Spell):
    """
    Chain Lightning Spell
    SRD p. 125
    Generated
    """

    def __init__(self):
        super().__init__(name="Chain Lightning",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Evocation,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fur; a piece of amber, glass, or a crystal rod; and three silver pins",
                         duration="Instantaneous",
                         description="You create a bolt of lightning that arcs toward a\ntarget of " +
                                    "your choice that you can see within range.\nThree bolts then " +
                                    "leap from that target to as many as\nthree other targets, each " +
                                    "of which must be within 30\nfeet of the first target. A target " +
                                    "can be a creature or\nan object and can be targeted by only " +
                                    "one of the\nbolts.\nA target must make a Dexterity saving " +
                                    "throw. The\ntarget takes 10d8 lightning damage on a failed " +
                                    "save,\nor half as much damage on a successful one. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, one additional bolt\nleaps from the first target to " +
                                          "another target for each\nslot level above 6th. ")


class CharmPerson(spells.Spell):
    """
    Charm Person Spell
    SRD p. 125
    Generated
    """

    def __init__(self):
        super().__init__(name="Charm Person",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You attempt to charm a humanoid you can see\nwithin range. It " +
                                    "must make a Wisdom saving throw,\nand does so with advantage " +
                                    "if you or your\ncompanions are fighting it. If it fails the " +
                                    "saving throw,\nit is charmed by you until the spell ends or " +
                                    "until you\nor your companions do anything harmful to it. " +
                                    "The\ncharmed creature regards you as a friendly\nacquaintance. " +
                                    "When the spell ends, the creature\nknows it was charmed by " +
                                    "you. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 1st. The\ncreatures must be within 30 feet of each " +
                                          "other when\nyou target them. ")


class ChillTouch(spells.Spell):
    """
    Chill Touch Spell
    SRD p. 125
    Generated
    """

    def __init__(self):
        super().__init__(name="Chill Touch",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Necromancy,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 round",
                         description="You create a ghostly, skeletal hand in the space of " +
                                    "a\ncreature within range. Make a ranged spell attack\nagainst " +
                                    "the creature to assail it with the chill of the\ngrave. On a " +
                                    "hit, the target takes 1d8 necrotic damage,\nand it can't " +
                                    "regain hit points until the start of your\nnext turn. Until " +
                                    "then, the hand clings to the target.\nIf you hit an undead " +
                                    "target, it also has\ndisadvantage on attack rolls against you " +
                                    "until the\nend of your next turn.\nThis spell's damage " +
                                    "increases by 1d8 when you\nreach 5th level (2d8), 11th level " +
                                    "(3d8), and 17th\nlevel (4d8). ",
                         at_higher_levels="")


class CircleOfDeath(spells.Spell):
    """
    Circle of Death Spell
    SRD p. 125
    Generated
    """

    def __init__(self):
        super().__init__(name="Circle of Death",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Necromancy,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="the powder of a crushed black pearl worth at least 500 gp",
                         duration="Instantaneous",
                         description="A sphere of negative energy ripples out in a 60-footradius " +
                                    "sphere from a point within range. Each\ncreature in that area " +
                                    "must make a Constitution\nsaving throw. A target takes 8d6 " +
                                    "necrotic damage on\na failed save, or half as much damage on a " +
                                    "successful\none. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, the damage increases\nby 2d6 for each slot level above " +
                                          "6th. ")


class Clairvoyance(spells.Spell):
    """
    Clairvoyance Spell
    SRD p. 125-126
    Generated
    """

    def __init__(self):
        super().__init__(name="Clairvoyance",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Divination,
                         spell_range="1 mile",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for seeing",
                         duration="10 minutes",
                         description="You create an invisible sensor within range in a\nlocation " +
                                    "familiar to you (a place you have visited or\nseen before) or " +
                                    "in an obvious location that is\nunfamiliar to you (such as " +
                                    "behind a door, around a\ncorner, or in a grove of trees). The " +
                                    "sensor remains in\nplace for the duration, and it can't be " +
                                    "attacked or\notherwise interacted with.\nWhen you cast the " +
                                    "spell, you choose seeing or\nhearing. You can use the chosen " +
                                    "sense through the\nsensor as if you were in its space. As your " +
                                    "action, you\ncan switch between seeing and hearing.\nA " +
                                    "creature that can see the sensor (such as a\ncreature " +
                                    "benefiting from see invisibility or truesight)\nsees a " +
                                    "luminous, intangible orb about the size of\nyour fist. ",
                         at_higher_levels="")


class Clone(spells.Spell):
    """
    Clone Spell
    SRD p. 126
    Generated
    """

    def __init__(self):
        super().__init__(name="Clone",
                         spell_lists=[SpellLists.ARCANE],
                         level=8,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a diamond worth at least 1,000 gp and at least 1 cubic inch of flesh of the creature that is to be cloned, which the spell consumes, and a vessel worth at least 2,000 gp that has a sealable lid and is large enough to hold a Medium creature, such as a huge urn, coffin, mudfilled cyst in the ground, or crystal container filled with salt water",
                         duration="Instantaneous",
                         description="This spell grows an inert duplicate of a living\ncreature as a " +
                                    "safeguard against death. This clone\nforms inside a sealed " +
                                    "vessel and grows to full size\nand maturity after 120 days; " +
                                    "you can also choose to\nhave the clone be a younger version of " +
                                    "the same\ncreature. It remains inert and endures " +
                                    "indefinitely,\nas long as its vessel remains undisturbed.\nAt " +
                                    "any time after the clone matures, if the original\ncreature " +
                                    "dies, its soul transfers to the clone,\nprovided that the soul " +
                                    "is free and willing to return.\nThe clone is physically " +
                                    "identical to the original and\nhas the same personality, " +
                                    "memories, and abilities,\nbut none of the original's " +
                                    "equipment. The original\ncreature's physical remains, if they " +
                                    "still exist,\nbecome inert and can't thereafter be restored to " +
                                    "life,\nsince the creature's soul is elsewhere. ",
                         at_higher_levels="")


class Cloudkill(spells.Spell):
    """
    Cloudkill Spell
    SRD p. 126
    Generated
    """

    def __init__(self):
        super().__init__(name="Cloudkill",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Conjuration,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You create a 20-foot-radius sphere of poisonous,\nyellow-green " +
                                    "fog centered on a point you choose\nwithin range. The fog " +
                                    "spreads around corners. It\nlasts for the duration or until " +
                                    "strong wind disperses\nthe fog, ending the spell. Its area is " +
                                    "heavily obscured.\nWhen a creature enters the spell's area for " +
                                    "the first\ntime on a turn or starts its turn there, that " +
                                    "creature\nmust make a Constitution saving throw. The\ncreature " +
                                    "takes 5d8 poison damage on a failed save,\nor half as much " +
                                    "damage on a successful one.\nCreatures are affected even if " +
                                    "they hold their breath\nor don't need to breathe.\nThe fog " +
                                    "moves 10 feet away from you at the start\nof each of your " +
                                    "turns, rolling along the surface of the\nground. The vapors, " +
                                    "being heavier than air, sink to\nthe lowest level of the land, " +
                                    "even pouring down\nopenings. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the damage increases\nby 1d8 for each slot level above " +
                                          "5th. ")


class ColorSpray(spells.Spell):
    """
    Color Spray Spell
    SRD p. 126
    Generated
    """

    def __init__(self):
        super().__init__(name="Color Spray",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Illusion,
                         spell_range="Self (15-foot cone)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of powder or sand that is colored red, yellow, and blue",
                         duration="1 round",
                         description="A dazzling array of flashing, colored light springs\nfrom your " +
                                    "hand. Roll 6d10; the total is how many hit\npoints of " +
                                    "creatures this spell can effect. Creatures in\na 15-foot cone " +
                                    "originating from you are affected in\nascending order of their " +
                                    "current hit points (ignoring\nunconscious creatures and " +
                                    "creatures that can't see).\nStarting with the creature that " +
                                    "has the lowest\ncurrent hit points, each creature affected by " +
                                    "this\nspell is blinded until the spell ends. Subtract " +
                                    "each\ncreature's hit points from the total before moving " +
                                    "on\nto the creature with the next lowest hit points. " +
                                    "A\ncreature's hit points must be equal to or less than\nthe " +
                                    "remaining total for that creature to be affected. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, roll an additional\n2d10 for each slot level above " +
                                          "1st. ")


class Command(spells.Spell):
    """
    Command Spell
    SRD p. 126-127
    Generated
    """

    def __init__(self):
        super().__init__(name="Command",
                         spell_lists=[SpellLists.DIVINE],
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 round",
                         description="You speak a one-word command to a creature you\ncan see within " +
                                    "range. The target must succeed on a\nWisdom saving throw or " +
                                    "follow the command on its\nnext turn. The spell has no effect " +
                                    "if the target is\nundead, if it doesn't understand your " +
                                    "language, or if\nyour command is directly harmful to it.\nSome " +
                                    "typical commands and their effects follow.\nYou might issue a " +
                                    "command other than one\ndescribed here. If you do so, the GM " +
                                    "determines how\nthe target behaves. If the target can't follow " +
                                    "your\ncommand, the spell ends.\nApproach. The target moves " +
                                    "toward you by the\nshortest and most direct route, ending its " +
                                    "turn if it\nmoves within 5 feet of you.\nDrop. The target " +
                                    "drops whatever it is holding and\nthen ends its turn.\nFlee. " +
                                    "The target spends its turn moving away from\nyou by the " +
                                    "fastest available means.\nGrovel. The target falls prone and " +
                                    "then ends its\nturn.\nHalt. The target doesn't move and takes " +
                                    "no actions.\nA flying creature stays aloft, provided that it " +
                                    "is able\nto do so. If it must move to stay aloft, it flies " +
                                    "the\nminimum distance needed to remain in the air. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you can affect one\nadditional creature for each slot " +
                                          "level above 1st. The\ncreatures must be within 30 feet of each " +
                                          "other when\nyou target them. ")


class Commune(spells.Spell):
    """
    Commune Spell
    SRD p. 127
    Generated
    """

    def __init__(self):
        super().__init__(name="Commune",
                         spell_lists=[SpellLists.DIVINE],
                         ritual=True,
                         level=5,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="incense and a vial of holy or unholy water",
                         duration="1 minute",
                         description="You contact your deity or a divine proxy and ask up\nto three " +
                                    "questions that can be answered with a yes\nor no. You must ask " +
                                    "your questions before the spell\nends. You receive a correct " +
                                    "answer for each question.\nDivine beings aren't necessarily " +
                                    "omniscient, so\nyou might receive “unclear” as an answer if " +
                                    "a\nquestion pertains to information that lies beyond " +
                                    "the\ndeity's knowledge. In a case where a one-word\nanswer " +
                                    "could be misleading or contrary to the\ndeity's interests, the " +
                                    "GM might offer a short phrase\nas an answer instead.\nIf you " +
                                    "cast the spell two or more times before\nfinishing your next " +
                                    "long rest, there is a cumulative\n25 percent chance for each " +
                                    "casting after the first that\nyou get no answer. The GM makes " +
                                    "this roll in secret. ",
                         at_higher_levels="")


class CommuneWithNature(spells.Spell):
    """
    Commune with Nature Spell
    SRD p. 127
    Generated
    """

    def __init__(self):
        super().__init__(name="Commune with Nature",
                         spell_lists=[SpellLists.PRIMAL],
                         ritual=True,
                         level=5,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You briefly become one with nature and gain\nknowledge of the " +
                                    "surrounding territory. In the\noutdoors, the spell gives you " +
                                    "knowledge of the land\nwithin 3 miles of you. In caves and " +
                                    "other natural\nunderground settings, the radius is limited to " +
                                    "300\nfeet. The spell doesn't function where nature has\nbeen " +
                                    "replaced by construction, such as in dungeons\nand towns.\nYou " +
                                    "instantly gain knowledge of up to three facts\nof your choice " +
                                    "about any of the following subjects as\nthey relate to the " +
                                    "area:\n• terrain and bodies of water\n• prevalent plants, " +
                                    "minerals, animals, or peoples\n• powerful celestials, fey, " +
                                    "fiends, elementals, or\nundead\n• influence from other planes " +
                                    "of existence\n• buildings\nFor example, you could determine " +
                                    "the location of\npowerful undead in the area, the location of " +
                                    "major\nsources of safe drinking water, and the location " +
                                    "of\nany nearby towns. ",
                         at_higher_levels="")


class ComprehendLanguages(spells.Spell):
    """
    Comprehend Languages Spell
    SRD p. 127
    Generated
    """

    def __init__(self):
        super().__init__(name="Comprehend Languages",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of soot and salt",
                         duration="1 hour",
                         description="For the duration, you understand the literal meaning\nof any " +
                                    "spoken language that you hear. You also\nunderstand any " +
                                    "written language that you see, but\nyou must be touching the " +
                                    "surface on which the\nwords are written. It takes about 1 " +
                                    "minute to read\none page of text.\nThis spell doesn't decode " +
                                    "secret messages in a text\nor a glyph, such as an arcane " +
                                    "sigil, that isn't part of a\nwritten language. ",
                         at_higher_levels="")


class Compulsion(spells.Spell):
    """
    Compulsion Spell
    SRD p. 127-128
    Generated
    """

    def __init__(self):
        super().__init__(name="Compulsion",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="Creatures of your choice that you can see within\nrange and " +
                                    "that can hear you must make a Wisdom\nsaving throw. A target " +
                                    "automatically succeeds on\nthis saving throw if it can't be " +
                                    "charmed. On a failed\nsave, a target is affected by this " +
                                    "spell. Until the spell\nends, you can use a bonus action on " +
                                    "each of your\nturns to designate a direction that is " +
                                    "horizontal to\nyou. Each affected target must use as much of " +
                                    "its\nmovement as possible to move in that direction on\nits " +
                                    "next turn. It can take its action before it moves.\nAfter " +
                                    "moving in this way, it can make another\nWisdom saving to try " +
                                    "to end the effect.\nA target isn't compelled to move into an " +
                                    "obviously\ndeadly hazard, such as a fire or pit, but it " +
                                    "will\nprovoke opportunity attacks to move in the\ndesignated " +
                                    "direction. ",
                         at_higher_levels="")


class ConeOfCold(spells.Spell):
    """
    Cone of Cold Spell
    SRD p. 128
    Generated
    """

    def __init__(self):
        super().__init__(name="Cone of Cold",
                         spell_lists=[SpellLists.ARCANE],
                         level=5,
                         school=SpellSchools.Evocation,
                         spell_range="Self (60-foot cone)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small crystal or glass cone",
                         duration="Instantaneous",
                         description="A blast of cold air erupts from your hands. Each\ncreature in " +
                                    "a 60-foot cone must make a Constitution\nsaving throw. A " +
                                    "creature takes 8d8 cold damage on a\nfailed save, or half as " +
                                    "much damage on a successful\none.\nA creature killed by this " +
                                    "spell becomes a frozen\nstatue until it thaws. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the damage increases\nby 1d8 for each slot level above " +
                                          "5th. ")


class Confusion(spells.Spell):
    """
    Confusion Spell
    SRD p. 128
    Generated
    """

    def __init__(self):
        super().__init__(name="Confusion",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Enchantment,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="three nut shells",
                         duration="1 minute",
                         description="This spell assaults and twists creatures' minds,\nspawning " +
                                    "delusions and provoking uncontrolled\naction. Each creature in " +
                                    "a 10-foot-radius sphere\ncentered on a point you choose within " +
                                    "range must\nsucceed on a Wisdom saving throw when you " +
                                    "cast\nthis spell or be affected by it.\nAn affected target " +
                                    "can't take reactions and must\nroll a d10 at the start of each " +
                                    "of its turns to\ndetermine its behavior for that turn.\nd10 " +
                                    "Behavior\n1 The creature uses all its movement to move in " +
                                    "a\nrandom direction. To determine the direction, roll\na d8 " +
                                    "and assign a direction to each die face. The\ncreature doesn't " +
                                    "take an action this turn.\n2–6 The creature doesn't move or " +
                                    "take actions this\nturn.\n7–8 The creature uses its action to " +
                                    "make a melee\nattack against a randomly determined " +
                                    "creature\nwithin its reach. If there is no creature within " +
                                    "its\nreach, the creature does nothing this turn.\n9–10 The " +
                                    "creature can act and move normally.\nAt the end of each of its " +
                                    "turns, an affected target\ncan make a Wisdom saving throw. If " +
                                    "it succeeds, this\neffect ends for that target. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 5th level or " +
                                          "higher, the radius of the\nsphere increases by 5 feet for each " +
                                          "slot level above\n4th. ")


class ConjureAnimals(spells.Spell):
    """
    Conjure Animals Spell
    SRD p. 128
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Animals",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You summon fey spirits that take the form of beasts\nand " +
                                    "appear in unoccupied spaces that you can see\nwithin range. " +
                                    "Choose one of the following options for\nwhat appears:\n• One " +
                                    "beast of challenge rating 2 or lower\n• Two beasts of " +
                                    "challenge rating 1 or lower\n• Four beasts of challenge rating " +
                                    "1/2 or lower\n• Eight beasts of challenge rating 1/4 or " +
                                    "lower\nEach beast is also considered fey, and it " +
                                    "disappears\nwhen it drops to 0 hit points or when the spell " +
                                    "ends.\nThe summoned creatures are friendly to you and\nyour " +
                                    "companions. Roll initiative for the summoned\ncreatures as a " +
                                    "group, which has its own turns. They\nobey any verbal commands " +
                                    "that you issue to them\n(no action required by you). If you " +
                                    "don't issue any\ncommands to them, they defend themselves " +
                                    "from\nhostile creatures, but otherwise take no actions.\nThe " +
                                    "GM has the creatures' statistics. ",
                         at_higher_levels="When you cast this spell using\ncertain higher-level spell " +
                                          "slots, you choose one of the\nsummoning options above, and " +
                                          "more creatures\nappear: twice as many with a 5th-level slot, " +
                                          "three\ntimes as many with a 7th-level slot, and four times " +
                                          "as\nmany with a 9th-level slot. ")


class ConjureCelestial(spells.Spell):
    """
    Conjure Celestial Spell
    SRD p. 128-129
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Celestial",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=7,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You summon a celestial of challenge rating 4 or\nlower, which " +
                                    "appears in an unoccupied space that\nyou can see within range. " +
                                    "The celestial disappears\nwhen it drops to 0 hit points or " +
                                    "when the spell ends.\nThe celestial is friendly to you and " +
                                    "your\ncompanions for the duration. Roll initiative for " +
                                    "the\ncelestial, which has its own turns. It obeys any " +
                                    "verbal\ncommands that you issue to it (no action required " +
                                    "by\nyou), as long as they don't violate its alignment. If\nyou " +
                                    "don't issue any commands to the celestial, it\ndefends itself " +
                                    "from hostile creatures but otherwise\ntakes no actions.\nThe " +
                                    "GM has the celestial's statistics. ",
                         at_higher_levels="When you cast this spell using a\n9th-level spell slot, you " +
                                          "summon a celestial of\nchallenge rating 5 or lower. ")


class ConjureElemental(spells.Spell):
    """
    Conjure Elemental Spell
    SRD p. 129
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Elemental",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="burning incense for air, soft clay for earth, sulfur and phosphorus for fire, or water and sand for water",
                         duration="1 hour",
                         description="You call forth an elemental servant. Choose an area of\nair, " +
                                    "earth, fire, or water that fills a 10-foot cube\nwithin range. " +
                                    "An elemental of challenge rating 5 or\nlower appropriate to " +
                                    "the area you chose appears in\nan unoccupied space within 10 " +
                                    "feet of it. For\nexample, a fire elemental emerges from a " +
                                    "bonfire,\nand an earth elemental rises up from the " +
                                    "ground.\nThe elemental disappears when it drops to 0 " +
                                    "hit\npoints or when the spell ends.\nThe elemental is friendly " +
                                    "to you and your\ncompanions for the duration. Roll initiative " +
                                    "for the\nelemental, which has its own turns. It obeys " +
                                    "any\nverbal commands that you issue to it (no action\nrequired " +
                                    "by you). If you don't issue any commands\nto the elemental, it " +
                                    "defends itself from hostile\ncreatures but otherwise takes no " +
                                    "actions.\nIf your concentration is broken, the " +
                                    "elemental\ndoesn't disappear. Instead, you lose control of " +
                                    "the\nelemental, it becomes hostile toward you and " +
                                    "your\ncompanions, and it might attack. An " +
                                    "uncontrolled\nelemental can't be dismissed by you, and " +
                                    "it\ndisappears 1 hour after you summoned it.\nThe GM has the " +
                                    "elemental's statistics. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the challenge rating\nincreases by 1 for each slot " +
                                          "level above 5th. ")


class ConjureFey(spells.Spell):
    """
    Conjure Fey Spell
    SRD p. 129
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Fey",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You summon a fey creature of challenge rating 6 or\nlower, or " +
                                    "a fey spirit that takes the form of a beast of\nchallenge " +
                                    "rating 6 or lower. It appears in an\nunoccupied space that you " +
                                    "can see within range. The\nfey creature disappears when it " +
                                    "drops to 0 hit points\nor when the spell ends.\nThe fey " +
                                    "creature is friendly to you and your\ncompanions for the " +
                                    "duration. Roll initiative for the\ncreature, which has its own " +
                                    "turns. It obeys any\nverbal commands that you issue to it (no " +
                                    "action\nrequired by you), as long as they don't violate " +
                                    "its\nalignment. If you don't issue any commands to the\nfey " +
                                    "creature, it defends itself from hostile creatures\nbut " +
                                    "otherwise takes no actions.\nIf your concentration is broken, " +
                                    "the fey creature\ndoesn't disappear. Instead, you lose control " +
                                    "of the\nfey creature, it becomes hostile toward you and " +
                                    "your\ncompanions, and it might attack. An uncontrolled " +
                                    "fey\ncreature can't be dismissed by you, and it disappears\n1 " +
                                    "hour after you summoned it.\nThe GM has the fey creature's " +
                                    "statistics. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, the challenge rating\nincreases by 1 for each slot " +
                                          "level above 6th. ")


class ConjureMinorElementals(spells.Spell):
    """
    Conjure Minor Elementals Spell
    SRD p. 129-130
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Minor Elementals",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You summon elementals that appear in unoccupied\nspaces that " +
                                    "you can see within range. You choose\none the following " +
                                    "options for what appears:\n• One elemental of challenge rating " +
                                    "2 or lower\n• Two elementals of challenge rating 1 or lower\n• " +
                                    "Four elementals of challenge rating 1/2 or lower\n• Eight " +
                                    "elementals of challenge rating 1/4 or lower.\nAn elemental " +
                                    "summoned by this spell disappears\nwhen it drops to 0 hit " +
                                    "points or when the spell ends.\nThe summoned creatures are " +
                                    "friendly to you and\nyour companions. Roll initiative for the " +
                                    "summoned\ncreatures as a group, which has its own turns. " +
                                    "They\nobey any verbal commands that you issue to them\n(no " +
                                    "action required by you). If you don't issue any\ncommands to " +
                                    "them, they defend themselves from\nhostile creatures, but " +
                                    "otherwise take no actions.\nThe GM has the creatures' " +
                                    "statistics. ",
                         at_higher_levels="When you cast this spell using\ncertain higher-level spell " +
                                          "slots, you choose one of the\nsummoning options above, and " +
                                          "more creatures\nappear: twice as many with a 6th-level slot " +
                                          "and three\ntimes as many with an 8th-level slot. ")


class ConjureWoodlandBeings(spells.Spell):
    """
    Conjure Woodland Beings Spell
    SRD p. 130
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Woodland Beings",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="one holly berry per creature summoned",
                         duration="1 hour",
                         description="You summon fey creatures that appear in\nunoccupied spaces " +
                                    "that you can see within range.\nChoose one of the following " +
                                    "options for what\nappears:\n• One fey creature of challenge " +
                                    "rating 2 or lower\n• Two fey creatures of challenge rating 1 " +
                                    "or lower\n• Four fey creatures of challenge rating 1/2 or " +
                                    "lower\n• Eight fey creatures of challenge rating 1/4 " +
                                    "or\nlower\nA summoned creature disappears when it drops to " +
                                    "0\nhit points or when the spell ends.\nThe summoned creatures " +
                                    "are friendly to you and\nyour companions. Roll initiative for " +
                                    "the summoned\ncreatures as a group, which have their own " +
                                    "turns.\nThey obey any verbal commands that you issue to\nthem " +
                                    "(no action required by you). If you don't issue\nany commands " +
                                    "to them, they defend themselves\nfrom hostile creatures, but " +
                                    "otherwise take no actions.\nThe GM has the creatures' " +
                                    "statistics. ",
                         at_higher_levels="When you cast this spell using\ncertain higher-level spell " +
                                          "slots, you choose one of the\nsummoning options above, and " +
                                          "more creatures\nappear: twice as many with a 6th-level slot " +
                                          "and three\ntimes as many with an 8th-level slot. ")


class ContactOtherPlane(spells.Spell):
    """
    Contact Other Plane Spell
    SRD p. 130
    Generated
    """

    def __init__(self):
        super().__init__(name="Contact Other Plane",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=5,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 minute",
                         description="You mentally contact a demigod, the spirit of a longdead sage, " +
                                    "or some other mysterious entity from\nanother plane. " +
                                    "Contacting this extraplanar\nintelligence can strain or even " +
                                    "break your mind.\nWhen you cast this spell, make a DC 15 " +
                                    "Intelligence\nsaving throw. On a failure, you take 6d6 " +
                                    "psychic\ndamage and are insane until you finish a long " +
                                    "rest.\nWhile insane, you can't take actions, can't\nunderstand " +
                                    "what other creatures say, can't read, and\nspeak only in " +
                                    "gibberish. A greater restoration spell\ncast on you ends this " +
                                    "effect.\nOn a successful save, you can ask the entity up " +
                                    "to\nfive questions. You must ask your questions before\nthe " +
                                    "spell ends. The GM answers each question with\none word, such " +
                                    "as “yes,” “no,” “maybe,” “never,”\n“irrelevant,” or “unclear” " +
                                    "(if the entity doesn't know\nthe answer to the question). If a " +
                                    "one-word answer\nwould be misleading, the GM might instead " +
                                    "offer a\nshort phrase as an answer. ",
                         at_higher_levels="")


class Contagion(spells.Spell):
    """
    Contagion Spell
    SRD p. 130-131
    Generated
    """

    def __init__(self):
        super().__init__(name="Contagion",
                         spell_lists=[SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="7 days",
                         description="Your touch inflicts disease. Make a melee spell " +
                                    "attack\nagainst a creature within your reach. On a hit, " +
                                    "you\nafflict the creature with a disease of your choice\nfrom " +
                                    "any of the ones described below.\nAt the end of each of the " +
                                    "target's turns, it must\nmake a Constitution saving throw. " +
                                    "After failing three\nof these saving throws, the disease's " +
                                    "effects last for\nthe duration, and the creature stops making " +
                                    "these\nsaves. After succeeding on three of these " +
                                    "saving\nthrows, the creature recovers from the disease, " +
                                    "and\nthe spell ends.\nSince this spell induces a natural " +
                                    "disease in its\ntarget, any effect that removes a disease " +
                                    "or\notherwise ameliorates a disease's effects apply to " +
                                    "it.\nBlinding Sickness. Pain grips the creature's mind,\nand " +
                                    "its eyes turn milky white. The creature has\ndisadvantage on " +
                                    "Wisdom checks and Wisdom saving\nthrows and is blinded.\nFilth " +
                                    "Fever. A raging fever sweeps through the\ncreature's body. The " +
                                    "creature has disadvantage on\nStrength checks, Strength saving " +
                                    "throws, and attack\nrolls that use Strength.\nFlesh Rot. The " +
                                    "creature's flesh decays. The\ncreature has disadvantage on " +
                                    "Charisma checks and\nvulnerability to all damage.\nMindfire. " +
                                    "The creature's mind becomes feverish.\nThe creature has " +
                                    "disadvantage on Intelligence\nchecks and Intelligence saving " +
                                    "throws, and the\ncreature behaves as if under the effects of " +
                                    "the\nconfusion spell during combat.\nSeizure. The creature is " +
                                    "overcome with shaking.\nThe creature has disadvantage on " +
                                    "Dexterity checks,\nDexterity saving throws, and attack rolls " +
                                    "that use\nDexterity.\nSlimy Doom. The creature begins to " +
                                    "bleed\nuncontrollably. The creature has disadvantage " +
                                    "on\nConstitution checks and Constitution saving throws.\nIn " +
                                    "addition, whenever the creature takes damage, it\nis stunned " +
                                    "until the end of its next turn. ",
                         at_higher_levels="")


class Contingency(spells.Spell):
    """
    Contingency Spell
    SRD p. 131
    Generated
    """

    def __init__(self):
        super().__init__(name="Contingency",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Evocation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a statuette of yourself carved from ivory and decorated with gems worth at least 1,500 gp",
                         duration="10 days",
                         description="Choose a spell of 5th level or lower that you can cast,\nthat " +
                                    "has a casting time of 1 action, and that can\ntarget you. You " +
                                    "cast that spell—called the contingent\nspell—as part of " +
                                    "casting contingency, expending\nspell slots for both, but the " +
                                    "contingent spell doesn't\ncome into effect. Instead, it takes " +
                                    "effect when a\ncertain circumstance occurs. You describe " +
                                    "that\ncircumstance when you cast the two spells. For\nexample, " +
                                    "a contingency cast with water breathing\nmight stipulate that " +
                                    "water breathing comes into\neffect when you are engulfed in " +
                                    "water or a similar\nliquid.\nThe contingent spell takes effect " +
                                    "immediately after\nthe circumstance is met for the first time, " +
                                    "whether or\nnot you want it to, and then contingency " +
                                    "ends.\nThe contingent spell takes effect only on you, even\nif " +
                                    "it can normally target others. You can use only " +
                                    "one\ncontingency spell at a time. If you cast this spell " +
                                    "again,\nthe effect of another contingency spell on you " +
                                    "ends.\nAlso, contingency ends on you if its " +
                                    "material\ncomponent is ever not on your person. ",
                         at_higher_levels="")


class ContinualFlame(spells.Spell):
    """
    Continual Flame Spell
    SRD p. 131
    Generated
    """

    def __init__(self):
        super().__init__(name="Continual Flame",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="ruby dust worth 50 gp, which the spell consumes",
                         duration="Until dispelled",
                         description="A flame, equivalent in brightness to a torch, springs\nforth " +
                                    "from an object that you touch. The effect looks\nlike a " +
                                    "regular flame, but it creates no heat and\ndoesn't use oxygen. " +
                                    "A continual flame can be covered\nor hidden but not smothered " +
                                    "or quenched. ",
                         at_higher_levels="")


class ControlWater(spells.Spell):
    """
    Control Water Spell
    SRD p. 131-132
    Generated
    """

    def __init__(self):
        super().__init__(name="Control Water",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Transmutation,
                         spell_range="300 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of water and a pinch of dust",
                         duration="10 minutes",
                         description="Until the spell ends, you control any freestanding\nwater " +
                                    "inside an area you choose that is a cube up to\n100 feet on a " +
                                    "side. You can choose from any of the\nfollowing effects when " +
                                    "you cast this spell. As an\naction on your turn, you can " +
                                    "repeat the same effect\nor choose a different one.\nFlood. You " +
                                    "cause the water level of all standing\nwater in the area to " +
                                    "rise by as much as 20 feet. If the\narea includes a shore, the " +
                                    "flooding water spills over\nonto dry land.\nIf you choose an " +
                                    "area in a large body of water, you\ninstead create a 20-foot " +
                                    "tall wave that travels from\none side of the area to the other " +
                                    "and then crashes\ndown. Any Huge or smaller vehicles in the " +
                                    "wave's\npath are carried with it to the other side. Any " +
                                    "Huge\nor smaller vehicles struck by the wave have a " +
                                    "25\npercent chance of capsizing.\nThe water level remains " +
                                    "elevated until the spell\nends or you choose a different " +
                                    "effect. If this effect\nproduced a wave, the wave repeats on " +
                                    "the start of\nyour next turn while the flood effect " +
                                    "lasts.\nPart Water. You cause water in the area to move\napart " +
                                    "and create a trench. The trench extends across\nthe spell's " +
                                    "area, and the separated water forms a\nwall to either side. " +
                                    "The trench remains until the spell\nends or you choose a " +
                                    "different effect. The water then\nslowly fills in the trench " +
                                    "over the course of the next\nround until the normal water " +
                                    "level is restored.\nRedirect Flow. You cause flowing water in " +
                                    "the\narea to move in a direction you choose, even if " +
                                    "the\nwater has to flow over obstacles, up walls, or in\nother " +
                                    "unlikely directions. The water in the area\nmoves as you " +
                                    "direct it, but once it moves beyond the\nspell's area, it " +
                                    "resumes its flow based on the terrain\nconditions. The water " +
                                    "continues to move in the\ndirection you chose until the spell " +
                                    "ends or you\nchoose a different effect.\nWhirlpool. This " +
                                    "effect requires a body of water at\nleast 50 feet square and " +
                                    "25 feet deep. You cause a\nwhirlpool to form in the center of " +
                                    "the area. The\nwhirlpool forms a vortex that is 5 feet wide at " +
                                    "the\nbase, up to 50 feet wide at the top, and 25 feet " +
                                    "tall.\nAny creature or object in the water and within 25\nfeet " +
                                    "of the vortex is pulled 10 feet toward it. A\ncreature can " +
                                    "swim away from the vortex by making a\nStrength (Athletics) " +
                                    "check against your spell save DC.\nWhen a creature enters the " +
                                    "vortex for the first\ntime on a turn or starts its turn there, " +
                                    "it must make a\nStrength saving throw. On a failed save, the " +
                                    "creature\ntakes 2d8 bludgeoning damage and is caught in " +
                                    "the\nvortex until the spell ends. On a successful save, " +
                                    "the\ncreature takes half damage, and isn't caught in " +
                                    "the\nvortex. A creature caught in the vortex can use " +
                                    "its\naction to try to swim away from the vortex as\ndescribed " +
                                    "above, but has disadvantage on the\nStrength (Athletics) check " +
                                    "to do so.\nThe first time each turn that an object enters " +
                                    "the\nvortex, the object takes 2d8 bludgeoning damage;\nthis " +
                                    "damage occurs each round it remains in the\nvortex. ",
                         at_higher_levels="")


class ControlWeather(spells.Spell):
    """
    Control Weather Spell
    SRD p. 132
    Generated
    """

    def __init__(self):
        super().__init__(name="Control Weather",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Transmutation,
                         spell_range="Self (5-mile radius)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="burning incense and bits of earth and wood mixed in water",
                         duration="8 hours",
                         description="You take control of the weather within 5 miles of you\nfor the " +
                                    "duration. You must be outdoors to cast this\nspell. Moving to " +
                                    "a place where you don't have a clear\npath to the sky ends the " +
                                    "spell early.\nWhen you cast the spell, you change the " +
                                    "current\nweather conditions, which are determined by the\nGM " +
                                    "based on the climate and season. You can " +
                                    "change\nprecipitation, temperature, and wind. It takes 1d4 " +
                                    "×\n10 minutes for the new conditions to take effect.\nOnce " +
                                    "they do so, you can change the conditions again.\nWhen the " +
                                    "spell ends, the weather gradually returns\nto normal.\nWhen " +
                                    "you change the weather conditions, find a\ncurrent condition " +
                                    "on the following tables and change\nits stage by one, up or " +
                                    "down. When changing the\nwind, you can change its " +
                                    "direction.\nPrecipitation\nStage Condition\n1 Clear\n2 Light " +
                                    "clouds\n3 Overcast or ground fog\n4 Rain, hail, or snow\n5 " +
                                    "Torrential rain, driving hail, or blizzard\nTemperature\nStage " +
                                    "Condition\n1 Unbearable heat\n2 Hot\n3 Warm\n4 Cool\n5 Cold\n6 " +
                                    "Arctic cold\nWind\nStage Condition\n1 Calm\n2 Moderate wind\n3 " +
                                    "Strong wind\n4 Gale\n5 Storm ",
                         at_higher_levels="")


class Counterspell(spells.Spell):
    """
    Counterspell Spell
    SRD p. 132
    Generated
    """

    def __init__(self):
        super().__init__(name="Counterspell",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="60 feet",
                         verbal_components=False,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You attempt to interrupt a creature in the process of\ncasting " +
                                    "a spell. If the creature is casting a spell of 3rd\nlevel or " +
                                    "lower, its spell fails and has no effect. If it is\ncasting a " +
                                    "spell of 4th level or higher, make an ability\ncheck using " +
                                    "your spellcasting ability. The DC equals\n10 + the spell's " +
                                    "level. On a success, the creature's\nspell fails and has no " +
                                    "effect. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the interrupted spell\nhas no effect if its level is " +
                                          "less than or equal to the\nlevel of the spell slot you used. ")


class CreateFoodAndWater(spells.Spell):
    """
    Create Food and Water Spell
    SRD p. 132-133
    Generated
    """

    def __init__(self):
        super().__init__(name="Create Food and Water",
                         spell_lists=[SpellLists.DIVINE],
                         level=3,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You create 45 pounds of food and 30 gallons of\nwater on the " +
                                    "ground or in containers within range,\nenough to sustain up to " +
                                    "fifteen humanoids or five\nsteeds for 24 hours. The food is " +
                                    "bland but nourishing,\nand spoils if uneaten after 24 hours. " +
                                    "The water is\nclean and doesn't go bad. ",
                         at_higher_levels="")


class CreateUndead(spells.Spell):
    """
    Create Undead Spell
    SRD p. 133
    Generated
    """

    def __init__(self):
        super().__init__(name="Create Undead",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Necromancy,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="one clay pot filled with grave dirt, one clay pot filled with brackish water, and one 150 gp black onyx stone for each corpse",
                         duration="Instantaneous",
                         description="You can cast this spell only at night. Choose up to\nthree " +
                                    "corpses of Medium or Small humanoids within\nrange. Each " +
                                    "corpse becomes a ghoul under your\ncontrol. (The GM has game " +
                                    "statistics for these\ncreatures.)\nAs a bonus action on each " +
                                    "of your turns, you can\nmentally command any creature you " +
                                    "animated with\nthis spell if the creature is within 120 feet " +
                                    "of you (if\nyou control multiple creatures, you can " +
                                    "command\nany or all of them at the same time, issuing the " +
                                    "same\ncommand to each one). You decide what action " +
                                    "the\ncreature will take and where it will move during " +
                                    "its\nnext turn, or you can issue a general command, such\nas " +
                                    "to guard a particular chamber or corridor. If you\nissue no " +
                                    "commands, the creature only defends itself\nagainst hostile " +
                                    "creatures. Once given an order, the\ncreature continues to " +
                                    "follow it until its task is\ncomplete.\nThe creature is under " +
                                    "your control for 24 hours,\nafter which it stops obeying any " +
                                    "command you have\ngiven it. To maintain control of the " +
                                    "creature for\nanother 24 hours, you must cast this spell on " +
                                    "the\ncreature before the current 24-hour period ends.\nThis " +
                                    "use of the spell reasserts your control over up\nto three " +
                                    "creatures you have animated with this spell,\nrather than " +
                                    "animating new ones. ",
                         at_higher_levels="When you cast this spell using a\n7th-level spell slot, you " +
                                          "can animate or reassert\ncontrol over four ghouls. When you " +
                                          "cast this spell\nusing an 8th-level spell slot, you can " +
                                          "animate or\nreassert control over five ghouls or two ghasts " +
                                          "or\nwights. When you cast this spell using a 9th-level\nspell " +
                                          "slot, you can animate or reassert control over\nsix ghouls, " +
                                          "three ghasts or wights, or two mummies. ")


class CreateOrDestroyWater(spells.Spell):
    """
    Create or Destroy Water Spell
    SRD p. 133
    Generated
    """

    def __init__(self):
        super().__init__(name="Create or Destroy Water",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of water if creating water or a few grains of sand if destroying it",
                         duration="Instantaneous",
                         description="You either create or destroy water.\nCreate Water. You create " +
                                    "up to 10 gallons of clean\nwater within range in an open " +
                                    "container.\nAlternatively, the water falls as rain in a " +
                                    "30-foot cube\nwithin range, extinguishing exposed flames in " +
                                    "the\narea.\nDestroy Water. You destroy up to 10 gallons " +
                                    "of\nwater in an open container within range.\nAlternatively, " +
                                    "you destroy fog in a 30-foot cube\nwithin range. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you create or\ndestroy 10 additional gallons of water, " +
                                          "or the size of\nthe cube increases by 5 feet, for each slot " +
                                          "level above\n1st. ")


class Creation(spells.Spell):
    """
    Creation Spell
    SRD p. 133
    Generated
    """

    def __init__(self):
        super().__init__(name="Creation",
                         spell_lists=[SpellLists.ARCANE],
                         level=5,
                         school=SpellSchools.Illusion,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny piece of matter of the same type of the item you plan to create",
                         duration="Special",
                         description="You pull wisps of shadow material from the\nShadowfell to " +
                                    "create a nonliving object of vegetable\nmatter within range: " +
                                    "soft goods, rope, wood, or\nsomething similar. You can also " +
                                    "use this spell to\ncreate mineral objects such as stone, " +
                                    "crystal, or\nmetal. The object created must be no larger than " +
                                    "a 5-\nfoot cube, and the object must be of a form " +
                                    "and\nmaterial that you have seen before.\nThe duration depends " +
                                    "on the object's material. If\nthe object is composed of " +
                                    "multiple materials, use the\nshortest " +
                                    "duration.\nMaterial\nDuration\nVegetable matter 1 day\nStone " +
                                    "or crystal 12 hours\nPrecious metals 1 hour\nGems 10 " +
                                    "minutes\nAdamantine or mithral 1 minute\nUsing any material " +
                                    "created by this spell as another\nspell's material component " +
                                    "causes that spell to fail. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the cube increases by\n5 feet for each slot level " +
                                          "above 5th. ")


class CureWounds(spells.Spell):
    """
    Cure Wounds Spell
    SRD p. 133-134
    Generated
    """

    def __init__(self):
        super().__init__(name="Cure Wounds",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="A creature you touch regains a number of hit points\nequal to " +
                                    "1d8 + your spellcasting ability modifier.\nThis spell has no " +
                                    "effect on undead or constructs. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the healing increases\nby 1d8 for each slot level " +
                                          "above 1st. ")


class DancingLights(spells.Spell):
    """
    Dancing Lights Spell
    SRD p. 134
    Generated
    """

    def __init__(self):
        super().__init__(name="Dancing Lights",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=0,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of phosphorus or wychwood, or a glowworm",
                         duration="1 minute",
                         description="You create up to four torch-sized lights within range,\nmaking " +
                                    "them appear as torches, lanterns, or glowing\norbs that hover " +
                                    "in the air for the duration. You can\nalso combine the four " +
                                    "lights into one glowing\nvaguely humanoid form of Medium size. " +
                                    "Whichever\nform you choose, each light sheds dim light in a " +
                                    "10-\nfoot radius.\nAs a bonus action on your turn, you can " +
                                    "move the\nlights up to 60 feet to a new spot within range. " +
                                    "A\nlight must be within 20 feet of another light created\nby " +
                                    "this spell, and a light winks out if it exceeds the\nspell's " +
                                    "range. ",
                         at_higher_levels="")


class Darkness(spells.Spell):
    """
    Darkness Spell
    SRD p. 134
    Generated
    """

    def __init__(self):
        super().__init__(name="Darkness",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list="bat fur and a drop of pitch or piece of coal",
                         duration="10 minutes",
                         description="Magical darkness spreads from a point you choose\nwithin range " +
                                    "to fill a 15-foot-radius sphere for the\nduration. The " +
                                    "darkness spreads around corners. A\ncreature with darkvision " +
                                    "can't see through this\ndarkness, and nonmagical light can't " +
                                    "illuminate it.\nIf the point you choose is on an object you " +
                                    "are\nholding or one that isn't being worn or carried, " +
                                    "the\ndarkness emanates from the object and moves with\nit. " +
                                    "Completely covering the source of the darkness\nwith an opaque " +
                                    "object, such as a bowl or a helm,\nblocks the darkness.\nIf " +
                                    "any of this spell's area overlaps with an area of\nlight " +
                                    "created by a spell of 2nd level or lower, the\nspell that " +
                                    "created the light is dispelled. ",
                         at_higher_levels="")


class Darkvision(spells.Spell):
    """
    Darkvision Spell
    SRD p. 134
    Generated
    """

    def __init__(self):
        super().__init__(name="Darkvision",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="either a pinch of dried carrot or an agate",
                         duration="8 hours",
                         description="You touch a willing creature to grant it the ability to\nsee " +
                                    "in the dark. For the duration, that creature has\ndarkvision " +
                                    "out to a range of 60 feet. ",
                         at_higher_levels="")


class Daylight(spells.Spell):
    """
    Daylight Spell
    SRD p. 134
    Generated
    """

    def __init__(self):
        super().__init__(name="Daylight",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="A 60-foot-radius sphere of light spreads out from a\npoint you " +
                                    "choose within range. The sphere is bright\nlight and sheds dim " +
                                    "light for an additional 60 feet.\nIf you chose a point on an " +
                                    "object you are holding\nor one that isn't being worn or " +
                                    "carried, the light\nshines from the object and moves with it. " +
                                    "Completely\ncovering the affected object with an opaque " +
                                    "object,\nsuch as a bowl or a helm, blocks the light.\nIf any " +
                                    "of this spell's area overlaps with an area of\ndarkness " +
                                    "created by a spell of 3rd level or lower, the\nspell that " +
                                    "created the darkness is dispelled. ",
                         at_higher_levels="")


class DeathWard(spells.Spell):
    """
    Death Ward Spell
    SRD p. 134
    Generated
    """

    def __init__(self):
        super().__init__(name="Death Ward",
                         spell_lists=[SpellLists.DIVINE],
                         level=4,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="8 hours",
                         description="You touch a creature and grant it a measure of\nprotection " +
                                    "from death.\nThe first time the target would drop to 0 hit " +
                                    "points\nas a result of taking damage, the target instead " +
                                    "drops\nto 1 hit point, and the spell ends.\nIf the spell is " +
                                    "still in effect when the target is\nsubjected to an effect " +
                                    "that would kill it\ninstantaneously without dealing damage, " +
                                    "that effect\nis instead negated against the target, and the " +
                                    "spell\nends. ",
                         at_higher_levels="")


class DelayedBlastFireball(spells.Spell):
    """
    Delayed Blast Fireball Spell
    SRD p. 134-135
    Generated
    """

    def __init__(self):
        super().__init__(name="Delayed Blast Fireball",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=7,
                         school=SpellSchools.Evocation,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny ball of bat guano and sulfur",
                         duration="1 minute",
                         description="A beam of yellow light flashes from your pointing\nfinger, " +
                                    "then condenses to linger at a chosen point\nwithin range as a " +
                                    "glowing bead for the duration.\nWhen the spell ends, either " +
                                    "because your\nconcentration is broken or because you decide " +
                                    "to\nend it, the bead blossoms with a low roar into " +
                                    "an\nexplosion of flame that spreads around corners.\nEach " +
                                    "creature in a 20-foot-radius sphere centered on\nthat point " +
                                    "must make a Dexterity saving throw. A\ncreature takes fire " +
                                    "damage equal to the total\naccumulated damage on a failed " +
                                    "save, or half as\nmuch damage on a successful one.\nThe " +
                                    "spell's base damage is 12d6. If at the end of\nyour turn the " +
                                    "bead has not yet detonated, the\ndamage increases by 1d6.\nIf " +
                                    "the glowing bead is touched before the interval\nhas expired, " +
                                    "the creature touching it must make a\nDexterity saving throw. " +
                                    "On a failed save, the spell\nends immediately, causing the " +
                                    "bead to erupt in flame.\nOn a successful save, the creature " +
                                    "can throw the\nbead up to 40 feet. When it strikes a creature " +
                                    "or a\nsolid object, the spell ends, and the bead " +
                                    "explodes.\nThe fire damages objects in the area and " +
                                    "ignites\nflammable objects that aren't being worn or carried. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 8th level or " +
                                          "higher, the base damage\nincreases by 1d6 for each slot level " +
                                          "above 7th. ")


class Demiplane(spells.Spell):
    """
    Demiplane Spell
    SRD p. 135
    Generated
    """

    def __init__(self):
        super().__init__(name="Demiplane",
                         spell_lists=[SpellLists.ARCANE],
                         level=8,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=False,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You create a shadowy door on a flat solid surface\nthat you " +
                                    "can see within range. The door is large\nenough to allow " +
                                    "Medium creatures to pass through\nunhindered. When opened, the " +
                                    "door leads to a\ndemiplane that appears to be an empty room 30 " +
                                    "feet\nin each dimension, made of wood or stone. When " +
                                    "the\nspell ends, the door disappears, and any creatures " +
                                    "or\nobjects inside the demiplane remain trapped there,\nas the " +
                                    "door also disappears from the other side.\nEach time you cast " +
                                    "this spell, you can create a new\ndemiplane, or have the " +
                                    "shadowy door connect to a\ndemiplane you created with a " +
                                    "previous casting of\nthis spell. Additionally, if you know the " +
                                    "nature and\ncontents of a demiplane created by a casting of " +
                                    "this\nspell by another creature, you can have the " +
                                    "shadowy\ndoor connect to its demiplane instead. ",
                         at_higher_levels="")


class DetectEvilAndGood(spells.Spell):
    """
    Detect Evil and Good Spell
    SRD p. 135
    Generated
    """

    def __init__(self):
        super().__init__(name="Detect Evil and Good",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="For the duration, you know if there is an " +
                                    "aberration,\ncelestial, elemental, fey, fiend, or undead " +
                                    "within 30\nfeet of you, as well as where the creature is " +
                                    "located.\nSimilarly, you know if there is a place or " +
                                    "object\nwithin 30 feet of you that has been " +
                                    "magically\nconsecrated or desecrated.\nThe spell can penetrate " +
                                    "most barriers, but it is\nblocked by 1 foot of stone, 1 inch " +
                                    "of common metal, a\nthin sheet of lead, or 3 feet of wood or " +
                                    "dirt. ",
                         at_higher_levels="")


class DetectMagic(spells.Spell):
    """
    Detect Magic Spell
    SRD p. 135
    Generated
    """

    def __init__(self):
        super().__init__(name="Detect Magic",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         ritual=True,
                         level=1,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="For the duration, you sense the presence of magic\nwithin 30 " +
                                    "feet of you. If you sense magic in this way,\nyou can use your " +
                                    "action to see a faint aura around\nany visible creature or " +
                                    "object in the area that bears\nmagic, and you learn its school " +
                                    "of magic, if any.\nThe spell can penetrate most barriers, but " +
                                    "it is\nblocked by 1 foot of stone, 1 inch of common metal, " +
                                    "a\nthin sheet of lead, or 3 feet of wood or dirt. ",
                         at_higher_levels="")


class DetectPoisonAndDisease(spells.Spell):
    """
    Detect Poison and Disease Spell
    SRD p. 135-136
    Generated
    """

    def __init__(self):
        super().__init__(name="Detect Poison and Disease",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         ritual=True,
                         level=1,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a yew leaf",
                         duration="10 minutes",
                         description="For the duration, you can sense the presence and\nlocation of " +
                                    "poisons, poisonous creatures, and\ndiseases within 30 feet of " +
                                    "you. You also identify the\nkind of poison, poisonous " +
                                    "creature, or disease in\neach case.\nThe spell can penetrate " +
                                    "most barriers, but it is\nblocked by 1 foot of stone, 1 inch " +
                                    "of common metal, a\nthin sheet of lead, or 3 feet of wood or " +
                                    "dirt. ",
                         at_higher_levels="")


class DetectThoughts(spells.Spell):
    """
    Detect Thoughts Spell
    SRD p. 136
    Generated
    """

    def __init__(self):
        super().__init__(name="Detect Thoughts",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a copper piece",
                         duration="1 minute",
                         description="For the duration, you can read the thoughts of\ncertain " +
                                    "creatures. When you cast the spell and as\nyour action on each " +
                                    "turn until the spell ends, you can\nfocus your mind on any one " +
                                    "creature that you can\nsee within 30 feet of you. If the " +
                                    "creature you choose\nhas an Intelligence of 3 or lower or " +
                                    "doesn't speak\nany language, the creature is unaffected.\nYou " +
                                    "initially learn the surface thoughts of the\ncreature—what is " +
                                    "most on its mind in that moment.\nAs an action, you can either " +
                                    "shift your attention to\nanother creature's thoughts or " +
                                    "attempt to probe\ndeeper into the same creature's mind. If you " +
                                    "probe\ndeeper, the target must make a Wisdom saving\nthrow. If " +
                                    "it fails, you gain insight into its reasoning (if\nany), its " +
                                    "emotional state, and something that looms\nlarge in its mind " +
                                    "(such as something it worries over,\nloves, or hates). If it " +
                                    "succeeds, the spell ends. Either\nway, the target knows that " +
                                    "you are probing into its\nmind, and unless you shift your " +
                                    "attention to another\ncreature's thoughts, the creature can " +
                                    "use its action\non its turn to make an Intelligence check " +
                                    "contested\nby your Intelligence check; if it succeeds, the " +
                                    "spell\nends.\nQuestions verbally directed at the target " +
                                    "creature\nnaturally shape the course of its thoughts, so " +
                                    "this\nspell is particularly effective as part of " +
                                    "an\ninterrogation.\nYou can also use this spell to detect the " +
                                    "presence\nof thinking creatures you can't see. When you " +
                                    "cast\nthe spell or as your action during the duration, " +
                                    "you\ncan search for thoughts within 30 feet of you. The\nspell " +
                                    "can penetrate barriers, but 2 feet of rock, 2\ninches of any " +
                                    "metal other than lead, or a thin sheet of\nlead blocks you. " +
                                    "You can't detect a creature with an\nIntelligence of 3 or " +
                                    "lower or one that doesn't speak\nany language.\nOnce you " +
                                    "detect the presence of a creature in this\nway, you can read " +
                                    "its thoughts for the rest of the\nduration as described above, " +
                                    "even if you can't see it,\nbut it must still be within range. ",
                         at_higher_levels="")


class DimensionDoor(spells.Spell):
    """
    Dimension Door Spell
    SRD p. 136
    Generated
    """

    def __init__(self):
        super().__init__(name="Dimension Door",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Conjuration,
                         spell_range="500 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You teleport yourself from your current location to\nany other " +
                                    "spot within range. You arrive at exactly\nthe spot desired. It " +
                                    "can be a place you can see, one\nyou can visualize, or one you " +
                                    "can describe by stating\ndistance and direction, such as “200 " +
                                    "feet straight\ndownward” or “upward to the northwest at a " +
                                    "45-\ndegree angle, 300 feet.”\nYou can bring along objects as " +
                                    "long as their weight\ndoesn't exceed what you can carry. You " +
                                    "can also\nbring one willing creature of your size or " +
                                    "smaller\nwho is carrying gear up to its carrying capacity. " +
                                    "The\ncreature must be within 5 feet of you when you cast\nthis " +
                                    "spell.\nIf you would arrive in a place already occupied by\nan " +
                                    "object or a creature, you and any creature\ntraveling with you " +
                                    "each take 4d6 force damage, and\nthe spell fails to teleport " +
                                    "you. ",
                         at_higher_levels="")


class DisguiseSelf(spells.Spell):
    """
    Disguise Self Spell
    SRD p. 136
    Generated
    """

    def __init__(self):
        super().__init__(name="Disguise Self",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Illusion,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You make yourself—including your clothing, armor,\nweapons, " +
                                    "and other belongings on your person—\nlook different until the " +
                                    "spell ends or until you use\nyour action to dismiss it. You " +
                                    "can seem 1 foot shorter\nor taller and can appear thin, fat, " +
                                    "or in between. You\ncan't change your body type, so you must " +
                                    "adopt a\nform that has the same basic arrangement of " +
                                    "limbs.\nOtherwise, the extent of the illusion is up to " +
                                    "you.\nThe changes wrought by this spell fail to hold up\nto " +
                                    "physical inspection. For example, if you use this\nspell to " +
                                    "add a hat to your outfit, objects pass through\nthe hat, and " +
                                    "anyone who touches it would feel\nnothing or would feel your " +
                                    "head and hair. If you use\nthis spell to appear thinner than " +
                                    "you are, the hand of\nsomeone who reaches out to touch you " +
                                    "would bump\ninto you while it was seemingly still in " +
                                    "midair.\nTo discern that you are disguised, a creature " +
                                    "can\nuse its action to inspect your appearance and " +
                                    "must\nsucceed on an Intelligence (Investigation) " +
                                    "check\nagainst your spell save DC. ",
                         at_higher_levels="")


class Disintegrate(spells.Spell):
    """
    Disintegrate Spell
    SRD p. 136-137
    Generated
    """

    def __init__(self):
        super().__init__(name="Disintegrate",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a lodestone and a pinch of dust",
                         duration="Instantaneous",
                         description="A thin green ray springs from your pointing finger to\na " +
                                    "target that you can see within range. The target can\nbe a " +
                                    "creature, an object, or a creation of magical\nforce, such as " +
                                    "the wall created by wall of force.\nA creature targeted by " +
                                    "this spell must make a\nDexterity saving throw. On a failed " +
                                    "save, the target\ntakes 10d6 + 40 force damage. If this " +
                                    "damage\nreduces the target to 0 hit points, it is " +
                                    "disintegrated.\nA disintegrated creature and everything it " +
                                    "is\nwearing and carrying, except magic items, are\nreduced to " +
                                    "a pile of fine gray dust. The creature can\nbe restored to " +
                                    "life only by means of a true\nresurrection or a wish " +
                                    "spell.\nThis spell automatically disintegrates a Large " +
                                    "or\nsmaller nonmagical object or a creation of magical\nforce. " +
                                    "If the target is a Huge or larger object or\ncreation of " +
                                    "force, this spell disintegrates a 10-footcube portion of it. A " +
                                    "magic item is unaffected by this\nspell. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, the damage increases\nby 3d6 for each slot level above " +
                                          "6th. ")


class DispelEvilAndGood(spells.Spell):
    """
    Dispel Evil and Good Spell
    SRD p. 137
    Generated
    """

    def __init__(self):
        super().__init__(name="Dispel Evil and Good",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Abjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="holy water or powdered silver and iron",
                         duration="1 minute",
                         description="Shimmering energy surrounds and protects you\nfrom fey, " +
                                    "undead, and creatures originating from\nbeyond the Material " +
                                    "Plane. For the duration,\ncelestials, elementals, fey, fiends, " +
                                    "and undead have\ndisadvantage on attack rolls against " +
                                    "you.\nYou can end the spell early by using either of " +
                                    "the\nfollowing special functions.\nBreak Enchantment. As your " +
                                    "action, you touch a\ncreature you can reach that is charmed, " +
                                    "frightened,\nor possessed by a celestial, an elemental, a fey, " +
                                    "a\nfiend, or an undead. The creature you touch is no\nlonger " +
                                    "charmed, frightened, or possessed by " +
                                    "such\ncreatures.\nDismissal. As your action, make a melee " +
                                    "spell\nattack against a celestial, an elemental, a fey, a " +
                                    "fiend,\nor an undead you can reach. On a hit, you attempt " +
                                    "to\ndrive the creature back to its home plane. The\ncreature " +
                                    "must succeed on a Charisma saving throw\nor be sent back to " +
                                    "its home plane (if it isn't there\nalready). If they aren't on " +
                                    "their home plane, undead\nare sent to the Shadowfell, and fey " +
                                    "are sent to the\nFeywild. ",
                         at_higher_levels="")


class DispelMagic(spells.Spell):
    """
    Dispel Magic Spell
    SRD p. 137
    Generated
    """

    def __init__(self):
        super().__init__(name="Dispel Magic",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Choose one creature, object, or magical effect within\nrange. " +
                                    "Any spell of 3rd level or lower on the target\nends. For each " +
                                    "spell of 4th level or higher on the\ntarget, make an ability " +
                                    "check using your spellcasting\nability. The DC equals 10 + the " +
                                    "spell's level. On a\nsuccessful check, the spell ends. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, you automatically\nend the effects of a spell on the " +
                                          "target if the spell's\nlevel is equal to or less than the " +
                                          "level of the spell slot\nyou used. ")


class Divination(spells.Spell):
    """
    Divination Spell
    SRD p. 137
    Generated
    """

    def __init__(self):
        super().__init__(name="Divination",
                         spell_lists=[SpellLists.DIVINE],
                         ritual=True,
                         level=4,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="incense and a sacrificial offering appropriate to your religion, together worth at least 25 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="Your magic and an offering put you in contact with a\ngod or a " +
                                    "god's servants. You ask a single question\nconcerning a " +
                                    "specific goal, event, or activity to occur\nwithin 7 days. The " +
                                    "GM offers a truthful reply. The\nreply might be a short " +
                                    "phrase, a cryptic rhyme, or an\nomen.\nThe spell doesn't take " +
                                    "into account any possible\ncircumstances that might change the " +
                                    "outcome, such\nas the casting of additional spells or the loss " +
                                    "or gain\nof a companion.\nIf you cast the spell two or more " +
                                    "times before\nfinishing your next long rest, there is a " +
                                    "cumulative\n25 percent chance for each casting after the first " +
                                    "that\nyou get a random reading. The GM makes this roll " +
                                    "in\nsecret. ",
                         at_higher_levels="")


class DivineFavor(spells.Spell):
    """
    Divine Favor Spell
    SRD p. 137-138
    Generated
    """

    def __init__(self):
        super().__init__(name="Divine Favor",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="Your prayer empowers you with divine radiance.\nUntil the " +
                                    "spell ends, your weapon attacks deal an\nextra 1d4 radiant " +
                                    "damage on a hit. ",
                         at_higher_levels="")


class DivineWord(spells.Spell):
    """
    Divine Word Spell
    SRD p. 138
    Generated
    """

    def __init__(self):
        super().__init__(name="Divine Word",
                         spell_lists=[SpellLists.DIVINE],
                         level=7,
                         school=SpellSchools.Evocation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You utter a divine word, imbued with the power that\nshaped " +
                                    "the world at the dawn of creation. Choose\nany number of " +
                                    "creatures you can see within range.\nEach creature that can " +
                                    "hear you must make a\nCharisma saving throw. On a failed save, " +
                                    "a creature\nsuffers an effect based on its current hit " +
                                    "points:\n• 50 hit points or fewer: deafened for 1 minute\n• 40 " +
                                    "hit points or fewer: deafened and blinded for\n10 minutes\n• " +
                                    "30 hit points or fewer: blinded, deafened, and\nstunned for 1 " +
                                    "hour\n• 20 hit points or fewer: killed instantly\nRegardless " +
                                    "of its current hit points, a celestial, an\nelemental, a fey, " +
                                    "or a fiend that fails its save is forced\nback to its plane of " +
                                    "origin (if it isn't there already)\nand can't return to your " +
                                    "current plane for 24 hours\nby any means short of a wish " +
                                    "spell. ",
                         at_higher_levels="")


class DominateBeast(spells.Spell):
    """
    Dominate Beast Spell
    SRD p. 138
    Generated
    """

    def __init__(self):
        super().__init__(name="Dominate Beast",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You attempt to beguile a beast that you can see\nwithin range. " +
                                    "It must succeed on a Wisdom saving\nthrow or be charmed by you " +
                                    "for the duration. If you\nor creatures that are friendly to " +
                                    "you are fighting it, it\nhas advantage on the saving " +
                                    "throw.\nWhile the beast is charmed, you have a " +
                                    "telepathic\nlink with it as long as the two of you are on the " +
                                    "same\nplane of existence. You can use this telepathic link " +
                                    "to\nissue commands to the creature while you are\nconscious " +
                                    "(no action required), which it does its best\nto obey. You can " +
                                    "specify a simple and general course\nof action, such as " +
                                    "“Attack that creature,” “Run over\nthere,” or “Fetch that " +
                                    "object.” If the creature\ncompletes the order and doesn't " +
                                    "receive further\ndirection from you, it defends and preserves " +
                                    "itself to\nthe best of its ability.\nYou can use your action " +
                                    "to take total and precise\ncontrol of the target. Until the " +
                                    "end of your next turn,\nthe creature takes only the actions " +
                                    "you choose, and\ndoesn't do anything that you don't allow it " +
                                    "to do.\nDuring this time, you can also cause the creature " +
                                    "to\nuse a reaction, but this requires you to use your " +
                                    "own\nreaction as well.\nEach time the target takes damage, it " +
                                    "makes a new\nWisdom saving throw against the spell. If the " +
                                    "saving\nthrow succeeds, the spell ends. ",
                         at_higher_levels="When you cast this spell with a\n5th-level spell slot, the " +
                                          "duration is concentration, up\nto 10 minutes. When you use a " +
                                          "6th-level spell slot,\nthe duration is concentration, up to 1 " +
                                          "hour. When\nyou use a spell slot of 7th level or higher, " +
                                          "the\nduration is concentration, up to 8 hours. ")


class DominateMonster(spells.Spell):
    """
    Dominate Monster Spell
    SRD p. 138-139
    Generated
    """

    def __init__(self):
        super().__init__(name="Dominate Monster",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You attempt to beguile a creature that you can see\nwithin " +
                                    "range. It must succeed on a Wisdom saving\nthrow or be charmed " +
                                    "by you for the duration. If you\nor creatures that are " +
                                    "friendly to you are fighting it, it\nhas advantage on the " +
                                    "saving throw.\nWhile the creature is charmed, you have " +
                                    "a\ntelepathic link with it as long as the two of you are\non " +
                                    "the same plane of existence. You can use this\ntelepathic link " +
                                    "to issue commands to the creature\nwhile you are conscious (no " +
                                    "action required), which\nit does its best to obey. You can " +
                                    "specify a simple and\ngeneral course of action, such as " +
                                    "“Attack that\ncreature,” “Run over there,” or “Fetch that " +
                                    "object.” If\nthe creature completes the order and doesn't " +
                                    "receive\nfurther direction from you, it defends and " +
                                    "preserves\nitself to the best of its ability.\nYou can use " +
                                    "your action to take total and precise\ncontrol of the target. " +
                                    "Until the end of your next turn,\nthe creature takes only the " +
                                    "actions you choose, and\ndoesn't do anything that you don't " +
                                    "allow it to do.\nDuring this time, you can also cause the " +
                                    "creature to\nuse a reaction, but this requires you to use your " +
                                    "own\nreaction as well.\nEach time the target takes damage, it " +
                                    "makes a new\nWisdom saving throw against the spell. If the " +
                                    "saving\nthrow succeeds, the spell ends. ",
                         at_higher_levels="When you cast this spell with a\n9th-level spell slot, the " +
                                          "duration is concentration, up\nto 8 hours. ")


class DominatePerson(spells.Spell):
    """
    Dominate Person Spell
    SRD p. 139
    Generated
    """

    def __init__(self):
        super().__init__(name="Dominate Person",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You attempt to beguile a humanoid that you can see\nwithin " +
                                    "range. It must succeed on a Wisdom saving\nthrow or be charmed " +
                                    "by you for the duration. If you\nor creatures that are " +
                                    "friendly to you are fighting it, it\nhas advantage on the " +
                                    "saving throw.\nWhile the target is charmed, you have a " +
                                    "telepathic\nlink with it as long as the two of you are on the " +
                                    "same\nplane of existence. You can use this telepathic link " +
                                    "to\nissue commands to the creature while you are\nconscious " +
                                    "(no action required), which it does its best\nto obey. You can " +
                                    "specify a simple and general course\nof action, such as " +
                                    "“Attack that creature,” “Run over\nthere,” or “Fetch that " +
                                    "object.” If the creature\ncompletes the order and doesn't " +
                                    "receive further\ndirection from you, it defends and preserves " +
                                    "itself to\nthe best of its ability.\nYou can use your action " +
                                    "to take total and precise\ncontrol of the target. Until the " +
                                    "end of your next turn,\nthe creature takes only the actions " +
                                    "you choose, and\ndoesn't do anything that you don't allow it " +
                                    "to do.\nDuring this time you can also cause the creature " +
                                    "to\nuse a reaction, but this requires you to use your " +
                                    "own\nreaction as well.\nEach time the target takes damage, it " +
                                    "makes a new\nWisdom saving throw against the spell. If the " +
                                    "saving\nthrow succeeds, the spell ends. ",
                         at_higher_levels="When you cast this spell using a\n6th-level spell slot, the " +
                                          "duration is concentration, up\nto 10 minutes. When you use a " +
                                          "7th-level spell slot,\nthe duration is concentration, up to 1 " +
                                          "hour. When\nyou use a spell slot of 8th level or higher, " +
                                          "the\nduration is concentration, up to 8 hours. ")


class Dream(spells.Spell):
    """
    Dream Spell
    SRD p. 139
    Generated
    """

    def __init__(self):
        super().__init__(name="Dream",
                         spell_lists=[SpellLists.ARCANE],
                         level=5,
                         school=SpellSchools.Illusion,
                         spell_range="Special",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a handful of sand, a dab of ink, and a writing quill plucked from a sleeping bird",
                         duration="8 hours",
                         description="This spell shapes a creature's dreams. Choose a\ncreature " +
                                    "known to you as the target of this spell. The\ntarget must be " +
                                    "on the same plane of existence as you.\nCreatures that don't " +
                                    "sleep, such as elves, can't be\ncontacted by this spell. You, " +
                                    "or a willing creature you\ntouch, enters a trance state, " +
                                    "acting as a messenger.\nWhile in the trance, the messenger is " +
                                    "aware of his or\nher surroundings, but can't take actions or " +
                                    "move.\nIf the target is asleep, the messenger appears in\nthe " +
                                    "target's dreams and can converse with the target\nas long as " +
                                    "it remains asleep, through the duration of\nthe spell. The " +
                                    "messenger can also shape the\nenvironment of the dream, " +
                                    "creating landscapes,\nobjects, and other images. The messenger " +
                                    "can\nemerge from the trance at any time, ending the effect\nof " +
                                    "the spell early. The target recalls the dream\nperfectly upon " +
                                    "waking. If the target is awake when\nyou cast the spell, the " +
                                    "messenger knows it, and can\neither end the trance (and the " +
                                    "spell) or wait for the\ntarget to fall asleep, at which point " +
                                    "the messenger\nappears in the target's dreams.\nYou can make " +
                                    "the messenger appear monstrous\nand terrifying to the target. " +
                                    "If you do, the messenger\ncan deliver a message of no more " +
                                    "than ten words\nand then the target must make a Wisdom " +
                                    "saving\nthrow. On a failed save, echoes of the " +
                                    "phantasmal\nmonstrosity spawn a nightmare that lasts " +
                                    "the\nduration of the target's sleep and prevents the " +
                                    "target\nfrom gaining any benefit from that rest. In " +
                                    "addition,\nwhen the target wakes up, it takes 3d6 " +
                                    "psychic\ndamage.\nIf you have a body part, lock of hair, " +
                                    "clipping from\na nail, or similar portion of the target's " +
                                    "body, the\ntarget makes its saving throw with disadvantage. ",
                         at_higher_levels="")


class Druidcraft(spells.Spell):
    """
    Druidcraft Spell
    SRD p. 139-140
    Generated
    """

    def __init__(self):
        super().__init__(name="Druidcraft",
                         spell_lists=[SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Whispering to the spirits of nature, you create one of\nthe " +
                                    "following effects within range:\n• You create a tiny, harmless " +
                                    "sensory effect that\npredicts what the weather will be at your " +
                                    "location\nfor the next 24 hours. The effect might manifest " +
                                    "as\na golden orb for clear skies, a cloud for rain, " +
                                    "falling\nsnowflakes for snow, and so on. This effect\npersists " +
                                    "for 1 round.\n• You instantly make a flower blossom, a seed " +
                                    "pod\nopen, or a leaf bud bloom.\n• You create an " +
                                    "instantaneous, harmless sensory\neffect, such as falling " +
                                    "leaves, a puff of wind, the\nsound of a small animal, or the " +
                                    "faint odor of skunk.\nThe effect must fit in a 5-foot cube.\n• " +
                                    "You instantly light or snuff out a candle, a torch, or\na " +
                                    "small campfire. ",
                         at_higher_levels="")


class Earthquake(spells.Spell):
    """
    Earthquake Spell
    SRD p. 140
    Generated
    """

    def __init__(self):
        super().__init__(name="Earthquake",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Evocation,
                         spell_range="500 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of dirt, a piece of rock, and a lump of clay",
                         duration="1 minute",
                         description="You create a seismic disturbance at a point on the\nground " +
                                    "that you can see within range. For the\nduration, an intense " +
                                    "tremor rips through the ground\nin a 100-foot-radius circle " +
                                    "centered on that point\nand shakes creatures and structures in " +
                                    "contact with\nthe ground in that area.\nThe ground in the area " +
                                    "becomes difficult terrain.\nEach creature on the ground that " +
                                    "is concentrating\nmust make a Constitution saving throw. On a " +
                                    "failed\nsave, the creature's concentration is broken.\nWhen " +
                                    "you cast this spell and at the end of each\nturn you spend " +
                                    "concentrating on it, each creature on\nthe ground in the area " +
                                    "must make a Dexterity saving\nthrow. On a failed save, the " +
                                    "creature is knocked\nprone.\nThis spell can have additional " +
                                    "effects depending\non the terrain in the area, as determined " +
                                    "by the GM.\nFissures. Fissures open throughout the " +
                                    "spell's\narea at the start of your next turn after you cast " +
                                    "the\nspell. A total of 1d6 such fissures open in " +
                                    "locations\nchosen by the GM. Each is 1d10 × 10 feet deep, " +
                                    "10\nfeet wide, and extends from one edge of the spell's\narea " +
                                    "to the opposite side. A creature standing on a\nspot where a " +
                                    "fissure opens must succeed on a\nDexterity saving throw or " +
                                    "fall in. A creature that\nsuccessfully saves moves with the " +
                                    "fissure's edge as it\nopens.\nA fissure that opens beneath a " +
                                    "structure causes it\nto automatically collapse (see " +
                                    "below).\nStructures. The tremor deals 50 bludgeoning\ndamage " +
                                    "to any structure in contact with the ground\nin the area when " +
                                    "you cast the spell and at the start of\neach of your turns " +
                                    "until the spell ends. If a structure\ndrops to 0 hit points, " +
                                    "it collapses and potentially\ndamages nearby creatures. A " +
                                    "creature within half the\ndistance of a structure's height " +
                                    "must make a\nDexterity saving throw. On a failed save, the " +
                                    "creature\ntakes 5d6 bludgeoning damage, is knocked prone,\nand " +
                                    "is buried in the rubble, requiring a DC 20\nStrength " +
                                    "(Athletics) check as an action to escape.\nThe GM can adjust " +
                                    "the DC higher or lower,\ndepending on the nature of the " +
                                    "rubble. On a\nsuccessful save, the creature takes half as " +
                                    "much\ndamage and doesn't fall prone or become buried. ",
                         at_higher_levels="")


class EnhanceAbility(spells.Spell):
    """
    Enhance Ability Spell
    SRD p. 140-141
    Generated
    """

    def __init__(self):
        super().__init__(name="Enhance Ability",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="fur or a feather from a beast",
                         duration="1 hour.",
                         description="You touch a creature and bestow upon it a " +
                                    "magical\nenhancement. Choose one of the following " +
                                    "effects;\nthe target gains that effect until the spell " +
                                    "ends.\nBear's Endurance. The target has advantage " +
                                    "on\nConstitution checks. It also gains 2d6 temporary " +
                                    "hit\npoints, which are lost when the spell ends.\nBull's " +
                                    "Strength. The target has advantage on\nStrength checks, and " +
                                    "his or her carrying capacity\ndoubles.\nCat's Grace. The " +
                                    "target has advantage on Dexterity\nchecks. It also doesn't " +
                                    "take damage from falling 20\nfeet or less if it isn't " +
                                    "incapacitated.\nEagle's Splendor. The target has advantage " +
                                    "on\nCharisma checks.\nFox's Cunning. The target has advantage " +
                                    "on\nIntelligence checks.\nOwl's Wisdom. The target has " +
                                    "advantage on\nWisdom checks. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 2nd. ")


class EnlargeReduce(spells.Spell):
    """
    Enlarge/Reduce Spell
    SRD p. 141
    Generated
    """

    def __init__(self):
        super().__init__(name="Enlarge/Reduce",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of powdered iron",
                         duration="1 minute",
                         description="You cause a creature or an object you can see within\nrange to " +
                                    "grow larger or smaller for the duration.\nChoose either a " +
                                    "creature or an object that is neither\nworn nor carried. If " +
                                    "the target is unwilling, it can\nmake a Constitution saving " +
                                    "throw. On a success, the\nspell has no effect.\nIf the target " +
                                    "is a creature, everything it is wearing\nand carrying changes " +
                                    "size with it. Any item dropped\nby an affected creature " +
                                    "returns to normal size at\nonce.\nEnlarge. The target's size " +
                                    "doubles in all\ndimensions, and its weight is multiplied by " +
                                    "eight.\nThis growth increases its size by one category—\nfrom " +
                                    "Medium to Large, for example. If there isn't\nenough room for " +
                                    "the target to double its size, the\ncreature or object attains " +
                                    "the maximum possible size\nin the space available. Until the " +
                                    "spell ends, the target\nalso has advantage on Strength checks " +
                                    "and Strength\nsaving throws. The target's weapons also grow " +
                                    "to\nmatch its new size. While these weapons are\nenlarged, the " +
                                    "target's attacks with them deal 1d4\nextra damage.\nReduce. " +
                                    "The target's size is halved in all\ndimensions, and its weight " +
                                    "is reduced to one-eighth\nof normal. This reduction decreases " +
                                    "its size by one\ncategory—from Medium to Small, for example. " +
                                    "Until\nthe spell ends, the target also has disadvantage " +
                                    "on\nStrength checks and Strength saving throws. The\ntarget's " +
                                    "weapons also shrink to match its new size.\nWhile these " +
                                    "weapons are reduced, the target's\nattacks with them deal 1d4 " +
                                    "less damage (this can't\nreduce the damage below 1). ",
                         at_higher_levels="")


class Entangle(spells.Spell):
    """
    Entangle Spell
    SRD p. 141
    Generated
    """

    def __init__(self):
        super().__init__(name="Entangle",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="Grasping weeds and vines sprout from the ground in\na 20-foot " +
                                    "square starting from a point within range.\nFor the duration, " +
                                    "these plants turn the ground in the\narea into difficult " +
                                    "terrain.\nA creature in the area when you cast the spell\nmust " +
                                    "succeed on a Strength saving throw or be\nrestrained by the " +
                                    "entangling plants until the spell\nends. A creature restrained " +
                                    "by the plants can use its\naction to make a Strength check " +
                                    "against your spell\nsave DC. On a success, it frees " +
                                    "itself.\nWhen the spell ends, the conjured plants wilt away. ",
                         at_higher_levels="")


class Enthrall(spells.Spell):
    """
    Enthrall Spell
    SRD p. 141
    Generated
    """

    def __init__(self):
        super().__init__(name="Enthrall",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You weave a distracting string of words, causing\ncreatures of " +
                                    "your choice that you can see within\nrange and that can hear " +
                                    "you to make a Wisdom\nsaving throw. Any creature that can't be " +
                                    "charmed\nsucceeds on this saving throw automatically, and " +
                                    "if\nyou or your companions are fighting a creature, it\nhas " +
                                    "advantage on the save. On a failed save, the\ntarget has " +
                                    "disadvantage on Wisdom (Perception)\nchecks made to perceive " +
                                    "any creature other than you\nuntil the spell ends or until the " +
                                    "target can no longer\nhear you. The spell ends if you are " +
                                    "incapacitated or\ncan no longer speak. ",
                         at_higher_levels="")


class Etherealness(spells.Spell):
    """
    Etherealness Spell
    SRD p. 141-142
    Generated
    """

    def __init__(self):
        super().__init__(name="Etherealness",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=7,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Up to 8 hours",
                         description="You step into the border regions of the Ethereal\nPlane, in " +
                                    "the area where it overlaps with your\ncurrent plane. You " +
                                    "remain in the Border Ethereal for\nthe duration or until you " +
                                    "use your action to dismiss\nthe spell. During this time, you " +
                                    "can move in any\ndirection. If you move up or down, every foot " +
                                    "of\nmovement costs an extra foot. You can see and hear\nthe " +
                                    "plane you originated from, but everything there\nlooks gray, " +
                                    "and you can't see anything more than 60\nfeet away.\nWhile on " +
                                    "the Ethereal Plane, you can only affect\nand be affected by " +
                                    "other creatures on that plane.\nCreatures that aren't on the " +
                                    "Ethereal Plane can't\nperceive you and can't interact with " +
                                    "you, unless a\nspecial ability or magic has given them the " +
                                    "ability to\ndo so.\nYou ignore all objects and effects that " +
                                    "aren't on the\nEthereal Plane, allowing you to move " +
                                    "through\nobjects you perceive on the plane you " +
                                    "originated\nfrom.\nWhen the spell ends, you immediately return " +
                                    "to\nthe plane you originated from in the spot you\ncurrently " +
                                    "occupy. If you occupy the same spot as a\nsolid object or " +
                                    "creature when this happens, you are\nimmediately shunted to " +
                                    "the nearest unoccupied\nspace that you can occupy and take " +
                                    "force damage\nequal to twice the number of feet you are " +
                                    "moved.\nThis spell has no effect if you cast it while you " +
                                    "are\non the Ethereal Plane or a plane that doesn't border\nit, " +
                                    "such as one of the Outer Planes. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 8th level or " +
                                          "higher, you can target up to\nthree willing creatures " +
                                          "(including you) for each slot\nlevel above 7th. The creatures " +
                                          "must be within 10 feet\nof you when you cast the spell. ")


class ExpeditiousRetreat(spells.Spell):
    """
    Expeditious Retreat Spell
    SRD p. 142
    Generated
    """

    def __init__(self):
        super().__init__(name="Expeditious Retreat",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="This spell allows you to move at an incredible pace.\nWhen you " +
                                    "cast this spell, and then as a bonus action\non each of your " +
                                    "turns until the spell ends, you can\ntake the Dash action. ",
                         at_higher_levels="")


class Eyebite(spells.Spell):
    """
    Eyebite Spell
    SRD p. 142
    Generated
    """

    def __init__(self):
        super().__init__(name="Eyebite",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Necromancy,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="For the spell's duration, your eyes become an inky\nvoid " +
                                    "imbued with dread power. One creature of your\nchoice within " +
                                    "60 feet of you that you can see must\nsucceed on a Wisdom " +
                                    "saving throw or be affected by\none of the following effects " +
                                    "of your choice for the\nduration. On each of your turns until " +
                                    "the spell ends,\nyou can use your action to target another " +
                                    "creature\nbut can't target a creature again if it has " +
                                    "succeeded\non a saving throw against this casting of " +
                                    "eyebite.\nAsleep. The target falls unconscious. It wakes up " +
                                    "if\nit takes any damage or if another creature uses " +
                                    "its\naction to shake the sleeper awake.\nPanicked. The target " +
                                    "is frightened of you. On each\nof its turns, the frightened " +
                                    "creature must take the\nDash action and move away from you by " +
                                    "the safest\nand shortest available route, unless there is " +
                                    "nowhere\nto move. If the target moves to a place at least 60 " +
                                    "feet\naway from you where it can no longer see you, " +
                                    "this\neffect ends.\nSickened. The target has disadvantage on " +
                                    "attack\nrolls and ability checks. At the end of each of " +
                                    "its\nturns, it can make another Wisdom saving throw. If\nit " +
                                    "succeeds, the effect ends. ",
                         at_higher_levels="")


class Fabricate(spells.Spell):
    """
    Fabricate Spell
    SRD p. 142
    Generated
    """

    def __init__(self):
        super().__init__(name="Fabricate",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Transmutation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You convert raw materials into products of the same\nmaterial. " +
                                    "For example, you can fabricate a wooden\nbridge from a clump " +
                                    "of trees, a rope from a patch of\nhemp, and clothes from flax " +
                                    "or wool.\nChoose raw materials that you can see within\nrange. " +
                                    "You can fabricate a Large or smaller object\n(contained within " +
                                    "a 10-foot cube, or eight connected\n5-foot cubes), given a " +
                                    "sufficient quantity of raw\nmaterial. If you are working with " +
                                    "metal, stone, or\nanother mineral substance, however, the " +
                                    "fabricated\nobject can be no larger than Medium " +
                                    "(contained\nwithin a single 5-foot cube). The quality of " +
                                    "objects\nmade by the spell is commensurate with the " +
                                    "quality\nof the raw materials.\nCreatures or magic items can't " +
                                    "be created or\ntransmuted by this spell. You also can't use it " +
                                    "to\ncreate items that ordinarily require a high degree " +
                                    "of\ncraftsmanship, such as jewelry, weapons, glass, or\narmor, " +
                                    "unless you have proficiency with the type of\nartisan's tools " +
                                    "used to craft such objects. ",
                         at_higher_levels="")


class FaerieFire(spells.Spell):
    """
    Faerie Fire Spell
    SRD p. 142-143
    Generated
    """

    def __init__(self):
        super().__init__(name="Faerie Fire",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 minute",
                         description="Each object in a 20-foot cube within range is\noutlined in " +
                                    "blue, green, or violet light (your choice).\nAny creature in " +
                                    "the area when the spell is cast is also\noutlined in light if " +
                                    "it fails a Dexterity saving throw.\nFor the duration, objects " +
                                    "and affected creatures shed\ndim light in a 10-foot " +
                                    "radius.\nAny attack roll against an affected creature " +
                                    "or\nobject has advantage if the attacker can see it, and\nthe " +
                                    "affected creature or object can't benefit from\nbeing " +
                                    "invisible. ",
                         at_higher_levels="")


class FaithfulHound(spells.Spell):
    """
    Faithful Hound Spell
    SRD p. 143
    Generated
    """

    def __init__(self):
        super().__init__(name="Faithful Hound",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny silver whistle, a piece of bone, and a thread",
                         duration="8 hours",
                         description="You conjure a phantom watchdog in an unoccupied\nspace that " +
                                    "you can see within range, where it\nremains for the duration, " +
                                    "until you dismiss it as an\naction, or until you move more " +
                                    "than 100 feet away\nfrom it.\nThe hound is invisible to all " +
                                    "creatures except you\nand can't be harmed. When a Small or " +
                                    "larger\ncreature comes within 30 feet of it without " +
                                    "first\nspeaking the password that you specify when you\ncast " +
                                    "this spell, the hound starts barking loudly. The\nhound sees " +
                                    "invisible creatures and can see into the\nEthereal Plane. It " +
                                    "ignores illusions.\nAt the start of each of your turns, the " +
                                    "hound\nattempts to bite one creature within 5 feet of it " +
                                    "that\nis hostile to you. The hound's attack bonus is equal\nto " +
                                    "your spellcasting ability modifier + your\nproficiency bonus. " +
                                    "On a hit, it deals 4d8 piercing\ndamage. ",
                         at_higher_levels="")


class FalseLife(spells.Spell):
    """
    False Life Spell
    SRD p. 143
    Generated
    """

    def __init__(self):
        super().__init__(name="False Life",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Necromancy,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small amount of alcohol or distilled spirits",
                         duration="1 hour",
                         description="Bolstering yourself with a necromantic facsimile of\nlife, you " +
                                    "gain 1d4 + 4 temporary hit points for the\nduration. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you gain 5 additional\ntemporary hit points for each " +
                                          "slot level above 1st. ")


class Fear(spells.Spell):
    """
    Fear Spell
    SRD p. 143
    Generated
    """

    def __init__(self):
        super().__init__(name="Fear",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Illusion,
                         spell_range="Self (30-foot cone)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a white feather or the heart of a hen",
                         duration="1 minute",
                         description="You project a phantasmal image of a creature's\nworst fears. " +
                                    "Each creature in a 30-foot cone must\nsucceed on a Wisdom " +
                                    "saving throw or drop\nwhatever it is holding and become " +
                                    "frightened for the\nduration.\nWhile frightened by this spell, " +
                                    "a creature must\ntake the Dash action and move away from you " +
                                    "by the\nsafest available route on each of its turns, " +
                                    "unless\nthere is nowhere to move. If the creature ends " +
                                    "its\nturn in a location where it doesn't have line of " +
                                    "sight\nto you, the creature can make a Wisdom saving\nthrow. " +
                                    "On a successful save, the spell ends for that\ncreature. ",
                         at_higher_levels="")


class FeatherFall(spells.Spell):
    """
    Feather Fall Spell
    SRD p. 143
    Generated
    """

    def __init__(self):
        super().__init__(name="Feather Fall",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list="a small feather or piece of down",
                         duration="1 minute",
                         description="Choose up to five falling creatures within range. A\nfalling " +
                                    "creature's rate of descent slows to 60 feet per\nround until " +
                                    "the spell ends. If the creature lands\nbefore the spell ends, " +
                                    "it takes no falling damage and\ncan land on its feet, and the " +
                                    "spell ends for that\ncreature. ",
                         at_higher_levels="")


class Feeblemind(spells.Spell):
    """
    Feeblemind Spell
    SRD p. 143-144
    Generated
    """

    def __init__(self):
        super().__init__(name="Feeblemind",
                         spell_lists=[SpellLists.ARCANE],
                         level=8,
                         school=SpellSchools.Enchantment,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a handful of clay, crystal, glass, or mineral spheres",
                         duration="Instantaneous",
                         description="You blast the mind of a creature that you can see\nwithin " +
                                    "range, attempting to shatter its intellect and\npersonality. " +
                                    "The target takes 4d6 psychic damage\nand must make an " +
                                    "Intelligence saving throw.\nOn a failed save, the creature's " +
                                    "Intelligence and\nCharisma scores become 1. The creature can't " +
                                    "cast\nspells, activate magic items, understand language, " +
                                    "or\ncommunicate in any intelligible way. The creature\ncan, " +
                                    "however, identify its friends, follow them, and\neven protect " +
                                    "them.\nAt the end of every 30 days, the creature can\nrepeat " +
                                    "its saving throw against this spell. If it\nsucceeds on its " +
                                    "saving throw, the spell ends.\nThe spell can also be ended by " +
                                    "greater restoration,\nheal, or wish. ",
                         at_higher_levels="")


class FindFamiliar(spells.Spell):
    """
    Find Familiar Spell
    SRD p. 144
    Generated
    """

    def __init__(self):
        super().__init__(name="Find Familiar",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Conjuration,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="10 gp worth of charcoal, incense, and herbs that must be consumed by fire in a brass brazier",
                         duration="Instantaneous",
                         description="You gain the service of a familiar, a spirit that takes\nan " +
                                    "animal form you choose: bat, cat, crab, frog (toad),\nhawk, " +
                                    "lizard, octopus, owl, poisonous snake, fish\n(quipper), rat, " +
                                    "raven, sea horse, spider, or weasel.\nAppearing in an " +
                                    "unoccupied space within range, the\nfamiliar has the " +
                                    "statistics of the chosen form, though\nit is a celestial, fey, " +
                                    "or fiend (your choice) instead of a\nbeast.\nYour familiar " +
                                    "acts independently of you, but it\nalways obeys your commands. " +
                                    "In combat, it rolls its\nown initiative and acts on its own " +
                                    "turn. A familiar\ncan't attack, but it can take other actions " +
                                    "as normal.\nWhen the familiar drops to 0 hit points, " +
                                    "it\ndisappears, leaving behind no physical form. It\nreappears " +
                                    "after you cast this spell again\nWhile your familiar is within " +
                                    "100 feet of you, you\ncan communicate with it telepathically. " +
                                    "Additionally,\nas an action, you can see through your " +
                                    "familiar's\neyes and hear what it hears until the start of " +
                                    "your\nnext turn, gaining the benefits of any special " +
                                    "senses\nthat the familiar has. During this time, you are " +
                                    "deaf\nand blind with regard to your own senses.\nAs an action, " +
                                    "you can temporarily dismiss your\nfamiliar. It disappears into " +
                                    "a pocket dimension\nwhere it awaits your summons. " +
                                    "Alternatively, you\ncan dismiss it forever. As an action while " +
                                    "it is\ntemporarily dismissed, you can cause it to reappear\nin " +
                                    "any unoccupied space within 30 feet of you.\nYou can't have " +
                                    "more than one familiar at a time. If\nyou cast this spell " +
                                    "while you already have a familiar,\nyou instead cause it to " +
                                    "adopt a new form. Choose one\nof the forms from the above " +
                                    "list. Your familiar\ntransforms into the chosen " +
                                    "creature.\nFinally, when you cast a spell with a range of " +
                                    "touch,\nyour familiar can deliver the spell as if it had cast " +
                                    "the\nspell. Your familiar must be within 100 feet of you,\nand " +
                                    "it must use its reaction to deliver the spell when\nyou cast " +
                                    "it. If the spell requires an attack roll, you use\nyour attack " +
                                    "modifier for the roll. ",
                         at_higher_levels="")


class FindSteed(spells.Spell):
    """
    Find Steed Spell
    SRD p. 144
    Generated
    """

    def __init__(self):
        super().__init__(name="Find Steed",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You summon a spirit that assumes the form of an\nunusually " +
                                    "intelligent, strong, and loyal steed,\ncreating a long-lasting " +
                                    "bond with it. Appearing in an\nunoccupied space within range, " +
                                    "the steed takes on a\nform that you choose: a warhorse, a " +
                                    "pony, a camel,\nan elk, or a mastiff. (Your GM might allow " +
                                    "other\nanimals to be summoned as steeds.) The steed has\nthe " +
                                    "statistics of the chosen form, though it is a\ncelestial, fey, " +
                                    "or fiend (your choice) instead of its\nnormal type. " +
                                    "Additionally, if your steed has an\nIntelligence of 5 or less, " +
                                    "its Intelligence becomes 6,\nand it gains the ability to " +
                                    "understand one language of\nyour choice that you speak.\nYour " +
                                    "steed serves you as a mount, both in combat\nand out, and you " +
                                    "have an instinctive bond with it\nthat allows you to fight as " +
                                    "a seamless unit. While\nmounted on your steed, you can make " +
                                    "any spell you\ncast that targets only you also target your " +
                                    "steed.\nWhen the steed drops to 0 hit points, it " +
                                    "disappears,\nleaving behind no physical form. You can " +
                                    "also\ndismiss your steed at any time as an action, causing\nit " +
                                    "to disappear. In either case, casting this spell " +
                                    "again\nsummons the same steed, restored to its hit " +
                                    "point\nmaximum.\nWhile your steed is within 1 mile of you, you " +
                                    "can\ncommunicate with it telepathically.\nYou can't have more " +
                                    "than one steed bonded by\nthis spell at a time. As an action, " +
                                    "you can release the\nsteed from its bond at any time, causing " +
                                    "it to\ndisappear. ",
                         at_higher_levels="")


class FindTraps(spells.Spell):
    """
    Find Traps Spell
    SRD p. 145
    Generated
    """

    def __init__(self):
        super().__init__(name="Find Traps",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.Divination,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You sense the presence of any trap within range that\nis " +
                                    "within line of sight. A trap, for the purpose of this\nspell, " +
                                    "includes anything that would inflict a sudden\nor unexpected " +
                                    "effect you consider harmful or\nundesirable, which was " +
                                    "specifically intended as such\nby its creator. Thus, the spell " +
                                    "would sense an area\naffected by the alarm spell, a glyph of " +
                                    "warding, or a\nmechanical pit trap, but it would not reveal a " +
                                    "natural\nweakness in the floor, an unstable ceiling, or " +
                                    "a\nhidden sinkhole.\nThis spell merely reveals that a trap is " +
                                    "present.\nYou don't learn the location of each trap, but you " +
                                    "do\nlearn the general nature of the danger posed by a\ntrap " +
                                    "you sense. ",
                         at_higher_levels="")


class FindThePath(spells.Spell):
    """
    Find the Path Spell
    SRD p. 144-145
    Generated
    """

    def __init__(self):
        super().__init__(name="Find the Path",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a set of divinatory tools—such as bones, ivory sticks, cards, teeth, or carved runes—worth 100 gp and an object from the location you wish to find",
                         duration="1 day",
                         description="This spell allows you to find the shortest, most " +
                                    "direct\nphysical route to a specific fixed location that " +
                                    "you\nare familiar with on the same plane of existence. If\nyou " +
                                    "name a destination on another plane of\nexistence, a " +
                                    "destination that moves (such as a mobile\nfortress), or a " +
                                    "destination that isn't specific (such as\n“a green dragon's " +
                                    "lair”), the spell fails.\nFor the duration, as long as you are " +
                                    "on the same\nplane of existence as the destination, you know " +
                                    "how\nfar it is and in what direction it lies. While you " +
                                    "are\ntraveling there, whenever you are presented with " +
                                    "a\nchoice of paths along the way, you automatically\ndetermine " +
                                    "which path is the shortest and most direct\nroute (but not " +
                                    "necessarily the safest route) to the\ndestination. ",
                         at_higher_levels="")


class FingerOfDeath(spells.Spell):
    """
    Finger of Death Spell
    SRD p. 145
    Generated
    """

    def __init__(self):
        super().__init__(name="Finger of Death",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Necromancy,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You send negative energy coursing through a\ncreature that you " +
                                    "can see within range, causing it\nsearing pain. The target " +
                                    "must make a Constitution\nsaving throw. It takes 7d8 + 30 " +
                                    "necrotic damage on a\nfailed save, or half as much damage on a " +
                                    "successful\none.\nA humanoid killed by this spell rises at the " +
                                    "start of\nyour next turn as a zombie that is " +
                                    "permanently\nunder your command, following your verbal " +
                                    "orders\nto the best of its ability. ",
                         at_higher_levels="")


class FireBolt(spells.Spell):
    """
    Fire Bolt Spell
    SRD p. 145
    Generated
    """

    def __init__(self):
        super().__init__(name="Fire Bolt",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You hurl a mote of fire at a creature or object within\nrange. " +
                                    "Make a ranged spell attack against the target.\nOn a hit, the " +
                                    "target takes 1d10 fire damage. A\nflammable object hit by this " +
                                    "spell ignites if it isn't\nbeing worn or carried.\nThis " +
                                    "spell's damage increases by 1d10 when you\nreach 5th level " +
                                    "(2d10), 11th level (3d10), and 17th\nlevel (4d10). ",
                         at_higher_levels="")


class FireShield(spells.Spell):
    """
    Fire Shield Spell
    SRD p. 145-146
    Generated
    """

    def __init__(self):
        super().__init__(name="Fire Shield",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Evocation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of phosphorus or a firefly",
                         duration="10 minutes",
                         description="Thin and wispy flames wreathe your body for the\nduration, " +
                                    "shedding bright light in a 10-foot radius\nand dim light for " +
                                    "an additional 10 feet. You can end\nthe spell early by using " +
                                    "an action to dismiss it.\nThe flames provide you with a warm " +
                                    "shield or a\nchill shield, as you choose. The warm shield " +
                                    "grants\nyou resistance to cold damage, and the chill " +
                                    "shield\ngrants you resistance to fire damage.\nIn addition, " +
                                    "whenever a creature within 5 feet of\nyou hits you with a " +
                                    "melee attack, the shield erupts\nwith flame. The attacker " +
                                    "takes 2d8 fire damage from\na warm shield, or 2d8 cold damage " +
                                    "from a cold\nshield. ",
                         at_higher_levels="")


class FireStorm(spells.Spell):
    """
    Fire Storm Spell
    SRD p. 146
    Generated
    """

    def __init__(self):
        super().__init__(name="Fire Storm",
                         spell_lists=[SpellLists.PRIMAL],
                         level=7,
                         school=SpellSchools.Evocation,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="A storm made up of sheets of roaring flame appears\nin a " +
                                    "location you choose within range. The area of\nthe storm " +
                                    "consists of up to ten 10-foot cubes, which\nyou can arrange as " +
                                    "you wish. Each cube must have at\nleast one face adjacent to " +
                                    "the face of another cube.\nEach creature in the area must make " +
                                    "a Dexterity\nsaving throw. It takes 7d10 fire damage on a " +
                                    "failed\nsave, or half as much damage on a successful one.\nThe " +
                                    "fire damages objects in the area and ignites\nflammable " +
                                    "objects that aren't being worn or carried.\nIf you choose, " +
                                    "plant life in the area is unaffected by\nthis spell. ",
                         at_higher_levels="")


class Fireball(spells.Spell):
    """
    Fireball Spell
    SRD p. 145
    Generated
    """

    def __init__(self):
        super().__init__(name="Fireball",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.Evocation,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny ball of bat guano and sulfur",
                         duration="Instantaneous",
                         description="A bright streak flashes from your pointing finger to a\npoint " +
                                    "you choose within range and then blossoms\nwith a low roar " +
                                    "into an explosion of flame. Each\ncreature in a 20-foot-radius " +
                                    "sphere centered on that\npoint must make a Dexterity saving " +
                                    "throw. A target\ntakes 8d6 fire damage on a failed save, or " +
                                    "half as\nmuch damage on a successful one.\nThe fire spreads " +
                                    "around corners. It ignites\nflammable objects in the area that " +
                                    "aren't being worn\nor carried. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the damage increases\nby 1d6 for each slot level above " +
                                          "3rd. ")


class FlameBlade(spells.Spell):
    """
    Flame Blade Spell
    SRD p. 146
    Generated
    """

    def __init__(self):
        super().__init__(name="Flame Blade",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="leaf of sumac",
                         duration="10 minutes",
                         description="You evoke a fiery blade in your free hand. The blade\nis " +
                                    "similar in size and shape to a scimitar, and it lasts\nfor the " +
                                    "duration. If you let go of the blade, it\ndisappears, but you " +
                                    "can evoke the blade again as a\nbonus action.\nYou can use " +
                                    "your action to make a melee spell\nattack with the fiery " +
                                    "blade. On a hit, the target takes\n3d6 fire damage.\nThe " +
                                    "flaming blade sheds bright light in a 10-foot\nradius and dim " +
                                    "light for an additional 10 feet. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the damage increases\nby 1d6 for every two slot levels " +
                                          "above 2nd. ")


class FlameStrike(spells.Spell):
    """
    Flame Strike Spell
    SRD p. 146
    Generated
    """

    def __init__(self):
        super().__init__(name="Flame Strike",
                         spell_lists=[SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="pinch of sulfur",
                         duration="Instantaneous",
                         description="A vertical column of divine fire roars down from the\nheavens " +
                                    "in a location you specify. Each creature in a\n10-foot-radius, " +
                                    "40-foot-high cylinder centered on a\npoint within range must " +
                                    "make a Dexterity saving\nthrow. A creature takes 4d6 fire " +
                                    "damage and 4d6\nradiant damage on a failed save, or half as " +
                                    "much\ndamage on a successful one. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the fire damage or\nthe radiant damage (your choice) " +
                                          "increases by 1d6\nfor each slot level above 5th. ")


class FlamingSphere(spells.Spell):
    """
    Flaming Sphere Spell
    SRD p. 146
    Generated
    """

    def __init__(self):
        super().__init__(name="Flaming Sphere",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of tallow, a pinch of brimstone, and a dusting of powdered iron",
                         duration="1 minute",
                         description="A 5-foot-diameter sphere of fire appears in an\nunoccupied " +
                                    "space of your choice within range and\nlasts for the duration. " +
                                    "Any creature that ends its turn\nwithin 5 feet of the sphere " +
                                    "must make a Dexterity\nsaving throw. The creature takes 2d6 " +
                                    "fire damage on\na failed save, or half as much damage on a " +
                                    "successful\none.\nAs a bonus action, you can move the sphere " +
                                    "up to\n30 feet. If you ram the sphere into a creature, " +
                                    "that\ncreature must make the saving throw against " +
                                    "the\nsphere's damage, and the sphere stops moving " +
                                    "this\nturn.\nWhen you move the sphere, you can direct it " +
                                    "over\nbarriers up to 5 feet tall and jump it across pits up " +
                                    "to\n10 feet wide. The sphere ignites flammable objects\nnot " +
                                    "being worn or carried, and it sheds bright light in\na 20-foot " +
                                    "radius and dim light for an additional 20\nfeet. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the damage\nincreases by 1d6 for each slot level above " +
                                          "2nd. ")


class FleshToStone(spells.Spell):
    """
    Flesh to Stone Spell
    SRD p. 146-147
    Generated
    """

    def __init__(self):
        super().__init__(name="Flesh to Stone",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of lime, water, and earth",
                         duration="1 minute",
                         description="You attempt to turn one creature that you can see\nwithin " +
                                    "range into stone. If the target's body is made\nof flesh, the " +
                                    "creature must make a Constitution\nsaving throw. On a failed " +
                                    "save, it is restrained as its\nflesh begins to harden. On a " +
                                    "successful save, the\ncreature isn't affected.\nA creature " +
                                    "restrained by this spell must make\nanother Constitution " +
                                    "saving throw at the end of each\nof its turns. If it " +
                                    "successfully saves against this spell\nthree times, the spell " +
                                    "ends. If it fails its saves three\ntimes, it is turned to " +
                                    "stone and subjected to the\npetrified condition for the " +
                                    "duration. The successes\nand failures don't need to be " +
                                    "consecutive; keep track\nof both until the target collects " +
                                    "three of a kind.\nIf the creature is physically broken while " +
                                    "petrified,\nit suffers from similar deformities if it reverts " +
                                    "to its\noriginal state.\nIf you maintain your concentration on " +
                                    "this spell\nfor the entire possible duration, the creature " +
                                    "is\nturned to stone until the effect is removed. ",
                         at_higher_levels="")


class FloatingDisk(spells.Spell):
    """
    Floating Disk Spell
    SRD p. 147
    Generated
    """

    def __init__(self):
        super().__init__(name="Floating Disk",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of mercury",
                         duration="1 hour",
                         description="This spell creates a circular, horizontal plane of force,\n3 " +
                                    "feet in diameter and 1 inch thick, that floats 3 feet\nabove " +
                                    "the ground in an unoccupied space of your\nchoice that you can " +
                                    "see within range. The disk\nremains for the duration, and can " +
                                    "hold up to 500\npounds. If more weight is placed on it, the " +
                                    "spell ends,\nand everything on the disk falls to the " +
                                    "ground.\nThe disk is immobile while you are within 20 feet\nof " +
                                    "it. If you move more than 20 feet away from it, the\ndisk " +
                                    "follows you so that it remains within 20 feet of\nyou. It can " +
                                    "move across uneven terrain, up or down\nstairs, slopes and the " +
                                    "like, but it can't cross an\nelevation change of 10 feet or " +
                                    "more. For example, the\ndisk can't move across a 10-foot-deep " +
                                    "pit, nor could\nit leave such a pit if it was created at the " +
                                    "bottom.\nIf you move more than 100 feet from the " +
                                    "disk\n(typically because it can't move around an obstacle\nto " +
                                    "follow you), the spell ends. ",
                         at_higher_levels="")


class Fly(spells.Spell):
    """
    Fly Spell
    SRD p. 147
    Generated
    """

    def __init__(self):
        super().__init__(name="Fly",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a wing feather from any bird",
                         duration="10 minutes",
                         description="You touch a willing creature. The target gains a\nflying speed " +
                                    "of 60 feet for the duration. When the\nspell ends, the target " +
                                    "falls if it is still aloft, unless it\ncan stop the fall. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 3rd. ")


class FogCloud(spells.Spell):
    """
    Fog Cloud Spell
    SRD p. 147
    Generated
    """

    def __init__(self):
        super().__init__(name="Fog Cloud",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Conjuration,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You create a 20-foot-radius sphere of fog centered\non a point " +
                                    "within range. The sphere spreads around\ncorners, and its area " +
                                    "is heavily obscured. It lasts for\nthe duration or until a " +
                                    "wind of moderate or greater\nspeed (at least 10 miles per " +
                                    "hour) disperses it. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the radius of the fog\nincreases by 20 feet for each " +
                                          "slot level above 1st. ")


class Forbiddance(spells.Spell):
    """
    Forbiddance Spell
    SRD p. 147-148
    Generated
    """

    def __init__(self):
        super().__init__(name="Forbiddance",
                         spell_lists=[SpellLists.DIVINE],
                         ritual=True,
                         level=6,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a sprinkling of holy water, rare incense, and powdered ruby worth at least 1,000 gp",
                         duration="1 day",
                         description="You create a ward against magical travel that\nprotects up to " +
                                    "40,000 square feet of floor space to a\nheight of 30 feet " +
                                    "above the floor. For the duration,\ncreatures can't teleport " +
                                    "into the area or use portals,\nsuch as those created by the " +
                                    "gate spell, to enter the\narea. The spell proofs the area " +
                                    "against planar travel,\nand therefore prevents creatures from " +
                                    "accessing the\narea by way of the Astral Plane, Ethereal " +
                                    "Plane,\nFeywild, Shadowfell, or the plane shift spell.\nIn " +
                                    "addition, the spell damages types of creatures\nthat you " +
                                    "choose when you cast it. Choose one or\nmore of the following: " +
                                    "celestials, elementals, fey,\nfiends, and undead. When a " +
                                    "chosen creature enters\nthe spell's area for the first time on " +
                                    "a turn or starts\nits turn there, the creature takes 5d10 " +
                                    "radiant or\nnecrotic damage (your choice when you cast " +
                                    "this\nspell).\nWhen you cast this spell, you can designate " +
                                    "a\npassword. A creature that speaks the password as it\nenters " +
                                    "the area takes no damage from the spell.\nThe spell's area " +
                                    "can't overlap with the area of\nanother forbiddance spell. If " +
                                    "you cast forbiddance\nevery day for 30 days in the same " +
                                    "location, the spell\nlasts until it is dispelled, and the " +
                                    "material\ncomponents are consumed on the last casting. ",
                         at_higher_levels="")


class Forcecage(spells.Spell):
    """
    Forcecage Spell
    SRD p. 148
    Generated
    """

    def __init__(self):
        super().__init__(name="Forcecage",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Evocation,
                         spell_range="100 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="ruby dust worth 1,500 gp",
                         duration="1 hour",
                         description="An immobile, invisible, cube-shaped prison\ncomposed of " +
                                    "magical force springs into existence\naround an area you " +
                                    "choose within range. The prison\ncan be a cage or a solid box, " +
                                    "as you choose.\nA prison in the shape of a cage can be up to " +
                                    "20 feet\non a side and is made from 1/2-inch diameter " +
                                    "bars\nspaced 1/2 inch apart.\nA prison in the shape of a box " +
                                    "can be up to 10 feet\non a side, creating a solid barrier that " +
                                    "prevents any\nmatter from passing through it and blocking " +
                                    "any\nspells cast into or out from the area.\nWhen you cast the " +
                                    "spell, any creature that is\ncompletely inside the cage's area " +
                                    "is trapped.\nCreatures only partially within the area, or " +
                                    "those too\nlarge to fit inside the area, are pushed away from " +
                                    "the\ncenter of the area until they are completely outside\nthe " +
                                    "area.\nA creature inside the cage can't leave it " +
                                    "by\nnonmagical means. If the creature tries to " +
                                    "use\nteleportation or interplanar travel to leave the " +
                                    "cage,\nit must first make a Charisma saving throw. On " +
                                    "a\nsuccess, the creature can use that magic to exit the\ncage. " +
                                    "On a failure, the creature can't exit the cage and\nwastes the " +
                                    "use of the spell or effect. The cage also\nextends into the " +
                                    "Ethereal Plane, blocking ethereal\ntravel.\nThis spell can't " +
                                    "be dispelled by dispel magic. ",
                         at_higher_levels="")


class Foresight(spells.Spell):
    """
    Foresight Spell
    SRD p. 148
    Generated
    """

    def __init__(self):
        super().__init__(name="Foresight",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=9,
                         school=SpellSchools.Divination,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a hummingbird feather",
                         duration="8 hours",
                         description="You touch a willing creature and bestow a limited\nability to " +
                                    "see into the immediate future. For the\nduration, the target " +
                                    "can't be surprised and has\nadvantage on attack rolls, ability " +
                                    "checks, and saving\nthrows. Additionally, other creatures " +
                                    "have\ndisadvantage on attack rolls against the target for\nthe " +
                                    "duration.\nThis spell immediately ends if you cast it " +
                                    "again\nbefore its duration ends. ",
                         at_higher_levels="")


class FreedomOfMovement(spells.Spell):
    """
    Freedom of Movement Spell
    SRD p. 148
    Generated
    """

    def __init__(self):
        super().__init__(name="Freedom of Movement",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=4,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a leather strap, bound around the arm or a similar appendage",
                         duration="1 hour",
                         description="You touch a willing creature. For the duration, the\ntarget's " +
                                    "movement is unaffected by difficult terrain,\nand spells and " +
                                    "other magical effects can neither\nreduce the target's speed " +
                                    "nor cause the target to be\nparalyzed or restrained.\nThe " +
                                    "target can also spend 5 feet of movement to\nautomatically " +
                                    "escape from nonmagical restraints,\nsuch as manacles or a " +
                                    "creature that has it grappled.\nFinally, being underwater " +
                                    "imposes no penalties on\nthe target's movement or attacks. ",
                         at_higher_levels="")


class FreezingSphere(spells.Spell):
    """
    Freezing Sphere Spell
    SRD p. 148-149
    Generated
    """

    def __init__(self):
        super().__init__(name="Freezing Sphere",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Evocation,
                         spell_range="300 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small crystal sphere",
                         duration="Instantaneous",
                         description="A frigid globe of cold energy streaks from your\nfingertips to " +
                                    "a point of your choice within range,\nwhere it explodes in a " +
                                    "60-foot-radius sphere. Each\ncreature within the area must " +
                                    "make a Constitution\nsaving throw. On a failed save, a " +
                                    "creature takes 10d6\ncold damage. On a successful save, it " +
                                    "takes half as\nmuch damage.\nIf the globe strikes a body of " +
                                    "water or a liquid that\nis principally water (not including " +
                                    "water-based\ncreatures), it freezes the liquid to a depth of 6 " +
                                    "inches\nover an area 30 feet square. This ice lasts for " +
                                    "1\nminute. Creatures that were swimming on the\nsurface of " +
                                    "frozen water are trapped in the ice. A\ntrapped creature can " +
                                    "use an action to make a\nStrength check against your spell " +
                                    "save DC to break\nfree.\nYou can refrain from firing the globe " +
                                    "after\ncompleting the spell, if you wish. A small globe " +
                                    "about\nthe size of a sling stone, cool to the touch, appears " +
                                    "in\nyour hand. At any time, you or a creature you give\nthe " +
                                    "globe to can throw the globe (to a range of 40\nfeet) or hurl " +
                                    "it with a sling (to the sling's normal\nrange). It shatters on " +
                                    "impact, with the same effect as\nthe normal casting of the " +
                                    "spell. You can also set the\nglobe down without shattering it. " +
                                    "After 1 minute, if\nthe globe hasn't already shattered, it " +
                                    "explodes. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, the damage increases\nby 1d6 for each slot level above " +
                                          "6th. ")


class GaseousForm(spells.Spell):
    """
    Gaseous Form Spell
    SRD p. 149
    Generated
    """

    def __init__(self):
        super().__init__(name="Gaseous Form",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of gauze and a wisp of smoke",
                         duration="1 hour",
                         description="You transform a willing creature you touch, along\nwith " +
                                    "everything it's wearing and carrying, into a\nmisty cloud for " +
                                    "the duration. The spell ends if the\ncreature drops to 0 hit " +
                                    "points. An incorporeal\ncreature isn't affected.\nWhile in " +
                                    "this form, the target's only method of\nmovement is a flying " +
                                    "speed of 10 feet. The target can\nenter and occupy the space " +
                                    "of another creature. The\ntarget has resistance to nonmagical " +
                                    "damage, and it\nhas advantage on Strength, Dexterity, " +
                                    "and\nConstitution saving throws. The target can pass\nthrough " +
                                    "small holes, narrow openings, and even\nmere cracks, though it " +
                                    "treats liquids as though they\nwere solid surfaces. The target " +
                                    "can't fall and remains\nhovering in the air even when stunned " +
                                    "or otherwise\nincapacitated.\nWhile in the form of a misty " +
                                    "cloud, the target can't\ntalk or manipulate objects, and any " +
                                    "objects it was\ncarrying or holding can't be dropped, used, " +
                                    "or\notherwise interacted with. The target can't attack " +
                                    "or\ncast spells. ",
                         at_higher_levels="")


class Gate(spells.Spell):
    """
    Gate Spell
    SRD p. 149
    Generated
    """

    def __init__(self):
        super().__init__(name="Gate",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=9,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a diamond worth at least 5,000 gp",
                         duration="1 minute",
                         description="You conjure a portal linking an unoccupied space\nyou can see " +
                                    "within range to a precise location on a\ndifferent plane of " +
                                    "existence. The portal is a circular\nopening, which you can " +
                                    "make 5 to 20 feet in\ndiameter. You can orient the portal in " +
                                    "any direction\nyou choose. The portal lasts for the " +
                                    "duration.\nThe portal has a front and a back on each " +
                                    "plane\nwhere it appears. Travel through the portal " +
                                    "is\npossible only by moving through its front. Anything\nthat " +
                                    "does so is instantly transported to the other\nplane, " +
                                    "appearing in the unoccupied space nearest to\nthe " +
                                    "portal.\nDeities and other planar rulers can prevent " +
                                    "portals\ncreated by this spell from opening in their " +
                                    "presence\nor anywhere within their domains.\nWhen you cast " +
                                    "this spell, you can speak the name\nof a specific creature (a " +
                                    "pseudonym, title, or\nnickname doesn't work). If that creature " +
                                    "is on a\nplane other than the one you are on, the portal " +
                                    "opens\nin the named creature's immediate vicinity and\ndraws " +
                                    "the creature through it to the nearest\nunoccupied space on " +
                                    "your side of the portal. You gain\nno special power over the " +
                                    "creature, and it is free to\nact as the GM deems appropriate. " +
                                    "It might leave,\nattack you, or help you. ",
                         at_higher_levels="")


class Geas(spells.Spell):
    """
    Geas Spell
    SRD p. 149
    Generated
    """

    def __init__(self):
        super().__init__(name="Geas",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="30 days",
                         description="You place a magical command on a creature that you\ncan see " +
                                    "within range, forcing it to carry out some\nservice or refrain " +
                                    "from some action or course of\nactivity as you decide. If the " +
                                    "creature can understand\nyou, it must succeed on a Wisdom " +
                                    "saving throw or\nbecome charmed by you for the duration. While " +
                                    "the\ncreature is charmed by you, it takes 5d10 psychic\ndamage " +
                                    "each time it acts in a manner directly\ncounter to your " +
                                    "instructions, but no more than once\neach day. A creature that " +
                                    "can't understand you is\nunaffected by the spell.\nYou can " +
                                    "issue any command you choose, short of\nan activity that would " +
                                    "result in certain death. Should\nyou issue a suicidal command, " +
                                    "the spell ends.\nYou can end the spell early by using an " +
                                    "action to\ndismiss it. A remove curse, greater restoration, " +
                                    "or\nwish spell also ends it. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th or 8th " +
                                          "level, the duration is 1 year.\nWhen you cast this spell using " +
                                          "a spell slot of 9th level,\nthe spell lasts until it is ended " +
                                          "by one of the spells\nmentioned above. ")


class GentleRepose(spells.Spell):
    """
    Gentle Repose Spell
    SRD p. 149-150
    Generated
    """

    def __init__(self):
        super().__init__(name="Gentle Repose",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         ritual=True,
                         level=2,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of salt and one copper piece placed on each of the corpse's eyes, which must remain there for the duration",
                         duration="10 days",
                         description="You touch a corpse or other remains. For the\nduration, the " +
                                    "target is protected from decay and\ncan't become undead.\nThe " +
                                    "spell also effectively extends the time limit on\nraising the " +
                                    "target from the dead, since days spent\nunder the influence of " +
                                    "this spell don't count against\nthe time limit of spells such " +
                                    "as raise dead. ",
                         at_higher_levels="")


class GiantInsect(spells.Spell):
    """
    Giant Insect Spell
    SRD p. 150
    Generated
    """

    def __init__(self):
        super().__init__(name="Giant Insect",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You transform up to ten centipedes, three spiders,\nfive " +
                                    "wasps, or one scorpion within range into giant\nversions of " +
                                    "their natural forms for the duration. A\ncentipede becomes a " +
                                    "giant centipede, a spider\nbecomes a giant spider, a wasp " +
                                    "becomes a giant\nwasp, and a scorpion becomes a giant " +
                                    "scorpion.\nEach creature obeys your verbal commands, and\nin " +
                                    "combat, they act on your turn each round. The GM\nhas the " +
                                    "statistics for these creatures and resolves\ntheir actions and " +
                                    "movement.\nA creature remains in its giant size for " +
                                    "the\nduration, until it drops to 0 hit points, or until " +
                                    "you\nuse an action to dismiss the effect on it.\nThe GM might " +
                                    "allow you to choose different\ntargets. For example, if you " +
                                    "transform a bee, its giant\nversion might have the same " +
                                    "statistics as a giant\nwasp. ",
                         at_higher_levels="")


class Glibness(spells.Spell):
    """
    Glibness Spell
    SRD p. 150
    Generated
    """

    def __init__(self):
        super().__init__(name="Glibness",
                         spell_lists=[SpellLists.ARCANE],
                         level=8,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 hour",
                         description="Until the spell ends, when you make a Charisma\ncheck, you can " +
                                    "replace the number you roll with a 15.\nAdditionally, no " +
                                    "matter what you say, magic that\nwould determine if you are " +
                                    "telling the truth indicates\nthat you are being truthful. ",
                         at_higher_levels="")


class GlobeOfInvulnerability(spells.Spell):
    """
    Globe of Invulnerability Spell
    SRD p. 150
    Generated
    """

    def __init__(self):
        super().__init__(name="Globe of Invulnerability",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Abjuration,
                         spell_range="Self (10-foot radius)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a glass or crystal bead that shatters when the spell ends",
                         duration="1 minute",
                         description="An immobile, faintly shimmering barrier springs " +
                                    "into\nexistence in a 10-foot radius around you and\nremains " +
                                    "for the duration.\nAny spell of 5th level or lower cast from " +
                                    "outside\nthe barrier can't affect creatures or objects within " +
                                    "it,\neven if the spell is cast using a higher level spell " +
                                    "slot.\nSuch a spell can target creatures and objects " +
                                    "within\nthe barrier, but the spell has no effect on " +
                                    "them.\nSimilarly, the area within the barrier is " +
                                    "excluded\nfrom the areas affected by such spells. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, the barrier blocks\nspells of one level higher for " +
                                          "each slot level above\n6th. ")


class GlyphOfWarding(spells.Spell):
    """
    Glyph of Warding Spell
    SRD p. 150-151
    Generated
    """

    def __init__(self):
        super().__init__(name="Glyph of Warding",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="incense and powdered diamond worth at least 200 gp, which the spell consumes",
                         duration="Until dispelled or triggered",
                         description="When you cast this spell, you inscribe a glyph that\nharms " +
                                    "other creatures, either upon a surface (such\nas a table or a " +
                                    "section of floor or wall) or within an\nobject that can be " +
                                    "closed (such as a book, a scroll, or\na treasure chest) to " +
                                    "conceal the glyph. If you choose\na surface, the glyph can " +
                                    "cover an area of the surface\nno larger than 10 feet in " +
                                    "diameter. If you choose an\nobject, that object must remain in " +
                                    "its place; if the\nobject is moved more than 10 feet from " +
                                    "where you\ncast this spell, the glyph is broken, and the spell " +
                                    "ends\nwithout being triggered.\nThe glyph is nearly invisible " +
                                    "and requires a\nsuccessful Intelligence (Investigation) check " +
                                    "against\nyour spell save DC to be found.\nYou decide what " +
                                    "triggers the glyph when you cast\nthe spell. For glyphs " +
                                    "inscribed on a surface, the most\ntypical triggers include " +
                                    "touching or standing on the\nglyph, removing another object " +
                                    "covering the glyph,\napproaching within a certain distance of " +
                                    "the glyph,\nor manipulating the object on which the glyph " +
                                    "is\ninscribed. For glyphs inscribed within an object, " +
                                    "the\nmost common triggers include opening that " +
                                    "object,\napproaching within a certain distance of the " +
                                    "object,\nor seeing or reading the glyph. Once a glyph " +
                                    "is\ntriggered, this spell ends.\nYou can further refine the " +
                                    "trigger so the spell\nactivates only under certain " +
                                    "circumstances or\naccording to physical characteristics (such " +
                                    "as height\nor weight), creature kind (for example, the " +
                                    "ward\ncould be set to affect aberrations or drow), " +
                                    "or\nalignment. You can also set conditions for creatures\nthat " +
                                    "don't trigger the glyph, such as those who say a\ncertain " +
                                    "password.\nWhen you inscribe the glyph, choose " +
                                    "explosive\nrunes or a spell glyph.\nExplosive Runes. When " +
                                    "triggered, the glyph\nerupts with magical energy in a " +
                                    "20-foot-radius\nsphere centered on the glyph. The sphere " +
                                    "spreads\naround corners. Each creature in the area must\nmake " +
                                    "a Dexterity saving throw. A creature takes 5d8\nacid, cold, " +
                                    "fire, lightning, or thunder damage on a\nfailed saving throw " +
                                    "(your choice when you create\nthe glyph), or half as much " +
                                    "damage on a successful\none.\nSpell Glyph. You can store a " +
                                    "prepared spell of 3rd\nlevel or lower in the glyph by casting " +
                                    "it as part of\ncreating the glyph. The spell must target a " +
                                    "single\ncreature or an area. The spell being stored has " +
                                    "no\nimmediate effect when cast in this way. When the\nglyph is " +
                                    "triggered, the stored spell is cast. If the spell\nhas a " +
                                    "target, it targets the creature that triggered the\nglyph. If " +
                                    "the spell affects an area, the area is centered\non that " +
                                    "creature. If the spell summons hostile\ncreatures or creates " +
                                    "harmful objects or traps, they\nappear as close as possible to " +
                                    "the intruder and attack\nit. If the spell requires " +
                                    "concentration, it lasts until the\nend of its full duration. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the damage of an\nexplosive runes glyph increases by " +
                                          "1d8 for each slot\nlevel above 3rd. If you create a spell " +
                                          "glyph, you can\nstore any spell of up to the same level as the " +
                                          "slot you\nuse for the glyph of warding. ")


class Goodberry(spells.Spell):
    """
    Goodberry Spell
    SRD p. 151
    Generated
    """

    def __init__(self):
        super().__init__(name="Goodberry",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a sprig of mistletoe",
                         duration="Instantaneous",
                         description="Up to ten berries appear in your hand and are\ninfused with " +
                                    "magic for the duration. A creature can\nuse its action to eat " +
                                    "one berry. Eating a berry\nrestores 1 hit point, and the berry " +
                                    "provides enough\nnourishment to sustain a creature for one " +
                                    "day.\nThe berries lose their potency if they have not\nbeen " +
                                    "consumed within 24 hours of the casting of this\nspell. ",
                         at_higher_levels="")


class Grease(spells.Spell):
    """
    Grease Spell
    SRD p. 151
    Generated
    """

    def __init__(self):
        super().__init__(name="Grease",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of pork rind or butter",
                         duration="1 minute",
                         description="Slick grease covers the ground in a 10-foot square\ncentered " +
                                    "on a point within range and turns it into\ndifficult terrain " +
                                    "for the duration.\nWhen the grease appears, each creature " +
                                    "standing\nin its area must succeed on a Dexterity saving " +
                                    "throw\nor fall prone. A creature that enters the area or " +
                                    "ends\nits turn there must also succeed on a Dexterity\nsaving " +
                                    "throw or fall prone. ",
                         at_higher_levels="")


class GreaterInvisibility(spells.Spell):
    """
    Greater Invisibility Spell
    SRD p. 151
    Generated
    """

    def __init__(self):
        super().__init__(name="Greater Invisibility",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Illusion,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You or a creature you touch becomes invisible until\nthe spell " +
                                    "ends. Anything the target is wearing or\ncarrying is invisible " +
                                    "as long as it is on the target's\nperson. ",
                         at_higher_levels="")


class GreaterRestoration(spells.Spell):
    """
    Greater Restoration Spell
    SRD p. 151
    Generated
    """

    def __init__(self):
        super().__init__(name="Greater Restoration",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=5,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="diamond dust worth at least 100 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="You imbue a creature you touch with positive energy\nto undo a " +
                                    "debilitating effect. You can reduce the\ntarget's exhaustion " +
                                    "level by one, or end one of the\nfollowing effects on the " +
                                    "target:\n• One effect that charmed or petrified the target\n• " +
                                    "One curse, including the target's attunement to a\ncursed " +
                                    "magic item\n• Any reduction to one of the target's ability " +
                                    "scores\n• One effect reducing the target's hit point\nmaximum ",
                         at_higher_levels="")


class GuardianOfFaith(spells.Spell):
    """
    Guardian of Faith Spell
    SRD p. 151-152
    Generated
    """

    def __init__(self):
        super().__init__(name="Guardian of Faith",
                         spell_lists=[SpellLists.DIVINE],
                         level=4,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="8 hours",
                         description="A Large spectral guardian appears and hovers for\nthe duration " +
                                    "in an unoccupied space of your choice\nthat you can see within " +
                                    "range. The guardian occupies\nthat space and is indistinct " +
                                    "except for a gleaming\nsword and shield emblazoned with the " +
                                    "symbol of\nyour deity.\nAny creature hostile to you that moves " +
                                    "to a space\nwithin 10 feet of the guardian for the first time " +
                                    "on a\nturn must succeed on a Dexterity saving throw. " +
                                    "The\ncreature takes 20 radiant damage on a failed save, " +
                                    "or\nhalf as much damage on a successful one. The\nguardian " +
                                    "vanishes when it has dealt a total of 60\ndamage. ",
                         at_higher_levels="")


class GuardsAndWards(spells.Spell):
    """
    Guards and Wards Spell
    SRD p. 152
    Generated
    """

    def __init__(self):
        super().__init__(name="Guards and Wards",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="burning incense, a small measure of brimstone and oil, a knotted string, a small amount of umber hulk blood, and a small silver rod worth at least 10 gp",
                         duration="24 hours",
                         description="You create a ward that protects up to 2,500 square\nfeet of " +
                                    "floor space (an area 50 feet square, or one\nhundred 5-foot " +
                                    "squares or twenty-five 10-foot\nsquares). The warded area can " +
                                    "be up to 20 feet tall,\nand shaped as you desire. You can ward " +
                                    "several\nstories of a stronghold by dividing the area " +
                                    "among\nthem, as long as you can walk into each " +
                                    "contiguous\narea while you are casting the spell.\nWhen you " +
                                    "cast this spell, you can specify\nindividuals that are " +
                                    "unaffected by any or all of the\neffects that you choose. You " +
                                    "can also specify a\npassword that, when spoken aloud, makes " +
                                    "the\nspeaker immune to these effects.\nGuards and wards " +
                                    "creates the following effects\nwithin the warded " +
                                    "area.\nCorridors. Fog fills all the warded corridors,\nmaking " +
                                    "them heavily obscured. In addition, at each\nintersection or " +
                                    "branching passage offering a choice\nof direction, there is a " +
                                    "50 percent chance that a\ncreature other than you will believe " +
                                    "it is going in the\nopposite direction from the one it " +
                                    "chooses.\nDoors. All doors in the warded area are " +
                                    "magically\nlocked, as if sealed by an arcane lock spell. " +
                                    "In\naddition, you can cover up to ten doors with an\nillusion " +
                                    "(equivalent to the illusory object function of\nthe minor " +
                                    "illusion spell) to make them appear as\nplain sections of " +
                                    "wall.\nStairs. Webs fill all stairs in the warded area " +
                                    "from\ntop to bottom, as the web spell. These strands\nregrow " +
                                    "in 10 minutes if they are burned or torn\naway while guards " +
                                    "and wards lasts.\nOther Spell Effect. You can place your " +
                                    "choice of\none of the following magical effects within " +
                                    "the\nwarded area of the stronghold.\n• Place dancing lights in " +
                                    "four corridors. You can\ndesignate a simple program that the " +
                                    "lights repeat\nas long as guards and wards lasts.\n• Place " +
                                    "magic mouth in two locations.\n• Place stinking cloud in two " +
                                    "locations. The vapors\nappear in the places you designate; " +
                                    "they return\nwithin 10 minutes if dispersed by wind " +
                                    "while\nguards and wards lasts.\n• Place a constant gust of " +
                                    "wind in one corridor or\nroom.\n• Place a suggestion in one " +
                                    "location. You select an\narea of up to 5 feet square, and any " +
                                    "creature that\nenters or passes through the area receives " +
                                    "the\nsuggestion mentally.\nThe whole warded area radiates " +
                                    "magic. A dispel\nmagic cast on a specific effect, if " +
                                    "successful, removes\nonly that effect.\nYou can create a " +
                                    "permanently guarded and\nwarded structure by casting this " +
                                    "spell there every\nday for one year. ",
                         at_higher_levels="")


class Guidance(spells.Spell):
    """
    Guidance Spell
    SRD p. 152
    Generated
    """

    def __init__(self):
        super().__init__(name="Guidance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         level=0,
                         school=SpellSchools.Divination,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You touch one willing creature. Once before the spell\nends, " +
                                    "the target can roll a d4 and add the number\nrolled to one " +
                                    "ability check of its choice. It can roll the\ndie before or " +
                                    "after making the ability check. The\nspell then ends. ",
                         at_higher_levels="")


class GuidingBolt(spells.Spell):
    """
    Guiding Bolt Spell
    SRD p. 152-153
    Generated
    """

    def __init__(self):
        super().__init__(name="Guiding Bolt",
                         spell_lists=[SpellLists.DIVINE],
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 round",
                         description="A flash of light streaks toward a creature of your\nchoice " +
                                    "within range. Make a ranged spell attack\nagainst the target. " +
                                    "On a hit, the target takes 4d6\nradiant damage, and the next " +
                                    "attack roll made\nagainst this target before the end of your " +
                                    "next turn\nhas advantage, thanks to the mystical dim " +
                                    "light\nglittering on the target until then. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the damage\nincreases by 1d6 for each slot level above " +
                                          "1st. ")


class GustOfWind(spells.Spell):
    """
    Gust of Wind Spell
    SRD p. 153
    Generated
    """

    def __init__(self):
        super().__init__(name="Gust of Wind",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="Self (60-foot line)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a legume seed",
                         duration="1 minute",
                         description="A line of strong wind 60 feet long and 10 feet wide\nblasts " +
                                    "from you in a direction you choose for the\nspell's duration. " +
                                    "Each creature that starts its turn in\nthe line must succeed " +
                                    "on a Strength saving throw or\nbe pushed 15 feet away from you " +
                                    "in a direction\nfollowing the line.\nAny creature in the line " +
                                    "must spend 2 feet of\nmovement for every 1 foot it moves when " +
                                    "moving\ncloser to you.\nThe gust disperses gas or vapor, and " +
                                    "it\nextinguishes candles, torches, and similar\nunprotected " +
                                    "flames in the area. It causes protected\nflames, such as those " +
                                    "of lanterns, to dance wildly and\nhas a 50 percent chance to " +
                                    "extinguish them.\nAs a bonus action on each of your turns " +
                                    "before the\nspell ends, you can change the direction in which " +
                                    "the\nline blasts from you. ",
                         at_higher_levels="")


class Hallow(spells.Spell):
    """
    Hallow Spell
    SRD p. 153
    Generated
    """

    def __init__(self):
        super().__init__(name="Hallow",
                         spell_lists=[SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.Evocation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="herbs, oils, and incense worth at least 1,000 gp, which the spell consumes",
                         duration="Until dispelled",
                         description="You touch a point and infuse an area around it with\nholy (or " +
                                    "unholy) power. The area can have a radius\nup to 60 feet, and " +
                                    "the spell fails if the radius includes\nan area already under " +
                                    "the effect a hallow spell. The\naffected area is subject to " +
                                    "the following effects.\nFirst, celestials, elementals, fey, " +
                                    "fiends, and undead\ncan't enter the area, nor can such " +
                                    "creatures charm,\nfrighten, or possess creatures within it. " +
                                    "Any creature\ncharmed, frightened, or possessed by such " +
                                    "a\ncreature is no longer charmed, frightened, or\npossessed " +
                                    "upon entering the area. You can exclude\none or more of those " +
                                    "types of creatures from this\neffect.\nSecond, you can bind an " +
                                    "extra effect to the area.\nChoose the effect from the " +
                                    "following list, or choose\nan effect offered by the GM. Some " +
                                    "of these effects\napply to creatures in the area; you can " +
                                    "designate\nwhether the effect applies to all creatures, " +
                                    "creatures\nthat follow a specific deity or leader, or " +
                                    "creatures of\na specific sort, such as orcs or trolls. When a " +
                                    "creature\nthat would be affected enters the spell's area for " +
                                    "the\nfirst time on a turn or starts its turn there, it " +
                                    "can\nmake a Charisma saving throw. On a success, the\ncreature " +
                                    "ignores the extra effect until it leaves the\narea.\nCourage. " +
                                    "Affected creatures can't be frightened\nwhile in the " +
                                    "area.\nDarkness. Darkness fills the area. Normal light, " +
                                    "as\nwell as magical light created by spells of a lower\nlevel " +
                                    "than the slot you used to cast this spell, can't\nilluminate " +
                                    "the area.\nDaylight. Bright light fills the area. " +
                                    "Magical\ndarkness created by spells of a lower level than " +
                                    "the\nslot you used to cast this spell can't extinguish " +
                                    "the\nlight.\nEnergy Protection. Affected creatures in the " +
                                    "area\nhave resistance to one damage type of your " +
                                    "choice,\nexcept for bludgeoning, piercing, or " +
                                    "slashing.\nEnergy Vulnerability. Affected creatures in " +
                                    "the\narea have vulnerability to one damage type of " +
                                    "your\nchoice, except for bludgeoning, piercing, or " +
                                    "slashing.\nEverlasting Rest. Dead bodies interred in the " +
                                    "area\ncan't be turned into undead.\nExtradimensional " +
                                    "Interference. Affected\ncreatures can't move or travel using " +
                                    "teleportation or\nby extradimensional or interplanar " +
                                    "means.\nFear. Affected creatures are frightened while in\nthe " +
                                    "area.\nSilence. No sound can emanate from within the\narea, " +
                                    "and no sound can reach into it.\nTongues. Affected creatures " +
                                    "can communicate\nwith any other creature in the area, even if " +
                                    "they\ndon't share a common language. ",
                         at_higher_levels="")


class HallucinatoryTerrain(spells.Spell):
    """
    Hallucinatory Terrain Spell
    SRD p. 153-154
    Generated
    """

    def __init__(self):
        super().__init__(name="Hallucinatory Terrain",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Illusion,
                         spell_range="300 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a stone, a twig, and a bit of green plant",
                         duration="24 hours",
                         description="You make natural terrain in a 150-foot cube in range\nlook, " +
                                    "sound, and smell like some other sort of natural\nterrain. " +
                                    "Thus, open fields or a road can be made to\nresemble a swamp, " +
                                    "hill, crevasse, or some other\ndifficult or impassable " +
                                    "terrain. A pond can be made\nto seem like a grassy meadow, a " +
                                    "precipice like a\ngentle slope, or a rock-strewn gully like a " +
                                    "wide and\nsmooth road. Manufactured structures, " +
                                    "equipment,\nand creatures within the area aren't changed " +
                                    "in\nappearance.\nThe tactile characteristics of the terrain " +
                                    "are\nunchanged, so creatures entering the area are likely\nto " +
                                    "see through the illusion. If the difference isn't\nobvious by " +
                                    "touch, a creature carefully examining the\nillusion can " +
                                    "attempt an Intelligence (Investigation)\ncheck against your " +
                                    "spell save DC to disbelieve it. A\ncreature who discerns the " +
                                    "illusion for what it is, sees\nit as a vague image " +
                                    "superimposed on the terrain. ",
                         at_higher_levels="")


class Harm(spells.Spell):
    """
    Harm Spell
    SRD p. 154
    Generated
    """

    def __init__(self):
        super().__init__(name="Harm",
                         spell_lists=[SpellLists.DIVINE],
                         level=6,
                         school=SpellSchools.Necromancy,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You unleash a virulent disease on a creature that you\ncan see " +
                                    "within range. The target must make a\nConstitution saving " +
                                    "throw. On a failed save, it takes\n14d6 necrotic damage, or " +
                                    "half as much damage on a\nsuccessful save. The damage can't " +
                                    "reduce the target's\nhit points below 1. If the target fails " +
                                    "the saving throw,\nits hit point maximum is reduced for 1 hour " +
                                    "by an\namount equal to the necrotic damage it took. " +
                                    "Any\neffect that removes a disease allows a creature's " +
                                    "hit\npoint maximum to return to normal before that " +
                                    "time\npasses. ",
                         at_higher_levels="")


class Haste(spells.Spell):
    """
    Haste Spell
    SRD p. 154
    Generated
    """

    def __init__(self):
        super().__init__(name="Haste",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a shaving of licorice root",
                         duration="1 minute",
                         description="Choose a willing creature that you can see within\nrange. " +
                                    "Until the spell ends, the target's speed is\ndoubled, it gains " +
                                    "a +2 bonus to AC, it has advantage\non Dexterity saving " +
                                    "throws, and it gains an\nadditional action on each of its " +
                                    "turns. That action can\nbe used only to take the Attack (one " +
                                    "weapon attack\nonly), Dash, Disengage, Hide, or Use an Object " +
                                    "action.\nWhen the spell ends, the target can't move or " +
                                    "take\nactions until after its next turn, as a wave of " +
                                    "lethargy\nsweeps over it. ",
                         at_higher_levels="")


class Heal(spells.Spell):
    """
    Heal Spell
    SRD p. 154
    Generated
    """

    def __init__(self):
        super().__init__(name="Heal",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Choose a creature that you can see within range. A\nsurge of " +
                                    "positive energy washes through the\ncreature, causing it to " +
                                    "regain 70 hit points. This spell\nalso ends blindness, " +
                                    "deafness, and any diseases\naffecting the target. This spell " +
                                    "has no effect on\nconstructs or undead. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, the amount of\nhealing increases by 10 for each slot " +
                                          "level above 6th. ")


class HealingWord(spells.Spell):
    """
    Healing Word Spell
    SRD p. 154
    Generated
    """

    def __init__(self):
        super().__init__(name="Healing Word",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="A creature of your choice that you can see within\nrange " +
                                    "regains hit points equal to 1d4 + your\nspellcasting ability " +
                                    "modifier. This spell has no effect\non undead or constructs. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the healing increases\nby 1d4 for each slot level " +
                                          "above 1st. ")


class HeatMetal(spells.Spell):
    """
    Heat Metal Spell
    SRD p. 154-155
    Generated
    """

    def __init__(self):
        super().__init__(name="Heat Metal",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of iron and a flame",
                         duration="1 minute",
                         description="Choose a manufactured metal object, such as a metal\nweapon or " +
                                    "a suit of heavy or medium metal armor,\nthat you can see " +
                                    "within range. You cause the object\nto glow red-hot. Any " +
                                    "creature in physical contact\nwith the object takes 2d8 fire " +
                                    "damage when you cast\nthe spell. Until the spell ends, you can " +
                                    "use a bonus\naction on each of your subsequent turns to " +
                                    "cause\nthis damage again.\nIf a creature is holding or wearing " +
                                    "the object and\ntakes the damage from it, the creature must " +
                                    "succeed\non a Constitution saving throw or drop the object " +
                                    "if\nit can. If it doesn't drop the object, it " +
                                    "has\ndisadvantage on attack rolls and ability checks " +
                                    "until\nthe start of your next turn. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the damage\nincreases by 1d8 for each slot level above " +
                                          "2nd. ")


class HellishRebuke(spells.Spell):
    """
    Hellish Rebuke Spell
    SRD p. 155
    Generated
    """

    def __init__(self):
        super().__init__(name="Hellish Rebuke",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You point your finger, and the creature that\ndamaged you is " +
                                    "momentarily surrounded by hellish\nflames. The creature must " +
                                    "make a Dexterity saving\nthrow. It takes 2d10 fire damage on a " +
                                    "failed save, or\nhalf as much damage on a successful one. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the damage\nincreases by 1d10 for each slot level " +
                                          "above 1st. ")


class HeroesFeast(spells.Spell):
    """
    Heroes' Feast Spell
    SRD p. 155
    Generated
    """

    def __init__(self):
        super().__init__(name="Heroes' Feast",
                         spell_lists=[SpellLists.DIVINE],
                         level=6,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a gem-encrusted bowl worth at least 1,000 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="You bring forth a great feast, including magnificent\nfood and " +
                                    "drink. The feast takes 1 hour to consume\nand disappears at " +
                                    "the end of that time, and the\nbeneficial effects don't set in " +
                                    "until this hour is over.\nUp to twelve other creatures can " +
                                    "partake of the feast.\nA creature that partakes of the feast " +
                                    "gains several\nbenefits. The creature is cured of all diseases " +
                                    "and\npoison, becomes immune to poison and being\nfrightened, " +
                                    "and makes all Wisdom saving throws\nwith advantage. Its hit " +
                                    "point maximum also\nincreases by 2d10, and it gains the same " +
                                    "number of\nhit points. These benefits last for 24 hours. ",
                         at_higher_levels="")


class Heroism(spells.Spell):
    """
    Heroism Spell
    SRD p. 155
    Generated
    """

    def __init__(self):
        super().__init__(name="Heroism",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="A willing creature you touch is imbued with bravery.\nUntil " +
                                    "the spell ends, the creature is immune to being\nfrightened " +
                                    "and gains temporary hit points equal to\nyour spellcasting " +
                                    "ability modifier at the start of each\nof its turns. When the " +
                                    "spell ends, the target loses any\nremaining temporary hit " +
                                    "points from this spell. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 1st. ")


class HideousLaughter(spells.Spell):
    """
    Hideous Laughter Spell
    SRD p. 155
    Generated
    """

    def __init__(self):
        super().__init__(name="Hideous Laughter",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="tiny tarts and a feather that is waved in the air",
                         duration="1 minute",
                         description="A creature of your choice that you can see within\nrange " +
                                    "perceives everything as hilariously funny and\nfalls into fits " +
                                    "of laughter if this spell affects it. The\ntarget must succeed " +
                                    "on a Wisdom saving throw or\nfall prone, becoming " +
                                    "incapacitated and unable to\nstand up for the duration. A " +
                                    "creature with an\nIntelligence score of 4 or less isn't " +
                                    "affected.\nAt the end of each of its turns, and each time " +
                                    "it\ntakes damage, the target can make another Wisdom\nsaving " +
                                    "throw. The target has advantage on the\nsaving throw if it's " +
                                    "triggered by damage. On a\nsuccess, the spell ends. ",
                         at_higher_levels="")


class HoldMonster(spells.Spell):
    """
    Hold Monster Spell
    SRD p. 155
    Generated
    """

    def __init__(self):
        super().__init__(name="Hold Monster",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Enchantment,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small, straight piece of iron",
                         duration="1 minute",
                         description="Choose a creature that you can see within range. The\ntarget " +
                                    "must succeed on a Wisdom saving throw or be\nparalyzed for the " +
                                    "duration. This spell has no effect\non undead. At the end of " +
                                    "each of its turns, the target\ncan make another Wisdom saving " +
                                    "throw. On a\nsuccess, the spell ends on the target. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 5th. The\ncreatures must be within 30 feet of each " +
                                          "other when\nyou target them. ")


class HoldPerson(spells.Spell):
    """
    Hold Person Spell
    SRD p. 155-156
    Generated
    """

    def __init__(self):
        super().__init__(name="Hold Person",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small, straight piece of iron",
                         duration="1 minute",
                         description="Choose a humanoid that you can see within range.\nThe target " +
                                    "must succeed on a Wisdom saving throw\nor be paralyzed for the " +
                                    "duration. At the end of each\nof its turns, the target can " +
                                    "make another Wisdom\nsaving throw. On a success, the spell " +
                                    "ends on the\ntarget. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, you can target one\nadditional humanoid for each slot " +
                                          "level above 2nd.\nThe humanoids must be within 30 feet of each " +
                                          "other\nwhen you target them. ")


class HolyAura(spells.Spell):
    """
    Holy Aura Spell
    SRD p. 156
    Generated
    """

    def __init__(self):
        super().__init__(name="Holy Aura",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Abjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny reliquary worth at least 1,000 gp containing a sacred relic, such as a scrap of cloth from a saint's robe or a piece of parchment from a religious text",
                         duration="1 minute",
                         description="Divine light washes out from you and coalesces in a\nsoft " +
                                    "radiance in a 30-foot radius around you.\nCreatures of your " +
                                    "choice in that radius when you\ncast this spell shed dim light " +
                                    "in a 5-foot radius and\nhave advantage on all saving throws, " +
                                    "and other\ncreatures have disadvantage on attack rolls " +
                                    "against\nthem until the spell ends. In addition, when a " +
                                    "fiend\nor an undead hits an affected creature with a " +
                                    "melee\nattack, the aura flashes with brilliant light. " +
                                    "The\nattacker must succeed on a Constitution saving\nthrow or " +
                                    "be blinded until the spell ends. ",
                         at_higher_levels="")


class HuntersMark(spells.Spell):
    """
    Hunter's Mark Spell
    SRD p. 156
    Generated
    """

    def __init__(self):
        super().__init__(name="Hunter's Mark",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Divination,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 hour",
                         description="You choose a creature you can see within range and\nmystically " +
                                    "mark it as your quarry. Until the spell\nends, you deal an " +
                                    "extra 1d6 damage to the target\nwhenever you hit it with a " +
                                    "weapon attack, and you\nhave advantage on any Wisdom " +
                                    "(Perception) or\nWisdom (Survival) check you make to find it. " +
                                    "If the\ntarget drops to 0 hit points before this spell " +
                                    "ends,\nyou can use a bonus action on a subsequent turn " +
                                    "of\nyours to mark a new creature. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd or 4th " +
                                          "level, you can maintain your\nconcentration on the spell for " +
                                          "up to 8 hours. When\nyou use a spell slot of 5th level or " +
                                          "higher, you can\nmaintain your concentration on the spell for " +
                                          "up to 24\nhours. ")


class HypnoticPattern(spells.Spell):
    """
    Hypnotic Pattern Spell
    SRD p. 156
    Generated
    """

    def __init__(self):
        super().__init__(name="Hypnotic Pattern",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Illusion,
                         spell_range="120 feet",
                         verbal_components=False,
                         somatic_components=True,
                         material_components_list="a glowing stick of incense or a crystal vial filled with phosphorescent material",
                         duration="1 minute",
                         description="You create a twisting pattern of colors that weaves\nthrough " +
                                    "the air inside a 30-foot cube within range.\nThe pattern " +
                                    "appears for a moment and vanishes.\nEach creature in the area " +
                                    "who sees the pattern must\nmake a Wisdom saving throw. On a " +
                                    "failed save, the\ncreature becomes charmed for the duration. " +
                                    "While\ncharmed by this spell, the creature is " +
                                    "incapacitated\nand has a speed of 0.\nThe spell ends for an " +
                                    "affected creature if it takes\nany damage or if someone else " +
                                    "uses an action to\nshake the creature out of its stupor. ",
                         at_higher_levels="")


class IceStorm(spells.Spell):
    """
    Ice Storm Spell
    SRD p. 156
    Generated
    """

    def __init__(self):
        super().__init__(name="Ice Storm",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=4,
                         school=SpellSchools.Evocation,
                         spell_range="300 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of dust and a few drops of water",
                         duration="Instantaneous",
                         description="A hail of rock-hard ice pounds to the ground in a " +
                                    "20-\nfoot-radius, 40-foot-high cylinder centered on a\npoint " +
                                    "within range. Each creature in the cylinder\nmust make a " +
                                    "Dexterity saving throw. A creature\ntakes 2d8 bludgeoning " +
                                    "damage and 4d6 cold damage\non a failed save, or half as much " +
                                    "damage on a\nsuccessful one.\nHailstones turn the storm's area " +
                                    "of effect into\ndifficult terrain until the end of your next " +
                                    "turn. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 5th level or " +
                                          "higher, the bludgeoning\ndamage increases by 1d8 for each slot " +
                                          "level above\n4th. ")


class Identify(spells.Spell):
    """
    Identify Spell
    SRD p. 156-157
    Generated
    """

    def __init__(self):
        super().__init__(name="Identify",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Divination,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pearl worth at least 100 gp and an owl feather",
                         duration="Instantaneous",
                         description="You choose one object that you must touch\nthroughout the " +
                                    "casting of the spell. If it is a magic\nitem or some other " +
                                    "magic-imbued object, you learn\nits properties and how to use " +
                                    "them, whether it\nrequires attunement to use, and how many " +
                                    "charges\nit has, if any. You learn whether any spells " +
                                    "are\naffecting the item and what they are. If the item " +
                                    "was\ncreated by a spell, you learn which spell created it.\nIf " +
                                    "you instead touch a creature throughout the\ncasting, you " +
                                    "learn what spells, if any, are currently\naffecting it. ",
                         at_higher_levels="")


class IllusoryScript(spells.Spell):
    """
    Illusory Script Spell
    SRD p. 157
    Generated
    """

    def __init__(self):
        super().__init__(name="Illusory Script",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Illusion,
                         spell_range="Touch",
                         verbal_components=False,
                         somatic_components=True,
                         material_components_list="a lead-based ink worth at least 10 gp, which the spell consumes",
                         duration="10 days",
                         description="You write on parchment, paper, or some other\nsuitable writing " +
                                    "material and imbue it with a potent\nillusion that lasts for " +
                                    "the duration.\nTo you and any creatures you designate when " +
                                    "you\ncast the spell, the writing appears normal, written " +
                                    "in\nyour hand, and conveys whatever meaning you\nintended when " +
                                    "you wrote the text. To all others, the\nwriting appears as if " +
                                    "it were written in an unknown\nor magical script that is " +
                                    "unintelligible. Alternatively,\nyou can cause the writing to " +
                                    "appear to be an entirely\ndifferent message, written in a " +
                                    "different hand and\nlanguage, though the language must be one " +
                                    "you\nknow.\nShould the spell be dispelled, the original " +
                                    "script\nand the illusion both disappear.\nA creature with " +
                                    "truesight can read the hidden\nmessage. ",
                         at_higher_levels="")


class Imprisonment(spells.Spell):
    """
    Imprisonment Spell
    SRD p. 157-158
    Generated
    """

    def __init__(self):
        super().__init__(name="Imprisonment",
                         spell_lists=[SpellLists.ARCANE],
                         level=9,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a vellum depiction or a carved statuette in the likeness of the target, and a special component that varies according to the version of the spell you choose, worth at least 500 gp per Hit Die of the target",
                         duration="Until dispelled",
                         description="You create a magical restraint to hold a creature that\nyou " +
                                    "can see within range. The target must succeed\non a Wisdom " +
                                    "saving throw or be bound by the spell;\nif it succeeds, it is " +
                                    "immune to this spell if you cast it\nagain. While affected by " +
                                    "this spell, the creature\ndoesn't need to breathe, eat, or " +
                                    "drink, and it doesn't\nage. Divination spells can't locate or " +
                                    "perceive the\ntarget.\nWhen you cast the spell, you choose one " +
                                    "of the\nfollowing forms of imprisonment.\nBurial. The target " +
                                    "is entombed far beneath the\nearth in a sphere of magical " +
                                    "force that is just large\nenough to contain the target. " +
                                    "Nothing can pass\nthrough the sphere, nor can any creature " +
                                    "teleport or\nuse planar travel to get into or out of it.\nThe " +
                                    "special component for this version of the spell\nis a small " +
                                    "mithral orb.\nChaining. Heavy chains, firmly rooted in " +
                                    "the\nground, hold the target in place. The target " +
                                    "is\nrestrained until the spell ends, and it can't move or\nbe " +
                                    "moved by any means until then.\nThe special component for this " +
                                    "version of the spell\nis a fine chain of precious " +
                                    "metal.\nHedged Prison. The spell transports the target\ninto a " +
                                    "tiny demiplane that is warded against\nteleportation and " +
                                    "planar travel. The demiplane can\nbe a labyrinth, a cage, a " +
                                    "tower, or any similar\nconfined structure or area of your " +
                                    "choice.\nThe special component for this version of the " +
                                    "spell\nis a miniature representation of the prison made\nfrom " +
                                    "jade.\nMinimus Containment. The target shrinks to a\nheight of " +
                                    "1 inch and is imprisoned inside a gemstone\nor similar object. " +
                                    "Light can pass through the\ngemstone normally (allowing the " +
                                    "target to see out\nand other creatures to see in), but nothing " +
                                    "else can\npass through, even by means of teleportation " +
                                    "or\nplanar travel. The gemstone can't be cut or broken\nwhile " +
                                    "the spell remains in effect.\nThe special component for this " +
                                    "version of the spell\nis a large, transparent gemstone, such " +
                                    "as a corundum,\ndiamond, or ruby.\nSlumber. The target falls " +
                                    "asleep and can't be\nawoken. The special component for this " +
                                    "version of\nthe spell consists of rare soporific " +
                                    "herbs.\nEnding the Spell. During the casting of the spell, " +
                                    "in\nany of its versions, you can specify a condition " +
                                    "that\nwill cause the spell to end and release the target. " +
                                    "The\ncondition can be as specific or as elaborate as " +
                                    "you\nchoose, but the GM must agree that the condition " +
                                    "is\nreasonable and has a likelihood of coming to pass.\nThe " +
                                    "conditions can be based on a creature's name,\nidentity, or " +
                                    "deity but otherwise must be based on\nobservable actions or " +
                                    "qualities and not based on\nintangibles such as level, class, " +
                                    "or hit points.\nA dispel magic spell can end the spell only if " +
                                    "it is\ncast as a 9th-level spell, targeting either the " +
                                    "prison\nor the special component used to create it.\nYou can " +
                                    "use a particular special component to\ncreate only one prison " +
                                    "at a time. If you cast the spell\nagain using the same " +
                                    "component, the target of the\nfirst casting is immediately " +
                                    "freed from its binding. ",
                         at_higher_levels="")


class IncendiaryCloud(spells.Spell):
    """
    Incendiary Cloud Spell
    SRD p. 158
    Generated
    """

    def __init__(self):
        super().__init__(name="Incendiary Cloud",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Conjuration,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="A swirling cloud of smoke shot through with whitehot embers " +
                                    "appears in a 20-foot-radius sphere\ncentered on a point within " +
                                    "range. The cloud spreads\naround corners and is heavily " +
                                    "obscured. It lasts for\nthe duration or until a wind of " +
                                    "moderate or greater\nspeed (at least 10 miles per hour) " +
                                    "disperses it.\nWhen the cloud appears, each creature in it " +
                                    "must\nmake a Dexterity saving throw. A creature takes\n10d8 " +
                                    "fire damage on a failed save, or half as much\ndamage on a " +
                                    "successful one. A creature must also\nmake this saving throw " +
                                    "when it enters the spell's\narea for the first time on a turn " +
                                    "or ends its turn there.\nThe cloud moves 10 feet directly away " +
                                    "from you in\na direction that you choose at the start of each " +
                                    "of\nyour turns. ",
                         at_higher_levels="")


class InflictWounds(spells.Spell):
    """
    Inflict Wounds Spell
    SRD p. 158
    Generated
    """

    def __init__(self):
        super().__init__(name="Inflict Wounds",
                         spell_lists=[SpellLists.DIVINE],
                         level=1,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Make a melee spell attack against a creature you can\nreach. " +
                                    "On a hit, the target takes 3d10 necrotic\ndamage. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the damage\nincreases by 1d10 for each slot level " +
                                          "above 1st. ")


class InsectPlague(spells.Spell):
    """
    Insect Plague Spell
    SRD p. 158
    Generated
    """

    def __init__(self):
        super().__init__(name="Insect Plague",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Conjuration,
                         spell_range="300 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a few grains of sugar, some kernels of grain, and a smear of fat",
                         duration="10 minutes",
                         description="Swarming, biting locusts fill a 20-foot-radius " +
                                    "sphere\ncentered on a point you choose within range. " +
                                    "The\nsphere spreads around corners. The sphere remains\nfor " +
                                    "the duration, and its area is lightly obscured. The\nsphere's " +
                                    "area is difficult terrain.\nWhen the area appears, each " +
                                    "creature in it must\nmake a Constitution saving throw. A " +
                                    "creature takes\n4d10 piercing damage on a failed save, or half " +
                                    "as\nmuch damage on a successful one. A creature must\nalso " +
                                    "make this saving throw when it enters the\nspell's area for " +
                                    "the first time on a turn or ends its\nturn there. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the damage increases\nby 1d10 for each slot level " +
                                          "above 5th. ")


class InstantSummons(spells.Spell):
    """
    Instant Summons Spell
    SRD p. 158
    Generated
    """

    def __init__(self):
        super().__init__(name="Instant Summons",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=6,
                         school=SpellSchools.Conjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a sapphire worth 1,000 gp",
                         duration="Until dispelled",
                         description="You touch an object weighing 10 pounds or less\nwhose longest " +
                                    "dimension is 6 feet or less. The spell\nleaves an invisible " +
                                    "mark on its surface and invisibly\ninscribes the name of the " +
                                    "item on the sapphire you\nuse as the material component. Each " +
                                    "time you cast\nthis spell, you must use a different " +
                                    "sapphire.\nAt any time thereafter, you can use your action " +
                                    "to\nspeak the item's name and crush the sapphire. The\nitem " +
                                    "instantly appears in your hand regardless of\nphysical or " +
                                    "planar distances, and the spell ends.\nIf another creature is " +
                                    "holding or carrying the item,\ncrushing the sapphire doesn't " +
                                    "transport the item to\nyou, but instead you learn who the " +
                                    "creature\npossessing the object is and roughly where " +
                                    "that\ncreature is located at that moment.\nDispel magic or a " +
                                    "similar effect successfully\napplied to the sapphire ends this " +
                                    "spell's effect. ",
                         at_higher_levels="")


class Invisibility(spells.Spell):
    """
    Invisibility Spell
    SRD p. 158-159
    Generated
    """

    def __init__(self):
        super().__init__(name="Invisibility",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Illusion,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an eyelash encased in gum arabic",
                         duration="1 hour",
                         description="A creature you touch becomes invisible until the\nspell ends. " +
                                    "Anything the target is wearing or\ncarrying is invisible as " +
                                    "long as it is on the target's\nperson. The spell ends for a " +
                                    "target that attacks or\ncasts a spell. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 2nd. ")


class IrresistibleDance(spells.Spell):
    """
    Irresistible Dance Spell
    SRD p. 159
    Generated
    """

    def __init__(self):
        super().__init__(name="Irresistible Dance",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="1 minute",
                         description="Choose one creature that you can see within range.\nThe target " +
                                    "begins a comic dance in place: shuffling,\ntapping its feet, " +
                                    "and capering for the duration.\nCreatures that can't be " +
                                    "charmed are immune to this\nspell.\nA dancing creature must " +
                                    "use all its movement to\ndance without leaving its space and " +
                                    "has\ndisadvantage on Dexterity saving throws and " +
                                    "attack\nrolls. While the target is affected by this spell, " +
                                    "other\ncreatures have advantage on attack rolls against " +
                                    "it.\nAs an action, a dancing creature makes a Wisdom\nsaving " +
                                    "throw to regain control of itself. On a\nsuccessful save, the " +
                                    "spell ends. ",
                         at_higher_levels="")


class Jump(spells.Spell):
    """
    Jump Spell
    SRD p. 159
    Generated
    """

    def __init__(self):
        super().__init__(name="Jump",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a grasshopper's hind leg",
                         duration="1 minute",
                         description="You touch a creature. The creature's jump distance is\ntripled " +
                                    "until the spell ends. ",
                         at_higher_levels="")


class Knock(spells.Spell):
    """
    Knock Spell
    SRD p. 159
    Generated
    """

    def __init__(self):
        super().__init__(name="Knock",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Choose an object that you can see within range. The\nobject " +
                                    "can be a door, a box, a chest, a set of manacles,\na padlock, " +
                                    "or another object that contains a\nmundane or magical means " +
                                    "that prevents access.\nA target that is held shut by a mundane " +
                                    "lock or\nthat is stuck or barred becomes unlocked, " +
                                    "unstuck,\nor unbarred. If the object has multiple locks, " +
                                    "only\none of them is unlocked.\nIf you choose a target that is " +
                                    "held shut with arcane\nlock, that spell is suppressed for 10 " +
                                    "minutes, during\nwhich time the target can be opened and " +
                                    "shut\nnormally.\nWhen you cast the spell, a loud knock, " +
                                    "audible\nfrom as far away as 300 feet, emanates from " +
                                    "the\ntarget object. ",
                         at_higher_levels="")


class LegendLore(spells.Spell):
    """
    Legend Lore Spell
    SRD p. 159
    Generated
    """

    def __init__(self):
        super().__init__(name="Legend Lore",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="incense worth at least 250 gp, which the spell consumes, and four ivory strips worth at least 50 gp each",
                         duration="Instantaneous",
                         description="Name or describe a person, place, or object. The spell\nbrings " +
                                    "to your mind a brief summary of the\nsignificant lore about " +
                                    "the thing you named. The lore\nmight consist of current tales, " +
                                    "forgotten stories, or\neven secret lore that has never been " +
                                    "widely known.\nIf the thing you named isn't of legendary " +
                                    "importance,\nyou gain no information. The more information " +
                                    "you\nalready have about the thing, the more precise " +
                                    "and\ndetailed the information you receive is.\nThe information " +
                                    "you learn is accurate but might be\ncouched in figurative " +
                                    "language. For example, if you\nhave a mysterious magic axe on " +
                                    "hand, the spell\nmight yield this information: “Woe to the " +
                                    "evildoer\nwhose hand touches the axe, for even the haft " +
                                    "slices\nthe hand of the evil ones. Only a true Child of " +
                                    "Stone,\nlover and beloved of Moradin, may awaken the " +
                                    "true\npowers of the axe, and only with the sacred " +
                                    "word\nRudnogg on the lips.” ",
                         at_higher_levels="")


class LesserRestoration(spells.Spell):
    """
    Lesser Restoration Spell
    SRD p. 159
    Generated
    """

    def __init__(self):
        super().__init__(name="Lesser Restoration",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You touch a creature and can end either one disease\nor one " +
                                    "condition afflicting it. The condition can be\nblinded, " +
                                    "deafened, paralyzed, or poisoned. ",
                         at_higher_levels="")


class Levitate(spells.Spell):
    """
    Levitate Spell
    SRD p. 159-160
    Generated
    """

    def __init__(self):
        super().__init__(name="Levitate",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end",
                         duration="10 minutes",
                         description="One creature or object of your choice that you can\nsee within " +
                                    "range rises vertically, up to 20 feet, and\nremains suspended " +
                                    "there for the duration. The spell\ncan levitate a target that " +
                                    "weighs up to 500 pounds.\nAn unwilling creature that succeeds " +
                                    "on a\nConstitution saving throw is unaffected.\nThe target can " +
                                    "move only by pushing or pulling\nagainst a fixed object or " +
                                    "surface within reach (such\nas a wall or a ceiling), which " +
                                    "allows it to move as if it\nwere climbing. You can change the " +
                                    "target's altitude\nby up to 20 feet in either direction on " +
                                    "your turn. If\nyou are the target, you can move up or down as " +
                                    "part\nof your move. Otherwise, you can use your action " +
                                    "to\nmove the target, which must remain within the\nspell's " +
                                    "range.\nWhen the spell ends, the target floats gently to " +
                                    "the\nground if it is still aloft. ",
                         at_higher_levels="")


class Light(spells.Spell):
    """
    Light Spell
    SRD p. 160
    Generated
    """

    def __init__(self):
        super().__init__(name="Light",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=0,
                         school=SpellSchools.Evocation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list="a firefly or phosphorescent moss",
                         duration="1 hour",
                         description="You touch one object that is no larger than 10 feet in\nany " +
                                    "dimension. Until the spell ends, the object sheds\nbright " +
                                    "light in a 20-foot radius and dim light for an\nadditional 20 " +
                                    "feet. The light can be colored as you\nlike. Completely " +
                                    "covering the object with something\nopaque blocks the light. " +
                                    "The spell ends if you cast it\nagain or dismiss it as an " +
                                    "action.\nIf you target an object held or worn by a " +
                                    "hostile\ncreature, that creature must succeed on a " +
                                    "Dexterity\nsaving throw to avoid the spell. ",
                         at_higher_levels="")


class LightningBolt(spells.Spell):
    """
    Lightning Bolt Spell
    SRD p. 160
    Generated
    """

    def __init__(self):
        super().__init__(name="Lightning Bolt",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.Evocation,
                         spell_range="Self (100-foot line)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fur and a rod of amber, crystal, or glass",
                         duration="Instantaneous",
                         description="A stroke of lightning forming a line 100 feet long and\n5 feet " +
                                    "wide blasts out from you in a direction you\nchoose. Each " +
                                    "creature in the line must make a\nDexterity saving throw. A " +
                                    "creature takes 8d6\nlightning damage on a failed save, or half " +
                                    "as much\ndamage on a successful one.\nThe lightning ignites " +
                                    "flammable objects in the area\nthat aren't being worn or " +
                                    "carried. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the damage increases\nby 1d6 for each slot level above " +
                                          "3rd. ")


class LocateAnimalsOrPlants(spells.Spell):
    """
    Locate Animals or Plants Spell
    SRD p. 160
    Generated
    """

    def __init__(self):
        super().__init__(name="Locate Animals or Plants",
                         spell_lists=[SpellLists.PRIMAL],
                         ritual=True,
                         level=2,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fur from a bloodhound",
                         duration="Instantaneous",
                         description="Describe or name a specific kind of beast or " +
                                    "plant.\nConcentrating on the voice of nature in " +
                                    "your\nsurroundings, you learn the direction and distance\nto " +
                                    "the closest creature or plant of that kind within 5\nmiles, if " +
                                    "any are present. ",
                         at_higher_levels="")


class LocateCreature(spells.Spell):
    """
    Locate Creature Spell
    SRD p. 160
    Generated
    """

    def __init__(self):
        super().__init__(name="Locate Creature",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fur from a bloodhound",
                         duration="1 hour",
                         description="Describe or name a creature that is familiar to you.\nYou " +
                                    "sense the direction to the creature's location, as\nlong as " +
                                    "that creature is within 1,000 feet of you. If\nthe creature is " +
                                    "moving, you know the direction of its\nmovement.\nThe spell " +
                                    "can locate a specific creature known to\nyou, or the nearest " +
                                    "creature of a specific kind (such\nas a human or a unicorn), " +
                                    "so long as you have seen\nsuch a creature up close—within 30 " +
                                    "feet—at least\nonce. If the creature you described or named is " +
                                    "in a\ndifferent form, such as being under the effects of " +
                                    "a\npolymorph spell, this spell doesn't locate the " +
                                    "creature.\nThis spell can't locate a creature if running " +
                                    "water\nat least 10 feet wide blocks a direct path between\nyou " +
                                    "and the creature. ",
                         at_higher_levels="")


class LocateObject(spells.Spell):
    """
    Locate Object Spell
    SRD p. 160-161
    Generated
    """

    def __init__(self):
        super().__init__(name="Locate Object",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a forked twig",
                         duration="10 minutes",
                         description="Describe or name an object that is familiar to you.\nYou sense " +
                                    "the direction to the object's location, as\nlong as that " +
                                    "object is within 1,000 feet of you. If the\nobject is in " +
                                    "motion, you know the direction of its\nmovement.\nThe spell " +
                                    "can locate a specific object known to you,\nas long as you " +
                                    "have seen it up close—within 30\nfeet—at least once. " +
                                    "Alternatively, the spell can locate\nthe nearest object of a " +
                                    "particular kind, such as a\ncertain kind of apparel, jewelry, " +
                                    "furniture, tool, or\nweapon.\nThis spell can't locate an " +
                                    "object if any thickness of\nlead, even a thin sheet, blocks a " +
                                    "direct path between\nyou and the object. ",
                         at_higher_levels="")


class Longstrider(spells.Spell):
    """
    Longstrider Spell
    SRD p. 161
    Generated
    """

    def __init__(self):
        super().__init__(name="Longstrider",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of dirt",
                         duration="1 hour",
                         description="You touch a creature. The target's speed increases by\n10 feet " +
                                    "until the spell ends. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, you can target one\nadditional creature for each slot " +
                                          "level above 1st. ")


class MageArmor(spells.Spell):
    """
    Mage Armor Spell
    SRD p. 161
    Generated
    """

    def __init__(self):
        super().__init__(name="Mage Armor",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of cured leather",
                         duration="8 hours",
                         description="You touch a willing creature who isn't wearing\narmor, and a " +
                                    "protective magical force surrounds it\nuntil the spell ends. " +
                                    "The target's base AC becomes 13\n+ its Dexterity modifier. The " +
                                    "spell ends if the target\ndons armor or if you dismiss the " +
                                    "spell as an action. ",
                         at_higher_levels="")


class MageHand(spells.Spell):
    """
    Mage Hand Spell
    SRD p. 161
    Generated
    """

    def __init__(self):
        super().__init__(name="Mage Hand",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="A spectral, floating hand appears at a point you\nchoose " +
                                    "within range. The hand lasts for the duration\nor until you " +
                                    "dismiss it as an action. The hand\nvanishes if it is ever more " +
                                    "than 30 feet away from\nyou or if you cast this spell " +
                                    "again.\nYou can use your action to control the hand. You\ncan " +
                                    "use the hand to manipulate an object, open an\nunlocked door " +
                                    "or container, stow or retrieve an item\nfrom an open " +
                                    "container, or pour the contents out of a\nvial. You can move " +
                                    "the hand up to 30 feet each time\nyou use it.\nThe hand can't " +
                                    "attack, activate magic items, or\ncarry more than 10 pounds. ",
                         at_higher_levels="")


class MagicCircle(spells.Spell):
    """
    Magic Circle Spell
    SRD p. 161
    Generated
    """

    def __init__(self):
        super().__init__(name="Magic Circle",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="holy water or powdered silver and iron worth at least 100 gp, which the spell consumes",
                         duration="1 hour",
                         description="You create a 10-foot-radius, 20-foot-tall cylinder of\nmagical " +
                                    "energy centered on a point on the ground\nthat you can see " +
                                    "within range. Glowing runes appear\nwherever the cylinder " +
                                    "intersects with the floor or\nother surface.\nChoose one or " +
                                    "more of the following types of\ncreatures: celestials, " +
                                    "elementals, fey, fiends, or\nundead. The circle affects a " +
                                    "creature of the chosen\ntype in the following ways:\n• The " +
                                    "creature can't willingly enter the cylinder by\nnonmagical " +
                                    "means. If the creature tries to use\nteleportation or " +
                                    "interplanar travel to do so, it must\nfirst succeed on a " +
                                    "Charisma saving throw.\n• The creature has disadvantage on " +
                                    "attack rolls\nagainst targets within the cylinder.\n• Targets " +
                                    "within the cylinder can't be charmed,\nfrightened, or " +
                                    "possessed by the creature.\nWhen you cast this spell, you can " +
                                    "elect to cause its\nmagic to operate in the reverse direction, " +
                                    "preventing\na creature of the specified type from leaving " +
                                    "the\ncylinder and protecting targets outside it. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the duration\nincreases by 1 hour for each slot level " +
                                          "above 3rd. ")


class MagicJar(spells.Spell):
    """
    Magic Jar Spell
    SRD p. 161-162
    Generated
    """

    def __init__(self):
        super().__init__(name="Magic Jar",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Necromancy,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a gem, crystal, reliquary, or some other ornamental container worth at least 500 gp",
                         duration="Until dispelled",
                         description="Your body falls into a catatonic state as your soul\nleaves it " +
                                    "and enters the container you used for the\nspell's material " +
                                    "component. While your soul inhabits\nthe container, you are " +
                                    "aware of your surroundings as\nif you were in the container's " +
                                    "space. You can't move\nor use reactions. The only action you " +
                                    "can take is to\nproject your soul up to 100 feet out of the " +
                                    "container,\neither returning to your living body (and ending " +
                                    "the\nspell) or attempting to possess a humanoids body.\nYou " +
                                    "can attempt to possess any humanoid within\n100 feet of you " +
                                    "that you can see (creatures warded\nby a protection from evil " +
                                    "and good or magic circle\nspell can't be possessed). The " +
                                    "target must make a\nCharisma saving throw. On a failure, your " +
                                    "soul\nmoves into the target's body, and the target's " +
                                    "soul\nbecomes trapped in the container. On a success, " +
                                    "the\ntarget resists your efforts to possess it, and you " +
                                    "can't\nattempt to possess it again for 24 hours.\nOnce you " +
                                    "possess a creature's body, you control it.\nYour game " +
                                    "statistics are replaced by the statistics of\nthe creature, " +
                                    "though you retain your alignment and\nyour Intelligence, " +
                                    "Wisdom, and Charisma scores. You\nretain the benefit of your " +
                                    "own class features. If the\ntarget has any class levels, you " +
                                    "can't use any of its\nclass features.\nMeanwhile, the " +
                                    "possessed creature's soul can\nperceive from the container " +
                                    "using its own senses,\nbut it can't move or take actions at " +
                                    "all.\nWhile possessing a body, you can use your action\nto " +
                                    "return from the host body to the container if it is\nwithin " +
                                    "100 feet of you, returning the host creature's\nsoul to its " +
                                    "body. If the host body dies while you're in\nit, the creature " +
                                    "dies, and you must make a Charisma\nsaving throw against your " +
                                    "own spellcasting DC. On a\nsuccess, you return to the " +
                                    "container if it is within\n100 feet of you. Otherwise, you " +
                                    "die.\nIf the container is destroyed or the spell ends,\nyour " +
                                    "soul immediately returns to your body. If your\nbody is more " +
                                    "than 100 feet away from you or if your\nbody is dead when you " +
                                    "attempt to return to it, you\ndie. If another creature's soul " +
                                    "is in the container\nwhen it is destroyed, the creature's soul " +
                                    "returns to\nits body if the body is alive and within 100 " +
                                    "feet.\nOtherwise, that creature dies.\nWhen the spell ends, " +
                                    "the container is destroyed. ",
                         at_higher_levels="")


class MagicMissile(spells.Spell):
    """
    Magic Missile Spell
    SRD p. 162
    Generated
    """

    def __init__(self):
        super().__init__(name="Magic Missile",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You create three glowing darts of magical force. Each\ndart " +
                                    "hits a creature of your choice that you can see\nwithin range. " +
                                    "A dart deals 1d4 + 1 force damage to\nits target. The darts " +
                                    "all strike simultaneously, and\nyou can direct them to hit one " +
                                    "creature or several. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the spell creates one\nmore dart for each slot level " +
                                          "above 1st. ")


class MagicMouth(spells.Spell):
    """
    Magic Mouth Spell
    SRD p. 162
    Generated
    """

    def __init__(self):
        super().__init__(name="Magic Mouth",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=2,
                         school=SpellSchools.Illusion,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small bit of honeycomb and jade dust worth at least 10 gp, which the spell consumes",
                         duration="Until dispelled",
                         description="You implant a message within an object in range, a\nmessage " +
                                    "that is uttered when a trigger condition is\nmet. Choose an " +
                                    "object that you can see and that isn't\nbeing worn or carried " +
                                    "by another creature. Then\nspeak the message, which must be 25 " +
                                    "words or less,\nthough it can be delivered over as long as " +
                                    "10\nminutes. Finally, determine the circumstance that\nwill " +
                                    "trigger the spell to deliver your message.\nWhen that " +
                                    "circumstance occurs, a magical mouth\nappears on the object " +
                                    "and recites the message in\nyour voice and at the same volume " +
                                    "you spoke. If the\nobject you chose has a mouth or something " +
                                    "that\nlooks like a mouth (for example, the mouth of " +
                                    "a\nstatue), the magical mouth appears there so that the\nwords " +
                                    "appear to come from the object's mouth.\nWhen you cast this " +
                                    "spell, you can have the spell end\nafter it delivers its " +
                                    "message, or it can remain and\nrepeat its message whenever the " +
                                    "trigger occurs.\nThe triggering circumstance can be as general " +
                                    "or\nas detailed as you like, though it must be based " +
                                    "on\nvisual or audible conditions that occur within 30 feet\nof " +
                                    "the object. For example, you could instruct the\nmouth to " +
                                    "speak when any creature moves within 30\nfeet of the object or " +
                                    "when a silver bell rings within\n30 feet of it. ",
                         at_higher_levels="")


class MagicWeapon(spells.Spell):
    """
    Magic Weapon Spell
    SRD p. 162-163
    Generated
    """

    def __init__(self):
        super().__init__(name="Magic Weapon",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You touch a nonmagical weapon. Until the spell ends,\nthat " +
                                    "weapon becomes a magic weapon with a +1\nbonus to attack rolls " +
                                    "and damage rolls. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the bonus increases\nto +2. When you use a spell slot " +
                                          "of 6th level or higher,\nthe bonus increases to +3. ")


class MagnificentMansion(spells.Spell):
    """
    Magnificent Mansion Spell
    SRD p. 163
    Generated
    """

    def __init__(self):
        super().__init__(name="Magnificent Mansion",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Conjuration,
                         spell_range="300 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a miniature portal carved from ivory, a small piece of polished marble, and a tiny silver spoon, each item worth at least 5 gp",
                         duration="24 hours",
                         description="You conjure an extradimensional dwelling in range\nthat lasts " +
                                    "for the duration. You choose where its one\nentrance is " +
                                    "located. The entrance shimmers faintly\nand is 5 feet wide and " +
                                    "10 feet tall. You and any\ncreature you designate when you " +
                                    "cast the spell can\nenter the extradimensional dwelling as " +
                                    "long as the\nportal remains open. You can open or close " +
                                    "the\nportal if you are within 30 feet of it. While closed, " +
                                    "the\nportal is invisible.\nBeyond the portal is a magnificent " +
                                    "foyer with\nnumerous chambers beyond. The atmosphere " +
                                    "is\nclean, fresh, and warm.\nYou can create any floor plan you " +
                                    "like, but the\nspace can't exceed 50 cubes, each cube being 10 " +
                                    "feet\non each side. The place is furnished and decorated " +
                                    "as\nyou choose. It contains sufficient food to serve " +
                                    "a\nnine-course banquet for up to 100 people. A staff of\n100 " +
                                    "near-transparent servants attends all who enter.\nYou decide " +
                                    "the visual appearance of these servants\nand their attire. " +
                                    "They are completely obedient to\nyour orders. Each servant can " +
                                    "perform any task a\nnormal human servant could perform, but " +
                                    "they can't\nattack or take any action that would directly " +
                                    "harm\nanother creature. Thus the servants can fetch " +
                                    "things,\nclean, mend, fold clothes, light fires, serve food, " +
                                    "pour\nwine, and so on. The servants can go anywhere in\nthe " +
                                    "mansion but can't leave it. Furnishings and other\nobjects " +
                                    "created by this spell dissipate into smoke if\nremoved from " +
                                    "the mansion. When the spell ends,\nany creatures inside the " +
                                    "extradimensional space are\nexpelled into the open spaces " +
                                    "nearest to the\nentrance. ",
                         at_higher_levels="")


class MajorImage(spells.Spell):
    """
    Major Image Spell
    SRD p. 163
    Generated
    """

    def __init__(self):
        super().__init__(name="Major Image",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Illusion,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fleece",
                         duration="10 minutes",
                         description="You create the image of an object, a creature, or\nsome other " +
                                    "visible phenomenon that is no larger\nthan a 20-foot cube. The " +
                                    "image appears at a spot that\nyou can see within range and " +
                                    "lasts for the duration.\nIt seems completely real, including " +
                                    "sounds, smells,\nand temperature appropriate to the thing " +
                                    "depicted.\nYou can't create sufficient heat or cold to " +
                                    "cause\ndamage, a sound loud enough to deal thunder\ndamage or " +
                                    "deafen a creature, or a smell that might\nsicken a creature " +
                                    "(like a troglodyte's stench).\nAs long as you are within range " +
                                    "of the illusion, you\ncan use your action to cause the image " +
                                    "to move to\nany other spot within range. As the image " +
                                    "changes\nlocation, you can alter its appearance so that " +
                                    "its\nmovements appear natural for the image. For\nexample, if " +
                                    "you create an image of a creature and\nmove it, you can alter " +
                                    "the image so that it appears to\nbe walking. Similarly, you " +
                                    "can cause the illusion to\nmake different sounds at different " +
                                    "times, even\nmaking it carry on a conversation, for " +
                                    "example.\nPhysical interaction with the image reveals it to " +
                                    "be\nan illusion, because things can pass through it. " +
                                    "A\ncreature that uses its action to examine the image\ncan " +
                                    "determine that it is an illusion with a " +
                                    "successful\nIntelligence (Investigation) check against your " +
                                    "spell\nsave DC. If a creature discerns the illusion for what " +
                                    "it\nis, the creature can see through the image, and its\nother " +
                                    "sensory qualities become faint to the creature. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the spell lasts until\ndispelled, without requiring " +
                                          "your concentration. ")


class MassCureWounds(spells.Spell):
    """
    Mass Cure Wounds Spell
    SRD p. 163-164
    Generated
    """

    def __init__(self):
        super().__init__(name="Mass Cure Wounds",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=5,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="A wave of healing energy washes out from a point of\nyour " +
                                    "choice within range. Choose up to six creatures\nin a " +
                                    "30-foot-radius sphere centered on that point.\nEach target " +
                                    "regains hit points equal to 3d8 + your\nspellcasting ability " +
                                    "modifier. This spell has no effect\non undead or constructs. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 6th level or " +
                                          "higher, the healing increases\nby 1d8 for each slot level " +
                                          "above 5th. ")


class MassHeal(spells.Spell):
    """
    Mass Heal Spell
    SRD p. 164
    Generated
    """

    def __init__(self):
        super().__init__(name="Mass Heal",
                         spell_lists=[SpellLists.DIVINE],
                         level=9,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="A flood of healing energy flows from you into " +
                                    "injured\ncreatures around you. You restore up to 700 " +
                                    "hit\npoints, divided as you choose among any number " +
                                    "of\ncreatures that you can see within range. Creatures\nhealed " +
                                    "by this spell are also cured of all diseases and\nany effect " +
                                    "making them blinded or deafened. This\nspell has no effect on " +
                                    "undead or constructs. ",
                         at_higher_levels="")


class MassHealingWord(spells.Spell):
    """
    Mass Healing Word Spell
    SRD p. 164
    Generated
    """

    def __init__(self):
        super().__init__(name="Mass Healing Word",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="As you call out words of restoration, up to six\ncreatures of " +
                                    "your choice that you can see within\nrange regain hit points " +
                                    "equal to 1d4 + your\nspellcasting ability modifier. This spell " +
                                    "has no effect\non undead or constructs. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the healing increases\nby 1d4 for each slot level " +
                                          "above 3rd. ")


class MassSuggestion(spells.Spell):
    """
    Mass Suggestion Spell
    SRD p. 164
    Generated
    """

    def __init__(self):
        super().__init__(name="Mass Suggestion",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list="a snake's tongue and either a bit of honeycomb or a drop of sweet oil",
                         duration="24 hours",
                         description="You suggest a course of activity (limited to a\nsentence or " +
                                    "two) and magically influence up to\ntwelve creatures of your " +
                                    "choice that you can see\nwithin range and that can hear and " +
                                    "understand you.\nCreatures that can't be charmed are immune to " +
                                    "this\neffect. The suggestion must be worded in such a\nmanner " +
                                    "as to make the course of action sound\nreasonable. Asking the " +
                                    "creature to stab itself, throw\nitself onto a spear, immolate " +
                                    "itself, or do some other\nobviously harmful act automatically " +
                                    "negates the\neffect of the spell.\nEach target must make a " +
                                    "Wisdom saving throw.\nOn a failed save, it pursues the course " +
                                    "of action you\ndescribed to the best of its ability. The " +
                                    "suggested\ncourse of action can continue for the entire " +
                                    "duration.\nIf the suggested activity can be completed in " +
                                    "a\nshorter time, the spell ends when the subject\nfinishes " +
                                    "what it was asked to do.\nYou can also specify conditions that " +
                                    "will trigger a\nspecial activity during the duration. For " +
                                    "example,\nyou might suggest that a group of soldiers give " +
                                    "all\ntheir money to the first beggar they meet. If " +
                                    "the\ncondition isn't met before the spell ends, the " +
                                    "activity\nisn't performed.\nIf you or any of your companions " +
                                    "damage a\ncreature affected by this spell, the spell ends for " +
                                    "that\ncreature. ",
                         at_higher_levels="When you cast this spell using a\n7th-level spell slot, the " +
                                          "duration is 10 days. When\nyou use an 8th-level spell slot, " +
                                          "the duration is 30\ndays. When you use a 9th-level spell slot, " +
                                          "the\nduration is a year and a day. ")


class Maze(spells.Spell):
    """
    Maze Spell
    SRD p. 164
    Generated
    """

    def __init__(self):
        super().__init__(name="Maze",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=8,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You banish a creature that you can see within range\ninto a " +
                                    "labyrinthine demiplane. The target remains\nthere for the " +
                                    "duration or until it escapes the maze.\nThe target can use its " +
                                    "action to attempt to escape.\nWhen it does so, it makes a DC " +
                                    "20 Intelligence check.\nIf it succeeds, it escapes, and the " +
                                    "spell ends (a\nminotaur or goristro demon automatically " +
                                    "succeeds).\nWhen the spell ends, the target reappears in " +
                                    "the\nspace it left or, if that space is occupied, in " +
                                    "the\nnearest unoccupied space. ",
                         at_higher_levels="")


class MeldIntoStone(spells.Spell):
    """
    Meld into Stone Spell
    SRD p. 164-165
    Generated
    """

    def __init__(self):
        super().__init__(name="Meld into Stone",
                         spell_lists=[SpellLists.PRIMAL],
                         ritual=True,
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="8 hours",
                         description="You step into a stone object or surface large enough\nto fully " +
                                    "contain your body, melding yourself and all\nthe equipment you " +
                                    "carry with the stone for the\nduration. Using your movement, " +
                                    "you step into the\nstone at a point you can touch. Nothing of " +
                                    "your\npresence remains visible or otherwise detectable " +
                                    "by\nnonmagical senses.\nWhile merged with the stone, you can't " +
                                    "see what\noccurs outside it, and any Wisdom " +
                                    "(Perception)\nchecks you make to hear sounds outside it are " +
                                    "made\nwith disadvantage. You remain aware of the passage\nof " +
                                    "time and can cast spells on yourself while merged\nin the " +
                                    "stone. You can use your movement to leave\nthe stone where you " +
                                    "entered it, which ends the spell.\nYou otherwise can't " +
                                    "move.\nMinor physical damage to the stone doesn't harm\nyou, " +
                                    "but its partial destruction or a change in its\nshape (to the " +
                                    "extent that you no longer fit within it)\nexpels you and deals " +
                                    "6d6 bludgeoning damage to\nyou. The stone's complete " +
                                    "destruction (or\ntransmutation into a different substance) " +
                                    "expels you\nand deals 50 bludgeoning damage to you. If " +
                                    "expelled,\nyou fall prone in an unoccupied space closest " +
                                    "to\nwhere you first entered. ",
                         at_higher_levels="")


class Mending(spells.Spell):
    """
    Mending Spell
    SRD p. 165
    Generated
    """

    def __init__(self):
        super().__init__(name="Mending",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="two lodestones",
                         duration="Instantaneous",
                         description="This spell repairs a single break or tear in an object\nyou " +
                                    "touch, such as a broken chain link, two halves of\na broken " +
                                    "key, a torn cloak, or a leaking wineskin. As\nlong as the " +
                                    "break or tear is no larger than 1 foot in\nany dimension, you " +
                                    "mend it, leaving no trace of the\nformer damage.\nThis spell " +
                                    "can physically repair a magic item or\nconstruct, but the " +
                                    "spell can't restore magic to such\nan object. ",
                         at_higher_levels="")


class Message(spells.Spell):
    """
    Message Spell
    SRD p. 165
    Generated
    """

    def __init__(self):
        super().__init__(name="Message",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.Transmutation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a short piece of copper wire",
                         duration="1 round",
                         description="You point your finger toward a creature within\nrange and " +
                                    "whisper a message. The target (and only\nthe target) hears the " +
                                    "message and can reply in a\nwhisper that only you can " +
                                    "hear.\nYou can cast this spell through solid objects if " +
                                    "you\nare familiar with the target and know it is beyond\nthe " +
                                    "barrier. Magical silence, 1 foot of stone, 1 inch of\ncommon " +
                                    "metal, a thin sheet of lead, or 3 feet of wood\nblocks the " +
                                    "spell. The spell doesn't have to follow a\nstraight line and " +
                                    "can travel freely around corners or\nthrough openings. ",
                         at_higher_levels="")


class MeteorSwarm(spells.Spell):
    """
    Meteor Swarm Spell
    SRD p. 165
    Generated
    """

    def __init__(self):
        super().__init__(name="Meteor Swarm",
                         spell_lists=[SpellLists.ARCANE],
                         level=9,
                         school=SpellSchools.Evocation,
                         spell_range="1 mile",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Blazing orbs of fire plummet to the ground at four\ndifferent " +
                                    "points you can see within range. Each\ncreature in a " +
                                    "40-foot-radius sphere centered on each\npoint you choose must " +
                                    "make a Dexterity saving\nthrow. The sphere spreads around " +
                                    "corners. A\ncreature takes 20d6 fire damage and " +
                                    "20d6\nbludgeoning damage on a failed save, or half as " +
                                    "much\ndamage on a successful one. A creature in the area " +
                                    "of\nmore than one fiery burst is affected only once.\nThe " +
                                    "spell damages objects in the area and ignites\nflammable " +
                                    "objects that aren't being worn or carried. ",
                         at_higher_levels="")


class MindBlank(spells.Spell):
    """
    Mind Blank Spell
    SRD p. 165
    Generated
    """

    def __init__(self):
        super().__init__(name="Mind Blank",
                         spell_lists=[SpellLists.ARCANE],
                         level=8,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="24 hours",
                         description="Until the spell ends, one willing creature you touch " +
                                    "is\nimmune to psychic damage, any effect that would\nsense its " +
                                    "emotions or read its thoughts, divination\nspells, and the " +
                                    "charmed condition. The spell even\nfoils wish spells and " +
                                    "spells or effects of similar power\nused to affect the " +
                                    "target's mind or to gain\ninformation about the target. ",
                         at_higher_levels="")


class MinorIllusion(spells.Spell):
    """
    Minor Illusion Spell
    SRD p. 165-166
    Generated
    """

    def __init__(self):
        super().__init__(name="Minor Illusion",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Illusion,
                         spell_range="30 feet",
                         verbal_components=False,
                         somatic_components=True,
                         material_components_list="a bit of fleece",
                         duration="1 minute",
                         description="You create a sound or an image of an object within\nrange that " +
                                    "lasts for the duration. The illusion also\nends if you dismiss " +
                                    "it as an action or cast this spell\nagain.\nIf you create a " +
                                    "sound, its volume can range from a\nwhisper to a scream. It " +
                                    "can be your voice, someone\nelse's voice, a lion's roar, a " +
                                    "beating of drums, or any\nother sound you choose. The sound " +
                                    "continues\nunabated throughout the duration, or you can " +
                                    "make\ndiscrete sounds at different times before the " +
                                    "spell\nends.\nIf you create an image of an object—such as " +
                                    "a\nchair, muddy footprints, or a small chest—it must be\nno " +
                                    "larger than a 5-foot cube. The image can't create\nsound, " +
                                    "light, smell, or any other sensory effect.\nPhysical " +
                                    "interaction with the image reveals it to be\nan illusion, " +
                                    "because things can pass through it.\nIf a creature uses its " +
                                    "action to examine the sound\nor image, the creature can " +
                                    "determine that it is an\nillusion with a successful " +
                                    "Intelligence (Investigation)\ncheck against your spell save " +
                                    "DC. If a creature\ndiscerns the illusion for what it is, the " +
                                    "illusion\nbecomes faint to the creature. ",
                         at_higher_levels="")


class MirageArcane(spells.Spell):
    """
    Mirage Arcane Spell
    SRD p. 166
    Generated
    """

    def __init__(self):
        super().__init__(name="Mirage Arcane",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Illusion,
                         spell_range="Sight",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 days",
                         description="You make terrain in an area up to 1 mile square look,\nsound, " +
                                    "smell, and even feel like some other sort of\nterrain. The " +
                                    "terrain's general shape remains the\nsame, however. Open " +
                                    "fields or a road could be made\nto resemble a swamp, hill, " +
                                    "crevasse, or some other\ndifficult or impassable terrain. A " +
                                    "pond can be made\nto seem like a grassy meadow, a precipice " +
                                    "like a\ngentle slope, or a rock-strewn gully like a wide " +
                                    "and\nsmooth road.\nSimilarly, you can alter the appearance " +
                                    "of\nstructures, or add them where none are present. The\nspell " +
                                    "doesn't disguise, conceal, or add creatures.\nThe illusion " +
                                    "includes audible, visual, tactile, and\nolfactory elements, so " +
                                    "it can turn clear ground into\ndifficult terrain (or vice " +
                                    "versa) or otherwise impede\nmovement through the area. Any " +
                                    "piece of the\nillusory terrain (such as a rock or stick) that " +
                                    "is\nremoved from the spell's area " +
                                    "disappears\nimmediately.\nCreatures with truesight can see " +
                                    "through the\nillusion to the terrain's true form; however, all " +
                                    "other\nelements of the illusion remain, so while the\ncreature " +
                                    "is aware of the illusion's presence, the\ncreature can still " +
                                    "physically interact with the illusion. ",
                         at_higher_levels="")


class MirrorImage(spells.Spell):
    """
    Mirror Image Spell
    SRD p. 166
    Generated
    """

    def __init__(self):
        super().__init__(name="Mirror Image",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Illusion,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="Three illusory duplicates of yourself appear in your\nspace. " +
                                    "Until the spell ends, the duplicates move with\nyou and mimic " +
                                    "your actions, shifting position so it's\nimpossible to track " +
                                    "which image is real. You can use\nyour action to dismiss the " +
                                    "illusory duplicates.\nEach time a creature targets you with an " +
                                    "attack\nduring the spell's duration, roll a d20 to " +
                                    "determine\nwhether the attack instead targets one of " +
                                    "your\nduplicates.\nIf you have three duplicates, you must roll " +
                                    "a 6 or\nhigher to change the attack's target to a " +
                                    "duplicate.\nWith two duplicates, you must roll an 8 or " +
                                    "higher.\nWith one duplicate, you must roll an 11 or higher.\nA " +
                                    "duplicate's AC equals 10 + your Dexterity\nmodifier. If an " +
                                    "attack hits a duplicate, the duplicate is\ndestroyed. A " +
                                    "duplicate can be destroyed only by an\nattack that hits it. It " +
                                    "ignores all other damage and\neffects. The spell ends when all " +
                                    "three duplicates are\ndestroyed.\nA creature is unaffected by " +
                                    "this spell if it can't see,\nif it relies on senses other than " +
                                    "sight, such as\nblindsight, or if it can perceive illusions as " +
                                    "false, as\nwith truesight. ",
                         at_higher_levels="")


class Mislead(spells.Spell):
    """
    Mislead Spell
    SRD p. 166
    Generated
    """

    def __init__(self):
        super().__init__(name="Mislead",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Illusion,
                         spell_range="Self",
                         verbal_components=False,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You become invisible at the same time that an\nillusory double " +
                                    "of you appears where you are\nstanding. The double lasts for " +
                                    "the duration, but the\ninvisibility ends if you attack or cast " +
                                    "a spell.\nYou can use your action to move your " +
                                    "illusory\ndouble up to twice your speed and make it " +
                                    "gesture,\nspeak, and behave in whatever way you choose.\nYou " +
                                    "can see through its eyes and hear through its\nears as if you " +
                                    "were located where it is. On each of\nyour turns as a bonus " +
                                    "action, you can switch from\nusing its senses to using your " +
                                    "own, or back again.\nWhile you are using its senses, you are " +
                                    "blinded and\ndeafened in regard to your own surroundings. ",
                         at_higher_levels="")


class MistyStep(spells.Spell):
    """
    Misty Step Spell
    SRD p. 166-167
    Generated
    """

    def __init__(self):
        super().__init__(name="Misty Step",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Conjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Briefly surrounded by silvery mist, you teleport up\nto 30 " +
                                    "feet to an unoccupied space that you can see. ",
                         at_higher_levels="")


class ModifyMemory(spells.Spell):
    """
    Modify Memory Spell
    SRD p. 167
    Generated
    """

    def __init__(self):
        super().__init__(name="Modify Memory",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You attempt to reshape another creature's memories.\nOne " +
                                    "creature that you can see must make a Wisdom\nsaving throw. If " +
                                    "you are fighting the creature, it has\nadvantage on the saving " +
                                    "throw. On a failed save, the\ntarget becomes charmed by you " +
                                    "for the duration.\nThe charmed target is incapacitated and " +
                                    "unaware of\nits surroundings, though it can still hear you. If " +
                                    "it\ntakes any damage or is targeted by another spell,\nthis " +
                                    "spell ends, and none of the target's memories\nare " +
                                    "modified.\nWhile this charm lasts, you can affect the " +
                                    "target's\nmemory of an event that it experienced within " +
                                    "the\nlast 24 hours and that lasted no more than 10\nminutes. " +
                                    "You can permanently eliminate all memory\nof the event, allow " +
                                    "the target to recall the event with\nperfect clarity and " +
                                    "exacting detail, change its\nmemory of the details of the " +
                                    "event, or create a\nmemory of some other event.\nYou must " +
                                    "speak to the target to describe how its\nmemories are " +
                                    "affected, and it must be able to\nunderstand your language for " +
                                    "the modified\nmemories to take root. Its mind fills in any " +
                                    "gaps in\nthe details of your description. If the spell " +
                                    "ends\nbefore you have finished describing the " +
                                    "modified\nmemories, the creature's memory isn't " +
                                    "altered.\nOtherwise, the modified memories take hold when\nthe " +
                                    "spell ends.\nA modified memory doesn't necessarily affect " +
                                    "how\na creature behaves, particularly if the " +
                                    "memory\ncontradicts the creature's natural " +
                                    "inclinations,\nalignment, or beliefs. An illogical modified " +
                                    "memory,\nsuch as implanting a memory of how much the\ncreature " +
                                    "enjoyed dousing itself in acid, is dismissed,\nperhaps as a " +
                                    "bad dream. The GM might deem a\nmodified memory too " +
                                    "nonsensical to affect a\ncreature in a significant manner.\nA " +
                                    "remove curse or greater restoration spell cast on\nthe target " +
                                    "restores the creature's true memory. ",
                         at_higher_levels="If you cast this spell using a spell\nslot of 6th level or " +
                                          "higher, you can alter the target's\nmemories of an event that " +
                                          "took place up to 7 days\nago (6th level), 30 days ago (7th " +
                                          "level), 1 year ago\n(8th level), or any time in the creature's " +
                                          "past (9th\nlevel). ")


class Moonbeam(spells.Spell):
    """
    Moonbeam Spell
    SRD p. 167
    Generated
    """

    def __init__(self):
        super().__init__(name="Moonbeam",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="several seeds of any moonseed plant and a piece of opalescent feldspar",
                         duration="1 minute",
                         description="A silvery beam of pale light shines down in a 5-footradius, " +
                                    "40-foot-high cylinder centered on a point\nwithin range. Until " +
                                    "the spell ends, dim light fills the\ncylinder.\nWhen a " +
                                    "creature enters the spell's area for the first\ntime on a turn " +
                                    "or starts its turn there, it is engulfed\nin ghostly flames " +
                                    "that cause searing pain, and it must\nmake a Constitution " +
                                    "saving throw. It takes 2d10\nradiant damage on a failed save, " +
                                    "or half as much\ndamage on a successful one.\nA shapechanger " +
                                    "makes its saving throw with\ndisadvantage. If it fails, it " +
                                    "also instantly reverts to its\noriginal form and can't assume " +
                                    "a different form until\nit leaves the spell's light.\nOn each " +
                                    "of your turns after you cast this spell, you\ncan use an " +
                                    "action to move the beam 60 feet in any\ndirection. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the damage\nincreases by 1d10 for each slot level " +
                                          "above 2nd. ")


class MoveEarth(spells.Spell):
    """
    Move Earth Spell
    SRD p. 167-168
    Generated
    """

    def __init__(self):
        super().__init__(name="Move Earth",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Transmutation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an iron blade and a small bag containing a mixture of soils—clay, loam, and sand",
                         duration="2 hours",
                         description="Choose an area of terrain no larger than 40 feet on a\nside " +
                                    "within range. You can reshape dirt, sand, or clay\nin the area " +
                                    "in any manner you choose for the\nduration. You can raise or " +
                                    "lower the area's elevation,\ncreate or fill in a trench, erect " +
                                    "or flatten a wall, or\nform a pillar. The extent of any such " +
                                    "changes can't\nexceed half the area's largest dimension. So, " +
                                    "if you\naffect a 40-foot square, you can create a pillar up " +
                                    "to\n20 feet high, raise or lower the square's elevation by\nup " +
                                    "to 20 feet, dig a trench up to 20 feet deep, and so\non. It " +
                                    "takes 10 minutes for these changes to\ncomplete.\nAt the end " +
                                    "of every 10 minutes you spend\nconcentrating on the spell, you " +
                                    "can choose a new\narea of terrain to affect.\nBecause the " +
                                    "terrain's transformation occurs\nslowly, creatures in the area " +
                                    "can't usually be trapped\nor injured by the ground's " +
                                    "movement.\nThis spell can't manipulate natural stone or " +
                                    "stone\nconstruction. Rocks and structures shift " +
                                    "to\naccommodate the new terrain. If the way you shape\nthe " +
                                    "terrain would make a structure unstable, it " +
                                    "might\ncollapse.\nSimilarly, this spell doesn't directly " +
                                    "affect plant\ngrowth. The moved earth carries any plants " +
                                    "along\nwith it. ",
                         at_higher_levels="")


class Nondetection(spells.Spell):
    """
    Nondetection Spell
    SRD p. 168
    Generated
    """

    def __init__(self):
        super().__init__(name="Nondetection",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes",
                         duration="8 hours",
                         description="For the duration, you hide a target that you touch\nfrom " +
                                    "divination magic. The target can be a willing\ncreature or a " +
                                    "place or an object no larger than 10\nfeet in any dimension. " +
                                    "The target can't be targeted\nby any divination magic or " +
                                    "perceived through\nmagical scrying sensors. ",
                         at_higher_levels="")


class PassWithoutTrace(spells.Spell):
    """
    Pass without Trace Spell
    SRD p. 168
    Generated
    """

    def __init__(self):
        super().__init__(name="Pass without Trace",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Abjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="ashes from a burned leaf of mistletoe and a sprig of spruce",
                         duration="1 hour",
                         description="A veil of shadows and silence radiates from you,\nmasking you " +
                                    "and your companions from detection.\nFor the duration, each " +
                                    "creature you choose within 30\nfeet of you (including you) has " +
                                    "a +10 bonus to\nDexterity (Stealth) checks and can't be " +
                                    "tracked\nexcept by magical means. A creature that " +
                                    "receives\nthis bonus leaves behind no tracks or other traces " +
                                    "of\nits passage. ",
                         at_higher_levels="")


class Passwall(spells.Spell):
    """
    Passwall Spell
    SRD p. 168
    Generated
    """

    def __init__(self):
        super().__init__(name="Passwall",
                         spell_lists=[SpellLists.ARCANE],
                         level=5,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of sesame seeds",
                         duration="1 hour",
                         description="A passage appears at a point of your choice that you\ncan see " +
                                    "on a wooden, plaster, or stone surface (such\nas a wall, a " +
                                    "ceiling, or a floor) within range, and lasts\nfor the " +
                                    "duration. You choose the opening's\ndimensions: up to 5 feet " +
                                    "wide, 8 feet tall, and 20 feet\ndeep. The passage creates no " +
                                    "instability in a\nstructure surrounding it.\nWhen the opening " +
                                    "disappears, any creatures or\nobjects still in the passage " +
                                    "created by the spell are\nsafely ejected to an unoccupied " +
                                    "space nearest to the\nsurface on which you cast the spell. ",
                         at_higher_levels="")


class PhantasmalKiller(spells.Spell):
    """
    Phantasmal Killer Spell
    SRD p. 168
    Generated
    """

    def __init__(self):
        super().__init__(name="Phantasmal Killer",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Illusion,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You tap into the nightmares of a creature you can\nsee within " +
                                    "range and create an illusory\nmanifestation of its deepest " +
                                    "fears, visible only to that\ncreature. The target must make a " +
                                    "Wisdom saving\nthrow. On a failed save, the target " +
                                    "becomes\nfrightened for the duration. At the end of each of " +
                                    "the\ntarget's turns before the spell ends, the target " +
                                    "must\nsucceed on a Wisdom saving throw or take 4d10\npsychic " +
                                    "damage. On a successful save, the spell ends. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 5th level or " +
                                          "higher, the damage increases\nby 1d10 for each slot level " +
                                          "above 4th. ")


class PhantomSteed(spells.Spell):
    """
    Phantom Steed Spell
    SRD p. 168-169
    Generated
    """

    def __init__(self):
        super().__init__(name="Phantom Steed",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=3,
                         school=SpellSchools.Illusion,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="A Large quasi-real, horselike creature appears on the\nground " +
                                    "in an unoccupied space of your choice within\nrange. You " +
                                    "decide the creature's appearance, but it is\nequipped with a " +
                                    "saddle, bit, and bridle. Any of the\nequipment created by the " +
                                    "spell vanishes in a puff of\nsmoke if it is carried more than " +
                                    "10 feet away from\nthe steed.\nFor the duration, you or a " +
                                    "creature you choose can\nride the steed. The creature uses the " +
                                    "statistics for a\nriding horse, except it has a speed of 100 " +
                                    "feet and\ncan travel 10 miles in an hour, or 13 miles at a " +
                                    "fast\npace. When the spell ends, the steed gradually " +
                                    "fades,\ngiving the rider 1 minute to dismount. The spell " +
                                    "ends\nif you use an action to dismiss it or if the steed " +
                                    "takes\nany damage. ",
                         at_higher_levels="")


class PlanarAlly(spells.Spell):
    """
    Planar Ally Spell
    SRD p. 169
    Generated
    """

    def __init__(self):
        super().__init__(name="Planar Ally",
                         spell_lists=[SpellLists.DIVINE],
                         level=6,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You beseech an otherworldly entity for aid. The\nbeing must be " +
                                    "known to you: a god, a primordial, a\ndemon prince, or some " +
                                    "other being of cosmic power.\nThat entity sends a celestial, " +
                                    "an elemental, or a fiend\nloyal to it to aid you, making the " +
                                    "creature appear in\nan unoccupied space within range. If you " +
                                    "know a\nspecific creature's name, you can speak that " +
                                    "name\nwhen you cast this spell to request that " +
                                    "creature,\nthough you might get a different creature " +
                                    "anyway\n(GM's choice).\nWhen the creature appears, it is under " +
                                    "no\ncompulsion to behave in any particular way. You can\nask " +
                                    "the creature to perform a service in exchange for\npayment, " +
                                    "but it isn't obliged to do so. The requested\ntask could range " +
                                    "from simple (fly us across the\nchasm, or help us fight a " +
                                    "battle) to complex (spy on\nour enemies, or protect us during " +
                                    "our foray into the\ndungeon). You must be able to communicate " +
                                    "with\nthe creature to bargain for its services.\nPayment can " +
                                    "take a variety of forms. A celestial\nmight require a sizable " +
                                    "donation of gold or magic\nitems to an allied temple, while a " +
                                    "fiend might\ndemand a living sacrifice or a gift of treasure. " +
                                    "Some\ncreatures might exchange their service for a " +
                                    "quest\nundertaken by you.\nAs a rule of thumb, a task that can " +
                                    "be measured in\nminutes requires a payment worth 100 gp " +
                                    "per\nminute. A task measured in hours requires 1,000 gp\nper " +
                                    "hour. And a task measured in days (up to 10\ndays) requires " +
                                    "10,000 gp per day. The GM can adjust\nthese payments based on " +
                                    "the circumstances under\nwhich you cast the spell. If the task " +
                                    "is aligned with\nthe creature's ethos, the payment might be " +
                                    "halved or\neven waived. Nonhazardous tasks typically " +
                                    "require\nonly half the suggested payment, while " +
                                    "especially\ndangerous tasks might require a greater " +
                                    "gift.\nCreatures rarely accept tasks that seem " +
                                    "suicidal.\nAfter the creature completes the task, or when " +
                                    "the\nagreed-upon duration of service expires, the\ncreature " +
                                    "returns to its home plane after reporting\nback to you, if " +
                                    "appropriate to the task and if possible.\nIf you are unable to " +
                                    "agree on a price for the\ncreature's service, the creature " +
                                    "immediately returns\nto its home plane.\nA creature enlisted " +
                                    "to join your group counts as a\nmember of it, receiving a full " +
                                    "share of experience\npoints awarded. ",
                         at_higher_levels="")


class PlanarBinding(spells.Spell):
    """
    Planar Binding Spell
    SRD p. 169
    Generated
    """

    def __init__(self):
        super().__init__(name="Planar Binding",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.Abjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a jewel worth at least 1,000 gp, which the spell consumes",
                         duration="24 hours",
                         description="With this spell, you attempt to bind a celestial, " +
                                    "an\nelemental, a fey, or a fiend to your service. " +
                                    "The\ncreature must be within range for the entire casting\nof " +
                                    "the spell. (Typically, the creature is first\nsummoned into " +
                                    "the center of an inverted magic\ncircle in order to keep it " +
                                    "trapped while this spell is\ncast.) At the completion of the " +
                                    "casting, the target\nmust make a Charisma saving throw. On a " +
                                    "failed save,\nit is bound to serve you for the duration. If " +
                                    "the\ncreature was summoned or created by another spell,\nthat " +
                                    "spell's duration is extended to match the\nduration of this " +
                                    "spell.\nA bound creature must follow your instructions to\nthe " +
                                    "best of its ability. You might command the\ncreature to " +
                                    "accompany you on an adventure, to\nguard a location, or to " +
                                    "deliver a message. The\ncreature obeys the letter of your " +
                                    "instructions, but if\nthe creature is hostile to you, it " +
                                    "strives to twist your\nwords to achieve its own objectives. If " +
                                    "the creature\ncarries out your instructions completely before " +
                                    "the\nspell ends, it travels to you to report this fact if " +
                                    "you\nare on the same plane of existence. If you are on " +
                                    "a\ndifferent plane of existence, it returns to the " +
                                    "place\nwhere you bound it and remains there until the " +
                                    "spell\nends. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of a higher " +
                                          "level, the duration increases to\n10 days with a 6th-level " +
                                          "slot, to 30 days with a 7thlevel slot, to 180 days with an " +
                                          "8th-level slot, and to a\nyear and a day with a 9th-level " +
                                          "spell slot. ")


class PlaneShift(spells.Spell):
    """
    Plane Shift Spell
    SRD p. 169-170
    Generated
    """

    def __init__(self):
        super().__init__(name="Plane Shift",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=7,
                         school=SpellSchools.Conjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a forked, metal rod worth at least 250 gp, attuned to a particular plane of existence",
                         duration="Instantaneous",
                         description="You and up to eight willing creatures who link hands\nin a " +
                                    "circle are transported to a different plane of\nexistence. You " +
                                    "can specify a target destination in\ngeneral terms, such as " +
                                    "the City of Brass on the\nElemental Plane of Fire or the " +
                                    "palace of Dispater on\nthe second level of the Nine Hells, and " +
                                    "you appear in\nor near that destination. If you are trying to " +
                                    "reach\nthe City of Brass, for example, you might arrive in " +
                                    "its\nStreet of Steel, before its Gate of Ashes, or looking " +
                                    "at\nthe city from across the Sea of Fire, at the " +
                                    "GM's\ndiscretion.\nAlternatively, if you know the sigil " +
                                    "sequence of a\nteleportation circle on another plane of " +
                                    "existence,\nthis spell can take you to that circle. If " +
                                    "the\nteleportation circle is too small to hold all " +
                                    "the\ncreatures you transported, they appear in the " +
                                    "closest\nunoccupied spaces next to the circle.\nYou can use " +
                                    "this spell to banish an unwilling\ncreature to another plane. " +
                                    "Choose a creature within\nyour reach and make a melee spell " +
                                    "attack against it.\nOn a hit, the creature must make a " +
                                    "Charisma saving\nthrow. If the creature fails this save, it is " +
                                    "transported\nto a random location on the plane of existence " +
                                    "you\nspecify. A creature so transported must find its own\nway " +
                                    "back to your current plane of existence. ",
                         at_higher_levels="")


class PlantGrowth(spells.Spell):
    """
    Plant Growth Spell
    SRD p. 170
    Generated
    """

    def __init__(self):
        super().__init__(name="Plant Growth",
                         spell_lists=[SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="This spell channels vitality into plants within a\nspecific " +
                                    "area. There are two possible uses for the\nspell, granting " +
                                    "either immediate or long-term\nbenefits.\nIf you cast this " +
                                    "spell using 1 action, choose a point\nwithin range. All normal " +
                                    "plants in a 100-foot radius\ncentered on that point become " +
                                    "thick and overgrown.\nA creature moving through the area must " +
                                    "spend 4\nfeet of movement for every 1 foot it moves.\nYou can " +
                                    "exclude one or more areas of any size\nwithin the spell's area " +
                                    "from being affected.\nIf you cast this spell over 8 hours, you " +
                                    "enrich the\nland. All plants in a half-mile radius centered on " +
                                    "a\npoint within range become enriched for 1 year. The\nplants " +
                                    "yield twice the normal amount of food when\nharvested. ",
                         at_higher_levels="")


class PoisonSpray(spells.Spell):
    """
    Poison Spray Spell
    SRD p. 170
    Generated
    """

    def __init__(self):
        super().__init__(name="Poison Spray",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.Conjuration,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You extend your hand toward a creature you can see\nwithin " +
                                    "range and project a puff of noxious gas from\nyour palm. The " +
                                    "creature must succeed on a\nConstitution saving throw or take " +
                                    "1d12 poison\ndamage.\nThis spell's damage increases by 1d12 " +
                                    "when you\nreach 5th level (2d12), 11th level (3d12), and " +
                                    "17th\nlevel (4d12). ",
                         at_higher_levels="")


class Polymorph(spells.Spell):
    """
    Polymorph Spell
    SRD p. 170-171
    Generated
    """

    def __init__(self):
        super().__init__(name="Polymorph",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a caterpillar cocoon",
                         duration="1 hour",
                         description="This spell transforms a creature that you can see " +
                                    "within\nrange into a new form. An unwilling creature " +
                                    "must\nmake a Wisdom saving throw to avoid the effect. " +
                                    "The\nspell has no effect on a shapechanger or a creature\nwith " +
                                    "0 hit points.\nThe transformation lasts for the duration, or " +
                                    "until\nthe target drops to 0 hit points or dies. The new " +
                                    "form\ncan be any beast whose challenge rating is equal to\nor " +
                                    "less than the target's (or the target's level, if it\ndoesn't " +
                                    "have a challenge rating). The target's game\nstatistics, " +
                                    "including mental ability scores, are\nreplaced by the " +
                                    "statistics of the chosen beast. It\nretains its alignment and " +
                                    "personality.\nThe target assumes the hit points of its new " +
                                    "form.\nWhen it reverts to its normal form, the " +
                                    "creature\nreturns to the number of hit points it had before " +
                                    "it\ntransformed. If it reverts as a result of dropping to " +
                                    "0\nhit points, any excess damage carries over to its\nnormal " +
                                    "form. As long as the excess damage doesn't\nreduce the " +
                                    "creature's normal form to 0 hit points, it\nisn't knocked " +
                                    "unconscious.\nThe creature is limited in the actions it " +
                                    "can\nperform by the nature of its new form, and it " +
                                    "can't\nspeak, cast spells, or take any other action " +
                                    "that\nrequires hands or speech.\nThe target's gear melds into " +
                                    "the new form. The\ncreature can't activate, use, wield, or " +
                                    "otherwise\nbenefit from any of its equipment. ",
                         at_higher_levels="")


class PowerWordKill(spells.Spell):
    """
    Power Word Kill Spell
    SRD p. 171
    Generated
    """

    def __init__(self):
        super().__init__(name="Power Word Kill",
                         spell_lists=[SpellLists.ARCANE],
                         level=9,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You utter a word of power that can compel one\ncreature you " +
                                    "can see within range to die instantly. If\nthe creature you " +
                                    "choose has 100 hit points or fewer,\nit dies. Otherwise, the " +
                                    "spell has no effect. ",
                         at_higher_levels="")


class PowerWordStun(spells.Spell):
    """
    Power Word Stun Spell
    SRD p. 171
    Generated
    """

    def __init__(self):
        super().__init__(name="Power Word Stun",
                         spell_lists=[SpellLists.ARCANE],
                         level=8,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You speak a word of power that can overwhelm the\nmind of one " +
                                    "creature you can see within range,\nleaving it dumbfounded. If " +
                                    "the target has 150 hit\npoints or fewer, it is stunned. " +
                                    "Otherwise, the spell\nhas no effect.\nThe stunned target must " +
                                    "make a Constitution\nsaving throw at the end of each of its " +
                                    "turns. On a\nsuccessful save, this stunning effect ends. ",
                         at_higher_levels="")


class PrayerOfHealing(spells.Spell):
    """
    Prayer of Healing Spell
    SRD p. 171
    Generated
    """

    def __init__(self):
        super().__init__(name="Prayer of Healing",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Up to six creatures of your choice that you can see\nwithin " +
                                    "range each regain hit points equal to 2d8 +\nyour spellcasting " +
                                    "ability modifier. This spell has no\neffect on undead or " +
                                    "constructs. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the healing increases\nby 1d8 for each slot level " +
                                          "above 2nd. ")


class Prestidigitation(spells.Spell):
    """
    Prestidigitation Spell
    SRD p. 171
    Generated
    """

    def __init__(self):
        super().__init__(name="Prestidigitation",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Transmutation,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Up to 1 hour",
                         description="This spell is a minor magical trick that novice\nspellcasters " +
                                    "use for practice. You create one of the\nfollowing magical " +
                                    "effects within range:\n• You create an instantaneous, harmless " +
                                    "sensory\neffect, such as a shower of sparks, a puff of " +
                                    "wind,\nfaint musical notes, or an odd odor.\n• You " +
                                    "instantaneously light or snuff out a candle, a\ntorch, or a " +
                                    "small campfire.\n• You instantaneously clean or soil an object " +
                                    "no\nlarger than 1 cubic foot.\n• You chill, warm, or flavor up " +
                                    "to 1 cubic foot of\nnonliving material for 1 hour.\n• You make " +
                                    "a color, a small mark, or a symbol\nappear on an object or a " +
                                    "surface for 1 hour.\n• You create a nonmagical trinket or an " +
                                    "illusory\nimage that can fit in your hand and that lasts " +
                                    "until\nthe end of your next turn.\nIf you cast this spell " +
                                    "multiple times, you can have up\nto three of its " +
                                    "non-instantaneous effects active at a\ntime, and you can " +
                                    "dismiss such an effect as an action. ",
                         at_higher_levels="")


class PrismaticSpray(spells.Spell):
    """
    Prismatic Spray Spell
    SRD p. 171-172
    Generated
    """

    def __init__(self):
        super().__init__(name="Prismatic Spray",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Evocation,
                         spell_range="Self (60-foot cone)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Eight multicolored rays of light flash from your hand.\nEach " +
                                    "ray is a different color and has a different\npower and " +
                                    "purpose. Each creature in a 60-foot cone\nmust make a " +
                                    "Dexterity saving throw. For each target,\nroll a d8 to " +
                                    "determine which color ray affects it.\n1. Red. The target " +
                                    "takes 10d6 fire damage on a\nfailed save, or half as much " +
                                    "damage on a successful\none.\n2. Orange. The target takes 10d6 " +
                                    "acid damage on\na failed save, or half as much damage on a " +
                                    "successful\none.\n3. Yellow. The target takes 10d6 lightning " +
                                    "damage\non a failed save, or half as much damage on " +
                                    "a\nsuccessful one.\n4. Green. The target takes 10d6 poison " +
                                    "damage on\na failed save, or half as much damage on a " +
                                    "successful\none.\n5. Blue. The target takes 10d6 cold damage " +
                                    "on a\nfailed save, or half as much damage on a " +
                                    "successful\none.\n6. Indigo. On a failed save, the target is " +
                                    "restrained.\nIt must then make a Constitution saving throw at " +
                                    "the\nend of each of its turns. If it successfully saves " +
                                    "three\ntimes, the spell ends. If it fails its save three " +
                                    "times, it\npermanently turns to stone and is subjected to " +
                                    "the\npetrified condition. The successes and failures " +
                                    "don't\nneed to be consecutive; keep track of both until " +
                                    "the\ntarget collects three of a kind.\n7. Violet. On a failed " +
                                    "save, the target is blinded. It\nmust then make a Wisdom " +
                                    "saving throw at the start\nof your next turn. A successful " +
                                    "save ends the\nblindness. If it fails that save, the creature " +
                                    "is\ntransported to another plane of existence of the " +
                                    "GM's\nchoosing and is no longer blinded. (Typically, " +
                                    "a\ncreature that is on a plane that isn't its home plane " +
                                    "is\nbanished home, while other creatures are usually\ncast " +
                                    "into the Astral or Ethereal planes.)\n8. Special. The target " +
                                    "is struck by two rays. Roll\ntwice more, rerolling any 8. ",
                         at_higher_levels="")


class PrismaticWall(spells.Spell):
    """
    Prismatic Wall Spell
    SRD p. 172
    Generated
    """

    def __init__(self):
        super().__init__(name="Prismatic Wall",
                         spell_lists=[SpellLists.ARCANE],
                         level=9,
                         school=SpellSchools.Abjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="A shimmering, multicolored plane of light forms a\nvertical " +
                                    "opaque wall—up to 90 feet long, 30 feet high,\nand 1 inch " +
                                    "thick—centered on a point you can see\nwithin range. " +
                                    "Alternatively, you can shape the wall\ninto a sphere up to 30 " +
                                    "feet in diameter centered on a\npoint you choose within range. " +
                                    "The wall remains in\nplace for the duration. If you position " +
                                    "the wall so that\nit passes through a space occupied by a " +
                                    "creature, the\nspell fails, and your action and the spell slot " +
                                    "are\nwasted.\nThe wall sheds bright light out to a range of " +
                                    "100\nfeet and dim light for an additional 100 feet. You " +
                                    "and\ncreatures you designate at the time you cast the " +
                                    "spell\ncan pass through and remain near the wall " +
                                    "without\nharm. If another creature that can see the " +
                                    "wall\nmoves to within 20 feet of it or starts its turn " +
                                    "there,\nthe creature must succeed on a Constitution " +
                                    "saving\nthrow or become blinded for 1 minute.\nThe wall " +
                                    "consists of seven layers, each with a\ndifferent color. When a " +
                                    "creature attempts to reach\ninto or pass through the wall, it " +
                                    "does so one layer at\na time through all the wall's layers. As " +
                                    "it passes or\nreaches through each layer, the creature must " +
                                    "make\na Dexterity saving throw or be affected by that\nlayer's " +
                                    "properties as described below.\nThe wall can be destroyed, " +
                                    "also one layer at a time,\nin order from red to violet, by " +
                                    "means specific to each\nlayer. Once a layer is destroyed, it " +
                                    "remains so for the\nduration of the spell. A rod of " +
                                    "cancellation destroys a\nprismatic wall, but an antimagic " +
                                    "field has no effect on\nit.\n1. Red. The creature takes 10d6 " +
                                    "fire damage on a\nfailed save, or half as much damage on a " +
                                    "successful\none. While this layer is in place, nonmagical " +
                                    "ranged\nattacks can't pass through the wall. The layer can " +
                                    "be\ndestroyed by dealing at least 25 cold damage to it.\n2. " +
                                    "Orange. The creature takes 10d6 acid damage\non a failed save, " +
                                    "or half as much damage on a\nsuccessful one. While this layer " +
                                    "is in place, magical\nranged attacks can't pass through the " +
                                    "wall. The layer\nis destroyed by a strong wind.\n3. Yellow. " +
                                    "The creature takes 10d6 lightning\ndamage on a failed save, or " +
                                    "half as much damage on\na successful one. This layer can be " +
                                    "destroyed by\ndealing at least 60 force damage to it.\n4. " +
                                    "Green. The creature takes 10d6 poison damage\non a failed " +
                                    "save, or half as much damage on a\nsuccessful one. A passwall " +
                                    "spell, or another spell of\nequal or greater level that can " +
                                    "open a portal on a\nsolid surface, destroys this layer.\n5. " +
                                    "Blue. The creature takes 10d6 cold damage on a\nfailed save, " +
                                    "or half as much damage on a successful\none. This layer can be " +
                                    "destroyed by dealing at least\n25 fire damage to it.\n6. " +
                                    "Indigo. On a failed save, the creature is\nrestrained. It must " +
                                    "then make a Constitution saving\nthrow at the end of each of " +
                                    "its turns. If it successfully\nsaves three times, the spell " +
                                    "ends. If it fails its save\nthree times, it permanently turns " +
                                    "to stone and is\nsubjected to the petrified condition. The " +
                                    "successes\nand failures don't need to be consecutive; keep " +
                                    "track\nof both until the creature collects three of a " +
                                    "kind.\nWhile this layer is in place, spells can't be " +
                                    "cast\nthrough the wall. The layer is destroyed by " +
                                    "bright\nlight shed by a daylight spell or a similar spell " +
                                    "of\nequal or higher level.\n7. Violet. On a failed save, the " +
                                    "creature is blinded.\nIt must then make a Wisdom saving throw " +
                                    "at the\nstart of your next turn. A successful save ends " +
                                    "the\nblindness. If it fails that save, the creature " +
                                    "is\ntransported to another plane of the GM's choosing\nand is " +
                                    "no longer blinded. (Typically, a creature that\nis on a plane " +
                                    "that isn't its home plane is banished\nhome, while other " +
                                    "creatures are usually cast into the\nAstral or Ethereal " +
                                    "planes.) This layer is destroyed by\na dispel magic spell or a " +
                                    "similar spell of equal or\nhigher level that can end spells " +
                                    "and magical effects. ",
                         at_higher_levels="")


class PrivateSanctum(spells.Spell):
    """
    Private Sanctum Spell
    SRD p. 172-173
    Generated
    """

    def __init__(self):
        super().__init__(name="Private Sanctum",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Abjuration,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a thin sheet of lead, a piece of opaque glass, a wad of cotton or cloth, and powdered chrysolite",
                         duration="24 hours",
                         description="You make an area within range magically secure.\nThe area is a " +
                                    "cube that can be as small as 5 feet to as\nlarge as 100 feet " +
                                    "on each side. The spell lasts for the\nduration or until you " +
                                    "use an action to dismiss it.\nWhen you cast the spell, you " +
                                    "decide what sort of\nsecurity the spell provides, choosing any " +
                                    "or all of the\nfollowing properties:\n• Sound can't pass " +
                                    "through the barrier at the edge of\nthe warded area.\n• The " +
                                    "barrier of the warded area appears dark and\nfoggy, preventing " +
                                    "vision (including darkvision)\nthrough it.\n• Sensors created " +
                                    "by divination spells can't appear\ninside the protected area " +
                                    "or pass through the\nbarrier at its perimeter.\n• Creatures in " +
                                    "the area can't be targeted by\ndivination spells.\n• Nothing " +
                                    "can teleport into or out of the warded\narea.\n• Planar travel " +
                                    "is blocked within the warded area.\nCasting this spell on the " +
                                    "same spot every day for a\nyear makes this effect permanent. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 5th level or " +
                                          "higher, you can increase the\nsize of the cube by 100 feet for " +
                                          "each slot level\nbeyond 4th. Thus you could protect a cube " +
                                          "that can\nbe up to 200 feet on one side by using a spell slot " +
                                          "of\n5th level. ")


class ProduceFlame(spells.Spell):
    """
    Produce Flame Spell
    SRD p. 173
    Generated
    """

    def __init__(self):
        super().__init__(name="Produce Flame",
                         spell_lists=[SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.Conjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="A flickering flame appears in your hand. The flame\nremains " +
                                    "there for the duration and harms neither\nyou nor your " +
                                    "equipment. The flame sheds bright\nlight in a 10-foot radius " +
                                    "and dim light for an\nadditional 10 feet. The spell ends if " +
                                    "you dismiss it as\nan action or if you cast it again.\nYou can " +
                                    "also attack with the flame, although doing\nso ends the spell. " +
                                    "When you cast this spell, or as an\naction on a later turn, " +
                                    "you can hurl the flame at a\ncreature within 30 feet of you. " +
                                    "Make a ranged spell\nattack. On a hit, the target takes 1d8 " +
                                    "fire damage.\nThis spell's damage increases by 1d8 when " +
                                    "you\nreach 5th level (2d8), 11th level (3d8), and 17th\nlevel " +
                                    "(4d8). ",
                         at_higher_levels="")


class ProgrammedIllusion(spells.Spell):
    """
    Programmed Illusion Spell
    SRD p. 173
    Generated
    """

    def __init__(self):
        super().__init__(name="Programmed Illusion",
                         spell_lists=[SpellLists.ARCANE],
                         level=6,
                         school=SpellSchools.Illusion,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fleece and jade dust worth at least 25 gp",
                         duration="Until dispelled",
                         description="You create an illusion of an object, a creature, or\nsome " +
                                    "other visible phenomenon within range that\nactivates when a " +
                                    "specific condition occurs. The\nillusion is imperceptible " +
                                    "until then. It must be no\nlarger than a 30-foot cube, and you " +
                                    "decide when you\ncast the spell how the illusion behaves and " +
                                    "what\nsounds it makes. This scripted performance can last\nup " +
                                    "to 5 minutes.\nWhen the condition you specify occurs, the " +
                                    "illusion\nsprings into existence and performs in the " +
                                    "manner\nyou described. Once the illusion finishes " +
                                    "performing,\nit disappears and remains dormant for 10 " +
                                    "minutes.\nAfter this time, the illusion can be activated " +
                                    "again.\nThe triggering condition can be as general or " +
                                    "as\ndetailed as you like, though it must be based on\nvisual " +
                                    "or audible conditions that occur within 30 feet\nof the area. " +
                                    "For example, you could create an illusion\nof yourself to " +
                                    "appear and warn off others who\nattempt to open a trapped " +
                                    "door, or you could set the\nillusion to trigger only when a " +
                                    "creature says the\ncorrect word or phrase.\nPhysical " +
                                    "interaction with the image reveals it to be\nan illusion, " +
                                    "because things can pass through it. A\ncreature that uses its " +
                                    "action to examine the image\ncan determine that it is an " +
                                    "illusion with a successful\nIntelligence (Investigation) check " +
                                    "against your spell\nsave DC. If a creature discerns the " +
                                    "illusion for what it\nis, the creature can see through the " +
                                    "image, and any\nnoise it makes sounds hollow to the creature. ",
                         at_higher_levels="")


class ProjectImage(spells.Spell):
    """
    Project Image Spell
    SRD p. 173-174
    Generated
    """

    def __init__(self):
        super().__init__(name="Project Image",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=7,
                         school=SpellSchools.Illusion,
                         spell_range="500 miles",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small replica of you made from materials worth at least 5 gp",
                         duration="1 day",
                         description="You create an illusory copy of yourself that lasts for\nthe " +
                                    "duration. The copy can appear at any location\nwithin range " +
                                    "that you have seen before, regardless of\nintervening " +
                                    "obstacles. The illusion looks and sounds\nlike you but is " +
                                    "intangible. If the illusion takes any\ndamage, it disappears, " +
                                    "and the spell ends.\nYou can use your action to move this " +
                                    "illusion up to\ntwice your speed, and make it gesture, speak, " +
                                    "and\nbehave in whatever way you choose. It mimics " +
                                    "your\nmannerisms perfectly.\nYou can see through its eyes and " +
                                    "hear through its\nears as if you were in its space. On your " +
                                    "turn as a\nbonus action, you can switch from using its senses " +
                                    "to\nusing your own, or back again. While you are using\nits " +
                                    "senses, you are blinded and deafened in regard to\nyour own " +
                                    "surroundings.\nPhysical interaction with the image reveals it " +
                                    "to be\nan illusion, because things can pass through it. " +
                                    "A\ncreature that uses its action to examine the image\ncan " +
                                    "determine that it is an illusion with a " +
                                    "successful\nIntelligence (Investigation) check against your " +
                                    "spell\nsave DC. If a creature discerns the illusion for what " +
                                    "it\nis, the creature can see through the image, and any\nnoise " +
                                    "it makes sounds hollow to the creature. ",
                         at_higher_levels="")


class ProtectionFromEnergy(spells.Spell):
    """
    Protection from Energy Spell
    SRD p. 174
    Generated
    """

    def __init__(self):
        super().__init__(name="Protection from Energy",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="For the duration, the willing creature you touch " +
                                    "has\nresistance to one damage type of your choice: " +
                                    "acid,\ncold, fire, lightning, or thunder. ",
                         at_higher_levels="")


class ProtectionFromEvilAndGood(spells.Spell):
    """
    Protection from Evil and Good Spell
    SRD p. 174
    Generated
    """

    def __init__(self):
        super().__init__(name="Protection from Evil and Good",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="holy water or powdered silver and iron, which the spell consumes",
                         duration="Concentration up to 10 minutes",
                         description="Until the spell ends, one willing creature you touch " +
                                    "is\nprotected against certain types of " +
                                    "creatures:\naberrations, celestials, elementals, fey, fiends, " +
                                    "and\nundead.\nThe protection grants several benefits. " +
                                    "Creatures\nof those types have disadvantage on attack " +
                                    "rolls\nagainst the target. The target also can't be " +
                                    "charmed,\nfrightened, or possessed by them. If the target " +
                                    "is\nalready charmed, frightened, or possessed by such " +
                                    "a\ncreature, the target has advantage on any new\nsaving throw " +
                                    "against the relevant effect. ",
                         at_higher_levels="")


class ProtectionFromPoison(spells.Spell):
    """
    Protection from Poison Spell
    SRD p. 174
    Generated
    """

    def __init__(self):
        super().__init__(name="Protection from Poison",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 hour",
                         description="You touch a creature. If it is poisoned, you neutralize\nthe " +
                                    "poison. If more than one poison afflicts the target,\nyou " +
                                    "neutralize one poison that you know is present,\nor you " +
                                    "neutralize one at random.\nFor the duration, the target has " +
                                    "advantage on\nsaving throws against being poisoned, and it " +
                                    "has\nresistance to poison damage. ",
                         at_higher_levels="")


class PurifyFoodAndDrink(spells.Spell):
    """
    Purify Food and Drink Spell
    SRD p. 174
    Generated
    """

    def __init__(self):
        super().__init__(name="Purify Food and Drink",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Transmutation,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="All nonmagical food and drink within a 5-foot-radius\nsphere " +
                                    "centered on a point of your choice within\nrange is purified " +
                                    "and rendered free of poison and\ndisease. ",
                         at_higher_levels="")


class RaiseDead(spells.Spell):
    """
    Raise Dead Spell
    SRD p. 174-175
    Generated
    """

    def __init__(self):
        super().__init__(name="Raise Dead",
                         spell_lists=[SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a diamond worth at least 500 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="You return a dead creature you touch to life,\nprovided that " +
                                    "it has been dead no longer than 10\ndays. If the creature's " +
                                    "soul is both willing and at\nliberty to rejoin the body, the " +
                                    "creature returns to life\nwith 1 hit point.\nThis spell also " +
                                    "neutralizes any poisons and cures\nnonmagical diseases that " +
                                    "affected the creature at the\ntime it died. This spell " +
                                    "doesn't, however, remove\nmagical diseases, curses, or similar " +
                                    "effects; if these\naren't first removed prior to casting the " +
                                    "spell, they\ntake effect when the creature returns to life. " +
                                    "The\nspell can't return an undead creature to life.\nThis " +
                                    "spell closes all mortal wounds, but it doesn't\nrestore " +
                                    "missing body parts. If the creature is lacking\nbody parts or " +
                                    "organs integral for its survival—its\nhead, for instance—the " +
                                    "spell automatically fails.\nComing back from the dead is an " +
                                    "ordeal. The\ntarget takes a −4 penalty to all attack rolls, " +
                                    "saving\nthrows, and ability checks. Every time the " +
                                    "target\nfinishes a long rest, the penalty is reduced by 1 " +
                                    "until\nit disappears. ",
                         at_higher_levels="")


class RayOfEnfeeblement(spells.Spell):
    """
    Ray of Enfeeblement Spell
    SRD p. 175
    Generated
    """

    def __init__(self):
        super().__init__(name="Ray of Enfeeblement",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Necromancy,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="A black beam of enervating energy springs from\nyour finger " +
                                    "toward a creature within range. Make a\nranged spell attack " +
                                    "against the target. On a hit, the\ntarget deals only half " +
                                    "damage with weapon attacks\nthat use Strength until the spell " +
                                    "ends.\nAt the end of each of the target's turns, it can " +
                                    "make\na Constitution saving throw against the spell. On " +
                                    "a\nsuccess, the spell ends. ",
                         at_higher_levels="")


class RayOfFrost(spells.Spell):
    """
    Ray of Frost Spell
    SRD p. 175
    Generated
    """

    def __init__(self):
        super().__init__(name="Ray of Frost",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="A frigid beam of blue-white light streaks toward a\ncreature " +
                                    "within range. Make a ranged spell attack\nagainst the target. " +
                                    "On a hit, it takes 1d8 cold damage,\nand its speed is reduced " +
                                    "by 10 feet until the start of\nyour next turn.\nThe spell's " +
                                    "damage increases by 1d8 when you\nreach 5th level (2d8), 11th " +
                                    "level (3d8), and 17th\nlevel (4d8). ",
                         at_higher_levels="")


class Regenerate(spells.Spell):
    """
    Regenerate Spell
    SRD p. 175
    Generated
    """

    def __init__(self):
        super().__init__(name="Regenerate",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=7,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a prayer wheel and holy water",
                         duration="1 hour",
                         description="You touch a creature and stimulate its natural\nhealing " +
                                    "ability. The target regains 4d8 + 15 hit points.\nFor the " +
                                    "duration of the spell, the target regains 1 hit\npoint at the " +
                                    "start of each of its turns (10 hit points\neach minute).\nThe " +
                                    "target's severed body members (fingers, legs,\ntails, and so " +
                                    "on), if any, are restored after 2 minutes.\nIf you have the " +
                                    "severed part and hold it to the stump,\nthe spell " +
                                    "instantaneously causes the limb to knit to\nthe stump. ",
                         at_higher_levels="")


class Reincarnate(spells.Spell):
    """
    Reincarnate Spell
    SRD p. 175
    Generated
    """

    def __init__(self):
        super().__init__(name="Reincarnate",
                         spell_lists=[SpellLists.PRIMAL],
                         level=5,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="rare oils and unguents worth at least 1,000 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="You touch a dead humanoid or a piece of a dead\nhumanoid. " +
                                    "Provided that the creature has been dead\nno longer than 10 " +
                                    "days, the spell forms a new adult\nbody for it and then calls " +
                                    "the soul to enter that body.\nIf the target's soul isn't free " +
                                    "or willing to do so, the\nspell fails.\nThe magic fashions a " +
                                    "new body for the creature to\ninhabit, which likely causes the " +
                                    "creature's race to\nchange. The GM rolls a d100 and consults " +
                                    "the\nfollowing table to determine what form the " +
                                    "creature\ntakes when restored to life, or the GM chooses " +
                                    "a\nform.\nd100 Race\n01–04 Dragonborn\n05–13 Dwarf, " +
                                    "hill\n14–21 Dwarf, mountain\n22–25 Elf, dark\n26–34 Elf, " +
                                    "high\n35–42 Elf, wood\n43–46 Gnome, forest\n47–52 Gnome, " +
                                    "rock\n53–56 Half-elf\n57–60 Half-orc\n61–68 Halfling, " +
                                    "lightfoot\n69–76 Halfling, stout\n77–96 Human\n97–00 " +
                                    "Tiefling\nThe reincarnated creature recalls its former " +
                                    "life\nand experiences. It retains the capabilities it had " +
                                    "in\nits original form, except it exchanges its original " +
                                    "race\nfor the new one and changes its racial " +
                                    "traits\naccordingly. ",
                         at_higher_levels="")


class RemoveCurse(spells.Spell):
    """
    Remove Curse Spell
    SRD p. 175-176
    Generated
    """

    def __init__(self):
        super().__init__(name="Remove Curse",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=3,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="At your touch, all curses affecting one creature or\nobject " +
                                    "end. If the object is a cursed magic item, its\ncurse remains, " +
                                    "but the spell breaks its owner's\nattunement to the object so " +
                                    "it can be removed or\ndiscarded. ",
                         at_higher_levels="")


class ResilientSphere(spells.Spell):
    """
    Resilient Sphere Spell
    SRD p. 176
    Generated
    """

    def __init__(self):
        super().__init__(name="Resilient Sphere",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Evocation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a hemispherical piece of clear crystal and a matching hemispherical piece of gum arabic",
                         duration="1 minute",
                         description="A sphere of shimmering force encloses a creature or\nobject of " +
                                    "Large size or smaller within range. An\nunwilling creature " +
                                    "must make a Dexterity saving\nthrow. On a failed save, the " +
                                    "creature is enclosed for\nthe duration.\nNothing—not physical " +
                                    "objects, energy, or other\nspell effects—can pass through the " +
                                    "barrier, in or out,\nthough a creature in the sphere can " +
                                    "breathe there.\nThe sphere is immune to all damage, and a " +
                                    "creature\nor object inside can't be damaged by attacks " +
                                    "or\neffects originating from outside, nor can a " +
                                    "creature\ninside the sphere damage anything outside it.\nThe " +
                                    "sphere is weightless and just large enough to\ncontain the " +
                                    "creature or object inside. An enclosed\ncreature can use its " +
                                    "action to push against the\nsphere's walls and thus roll the " +
                                    "sphere at up to half\nthe creature's speed. Similarly, the " +
                                    "globe can be\npicked up and moved by other creatures.\nA " +
                                    "disintegrate spell targeting the globe destroys it\nwithout " +
                                    "harming anything inside it. ",
                         at_higher_levels="")


class Resistance(spells.Spell):
    """
    Resistance Spell
    SRD p. 176
    Generated
    """

    def __init__(self):
        super().__init__(name="Resistance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         level=0,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a miniature cloak",
                         duration="1 minute",
                         description="You touch one willing creature. Once before the spell\nends, " +
                                    "the target can roll a d4 and add the number\nrolled to one " +
                                    "saving throw of its choice. It can roll the\ndie before or " +
                                    "after making the saving throw. The\nspell then ends. ",
                         at_higher_levels="")


class Resurrection(spells.Spell):
    """
    Resurrection Spell
    SRD p. 176
    Generated
    """

    def __init__(self):
        super().__init__(name="Resurrection",
                         spell_lists=[SpellLists.DIVINE],
                         level=7,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a diamond worth at least 1,000 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="You touch a dead creature that has been dead for no\nmore than " +
                                    "a century, that didn't die of old age, and\nthat isn't undead. " +
                                    "If its soul is free and willing, the\ntarget returns to life " +
                                    "with all its hit points.\nThis spell neutralizes any poisons " +
                                    "and cures\nnormal diseases afflicting the creature when it " +
                                    "died.\nIt doesn't, however, remove magical diseases, " +
                                    "curses,\nand the like; if such effects aren't removed prior " +
                                    "to\ncasting the spell, they afflict the target on its " +
                                    "return\nto life.\nThis spell closes all mortal wounds and " +
                                    "restores\nany missing body parts.\nComing back from the dead " +
                                    "is an ordeal. The\ntarget takes a −4 penalty to all attack " +
                                    "rolls, saving\nthrows, and ability checks. Every time the " +
                                    "target\nfinishes a long rest, the penalty is reduced by 1 " +
                                    "until\nit disappears.\nCasting this spell to restore life to a " +
                                    "creature that\nhas been dead for one year or longer taxes " +
                                    "you\ngreatly. Until you finish a long rest, you can't " +
                                    "cast\nspells again, and you have disadvantage on all " +
                                    "attack\nrolls, ability checks, and saving throws. ",
                         at_higher_levels="")


class ReverseGravity(spells.Spell):
    """
    Reverse Gravity Spell
    SRD p. 176
    Generated
    """

    def __init__(self):
        super().__init__(name="Reverse Gravity",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=7,
                         school=SpellSchools.Transmutation,
                         spell_range="100 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a lodestone and iron filings",
                         duration="1 minute",
                         description="This spell reverses gravity in a 50-foot-radius, 100-\nfoot " +
                                    "high cylinder centered on a point within range.\nAll creatures " +
                                    "and objects that aren't somehow\nanchored to the ground in the " +
                                    "area fall upward and\nreach the top of the area when you cast " +
                                    "this spell. A\ncreature can make a Dexterity saving throw to " +
                                    "grab\nonto a fixed object it can reach, thus avoiding the " +
                                    "fall.\nIf some solid object (such as a ceiling) " +
                                    "is\nencountered in this fall, falling objects and " +
                                    "creatures\nstrike it just as they would during a " +
                                    "normal\ndownward fall. If an object or creature reaches " +
                                    "the\ntop of the area without striking anything, it " +
                                    "remains\nthere, oscillating slightly, for the duration.\nAt " +
                                    "the end of the duration, affected objects and\ncreatures fall " +
                                    "back down. ",
                         at_higher_levels="")


class Revivify(spells.Spell):
    """
    Revivify Spell
    SRD p. 176-177
    Generated
    """

    def __init__(self):
        super().__init__(name="Revivify",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="diamonds worth 300 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="You touch a creature that has died within the last\nminute. " +
                                    "That creature returns to life with 1 hit point.\nThis spell " +
                                    "can't return to life a creature that has died\nof old age, nor " +
                                    "can it restore any missing body parts. ",
                         at_higher_levels="")


class RopeTrick(spells.Spell):
    """
    Rope Trick Spell
    SRD p. 177
    Generated
    """

    def __init__(self):
        super().__init__(name="Rope Trick",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="powdered corn extract and a twisted loop of parchment",
                         duration="1 hour",
                         description="You touch a length of rope that is up to 60 feet long.\nOne " +
                                    "end of the rope then rises into the air until the\nwhole rope " +
                                    "hangs perpendicular to the ground. At\nthe upper end of the " +
                                    "rope, an invisible entrance\nopens to an extradimensional " +
                                    "space that lasts until\nthe spell ends.\nThe extradimensional " +
                                    "space can be reached by\nclimbing to the top of the rope. The " +
                                    "space can hold as\nmany as eight Medium or smaller creatures. " +
                                    "The\nrope can be pulled into the space, making the " +
                                    "rope\ndisappear from view outside the space.\nAttacks and " +
                                    "spells can't cross through the entrance\ninto or out of the " +
                                    "extradimensional space, but those\ninside can see out of it as " +
                                    "if through a 3-foot-by-5-\nfoot window centered on the " +
                                    "rope.\nAnything inside the extradimensional space drops\nout " +
                                    "when the spell ends. ",
                         at_higher_levels="")


class SacredFlame(spells.Spell):
    """
    Sacred Flame Spell
    SRD p. 177
    Generated
    """

    def __init__(self):
        super().__init__(name="Sacred Flame",
                         spell_lists=[SpellLists.DIVINE],
                         level=0,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Flame-like radiance descends on a creature that you\ncan see " +
                                    "within range. The target must succeed on a\nDexterity saving " +
                                    "throw or take 1d8 radiant damage.\nThe target gains no benefit " +
                                    "from cover for this saving\nthrow.\nThe spell's damage " +
                                    "increases by 1d8 when you\nreach 5th level (2d8), 11th level " +
                                    "(3d8), and 17th\nlevel (4d8). ",
                         at_higher_levels="")


class Sanctuary(spells.Spell):
    """
    Sanctuary Spell
    SRD p. 177
    Generated
    """

    def __init__(self):
        super().__init__(name="Sanctuary",
                         spell_lists=[SpellLists.DIVINE],
                         level=1,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small silver mirror",
                         duration="1 minute",
                         description="You ward a creature within range against attack.\nUntil the " +
                                    "spell ends, any creature who targets the\nwarded creature with " +
                                    "an attack or a harmful spell\nmust first make a Wisdom saving " +
                                    "throw. On a failed\nsave, the creature must choose a new " +
                                    "target or lose\nthe attack or spell. This spell doesn't " +
                                    "protect the\nwarded creature from area effects, such as " +
                                    "the\nexplosion of a fireball.\nIf the warded creature makes an " +
                                    "attack or casts a\nspell that affects an enemy creature, this " +
                                    "spell ends. ",
                         at_higher_levels="")


class ScorchingRay(spells.Spell):
    """
    Scorching Ray Spell
    SRD p. 177
    Generated
    """

    def __init__(self):
        super().__init__(name="Scorching Ray",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You create three rays of fire and hurl them at targets\nwithin " +
                                    "range. You can hurl them at one target or\nseveral.\nMake a " +
                                    "ranged spell attack for each ray. On a hit,\nthe target takes " +
                                    "2d6 fire damage. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, you create one\nadditional ray for each slot level " +
                                          "above 2nd. ")


class Scrying(spells.Spell):
    """
    Scrying Spell
    SRD p. 177-178
    Generated
    """

    def __init__(self):
        super().__init__(name="Scrying",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a focus worth at least 1,000 gp, such as a crystal ball, a silver mirror, or a font filled with holy water",
                         duration="10 minutes",
                         description="You can see and hear a particular creature you\nchoose that is " +
                                    "on the same plane of existence as you.\nThe target must make a " +
                                    "Wisdom saving throw,\nwhich is modified by how well you know " +
                                    "the target\nand the sort of physical connection you have to " +
                                    "it. If\na target knows you're casting this spell, it can fail " +
                                    "the\nsaving throw voluntarily if it wants to be " +
                                    "observed.\nKnowledge Save Modifier\nSecondhand (you have heard " +
                                    "of the target) +5\nFirsthand (you have met the target) " +
                                    "+0\nFamiliar (you know the target well) −5\nConnection Save " +
                                    "Modifier\nLikeness or picture −2\nPossession or garment " +
                                    "−4\nBody part, lock of hair, bit of nail, or the like −10\nOn " +
                                    "a successful save, the target isn't affected, and\nyou can't " +
                                    "use this spell against it again for 24 hours.\nOn a failed " +
                                    "save, the spell creates an invisible\nsensor within 10 feet of " +
                                    "the target. You can see and\nhear through the sensor as if you " +
                                    "were there. The\nsensor moves with the target, remaining " +
                                    "within 10\nfeet of it for the duration. A creature that can " +
                                    "see\ninvisible objects sees the sensor as a luminous " +
                                    "orb\nabout the size of your fist.\nInstead of targeting a " +
                                    "creature, you can choose a\nlocation you have seen before as " +
                                    "the target of this\nspell. When you do, the sensor appears at " +
                                    "that\nlocation and doesn't move. ",
                         at_higher_levels="")


class SecretChest(spells.Spell):
    """
    Secret Chest Spell
    SRD p. 178
    Generated
    """

    def __init__(self):
        super().__init__(name="Secret Chest",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.Conjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an exquisite chest, 3 feet by 2 feet by 2 feet, constructed from rare materials worth at least 5,000 gp, and a Tiny replica made from the same materials worth at least 50 gp",
                         duration="Instantaneous",
                         description="You hide a chest, and all its contents, on the " +
                                    "Ethereal\nPlane. You must touch the chest and the " +
                                    "miniature\nreplica that serves as a material component for " +
                                    "the\nspell. The chest can contain up to 12 cubic feet " +
                                    "of\nnonliving material (3 feet by 2 feet by 2 feet).\nWhile " +
                                    "the chest remains on the Ethereal Plane, you\ncan use an " +
                                    "action and touch the replica to recall the\nchest. It appears " +
                                    "in an unoccupied space on the\nground within 5 feet of you. " +
                                    "You can send the chest\nback to the Ethereal Plane by using an " +
                                    "action and\ntouching both the chest and the replica.\nAfter 60 " +
                                    "days, there is a cumulative 5 percent\nchance per day that the " +
                                    "spell's effect ends. This effect\nends if you cast this spell " +
                                    "again, if the smaller replica\nchest is destroyed, or if you " +
                                    "choose to end the spell\nas an action. If the spell ends and " +
                                    "the larger chest is\non the Ethereal Plane, it is " +
                                    "irretrievably lost. ",
                         at_higher_levels="")


class SeeInvisibility(spells.Spell):
    """
    See Invisibility Spell
    SRD p. 178
    Generated
    """

    def __init__(self):
        super().__init__(name="See Invisibility",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of talc and a small sprinkling of powdered silver",
                         duration="1 hour",
                         description="For the duration, you see invisible creatures and\nobjects as " +
                                    "if they were visible, and you can see into\nthe Ethereal " +
                                    "Plane. Ethereal creatures and objects\nappear ghostly and " +
                                    "translucent. ",
                         at_higher_levels="")


class Seeming(spells.Spell):
    """
    Seeming Spell
    SRD p. 178
    Generated
    """

    def __init__(self):
        super().__init__(name="Seeming",
                         spell_lists=[SpellLists.ARCANE],
                         level=5,
                         school=SpellSchools.Illusion,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="8 hours",
                         description="This spell allows you to change the appearance of\nany number " +
                                    "of creatures that you can see within\nrange. You give each " +
                                    "target you choose a new,\nillusory appearance. An unwilling " +
                                    "target can make a\nCharisma saving throw, and if it succeeds, " +
                                    "it is\nunaffected by this spell.\nThe spell disguises physical " +
                                    "appearance as well as\nclothing, armor, weapons, and " +
                                    "equipment. You can\nmake each creature seem 1 foot shorter or " +
                                    "taller and\nappear thin, fat, or in between. You can't change " +
                                    "a\ntarget's body type, so you must choose a form that\nhas the " +
                                    "same basic arrangement of limbs. Otherwise,\nthe extent of the " +
                                    "illusion is up to you. The spell lasts\nfor the duration, " +
                                    "unless you use your action to\ndismiss it sooner.\nThe changes " +
                                    "wrought by this spell fail to hold up\nto physical inspection. " +
                                    "For example, if you use this\nspell to add a hat to a " +
                                    "creature's outfit, objects pass\nthrough the hat, and anyone " +
                                    "who touches it would\nfeel nothing or would feel the " +
                                    "creature's head and\nhair. If you use this spell to appear " +
                                    "thinner than you\nare, the hand of someone who reaches out to " +
                                    "touch\nyou would bump into you while it was seemingly\nstill " +
                                    "in midair.\nA creature can use its action to inspect a " +
                                    "target\nand make an Intelligence (Investigation) " +
                                    "check\nagainst your spell save DC. If it succeeds, it " +
                                    "becomes\naware that the target is disguised. ",
                         at_higher_levels="")


class Sending(spells.Spell):
    """
    Sending Spell
    SRD p. 178-179
    Generated
    """

    def __init__(self):
        super().__init__(name="Sending",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.Evocation,
                         spell_range="Unlimited",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a short piece of fine copper wire",
                         duration="1 round",
                         description="You send a short message of twenty-five words or\nless to a " +
                                    "creature with which you are familiar. The\ncreature hears the " +
                                    "message in its mind, recognizes\nyou as the sender if it knows " +
                                    "you, and can answer in\na like manner immediately. The spell " +
                                    "enables\ncreatures with Intelligence scores of at least 1 " +
                                    "to\nunderstand the meaning of your message.\nYou can send the " +
                                    "message across any distance and\neven to other planes of " +
                                    "existence, but if the target is\non a different plane than " +
                                    "you, there is a 5 percent\nchance that the message doesn't " +
                                    "arrive. ",
                         at_higher_levels="")


class Sequester(spells.Spell):
    """
    Sequester Spell
    SRD p. 179
    Generated
    """

    def __init__(self):
        super().__init__(name="Sequester",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a powder composed of diamond, emerald, ruby, and sapphire dust worth at least 5,000 gp, which the spell consumes",
                         duration="Until dispelled",
                         description="By means of this spell, a willing creature or an object\ncan " +
                                    "be hidden away, safe from detection for the\nduration. When " +
                                    "you cast the spell and touch the\ntarget, it becomes invisible " +
                                    "and can't be targeted by\ndivination spells or perceived " +
                                    "through scrying\nsensors created by divination spells.\nIf the " +
                                    "target is a creature, it falls into a state of\nsuspended " +
                                    "animation. Time ceases to flow for it, and\nit doesn't grow " +
                                    "older.\nYou can set a condition for the spell to end " +
                                    "early.\nThe condition can be anything you choose, but it\nmust " +
                                    "occur or be visible within 1 mile of the target.\nExamples " +
                                    "include “after 1,000 years” or “when the\ntarrasque awakens.” " +
                                    "This spell also ends if the target\ntakes any damage. ",
                         at_higher_levels="")


class Shapechange(spells.Spell):
    """
    Shapechange Spell
    SRD p. 179
    Generated
    """

    def __init__(self):
        super().__init__(name="Shapechange",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=9,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a jade circlet worth at least 1,500 gp, which you must place on your head before you cast the spell",
                         duration="1 hour",
                         description="You assume the form of a different creature for the\nduration. " +
                                    "The new form can be of any creature with\na challenge rating " +
                                    "equal to your level or lower. The\ncreature can't be a " +
                                    "construct or an undead, and you\nmust have seen the sort of " +
                                    "creature at least once.\nYou transform into an average example " +
                                    "of that\ncreature, one without any class levels or " +
                                    "the\nSpellcasting trait.\nYour game statistics are replaced by " +
                                    "the statistics\nof the chosen creature, though you retain " +
                                    "your\nalignment and Intelligence, Wisdom, and " +
                                    "Charisma\nscores. You also retain all of your skill and " +
                                    "saving\nthrow proficiencies, in addition to gaining those " +
                                    "of\nthe creature. If the creature has the same proficiency\nas " +
                                    "you and the bonus listed in its statistics is higher\nthan " +
                                    "yours, use the creature's bonus in place of\nyours. You can't " +
                                    "use any legendary actions or lair\nactions of the new " +
                                    "form.\nYou assume the hit points and Hit Dice of the " +
                                    "new\nform. When you revert to your normal form, you\nreturn to " +
                                    "the number of hit points you had before\nyou transformed. If " +
                                    "you revert as a result of\ndropping to 0 hit points, any " +
                                    "excess damage carries\nover to your normal form. As long as " +
                                    "the excess\ndamage doesn't reduce your normal form to 0 " +
                                    "hit\npoints, you aren't knocked unconscious.\nYou retain the " +
                                    "benefit of any features from your\nclass, race, or other " +
                                    "source and can use them,\nprovided that your new form is " +
                                    "physically capable of\ndoing so. You can't use any special " +
                                    "senses you have\n(for example, darkvision) unless your new " +
                                    "form also\nhas that sense. You can only speak if the creature " +
                                    "can\nnormally speak.\nWhen you transform, you choose whether " +
                                    "your\nequipment falls to the ground, merges into the " +
                                    "new\nform, or is worn by it. Worn equipment functions " +
                                    "as\nnormal. The GM determines whether it is practical\nfor the " +
                                    "new form to wear a piece of equipment,\nbased on the " +
                                    "creature's shape and size. Your\nequipment doesn't change " +
                                    "shape or size to match the\nnew form, and any equipment that " +
                                    "the new form\ncan't wear must either fall to the ground or " +
                                    "merge\ninto your new form. Equipment that merges has " +
                                    "no\neffect in that state.\nDuring this spell's duration, you " +
                                    "can use your\naction to assume a different form following the " +
                                    "same\nrestrictions and rules for the original form, with " +
                                    "one\nexception: if your new form has more hit points " +
                                    "than\nyour current one, your hit points remain at " +
                                    "their\ncurrent value. ",
                         at_higher_levels="")


class Shatter(spells.Spell):
    """
    Shatter Spell
    SRD p. 179-180
    Generated
    """

    def __init__(self):
        super().__init__(name="Shatter",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a chip of mica",
                         duration="Instantaneous",
                         description="A sudden loud ringing noise, painfully intense,\nerupts from a " +
                                    "point of your choice within range.\nEach creature in a " +
                                    "10-foot-radius sphere centered on\nthat point must make a " +
                                    "Constitution saving throw. A\ncreature takes 3d8 thunder " +
                                    "damage on a failed save,\nor half as much damage on a " +
                                    "successful one. A\ncreature made of inorganic material such as " +
                                    "stone,\ncrystal, or metal has disadvantage on this " +
                                    "saving\nthrow.\nA nonmagical object that isn't being worn " +
                                    "or\ncarried also takes the damage if it's in the " +
                                    "spell's\narea. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the damage\nincreases by 1d8 for each slot level above " +
                                          "2nd. ")


class Shield(spells.Spell):
    """
    Shield Spell
    SRD p. 180
    Generated
    """

    def __init__(self):
        super().__init__(name="Shield",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Abjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 round",
                         description="An invisible barrier of magical force appears and\nprotects " +
                                    "you. Until the start of your next turn, you\nhave a +5 bonus " +
                                    "to AC, including against the\ntriggering attack, and you take " +
                                    "no damage from\nmagic missile. ",
                         at_higher_levels="")


class ShieldOfFaith(spells.Spell):
    """
    Shield of Faith Spell
    SRD p. 180
    Generated
    """

    def __init__(self):
        super().__init__(name="Shield of Faith",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Abjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small parchment with a bit of holy text written on it",
                         duration="10 minutes",
                         description="A shimmering field appears and surrounds a\ncreature of your " +
                                    "choice within range, granting it a +2\nbonus to AC for the " +
                                    "duration. ",
                         at_higher_levels="")


class Shillelagh(spells.Spell):
    """
    Shillelagh Spell
    SRD p. 180
    Generated
    """

    def __init__(self):
        super().__init__(name="Shillelagh",
                         spell_lists=[SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="mistletoe, a shamrock leaf, and a club or quarterstaff",
                         duration="1 minute",
                         description="The wood of a club or quarterstaff you are holding is\nimbued " +
                                    "with nature's power. For the duration, you\ncan use your " +
                                    "spellcasting ability instead of Strength\nfor the attack and " +
                                    "damage rolls of melee attacks\nusing that weapon, and the " +
                                    "weapon's damage die\nbecomes a d8. The weapon also becomes " +
                                    "magical, if\nit isn't already. The spell ends if you cast it " +
                                    "again or if\nyou let go of the weapon. ",
                         at_higher_levels="")


class ShockingGrasp(spells.Spell):
    """
    Shocking Grasp Spell
    SRD p. 180
    Generated
    """

    def __init__(self):
        super().__init__(name="Shocking Grasp",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Evocation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Lightning springs from your hand to deliver a shock\nto a " +
                                    "creature you try to touch. Make a melee spell\nattack against " +
                                    "the target. You have advantage on the\nattack roll if the " +
                                    "target is wearing armor made of\nmetal. On a hit, the target " +
                                    "takes 1d8 lightning\ndamage, and it can't take reactions until " +
                                    "the start of\nits next turn.\nThe spell's damage increases by " +
                                    "1d8 when you\nreach 5th level (2d8), 11th level (3d8), and " +
                                    "17th\nlevel (4d8). ",
                         at_higher_levels="")


class Silence(spells.Spell):
    """
    Silence Spell
    SRD p. 180
    Generated
    """

    def __init__(self):
        super().__init__(name="Silence",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         ritual=True,
                         level=2,
                         school=SpellSchools.Illusion,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="For the duration, no sound can be created within or\npass " +
                                    "through a 20-foot-radius sphere centered on a\npoint you " +
                                    "choose within range. Any creature or\nobject entirely inside " +
                                    "the sphere is immune to\nthunder damage, and creatures are " +
                                    "deafened while\nentirely inside it. Casting a spell that " +
                                    "includes a\nverbal component is impossible there. ",
                         at_higher_levels="")


class SilentImage(spells.Spell):
    """
    Silent Image Spell
    SRD p. 180-181
    Generated
    """

    def __init__(self):
        super().__init__(name="Silent Image",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=1,
                         school=SpellSchools.Illusion,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fleece",
                         duration="10 minutes",
                         description="You create the image of an object, a creature, or\nsome other " +
                                    "visible phenomenon that is no larger\nthan a 15-foot cube. The " +
                                    "image appears at a spot\nwithin range and lasts for the " +
                                    "duration. The image is\npurely visual; it isn't accompanied by " +
                                    "sound, smell,\nor other sensory effects.\nYou can use your " +
                                    "action to cause the image to\nmove to any spot within range. " +
                                    "As the image changes\nlocation, you can alter its appearance " +
                                    "so that its\nmovements appear natural for the image. " +
                                    "For\nexample, if you create an image of a creature and\nmove " +
                                    "it, you can alter the image so that it appears to\nbe " +
                                    "walking.\nPhysical interaction with the image reveals it to " +
                                    "be\nan illusion, because things can pass through it. " +
                                    "A\ncreature that uses its action to examine the image\ncan " +
                                    "determine that it is an illusion with a " +
                                    "successful\nIntelligence (Investigation) check against your " +
                                    "spell\nsave DC. If a creature discerns the illusion for what " +
                                    "it\nis, the creature can see through the image. ",
                         at_higher_levels="")


class Simulacrum(spells.Spell):
    """
    Simulacrum Spell
    SRD p. 181
    Generated
    """

    def __init__(self):
        super().__init__(name="Simulacrum",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Illusion,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="snow or ice in quantities sufficient to made a life-size copy of the duplicated creature; some hair, fingernail clippings, or other piece of that creature's body placed inside the snow or ice; and powdered ruby worth 1,500 gp, sprinkled over the duplicate and consumed by the spell",
                         duration="Until dispelled",
                         description="You shape an illusory duplicate of one beast or\nhumanoid that " +
                                    "is within range for the entire casting\ntime of the spell. The " +
                                    "duplicate is a creature, partially\nreal and formed from ice " +
                                    "or snow, and it can take\nactions and otherwise be affected as " +
                                    "a normal\ncreature. It appears to be the same as the " +
                                    "original,\nbut it has half the creature's hit point maximum " +
                                    "and\nis formed without any equipment. Otherwise, the\nillusion " +
                                    "uses all the statistics of the creature it\nduplicates.\nThe " +
                                    "simulacrum is friendly to you and creatures\nyou designate. It " +
                                    "obeys your spoken commands,\nmoving and acting in accordance " +
                                    "with your wishes\nand acting on your turn in combat. The " +
                                    "simulacrum\nlacks the ability to learn or become more " +
                                    "powerful,\nso it never increases its level or other abilities, " +
                                    "nor\ncan it regain expended spell slots.\nIf the simulacrum is " +
                                    "damaged, you can repair it in\nan alchemical laboratory, using " +
                                    "rare herbs and\nminerals worth 100 gp per hit point it " +
                                    "regains. The\nsimulacrum lasts until it drops to 0 hit points, " +
                                    "at\nwhich point it reverts to snow and melts instantly.\nIf " +
                                    "you cast this spell again, any currently active\nduplicates " +
                                    "you created with this spell are instantly\ndestroyed. ",
                         at_higher_levels="")


class Sleep(spells.Spell):
    """
    Sleep Spell
    SRD p. 181
    Generated
    """

    def __init__(self):
        super().__init__(name="Sleep",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.Enchantment,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of fine sand, rose petals, or a cricket",
                         duration="1 minute",
                         description="This spell sends creatures into a magical slumber.\nRoll 5d8; " +
                                    "the total is how many hit points of\ncreatures this spell can " +
                                    "affect. Creatures within 20\nfeet of a point you choose within " +
                                    "range are affected\nin ascending order of their current hit " +
                                    "points\n(ignoring unconscious creatures).\nStarting with the " +
                                    "creature that has the lowest\ncurrent hit points, each " +
                                    "creature affected by this\nspell falls unconscious until the " +
                                    "spell ends, the\nsleeper takes damage, or someone uses an " +
                                    "action to\nshake or slap the sleeper awake. Subtract " +
                                    "each\ncreature's hit points from the total before moving " +
                                    "on\nto the creature with the next lowest hit points. " +
                                    "A\ncreature's hit points must be equal to or less than\nthe " +
                                    "remaining total for that creature to be affected.\nUndead and " +
                                    "creatures immune to being charmed\naren't affected by this " +
                                    "spell. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, roll an additional\n2d8 for each slot level above 1st. ")


class SleetStorm(spells.Spell):
    """
    Sleet Storm Spell
    SRD p. 181
    Generated
    """

    def __init__(self):
        super().__init__(name="Sleet Storm",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Conjuration,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of dust and a few drops of water",
                         duration="1 minute",
                         description="Until the spell ends, freezing rain and sleet fall in " +
                                    "a\n20-foot-tall cylinder with a 40-foot radius centered\non a " +
                                    "point you choose within range. The area is\nheavily obscured, " +
                                    "and exposed flames in the area are\ndoused.\nThe ground in the " +
                                    "area is covered with slick ice,\nmaking it difficult terrain. " +
                                    "When a creature enters\nthe spell's area for the first time on " +
                                    "a turn or starts\nits turn there, it must make a Dexterity " +
                                    "saving throw.\nOn a failed save, it falls prone.\nIf a " +
                                    "creature is concentrating in the spell's area,\nthe creature " +
                                    "must make a successful Constitution\nsaving throw against your " +
                                    "spell save DC or lose\nconcentration. ",
                         at_higher_levels="")


class Slow(spells.Spell):
    """
    Slow Spell
    SRD p. 181-182
    Generated
    """

    def __init__(self):
        super().__init__(name="Slow",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of molasses",
                         duration="1 minute",
                         description="You alter time around up to six creatures of your\nchoice in a " +
                                    "40-foot cube within range. Each target\nmust succeed on a " +
                                    "Wisdom saving throw or be\naffected by this spell for the " +
                                    "duration.\nAn affected target's speed is halved, it takes a " +
                                    "−2\npenalty to AC and Dexterity saving throws, and it\ncan't " +
                                    "use reactions. On its turn, it can use either an\naction or a " +
                                    "bonus action, not both. Regardless of the\ncreature's " +
                                    "abilities or magic items, it can't make\nmore than one melee " +
                                    "or ranged attack during its\nturn.\nIf the creature attempts " +
                                    "to cast a spell with a\ncasting time of 1 action, roll a d20. " +
                                    "On an 11 or\nhigher, the spell doesn't take effect until " +
                                    "the\ncreature's next turn, and the creature must use " +
                                    "its\naction on that turn to complete the spell. If it " +
                                    "can't,\nthe spell is wasted.\nA creature affected by this " +
                                    "spell makes another\nWisdom saving throw at the end of its " +
                                    "turn. On a\nsuccessful save, the effect ends for it. ",
                         at_higher_levels="")


class SpareTheDying(spells.Spell):
    """
    Spare the Dying Spell
    SRD p. 182
    Generated
    """

    def __init__(self):
        super().__init__(name="Spare the Dying",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You touch a living creature that has 0 hit points. " +
                                    "The\ncreature becomes stable. This spell has no effect " +
                                    "on\nundead or constructs. ",
                         at_higher_levels="")


class SpeakWithAnimals(spells.Spell):
    """
    Speak with Animals Spell
    SRD p. 182
    Generated
    """

    def __init__(self):
        super().__init__(name="Speak with Animals",
                         spell_lists=[SpellLists.PRIMAL],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You gain the ability to comprehend and verbally\ncommunicate " +
                                    "with beasts for the duration. The\nknowledge and awareness of " +
                                    "many beasts is limited\nby their intelligence, but at minimum, " +
                                    "beasts can\ngive you information about nearby locations " +
                                    "and\nmonsters, including whatever they can perceive or\nhave " +
                                    "perceived within the past day. You might be\nable to persuade " +
                                    "a beast to perform a small favor for\nyou, at the GM's " +
                                    "discretion. ",
                         at_higher_levels="")


class SpeakWithDead(spells.Spell):
    """
    Speak with Dead Spell
    SRD p. 182
    Generated
    """

    def __init__(self):
        super().__init__(name="Speak with Dead",
                         spell_lists=[SpellLists.DIVINE],
                         level=3,
                         school=SpellSchools.Necromancy,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="burning incense",
                         duration="10 minutes",
                         description="You grant the semblance of life and intelligence to a\ncorpse " +
                                    "of your choice within range, allowing it to\nanswer the " +
                                    "questions you pose. The corpse must still\nhave a mouth and " +
                                    "can't be undead. The spell fails if\nthe corpse was the target " +
                                    "of this spell within the last\n10 days.\nUntil the spell ends, " +
                                    "you can ask the corpse up to\nfive questions. The corpse knows " +
                                    "only what it knew\nin life, including the languages it knew. " +
                                    "Answers are\nusually brief, cryptic, or repetitive, and the " +
                                    "corpse is\nunder no compulsion to offer a truthful answer " +
                                    "if\nyou are hostile to it or it recognizes you as an " +
                                    "enemy.\nThis spell doesn't return the creature's soul to " +
                                    "its\nbody, only its animating spirit. Thus, the corpse " +
                                    "can't\nlearn new information, doesn't comprehend\nanything " +
                                    "that has happened since it died, and can't\nspeculate about " +
                                    "future events. ",
                         at_higher_levels="")


class SpeakWithPlants(spells.Spell):
    """
    Speak with Plants Spell
    SRD p. 182-183
    Generated
    """

    def __init__(self):
        super().__init__(name="Speak with Plants",
                         spell_lists=[SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="Self (30-foot radius)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You imbue plants within 30 feet of you with limited\nsentience " +
                                    "and animation, giving them the ability to\ncommunicate with " +
                                    "you and follow your simple\ncommands. You can question plants " +
                                    "about events in\nthe spell's area within the past day, " +
                                    "gaining\ninformation about creatures that have " +
                                    "passed,\nweather, and other circumstances.\nYou can also turn " +
                                    "difficult terrain caused by plant\ngrowth (such as thickets " +
                                    "and undergrowth) into\nordinary terrain that lasts for the " +
                                    "duration. Or you\ncan turn ordinary terrain where plants are " +
                                    "present\ninto difficult terrain that lasts for the " +
                                    "duration,\ncausing vines and branches to hinder pursuers, " +
                                    "for\nexample.\nPlants might be able to perform other tasks " +
                                    "on\nyour behalf, at the GM's discretion. The spell " +
                                    "doesn't\nenable plants to uproot themselves and move " +
                                    "about,\nbut they can freely move branches, tendrils, " +
                                    "and\nstalks.\nIf a plant creature is in the area, you " +
                                    "can\ncommunicate with it as if you shared a common\nlanguage, " +
                                    "but you gain no magical ability to influence\nit.\nThis spell " +
                                    "can cause the plants created by the\nentangle spell to release " +
                                    "a restrained creature. ",
                         at_higher_levels="")


class SpiderClimb(spells.Spell):
    """
    Spider Climb Spell
    SRD p. 183
    Generated
    """

    def __init__(self):
        super().__init__(name="Spider Climb",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of bitumen and a spider",
                         duration="1 hour",
                         description="Until the spell ends, one willing creature you touch\ngains " +
                                    "the ability to move up, down, and across\nvertical surfaces " +
                                    "and upside down along ceilings,\nwhile leaving its hands free. " +
                                    "The target also gains a\nclimbing speed equal to its walking " +
                                    "speed. ",
                         at_higher_levels="")


class SpikeGrowth(spells.Spell):
    """
    Spike Growth Spell
    SRD p. 183
    Generated
    """

    def __init__(self):
        super().__init__(name="Spike Growth",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Transmutation,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="seven sharp thorns or seven small twigs, each sharpened to a point",
                         duration="10 minutes",
                         description="The ground in a 20-foot radius centered on a point\nwithin " +
                                    "range twists and sprouts hard spikes and\nthorns. The area " +
                                    "becomes difficult terrain for the\nduration. When a creature " +
                                    "moves into or within the\narea, it takes 2d4 piercing damage " +
                                    "for every 5 feet it\ntravels.\nThe transformation of the " +
                                    "ground is camouflaged\nto look natural. Any creature that " +
                                    "can't see the area\nat the time the spell is cast must make a " +
                                    "Wisdom\n(Perception) check against your spell save DC " +
                                    "to\nrecognize the terrain as hazardous before entering it. ",
                         at_higher_levels="")


class SpiritGuardians(spells.Spell):
    """
    Spirit Guardians Spell
    SRD p. 183
    Generated
    """

    def __init__(self):
        super().__init__(name="Spirit Guardians",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Conjuration,
                         spell_range="Self (15-foot radius)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a holy symbol",
                         duration="10 minutes",
                         description="You call forth spirits to protect you. They flit around\nyou " +
                                    "to a distance of 15 feet for the duration. If you\nare good or " +
                                    "neutral, their spectral form appears\nangelic or fey (your " +
                                    "choice). If you are evil, they\nappear fiendish.\nWhen you " +
                                    "cast this spell, you can designate any\nnumber of creatures " +
                                    "you can see to be unaffected by\nit. An affected creature's " +
                                    "speed is halved in the area,\nand when the creature enters the " +
                                    "area for the first\ntime on a turn or starts its turn there, " +
                                    "it must make a\nWisdom saving throw. On a failed save, the " +
                                    "creature\ntakes 3d8 radiant damage (if you are good " +
                                    "or\nneutral) or 3d8 necrotic damage (if you are evil). On\na " +
                                    "successful save, the creature takes half as much\ndamage. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the damage increases\nby 1d8 for each slot level above " +
                                          "3rd. ")


class SpiritualWeapon(spells.Spell):
    """
    Spiritual Weapon Spell
    SRD p. 183
    Generated
    """

    def __init__(self):
        super().__init__(name="Spiritual Weapon",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You create a floating, spectral weapon within range\nthat " +
                                    "lasts for the duration or until you cast this spell\nagain. " +
                                    "When you cast the spell, you can make a melee\nspell attack " +
                                    "against a creature within 5 feet of the\nweapon. On a hit, the " +
                                    "target takes force damage\nequal to 1d8 + your spellcasting " +
                                    "ability modifier.\nAs a bonus action on your turn, you can " +
                                    "move the\nweapon up to 20 feet and repeat the attack against " +
                                    "a\ncreature within 5 feet of it.\nThe weapon can take whatever " +
                                    "form you choose.\nClerics of deities who are associated with " +
                                    "a\nparticular weapon (as St. Cuthbert is known for his\nmace " +
                                    "and Thor for his hammer) make this spell's\neffect resemble " +
                                    "that weapon. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 3rd level or " +
                                          "higher, the damage\nincreases by 1d8 for every two slot levels " +
                                          "above 2nd. ")


class StinkingCloud(spells.Spell):
    """
    Stinking Cloud Spell
    SRD p. 183-184
    Generated
    """

    def __init__(self):
        super().__init__(name="Stinking Cloud",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a rotten egg or several skunk cabbage leaves",
                         duration="1 minute",
                         description="You create a 20-foot-radius sphere of yellow,\nnauseating gas " +
                                    "centered on a point within range. The\ncloud spreads around " +
                                    "corners, and its area is heavily\nobscured. The cloud lingers " +
                                    "in the air for the\nduration.\nEach creature that is " +
                                    "completely within the cloud\nat the start of its turn must " +
                                    "make a Constitution\nsaving throw against poison. On a failed " +
                                    "save, the\ncreature spends its action that turn retching " +
                                    "and\nreeling. Creatures that don't need to breathe or " +
                                    "are\nimmune to poison automatically succeed on this\nsaving " +
                                    "throw.\nA moderate wind (at least 10 miles per " +
                                    "hour)\ndisperses the cloud after 4 rounds. A strong wind " +
                                    "(at\nleast 20 miles per hour) disperses it after 1 round. ",
                         at_higher_levels="")


class StoneShape(spells.Spell):
    """
    Stone Shape Spell
    SRD p. 184
    Generated
    """

    def __init__(self):
        super().__init__(name="Stone Shape",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=4,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="soft clay, which must be worked into roughly the desired shape of the stone object",
                         duration="Instantaneous",
                         description="You touch a stone object of Medium size or smaller\nor a " +
                                    "section of stone no more than 5 feet in any\ndimension and " +
                                    "form it into any shape that suits your\npurpose. So, for " +
                                    "example, you could shape a large\nrock into a weapon, idol, or " +
                                    "coffer, or make a small\npassage through a wall, as long as " +
                                    "the wall is less\nthan 5 feet thick. You could also shape a " +
                                    "stone door\nor its frame to seal the door shut. The object " +
                                    "you\ncreate can have up to two hinges and a latch, but\nfiner " +
                                    "mechanical detail isn't possible. ",
                         at_higher_levels="")


class Stoneskin(spells.Spell):
    """
    Stoneskin Spell
    SRD p. 184
    Generated
    """

    def __init__(self):
        super().__init__(name="Stoneskin",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="diamond dust worth 100 gp, which the spell consumes",
                         duration="1 hour",
                         description="This spell turns the flesh of a willing creature you\ntouch as " +
                                    "hard as stone. Until the spell ends, the\ntarget has " +
                                    "resistance to nonmagical bludgeoning,\npiercing, and slashing " +
                                    "damage. ",
                         at_higher_levels="")


class StormOfVengeance(spells.Spell):
    """
    Storm of Vengeance Spell
    SRD p. 184
    Generated
    """

    def __init__(self):
        super().__init__(name="Storm of Vengeance",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=9,
                         school=SpellSchools.Conjuration,
                         spell_range="Sight",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="A churning storm cloud forms, centered on a point\nyou can see " +
                                    "and spreading to a radius of 360 feet.\nLightning flashes in " +
                                    "the area, thunder booms, and\nstrong winds roar. Each creature " +
                                    "under the cloud\n(no more than 5,000 feet beneath the cloud) " +
                                    "when it\nappears must make a Constitution saving throw. On\na " +
                                    "failed save, a creature takes 2d6 thunder damage\nand becomes " +
                                    "deafened for 5 minutes.\nEach round you maintain concentration " +
                                    "on this\nspell, the storm produces additional effects on " +
                                    "your\nturn.\nRound 2. Acidic rain falls from the cloud. " +
                                    "Each\ncreature and object under the cloud takes 1d6 " +
                                    "acid\ndamage.\nRound 3. You call six bolts of lightning from " +
                                    "the\ncloud to strike six creatures or objects of your " +
                                    "choice\nbeneath the cloud. A given creature or object can't " +
                                    "be\nstruck by more than one bolt. A struck creature must\nmake " +
                                    "a Dexterity saving throw. The creature takes\n10d6 lightning " +
                                    "damage on a failed save, or half as\nmuch damage on a " +
                                    "successful one.\nRound 4. Hailstones rain down from the " +
                                    "cloud.\nEach creature under the cloud takes 2d6\nbludgeoning " +
                                    "damage.\nRound 5–10. Gusts and freezing rain assail the\narea " +
                                    "under the cloud. The area becomes difficult\nterrain and is " +
                                    "heavily obscured. Each creature there\ntakes 1d6 cold " +
                                    "damage.\nRanged weapon attacks in\nthe area are impossible. " +
                                    "The wind and rain count as\na severe distraction for the " +
                                    "purposes of maintaining\nconcentration on spells. Finally, " +
                                    "gusts of strong wind\n(ranging from 20 to 50 miles per " +
                                    "hour)\nautomatically disperse fog, mists, and " +
                                    "similar\nphenomena in the area, whether mundane or\nmagical. ",
                         at_higher_levels="")


class Suggestion(spells.Spell):
    """
    Suggestion Spell
    SRD p. 184-185
    Generated
    """

    def __init__(self):
        super().__init__(name="Suggestion",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list="a snake's tongue and either a bit of honeycomb or a drop of sweet oil",
                         duration="8 hours",
                         description="You suggest a course of activity (limited to a\nsentence or " +
                                    "two) and magically influence a creature\nyou can see within " +
                                    "range that can hear and\nunderstand you. Creatures that can't " +
                                    "be charmed are\nimmune to this effect. The suggestion must " +
                                    "be\nworded in such a manner as to make the course of\naction " +
                                    "sound reasonable. Asking the creature to stab\nitself, throw " +
                                    "itself onto a spear, immolate itself, or do\nsome other " +
                                    "obviously harmful act ends the spell.\nThe target must make a " +
                                    "Wisdom saving throw. On\na failed save, it pursues the course " +
                                    "of action you\ndescribed to the best of its ability. The " +
                                    "suggested\ncourse of action can continue for the entire " +
                                    "duration.\nIf the suggested activity can be completed in " +
                                    "a\nshorter time, the spell ends when the subject\nfinishes " +
                                    "what it was asked to do.\nYou can also specify conditions that " +
                                    "will trigger a\nspecial activity during the duration. For " +
                                    "example,\nyou might suggest that a knight give her warhorse " +
                                    "to\nthe first beggar she meets. If the condition isn't " +
                                    "met\nbefore the spell expires, the activity isn't " +
                                    "performed.\nIf you or any of your companions damage " +
                                    "the\ntarget, the spell ends. ",
                         at_higher_levels="")


class Sunbeam(spells.Spell):
    """
    Sunbeam Spell
    SRD p. 185
    Generated
    """

    def __init__(self):
        super().__init__(name="Sunbeam",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE, SpellLists.PRIMAL],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Evocation,
                         spell_range="Self (60-foot line)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a magnifying glass",
                         duration="1 minute",
                         description="A beam of brilliant light flashes out from your hand\nin a " +
                                    "5-foot-wide, 60-foot-long line. Each creature in\nthe line " +
                                    "must make a Constitution saving throw. On a\nfailed save, a " +
                                    "creature takes 6d8 radiant damage and\nis blinded until your " +
                                    "next turn. On a successful save,\nit takes half as much damage " +
                                    "and isn't blinded by\nthis spell. Undead and oozes have " +
                                    "disadvantage on\nthis saving throw.\nYou can create a new line " +
                                    "of radiance as your\naction on any turn until the spell " +
                                    "ends.\nFor the duration, a mote of brilliant radiance\nshines " +
                                    "in your hand. It sheds bright light in a 30-foot\nradius and " +
                                    "dim light for an additional 30 feet. This\nlight is sunlight. ",
                         at_higher_levels="")


class Sunburst(spells.Spell):
    """
    Sunburst Spell
    SRD p. 185
    Generated
    """

    def __init__(self):
        super().__init__(name="Sunburst",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=8,
                         school=SpellSchools.Evocation,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="fire and a piece of sunstone",
                         duration="Instantaneous",
                         description="Brilliant sunlight flashes in a 60-foot radius centered\non a " +
                                    "point you choose within range. Each creature in\nthat light " +
                                    "must make a Constitution saving throw. On\na failed save, a " +
                                    "creature takes 12d6 radiant damage\nand is blinded for 1 " +
                                    "minute. On a successful save, it\ntakes half as much damage " +
                                    "and isn't blinded by this\nspell. Undead and oozes have " +
                                    "disadvantage on this\nsaving throw.\nA creature blinded by " +
                                    "this spell makes another\nConstitution saving throw at the end " +
                                    "of each of its\nturns. On a successful save, it is no longer " +
                                    "blinded.\nThis spell dispels any darkness in its area that " +
                                    "was\ncreated by a spell. ",
                         at_higher_levels="")


class Symbol(spells.Spell):
    """
    Symbol Spell
    SRD p. 185-186
    Generated
    """

    def __init__(self):
        super().__init__(name="Symbol",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=7,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="mercury, phosphorus, and powdered diamond and opal with a total value of at least 1,000 gp, which the spell consumes",
                         duration="Until dispelled or triggered",
                         description="When you cast this spell, you inscribe a harmful\nglyph either " +
                                    "on a surface (such as a section of floor, a\nwall, or a table) " +
                                    "or within an object that can be\nclosed to conceal the glyph " +
                                    "(such as a book, a scroll,\nor a treasure chest). If you " +
                                    "choose a surface, the\nglyph can cover an area of the surface " +
                                    "no larger than\n10 feet in diameter. If you choose an object, " +
                                    "that\nobject must remain in its place; if the object is\nmoved " +
                                    "more than 10 feet from where you cast this\nspell, the glyph " +
                                    "is broken, and the spell ends without\nbeing triggered.\nThe " +
                                    "glyph is nearly invisible, requiring an\nIntelligence " +
                                    "(Investigation) check against your spell\nsave DC to find " +
                                    "it.\nYou decide what triggers the glyph when you cast\nthe " +
                                    "spell. For glyphs inscribed on a surface, the most\ntypical " +
                                    "triggers include touching or stepping on the\nglyph, removing " +
                                    "another object covering it,\napproaching within a certain " +
                                    "distance of it, or\nmanipulating the object that holds it. For " +
                                    "glyphs\ninscribed within an object, the most common\ntriggers " +
                                    "are opening the object, approaching within a\ncertain distance " +
                                    "of it, or seeing or reading the glyph.\nYou can further refine " +
                                    "the trigger so the spell is\nactivated only under certain " +
                                    "circumstances or\naccording to a creature's physical " +
                                    "characteristics\n(such as height or weight), or physical kind " +
                                    "(for\nexample, the ward could be set to affect hags " +
                                    "or\nshapechangers). You can also specify creatures that\ndon't " +
                                    "trigger the glyph, such as those who say a\ncertain " +
                                    "password.\nWhen you inscribe the glyph, choose one of " +
                                    "the\noptions below for its effect. Once triggered, the " +
                                    "glyph\nglows, filling a 60-foot-radius sphere with dim " +
                                    "light\nfor 10 minutes, after which time the spell ends. " +
                                    "Each\ncreature in the sphere when the glyph activates " +
                                    "is\ntargeted by its effect, as is a creature that enters " +
                                    "the\nsphere for the first time on a turn or ends its " +
                                    "turn\nthere.\nDeath. Each target must make a " +
                                    "Constitution\nsaving throw, taking 10d10 necrotic damage on " +
                                    "a\nfailed save, or half as much damage on a " +
                                    "successful\nsave.\nDiscord. Each target must make a " +
                                    "Constitution\nsaving throw. On a failed save, a target bickers " +
                                    "and\nargues with other creatures for 1 minute. During " +
                                    "this\ntime, it is incapable of meaningful communication\nand " +
                                    "has disadvantage on attack rolls and ability\nchecks.\nFear. " +
                                    "Each target must make a Wisdom saving\nthrow and becomes " +
                                    "frightened for 1 minute on a\nfailed save. While frightened, " +
                                    "the target drops\nwhatever it is holding and must move at " +
                                    "least 30 feet\naway from the glyph on each of its turns, if " +
                                    "able.\nHopelessness. Each target must make a Charisma\nsaving " +
                                    "throw. On a failed save, the target is\noverwhelmed with " +
                                    "despair for 1 minute. During this\ntime, it can't attack or " +
                                    "target any creature with\nharmful abilities, spells, or other " +
                                    "magical effects.\nInsanity. Each target must make an " +
                                    "Intelligence\nsaving throw. On a failed save, the target is " +
                                    "driven\ninsane for 1 minute. An insane creature can't " +
                                    "take\nactions, can't understand what other creatures " +
                                    "say,\ncan't read, and speaks only in gibberish. The " +
                                    "GM\ncontrols its movement, which is erratic.\nPain. Each " +
                                    "target must make a Constitution saving\nthrow and becomes " +
                                    "incapacitated with excruciating\npain for 1 minute on a failed " +
                                    "save.\nSleep. Each target must make a Wisdom saving\nthrow and " +
                                    "falls unconscious for 10 minutes on a\nfailed save. A creature " +
                                    "awakens if it takes damage or\nif someone uses an action to " +
                                    "shake or slap it awake.\nStunning. Each target must make a " +
                                    "Wisdom\nsaving throw and becomes stunned for 1 minute on\na " +
                                    "failed save. ",
                         at_higher_levels="")


class Telekinesis(spells.Spell):
    """
    Telekinesis Spell
    SRD p. 186
    Generated
    """

    def __init__(self):
        super().__init__(name="Telekinesis",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Transmutation,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You gain the ability to move or manipulate creatures\nor " +
                                    "objects by thought. When you cast the spell, and\nas your " +
                                    "action each round for the duration, you can\nexert your will " +
                                    "on one creature or object that you\ncan see within range, " +
                                    "causing the appropriate effect\nbelow. You can affect the same " +
                                    "target round after\nround, or choose a new one at any time. If " +
                                    "you switch\ntargets, the prior target is no longer affected by " +
                                    "the\nspell.\nCreature. You can try to move a Huge or " +
                                    "smaller\ncreature. Make an ability check with " +
                                    "your\nspellcasting ability contested by the " +
                                    "creature's\nStrength check. If you win the contest, you move " +
                                    "the\ncreature up to 30 feet in any direction, " +
                                    "including\nupward but not beyond the range of this spell. " +
                                    "Until\nthe end of your next turn, the creature is " +
                                    "restrained\nin your telekinetic grip. A creature lifted upward " +
                                    "is\nsuspended in mid-air.\nOn subsequent rounds, you can use " +
                                    "your action to\nattempt to maintain your telekinetic grip on " +
                                    "the\ncreature by repeating the contest.\nObject. You can try " +
                                    "to move an object that weighs\nup to 1,000 pounds. If the " +
                                    "object isn't being worn or\ncarried, you automatically move it " +
                                    "up to 30 feet in\nany direction, but not beyond the range of " +
                                    "this spell.\nIf the object is worn or carried by a creature, " +
                                    "you\nmust make an ability check with your " +
                                    "spellcasting\nability contested by that creature's Strength " +
                                    "check. If\nyou succeed, you pull the object away from " +
                                    "that\ncreature and can move it up to 30 feet in any\ndirection " +
                                    "but not beyond the range of this spell.\nYou can exert fine " +
                                    "control on objects with your\ntelekinetic grip, such as " +
                                    "manipulating a simple tool,\nopening a door or a container, " +
                                    "stowing or retrieving\nan item from an open container, or " +
                                    "pouring the\ncontents from a vial. ",
                         at_higher_levels="")


class TelepathicBond(spells.Spell):
    """
    Telepathic Bond Spell
    SRD p. 186
    Generated
    """

    def __init__(self):
        super().__init__(name="Telepathic Bond",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=5,
                         school=SpellSchools.Divination,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="pieces of eggshell from two different kinds of creatures",
                         duration="1 hour",
                         description="You forge a telepathic link among up to eight " +
                                    "willing\ncreatures of your choice within range, " +
                                    "psychically\nlinking each creature to all the others for " +
                                    "the\nduration. Creatures with Intelligence scores of 2 " +
                                    "or\nless aren't affected by this spell.\nUntil the spell ends, " +
                                    "the targets can communicate\ntelepathically through the bond " +
                                    "whether or not they\nhave a common language. The communication " +
                                    "is\npossible over any distance, though it can't extend " +
                                    "to\nother planes of existence. ",
                         at_higher_levels="")


class Teleport(spells.Spell):
    """
    Teleport Spell
    SRD p. 186-187
    Generated
    """

    def __init__(self):
        super().__init__(name="Teleport",
                         spell_lists=[SpellLists.ARCANE],
                         level=7,
                         school=SpellSchools.Conjuration,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="This spell instantly transports you and up to eight\nwilling " +
                                    "creatures of your choice that you can see\nwithin range, or a " +
                                    "single object that you can see\nwithin range, to a destination " +
                                    "you select. If you\ntarget an object, it must be able to fit " +
                                    "entirely inside\na 10-foot cube, and it can't be held or " +
                                    "carried by an\nunwilling creature.\nThe destination you choose " +
                                    "must be known to you,\nand it must be on the same plane of " +
                                    "existence as you.\nYour familiarity with the destination " +
                                    "determines\nwhether you arrive there successfully. The GM " +
                                    "rolls\nd100 and consults the table.\nFamiliarity " +
                                    "Mishap\nSimilar\nArea\nOff\nTarget\nOn\nTarget\nPermanent\ncircle\n— " +
                                    "— — 01–100\nAssociated\nobject\n— — — 01–100\nVery familiar " +
                                    "01–05 06–13 14–24 25–100\nSeen casually 01–33 34–43 44–53 " +
                                    "54–100\nViewed once 01–43 44–53 54–73 74–100\nDescription " +
                                    "01–43 44–53 54–73 74–100\nFalse\ndestination\n01–50 51–100 — " +
                                    "—\nFamiliarity. “Permanent circle” means a\npermanent " +
                                    "teleportation circle whose sigil sequence\nyou know. " +
                                    "“Associated object” means that you\npossess an object taken " +
                                    "from the desired destination\nwithin the last six months, such " +
                                    "as a book from a\nwizard's library, bed linen from a royal " +
                                    "suite, or a\nchunk of marble from a lich's secret tomb.\n“Very " +
                                    "familiar” is a place you have been very often,\na place you " +
                                    "have carefully studied, or a place you can\nsee when you cast " +
                                    "the spell. “Seen casually” is\nsomeplace you have seen more " +
                                    "than once but with\nwhich you aren't very familiar. “Viewed " +
                                    "once” is a\nplace you have seen once, possibly using " +
                                    "magic.\n“Description” is a place whose location " +
                                    "and\nappearance you know through someone else's\ndescription, " +
                                    "perhaps from a map.\n“False destination” is a place that " +
                                    "doesn't exist.\nPerhaps you tried to scry an enemy's sanctum " +
                                    "but\ninstead viewed an illusion, or you are attempting " +
                                    "to\nteleport to a familiar location that no longer exists.\nOn " +
                                    "Target. You and your group (or the target\nobject) appear " +
                                    "where you want to.\nOff Target. You and your group (or the " +
                                    "target\nobject) appear a random distance away from " +
                                    "the\ndestination in a random direction. Distance off " +
                                    "target\nis 1d10 × 1d10 percent of the distance that was to " +
                                    "be\ntraveled. For example, if you tried to travel 120\nmiles, " +
                                    "landed off target, and rolled a 5 and 3 on the\ntwo d10s, then " +
                                    "you would be off target by 15 percent,\nor 18 miles. The GM " +
                                    "determines the direction off\ntarget randomly by rolling a d8 " +
                                    "and designating 1 as\nnorth, 2 as northeast, 3 as east, and so " +
                                    "on around the\npoints of the compass. If you were teleporting " +
                                    "to a\ncoastal city and wound up 18 miles out at sea, " +
                                    "you\ncould be in trouble.\nSimilar Area. You and your group " +
                                    "(or the target\nobject) wind up in a different area that's " +
                                    "visually or\nthematically similar to the target area. If you " +
                                    "are\nheading for your home laboratory, for example, you\nmight " +
                                    "wind up in another wizard's laboratory or in\nan alchemical " +
                                    "supply shop that has many of the same\ntools and implements as " +
                                    "your laboratory. Generally,\nyou appear in the closest similar " +
                                    "place, but since the\nspell has no range limit, you could " +
                                    "conceivably wind\nup anywhere on the plane.\nMishap. The " +
                                    "spell's unpredictable magic results in\na difficult journey. " +
                                    "Each teleporting creature (or the\ntarget object) takes 3d10 " +
                                    "force damage, and the GM\nrerolls on the table to see where " +
                                    "you wind up\n(multiple mishaps can occur, dealing damage " +
                                    "each\ntime). ",
                         at_higher_levels="")


class TeleportationCircle(spells.Spell):
    """
    Teleportation Circle Spell
    SRD p. 187-188
    Generated
    """

    def __init__(self):
        super().__init__(name="Teleportation Circle",
                         spell_lists=[SpellLists.ARCANE],
                         level=5,
                         school=SpellSchools.Conjuration,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list="rare chalks and inks infused with precious gems with 50 gp, which the spell consumes",
                         duration="1 round",
                         description="As you cast the spell, you draw a 10-foot-diameter\ncircle on " +
                                    "the ground inscribed with sigils that link\nyour location to a " +
                                    "permanent teleportation circle of\nyour choice whose sigil " +
                                    "sequence you know and that\nis on the same plane of existence " +
                                    "as you. A\nshimmering portal opens within the circle you " +
                                    "drew\nand remains open until the end of your next turn.\nAny " +
                                    "creature that enters the portal instantly appears\nwithin 5 " +
                                    "feet of the destination circle or in the\nnearest unoccupied " +
                                    "space if that space is occupied.\nMany major temples, guilds, " +
                                    "and other important\nplaces have permanent teleportation " +
                                    "circles\ninscribed somewhere within their confines. Each\nsuch " +
                                    "circle includes a unique sigil sequence—a\nstring of magical " +
                                    "runes arranged in a particular\npattern. When you first gain " +
                                    "the ability to cast this\nspell, you learn the sigil sequences " +
                                    "for two\ndestinations on the Material Plane, determined " +
                                    "by\nthe GM. You can learn additional sigil sequences\nduring " +
                                    "your adventures. You can commit a new sigil\nsequence to " +
                                    "memory after studying it for 1 minute.\nYou can create a " +
                                    "permanent teleportation circle by\ncasting this spell in the " +
                                    "same location every day for\none year. You need not use the " +
                                    "circle to teleport\nwhen you cast the spell in this way. ",
                         at_higher_levels="")


class Thaumaturgy(spells.Spell):
    """
    Thaumaturgy Spell
    SRD p. 188
    Generated
    """

    def __init__(self):
        super().__init__(name="Thaumaturgy",
                         spell_lists=[SpellLists.DIVINE],
                         level=0,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Up to 1 minute",
                         description="You manifest a minor wonder, a sign of supernatural\npower, " +
                                    "within range. You create one of the following\nmagical effects " +
                                    "within range:\n• Your voice booms up to three times as loud " +
                                    "as\nnormal for 1 minute.\n• You cause flames to flicker, " +
                                    "brighten, dim, or\nchange color for 1 minute.\n• You cause " +
                                    "harmless tremors in the ground for 1\nminute.\n• You create an " +
                                    "instantaneous sound that originates\nfrom a point of your " +
                                    "choice within range, such as a\nrumble of thunder, the cry of " +
                                    "a raven, or ominous\nwhispers.\n• You instantaneously cause an " +
                                    "unlocked door or\nwindow to fly open or slam shut.\n• You " +
                                    "alter the appearance of your eyes for 1 minute.\nIf you cast " +
                                    "this spell multiple times, you can have up\nto three of its " +
                                    "1-minute effects active at a time, and\nyou can dismiss such " +
                                    "an effect as an action. ",
                         at_higher_levels="")


class Thunderwave(spells.Spell):
    """
    Thunderwave Spell
    SRD p. 188
    Generated
    """

    def __init__(self):
        super().__init__(name="Thunderwave",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.Evocation,
                         spell_range="Self (15-foot cube)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="A wave of thunderous force sweeps out from you.\nEach creature " +
                                    "in a 15-foot cube originating from you\nmust make a " +
                                    "Constitution saving throw. On a failed\nsave, a creature takes " +
                                    "2d8 thunder damage and is\npushed 10 feet away from you. On a " +
                                    "successful save,\nthe creature takes half as much damage and " +
                                    "isn't\npushed.\nIn addition, unsecured objects that are " +
                                    "completely\nwithin the area of effect are automatically pushed " +
                                    "10\nfeet away from you by the spell's effect, and the " +
                                    "spell\nemits a thunderous boom audible out to 300 feet. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 2nd level or " +
                                          "higher, the damage\nincreases by 1d8 for each slot level above " +
                                          "1st. ")


class TimeStop(spells.Spell):
    """
    Time Stop Spell
    SRD p. 188
    Generated
    """

    def __init__(self):
        super().__init__(name="Time Stop",
                         spell_lists=[SpellLists.ARCANE],
                         level=9,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You briefly stop the flow of time for everyone but\nyourself. " +
                                    "No time passes for other creatures, while\nyou take 1d4 + 1 " +
                                    "turns in a row, during which you\ncan use actions and move as " +
                                    "normal.\nThis spell ends if one of the actions you use " +
                                    "during\nthis period, or any effects that you create during " +
                                    "this\nperiod, affects a creature other than you or an " +
                                    "object\nbeing worn or carried by someone other than you. " +
                                    "In\naddition, the spell ends if you move to a place more\nthan " +
                                    "1,000 feet from the location where you cast it. ",
                         at_higher_levels="")


class TinyHut(spells.Spell):
    """
    Tiny Hut Spell
    SRD p. 188
    Generated
    """

    def __init__(self):
        super().__init__(name="Tiny Hut",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=3,
                         school=SpellSchools.Evocation,
                         spell_range="Self (10-foot-radius hemisphere)",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small crystal bead",
                         duration="8 hours",
                         description="A 10-foot-radius immobile dome of force springs\ninto " +
                                    "existence around and above you and remains\nstationary for the " +
                                    "duration. The spell ends if you leave\nits area.\nNine " +
                                    "creatures of Medium size or smaller can fit\ninside the dome " +
                                    "with you. The spell fails if its area\nincludes a larger " +
                                    "creature or more than nine\ncreatures. Creatures and objects " +
                                    "within the dome\nwhen you cast this spell can move through it " +
                                    "freely.\nAll other creatures and objects are barred " +
                                    "from\npassing through it. Spells and other magical " +
                                    "effects\ncan't extend through the dome or be cast through " +
                                    "it.\nThe atmosphere inside the space is comfortable and\ndry, " +
                                    "regardless of the weather outside.\nUntil the spell ends, you " +
                                    "can command the interior\nto become dimly lit or dark. The " +
                                    "dome is opaque\nfrom the outside, of any color you choose, but " +
                                    "it is\ntransparent from the inside. ",
                         at_higher_levels="")


class Tongues(spells.Spell):
    """
    Tongues Spell
    SRD p. 188-189
    Generated
    """

    def __init__(self):
        super().__init__(name="Tongues",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=3,
                         school=SpellSchools.Divination,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list="a small clay model of a ziggurat",
                         duration="1 hour",
                         description="This spell grants the creature you touch the ability " +
                                    "to\nunderstand any spoken language it hears. Moreover,\nwhen " +
                                    "the target speaks, any creature that knows at\nleast one " +
                                    "language and can hear the target\nunderstands what it says. ",
                         at_higher_levels="")


class TransportViaPlants(spells.Spell):
    """
    Transport via Plants Spell
    SRD p. 189
    Generated
    """

    def __init__(self):
        super().__init__(name="Transport via Plants",
                         spell_lists=[SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.Conjuration,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 round",
                         description="This spell creates a magical link between a Large or\nlarger " +
                                    "inanimate plant within range and another\nplant, at any " +
                                    "distance, on the same plane of existence.\nYou must have seen " +
                                    "or touched the destination plant\nat least once before. For " +
                                    "the duration, any creature\ncan step into the target plant and " +
                                    "exit from the\ndestination plant by using 5 feet of movement. ",
                         at_higher_levels="")


class TreeStride(spells.Spell):
    """
    Tree Stride Spell
    SRD p. 189
    Generated
    """

    def __init__(self):
        super().__init__(name="Tree Stride",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Conjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="You gain the ability to enter a tree and move from\ninside it " +
                                    "to inside another tree of the same kind\nwithin 500 feet. Both " +
                                    "trees must be living and at\nleast the same size as you. You " +
                                    "must use 5 feet of\nmovement to enter a tree. You instantly " +
                                    "know the\nlocation of all other trees of the same kind " +
                                    "within\n500 feet and, as part of the move used to enter " +
                                    "the\ntree, can either pass into one of those trees or " +
                                    "step\nout of the tree you're in. You appear in a spot of " +
                                    "your\nchoice within 5 feet of the destination tree, " +
                                    "using\nanother 5 feet of movement. If you have no\nmovement " +
                                    "left, you appear within 5 feet of the tree\nyou entered.\nYou " +
                                    "can use this transportation ability once per\nround for the " +
                                    "duration. You must end each turn\noutside a tree. ",
                         at_higher_levels="")


class TruePolymorph(spells.Spell):
    """
    True Polymorph Spell
    SRD p. 189-190
    Generated
    """

    def __init__(self):
        super().__init__(name="True Polymorph",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=9,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of mercury, a dollop of gum arabic, and a wisp of smoke",
                         duration="1 hour",
                         description="Choose one creature or nonmagical object that you\ncan see " +
                                    "within range. You transform the creature\ninto a different " +
                                    "creature, the creature into an object,\nor the object into a " +
                                    "creature (the object must be\nneither worn nor carried by " +
                                    "another creature). The\ntransformation lasts for the duration, " +
                                    "or until the\ntarget drops to 0 hit points or dies. If " +
                                    "you\nconcentrate on this spell for the full duration, " +
                                    "the\ntransformation lasts until it is dispelled.\nThis spell " +
                                    "has no effect on a shapechanger or a\ncreature with 0 hit " +
                                    "points. An unwilling creature can\nmake a Wisdom saving throw, " +
                                    "and if it succeeds, it\nisn't affected by this " +
                                    "spell.\nCreature into Creature. If you turn a creature " +
                                    "into\nanother kind of creature, the new form can be any\nkind " +
                                    "you choose whose challenge rating is equal to\nor less than " +
                                    "the target's (or its level, if the target\ndoesn't have a " +
                                    "challenge rating). The target's game\nstatistics, including " +
                                    "mental ability scores, are\nreplaced by the statistics of the " +
                                    "new form. It retains\nits alignment and personality.\nThe " +
                                    "target assumes the hit points of its new form,\nand when it " +
                                    "reverts to its normal form, the creature\nreturns to the " +
                                    "number of hit points it had before it\ntransformed. If it " +
                                    "reverts as a result of dropping to 0\nhit points, any excess " +
                                    "damage carries over to its\nnormal form. As long as the excess " +
                                    "damage doesn't\nreduce the creature's normal form to 0 hit " +
                                    "points, it\nisn't knocked unconscious.\nThe creature is " +
                                    "limited in the actions it can\nperform by the nature of its " +
                                    "new form, and it can't\nspeak, cast spells, or take any other " +
                                    "action that\nrequires hands or speech, unless its new form " +
                                    "is\ncapable of such actions.\nThe target's gear melds into the " +
                                    "new form. The\ncreature can't activate, use, wield, or " +
                                    "otherwise\nbenefit from any of its equipment.\nObject into " +
                                    "Creature. You can turn an object into\nany kind of creature, " +
                                    "as long as the creature's size is\nno larger than the object's " +
                                    "size and the creature's\nchallenge rating is 9 or lower. The " +
                                    "creature is\nfriendly to you and your companions. It acts on " +
                                    "each\nof your turns. You decide what action it takes and\nhow " +
                                    "it moves. The GM has the creature's statistics\nand resolves " +
                                    "all of its actions and movement.\nIf the spell becomes " +
                                    "permanent, you no longer\ncontrol the creature. It might " +
                                    "remain friendly to you,\ndepending on how you have treated " +
                                    "it.\nCreature into Object. If you turn a creature into\nan " +
                                    "object, it transforms along with whatever it is\nwearing and " +
                                    "carrying into that form. The creature's\nstatistics become " +
                                    "those of the object, and the\ncreature has no memory of time " +
                                    "spent in this form,\nafter the spell ends and it returns to " +
                                    "its normal form. ",
                         at_higher_levels="")


class TrueResurrection(spells.Spell):
    """
    True Resurrection Spell
    SRD p. 190
    Generated
    """

    def __init__(self):
        super().__init__(name="True Resurrection",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=9,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a sprinkle of holy water and diamonds worth at least 25,000 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="You touch a creature that has been dead for no\nlonger than " +
                                    "200 years and that died for any reason\nexcept old age. If the " +
                                    "creature's soul is free and\nwilling, the creature is restored " +
                                    "to life with all its hit\npoints.\nThis spell closes all " +
                                    "wounds, neutralizes any\npoison, cures all diseases, and lifts " +
                                    "any curses\naffecting the creature when it died. The " +
                                    "spell\nreplaces damaged or missing organs and limbs.\nThe " +
                                    "spell can even provide a new body if the\noriginal no longer " +
                                    "exists, in which case you must\nspeak the creature's name. The " +
                                    "creature then\nappears in an unoccupied space you choose " +
                                    "within\n10 feet of you. ",
                         at_higher_levels="")


class TrueSeeing(spells.Spell):
    """
    True Seeing Spell
    SRD p. 190
    Generated
    """

    def __init__(self):
        super().__init__(name="True Seeing",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=6,
                         school=SpellSchools.Divination,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an ointment for the eyes that costs 25 gp; is made from mushroom powder, saffron, and fat; and is consumed by the spell",
                         duration="1 hour",
                         description="This spell gives the willing creature you touch the\nability " +
                                    "to see things as they actually are. For the\nduration, the " +
                                    "creature has truesight, notices secret\ndoors hidden by magic, " +
                                    "and can see into the Ethereal\nPlane, all out to a range of " +
                                    "120 feet. ",
                         at_higher_levels="")


class TrueStrike(spells.Spell):
    """
    True Strike Spell
    SRD p. 190
    Generated
    """

    def __init__(self):
        super().__init__(name="True Strike",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=0,
                         school=SpellSchools.Divination,
                         spell_range="30 feet",
                         verbal_components=False,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 round",
                         description="You extend your hand and point a finger at a target\nin range. " +
                                    "Your magic grants you a brief insight into\nthe target's " +
                                    "defenses. On your next turn, you gain\nadvantage on your first " +
                                    "attack roll against the target,\nprovided that this spell " +
                                    "hasn't ended. ",
                         at_higher_levels="")


class UnseenServant(spells.Spell):
    """
    Unseen Servant Spell
    SRD p. 190
    Generated
    """

    def __init__(self):
        super().__init__(name="Unseen Servant",
                         spell_lists=[SpellLists.ARCANE],
                         ritual=True,
                         level=1,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of string and a bit of wood",
                         duration="1 hour",
                         description="This spell creates an invisible, mindless, shapeless\nforce " +
                                    "that performs simple tasks at your command\nuntil the spell " +
                                    "ends. The servant springs into\nexistence in an unoccupied " +
                                    "space on the ground\nwithin range. It has AC 10, 1 hit point, " +
                                    "and a Strength\nof 2, and it can't attack. If it drops to 0 " +
                                    "hit points, the\nspell ends.\nOnce on each of your turns as a " +
                                    "bonus action, you\ncan mentally command the servant to move up " +
                                    "to 15\nfeet and interact with an object. The servant " +
                                    "can\nperform simple tasks that a human servant could do,\nsuch " +
                                    "as fetching things, cleaning, mending, folding\nclothes, " +
                                    "lighting fires, serving food, and pouring wine.\nOnce you give " +
                                    "the command, the servant performs\nthe task to the best of its " +
                                    "ability until it completes the\ntask, then waits for your next " +
                                    "command.\nIf you command the servant to perform a task " +
                                    "that\nwould move it more than 60 feet away from you, " +
                                    "the\nspell ends. ",
                         at_higher_levels="")


class VampiricTouch(spells.Spell):
    """
    Vampiric Touch Spell
    SRD p. 190
    Generated
    """

    def __init__(self):
        super().__init__(name="Vampiric Touch",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Necromancy,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="1 minute",
                         description="The touch of your shadow-wreathed hand can\nsiphon life force " +
                                    "from others to heal your wounds.\nMake a melee spell attack " +
                                    "against a creature within\nyour reach. On a hit, the target " +
                                    "takes 3d6 necrotic\ndamage, and you regain hit points equal to " +
                                    "half the\namount of necrotic damage dealt. Until the " +
                                    "spell\nends, you can make the attack again on each of " +
                                    "your\nturns as an action. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 4th level or " +
                                          "higher, the damage increases\nby 1d6 for each slot level above " +
                                          "3rd. ")


class ViciousMockery(spells.Spell):
    """
    Vicious Mockery Spell
    SRD p. 190-191
    Generated
    """

    def __init__(self):
        super().__init__(name="Vicious Mockery",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You unleash a string of insults laced with " +
                                    "subtle\nenchantments at a creature you can see within " +
                                    "range.\nIf the target can hear you (though it need " +
                                    "not\nunderstand you), it must succeed on a Wisdom\nsaving " +
                                    "throw or take 1d4 psychic damage and have\ndisadvantage on the " +
                                    "next attack roll it makes before\nthe end of its next " +
                                    "turn.\nThis spell's damage increases by 1d4 when you\nreach " +
                                    "5th level (2d4), 11th level (3d4), and 17th\nlevel (4d4). ",
                         at_higher_levels="")


class WallOfFire(spells.Spell):
    """
    Wall of Fire Spell
    SRD p. 191
    Generated
    """

    def __init__(self):
        super().__init__(name="Wall of Fire",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small piece of phosphorus",
                         duration="1 minute",
                         description="You create a wall of fire on a solid surface within\nrange. " +
                                    "You can make the wall up to 60 feet long, 20\nfeet high, and 1 " +
                                    "foot thick, or a ringed wall up to 20\nfeet in diameter, 20 " +
                                    "feet high, and 1 foot thick. The\nwall is opaque and lasts for " +
                                    "the duration.\nWhen the wall appears, each creature within " +
                                    "its\narea must make a Dexterity saving throw. On a " +
                                    "failed\nsave, a creature takes 5d8 fire damage, or half " +
                                    "as\nmuch damage on a successful save.\nOne side of the wall, " +
                                    "selected by you when you\ncast this spell, deals 5d8 fire " +
                                    "damage to each\ncreature that ends its turn within 10 feet of " +
                                    "that side\nor inside the wall. A creature takes the same " +
                                    "damage\nwhen it enters the wall for the first time on a turn " +
                                    "or\nends its turn there. The other side of the wall deals\nno " +
                                    "damage. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 5th level or " +
                                          "higher, the damage increases\nby 1d8 for each slot level above " +
                                          "4th. ")


class WallOfForce(spells.Spell):
    """
    Wall of Force Spell
    SRD p. 191
    Generated
    """

    def __init__(self):
        super().__init__(name="Wall of Force",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of powder made by crushing a clear gemstone",
                         duration="10 minutes",
                         description="An invisible wall of force springs into existence at a\npoint " +
                                    "you choose within range. The wall appears in\nany orientation " +
                                    "you choose, as a horizontal or\nvertical barrier or at an " +
                                    "angle. It can be free floating\nor resting on a solid surface. " +
                                    "You can form it into a\nhemispherical dome or a sphere with a " +
                                    "radius of up\nto 10 feet, or you can shape a flat surface made " +
                                    "up of\nten 10-foot-by-10-foot panels. Each panel must " +
                                    "be\ncontiguous with another panel. In any form, the wall\nis " +
                                    "1/4 inch thick. It lasts for the duration. If the wall\ncuts " +
                                    "through a creature's space when it appears, the\ncreature is " +
                                    "pushed to one side of the wall (your\nchoice which " +
                                    "side).\nNothing can physically pass through the wall. It " +
                                    "is\nimmune to all damage and can't be dispelled by\ndispel " +
                                    "magic. A disintegrate spell destroys the wall\ninstantly, " +
                                    "however. The wall also extends into the\nEthereal Plane, " +
                                    "blocking ethereal travel through the\nwall. ",
                         at_higher_levels="")


class WallOfIce(spells.Spell):
    """
    Wall of Ice Spell
    SRD p. 191
    Generated
    """

    def __init__(self):
        super().__init__(name="Wall of Ice",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small piece of quartz",
                         duration="10 minutes",
                         description="You create a wall of ice on a solid surface within\nrange. You " +
                                    "can form it into a hemispherical dome or\na sphere with a " +
                                    "radius of up to 10 feet, or you can\nshape a flat surface made " +
                                    "up of ten 10-foot-square\npanels. Each panel must be " +
                                    "contiguous with another\npanel. In any form, the wall is 1 " +
                                    "foot thick and lasts\nfor the duration.\nIf the wall cuts " +
                                    "through a creature's space when it\nappears, the creature " +
                                    "within its area is pushed to\none side of the wall and must " +
                                    "make a Dexterity\nsaving throw. On a failed save, the creature " +
                                    "takes\n10d6 cold damage, or half as much damage on " +
                                    "a\nsuccessful save.\nThe wall is an object that can be damaged " +
                                    "and thus\nbreached. It has AC 12 and 30 hit points per " +
                                    "10-foot\nsection, and it is vulnerable to fire damage. " +
                                    "Reducing\na 10-foot section of wall to 0 hit points destroys " +
                                    "it\nand leaves behind a sheet of frigid air in the space\nthe " +
                                    "wall occupied. A creature moving through the\nsheet of frigid " +
                                    "air for the first time on a turn must\nmake a Constitution " +
                                    "saving throw. That creature\ntakes 5d6 cold damage on a failed " +
                                    "save, or half as\nmuch damage on a successful one. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, the damage the wall\ndeals when it appears increases " +
                                          "by 2d6, and the\ndamage from passing through the sheet of " +
                                          "frigid air\nincreases by 1d6, for each slot level above 6th. ")


class WallOfStone(spells.Spell):
    """
    Wall of Stone Spell
    SRD p. 191-192
    Generated
    """

    def __init__(self):
        super().__init__(name="Wall of Stone",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small block of granite",
                         duration="10 minutes",
                         description="A nonmagical wall of solid stone springs into\nexistence at a " +
                                    "point you choose within range. The\nwall is 6 inches thick and " +
                                    "is composed of ten 10-footby-10-foot panels. Each panel must " +
                                    "be contiguous\nwith at least one other panel. Alternatively, " +
                                    "you can\ncreate 10-foot-by-20-foot panels that are only " +
                                    "3\ninches thick.\nIf the wall cuts through a creature's space " +
                                    "when it\nappears, the creature is pushed to one side of " +
                                    "the\nwall (your choice). If a creature would be\nsurrounded on " +
                                    "all sides by the wall (or the wall and\nanother solid " +
                                    "surface), that creature can make a\nDexterity saving throw. On " +
                                    "a success, it can use its\nreaction to move up to its speed so " +
                                    "that it is no\nlonger enclosed by the wall.\nThe wall can have " +
                                    "any shape you desire, though it\ncan't occupy the same space " +
                                    "as a creature or object.\nThe wall doesn't need to be vertical " +
                                    "or rest on any\nfirm foundation. It must, however, merge with " +
                                    "and\nbe solidly supported by existing stone. Thus, you " +
                                    "can\nuse this spell to bridge a chasm or create a ramp.\nIf " +
                                    "you create a span greater than 20 feet in length,\nyou must " +
                                    "halve the size of each panel to create\nsupports. You can " +
                                    "crudely shape the wall to create\ncrenellations, battlements, " +
                                    "and so on.\nThe wall is an object made of stone that can " +
                                    "be\ndamaged and thus breached. Each panel has AC 15\nand 30 " +
                                    "hit points per inch of thickness. Reducing a\npanel to 0 hit " +
                                    "points destroys it and might cause\nconnected panels to " +
                                    "collapse at the GM's discretion.\nIf you maintain your " +
                                    "concentration on this spell\nfor its whole duration, the wall " +
                                    "becomes permanent\nand can't be dispelled. Otherwise, the " +
                                    "wall\ndisappears when the spell ends. ",
                         at_higher_levels="")


class WallOfThorns(spells.Spell):
    """
    Wall of Thorns Spell
    SRD p. 192
    Generated
    """

    def __init__(self):
        super().__init__(name="Wall of Thorns",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=6,
                         school=SpellSchools.Conjuration,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a handful of thorns",
                         duration="10 minutes",
                         description="You create a wall of tough, pliable, tangled brush\nbristling " +
                                    "with needle-sharp thorns. The wall appears\nwithin range on a " +
                                    "solid surface and lasts for the\nduration. You choose to make " +
                                    "the wall up to 60 feet\nlong, 10 feet high, and 5 feet thick " +
                                    "or a circle that has\na 20-foot diameter and is up to 20 feet " +
                                    "high and 5\nfeet thick. The wall blocks line of sight.\nWhen " +
                                    "the wall appears, each creature within its\narea must make a " +
                                    "Dexterity saving throw. On a failed\nsave, a creature takes " +
                                    "7d8 piercing damage, or half\nas much damage on a successful " +
                                    "save.\nA creature can move through the wall, albeit\nslowly " +
                                    "and painfully. For every 1 foot a creature\nmoves through the " +
                                    "wall, it must spend 4 feet of\nmovement. Furthermore, the " +
                                    "first time a creature\nenters the wall on a turn or ends its " +
                                    "turn there, the\ncreature must make a Dexterity saving throw. " +
                                    "It\ntakes 7d8 slashing damage on a failed save, or half " +
                                    "as\nmuch damage on a successful one. ",
                         at_higher_levels="When you cast this spell using a\nspell slot of 7th level or " +
                                          "higher, both types of damage\nincrease by 1d8 for each slot " +
                                          "level above 6th. ")


class WardingBond(spells.Spell):
    """
    Warding Bond Spell
    SRD p. 192
    Generated
    """

    def __init__(self):
        super().__init__(name="Warding Bond",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pair of platinum rings worth at least 50 gp each, which you and the target must wear for the duration",
                         duration="1 hour",
                         description="This spell wards a willing creature you touch and\ncreates a " +
                                    "mystic connection between you and the\ntarget until the spell " +
                                    "ends. While the target is within\n60 feet of you, it gains a " +
                                    "+1 bonus to AC and saving\nthrows, and it has resistance to " +
                                    "all damage. Also,\neach time it takes damage, you take the " +
                                    "same\namount of damage.\nThe spell ends if you drop to 0 hit " +
                                    "points or if you\nand the target become separated by more than " +
                                    "60\nfeet. It also ends if the spell is cast again on either " +
                                    "of\nthe connected creatures. You can also dismiss the\nspell " +
                                    "as an action. ",
                         at_higher_levels="")


class WaterBreathing(spells.Spell):
    """
    Water Breathing Spell
    SRD p. 192
    Generated
    """

    def __init__(self):
        super().__init__(name="Water Breathing",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         ritual=True,
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a short reed or piece of straw",
                         duration="24 hours",
                         description="This spell grants up to ten willing creatures you can\nsee " +
                                    "within range the ability to breathe underwater\nuntil the " +
                                    "spell ends. Affected creatures also retain\ntheir normal mode " +
                                    "of respiration. ",
                         at_higher_levels="")


class WaterWalk(spells.Spell):
    """
    Water Walk Spell
    SRD p. 192-193
    Generated
    """

    def __init__(self):
        super().__init__(name="Water Walk",
                         spell_lists=[SpellLists.PRIMAL],
                         ritual=True,
                         level=3,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of cork",
                         duration="1 hour",
                         description="This spell grants the ability to move across any\nliquid " +
                                    "surface—such as water, acid, mud, snow,\nquicksand, or lava—as " +
                                    "if it were harmless solid\nground (creatures crossing molten " +
                                    "lava can still take\ndamage from the heat). Up to ten willing " +
                                    "creatures\nyou can see within range gain this ability for " +
                                    "the\nduration.\nIf you target a creature submerged in a " +
                                    "liquid, the\nspell carries the target to the surface of the " +
                                    "liquid at\na rate of 60 feet per round. ",
                         at_higher_levels="")


class Web(spells.Spell):
    """
    Web Spell
    SRD p. 193
    Generated
    """

    def __init__(self):
        super().__init__(name="Web",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of spiderweb",
                         duration="1 hour",
                         description="You conjure a mass of thick, sticky webbing at a\npoint of " +
                                    "your choice within range. The webs fill a 20-\nfoot cube from " +
                                    "that point for the duration. The webs\nare difficult terrain " +
                                    "and lightly obscure their area.\nIf the webs aren't anchored " +
                                    "between two solid\nmasses (such as walls or trees) or layered " +
                                    "across a\nfloor, wall, or ceiling, the conjured web collapses " +
                                    "on\nitself, and the spell ends at the start of your next " +
                                    "turn.\nWebs layered over a flat surface have a depth of " +
                                    "5\nfeet.\nEach creature that starts its turn in the webs " +
                                    "or\nthat enters them during its turn must make a\nDexterity " +
                                    "saving throw. On a failed save, the creature\nis restrained as " +
                                    "long as it remains in the webs or\nuntil it breaks free.\nA " +
                                    "creature restrained by the webs can use its\naction to make a " +
                                    "Strength check against your spell\nsave DC. If it succeeds, it " +
                                    "is no longer restrained.\nThe webs are flammable. Any 5-foot " +
                                    "cube of webs\nexposed to fire burns away in 1 round, dealing " +
                                    "2d4\nfire damage to any creature that starts its turn in " +
                                    "the\nfire. ",
                         at_higher_levels="")


class Weird(spells.Spell):
    """
    Weird Spell
    SRD p. 193
    Generated
    """

    def __init__(self):
        super().__init__(name="Weird",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=9,
                         school=SpellSchools.Illusion,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="one minute",
                         description="Drawing on the deepest fears of a group of creatures,\nyou " +
                                    "create illusory creatures in their minds, visible\nonly to " +
                                    "them. Each creature in a 30-foot-radius\nsphere centered on a " +
                                    "point of your choice within\nrange must make a Wisdom saving " +
                                    "throw. On a\nfailed save, a creature becomes frightened for " +
                                    "the\nduration. The illusion calls on the creature's " +
                                    "deepest\nfears, manifesting its worst nightmares as " +
                                    "an\nimplacable threat. At the end of each of the\nfrightened " +
                                    "creature's turns, it must succeed on a\nWisdom saving throw or " +
                                    "take 4d10 psychic damage.\nOn a successful save, the spell " +
                                    "ends for that creature. ",
                         at_higher_levels="")


class WindWalk(spells.Spell):
    """
    Wind Walk Spell
    SRD p. 193
    Generated
    """

    def __init__(self):
        super().__init__(name="Wind Walk",
                         spell_lists=[SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="fire and holy water",
                         duration="8 hours",
                         description="You and up to ten willing creatures you can see\nwithin range " +
                                    "assume a gaseous form for the duration,\nappearing as wisps of " +
                                    "cloud. While in this cloud form,\na creature has a flying " +
                                    "speed of 300 feet and has\nresistance to damage from " +
                                    "nonmagical weapons. The\nonly actions a creature can take in " +
                                    "this form are the\nDash action or to revert to its normal " +
                                    "form.\nReverting takes 1 minute, during which time a\ncreature " +
                                    "is incapacitated and can't move. Until the\nspell ends, a " +
                                    "creature can revert to cloud form, which\nalso requires the " +
                                    "1-minute transformation.\nIf a creature is in cloud form and " +
                                    "flying when the\neffect ends, the creature descends 60 feet " +
                                    "per round\nfor 1 minute until it lands, which it does safely. " +
                                    "If it\ncan't land after 1 minute, the creature falls " +
                                    "the\nremaining distance. ",
                         at_higher_levels="")


class WindWall(spells.Spell):
    """
    Wind Wall Spell
    SRD p. 193-194
    Generated
    """

    def __init__(self):
        super().__init__(name="Wind Wall",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=3,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny fan and a feather of exotic origin",
                         duration="1 minute",
                         description="A wall of strong wind rises from the ground at a\npoint you " +
                                    "choose within range. You can make the\nwall up to 50 feet " +
                                    "long, 15 feet high, and 1 foot thick.\nYou can shape the wall " +
                                    "in any way you choose so\nlong as it makes one continuous path " +
                                    "along the\nground. The wall lasts for the duration.\nWhen the " +
                                    "wall appears, each creature within its\narea must make a " +
                                    "Strength saving throw. A creature\ntakes 3d8 bludgeoning " +
                                    "damage on a failed save, or\nhalf as much damage on a " +
                                    "successful one.\nThe strong wind keeps fog, smoke, and other " +
                                    "gases\nat bay. Small or smaller flying creatures or " +
                                    "objects\ncan't pass through the wall. Loose, " +
                                    "lightweight\nmaterials brought into the wall fly upward. " +
                                    "Arrows,\nbolts, and other ordinary projectiles launched " +
                                    "at\ntargets behind the wall are deflected upward " +
                                    "and\nautomatically miss. (Boulders hurled by giants or\nsiege " +
                                    "engines, and similar projectiles, are\nunaffected.) Creatures " +
                                    "in gaseous form can't pass\nthrough it. ",
                         at_higher_levels="")


class Wish(spells.Spell):
    """
    Wish Spell
    SRD p. 194
    Generated
    """

    def __init__(self):
        super().__init__(name="Wish",
                         spell_lists=[SpellLists.ARCANE],
                         level=9,
                         school=SpellSchools.Conjuration,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="Wish is the mightiest spell a mortal creature can cast.\nBy " +
                                    "simply speaking aloud, you can alter the very\nfoundations of " +
                                    "reality in accord with your desires.\nThe basic use of this " +
                                    "spell is to duplicate any other\nspell of 8th level or lower. " +
                                    "You don't need to meet\nany requirements in that spell, " +
                                    "including costly\ncomponents. The spell simply takes " +
                                    "effect.\nAlternatively, you can create one of the " +
                                    "following\neffects of your choice:\n• You create one object of " +
                                    "up to 25,000 gp in value\nthat isn't a magic item. The object " +
                                    "can be no more\nthan 300 feet in any dimension, and it appears " +
                                    "in\nan unoccupied space you can see on the ground.\n• You " +
                                    "allow up to twenty creatures that you can see\nto regain all " +
                                    "hit points, and you end all effects on\nthem described in the " +
                                    "greater restoration spell.\n• You grant up to ten creatures " +
                                    "that you can see\nresistance to a damage type you choose.\n• " +
                                    "You grant up to ten creatures you can see\nimmunity to a " +
                                    "single spell or other magical effect\nfor 8 hours. For " +
                                    "instance, you could make yourself\nand all your companions " +
                                    "immune to a lich's life\ndrain attack.\n• You undo a single " +
                                    "recent event by forcing a reroll\nof any roll made within the " +
                                    "last round (including\nyour last turn). Reality reshapes " +
                                    "itself to\naccommodate the new result. For example, a " +
                                    "wish\nspell could undo an opponent's successful save, a\nfoe's " +
                                    "critical hit, or a friend's failed save. You can\nforce the " +
                                    "reroll to be made with advantage or\ndisadvantage, and you can " +
                                    "choose whether to use\nthe reroll or the original roll.\nYou " +
                                    "might be able to achieve something beyond the\nscope of the " +
                                    "above examples. State your wish to the\nGM as precisely as " +
                                    "possible. The GM has great\nlatitude in ruling what occurs in " +
                                    "such an instance;\nthe greater the wish, the greater the " +
                                    "likelihood that\nsomething goes wrong. This spell might simply " +
                                    "fail,\nthe effect you desire might only be partly " +
                                    "achieved,\nor you might suffer some unforeseen consequence " +
                                    "as\na result of how you worded the wish. For example,\nwishing " +
                                    "that a villain were dead might propel you\nforward in time to " +
                                    "a period when that villain is no\nlonger alive, effectively " +
                                    "removing you from the game.\nSimilarly, wishing for a " +
                                    "legendary magic item or\nartifact might instantly transport " +
                                    "you to the\npresence of the item's current owner.\nThe stress " +
                                    "of casting this spell to produce any\neffect other than " +
                                    "duplicating another spell weakens\nyou. After enduring that " +
                                    "stress, each time you cast a\nspell until you finish a long " +
                                    "rest, you take 1d10\nnecrotic damage per level of that spell. " +
                                    "This damage\ncan't be reduced or prevented in any way. " +
                                    "In\naddition, your Strength drops to 3, if it isn't 3 " +
                                    "or\nlower already, for 2d4 days. For each of those days\nthat " +
                                    "you spend resting and doing nothing more than\nlight activity, " +
                                    "your remaining recovery time\ndecreases by 2 days. Finally, " +
                                    "there is a 33 percent\nchance that you are unable to cast wish " +
                                    "ever again if\nyou suffer this stress. ",
                         at_higher_levels="")


class WordOfRecall(spells.Spell):
    """
    Word of Recall Spell
    SRD p. 194
    Generated
    """

    def __init__(self):
        super().__init__(name="Word of Recall",
                         spell_lists=[SpellLists.DIVINE],
                         level=6,
                         school=SpellSchools.Conjuration,
                         spell_range="5 feet",
                         verbal_components=True,
                         somatic_components=False,
                         material_components_list=None,
                         duration="Instantaneous",
                         description="You and up to five willing creatures within 5 feet of\nyou " +
                                    "instantly teleport to a previously designated\nsanctuary. You " +
                                    "and any creatures that teleport with\nyou appear in the " +
                                    "nearest unoccupied space to the\nspot you designated when you " +
                                    "prepared your\nsanctuary (see below). If you cast this spell " +
                                    "without\nfirst preparing a sanctuary, the spell has no " +
                                    "effect.\nYou must designate a sanctuary by casting this\nspell " +
                                    "within a location, such as a temple, dedicated to\nor strongly " +
                                    "linked to your deity. If you attempt to\ncast the spell in " +
                                    "this manner in an area that isn't\ndedicated to your deity, " +
                                    "the spell has no effect. ",
                         at_higher_levels="")


class ZoneOfTruth(spells.Spell):
    """
    Zone of Truth Spell
    SRD p. 194-195
    Generated
    """

    def __init__(self):
        super().__init__(name="Zone of Truth",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list=None,
                         duration="10 minutes",
                         description="You create a magical zone that guards against\ndeception in a " +
                                    "15-foot-radius sphere centered on a\npoint of your choice " +
                                    "within range. Until the spell\nends, a creature that enters " +
                                    "the spell's area for the\nfirst time on a turn or starts its " +
                                    "turn there must\nmake a Charisma saving throw. On a failed " +
                                    "save, a\ncreature can't speak a deliberate lie while in " +
                                    "the\nradius. You know whether each creature succeeds or\nfails " +
                                    "on its saving throw.\nAn affected creature is aware of the " +
                                    "spell and can\nthus avoid answering questions to which it " +
                                    "would\nnormally respond with a lie. Such a creature can " +
                                    "be\nevasive in its answers as long as it remains within\nthe " +
                                    "boundaries of the truth ",
                         at_higher_levels="")
