"""
Content from the Dungeons and Dragons System Reference Document v5.1.
https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf
"""

from rules import armors, spells, weapons
from rules.enums import ArmorTraining, DamageTypes, SpellLists, SpellSchools, WeaponTypes


class Padded(armors.Armor):
    """
    Padded Armor
    SRD p. 63
    """

    def __init__(self):
        super().__init__(name="Padded",
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=11,
                         stealth_disadvantage=True)


class Leather(armors.Armor):
    """
    Leather Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Leather",
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=11)


class StuddedLeather(armors.Armor):
    """
    Studded Leather Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Studded Leather",
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=12)


class Hide(armors.Armor):
    """
    Hide Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Hide",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=12)


class ChainShirt(armors.Armor):
    """
    Chain Shirt Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Chain Shirt",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=13)


class ScaleMail(armors.Armor):
    """
    Scale Mail Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Scale Mail",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=14,
                         stealth_disadvantage=True)


class Breastplate(armors.Armor):
    """
    Breastplate Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Breastplate",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=14)


class HalfPlate(armors.Armor):
    """
    Half Plate Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Half Plate",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=15,
                         stealth_disadvantage=True)


class RingMail(armors.Armor):
    """
    Ring Mail Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Ring Mail",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=14,
                         stealth_disadvantage=True)


class ChainMail(armors.Armor):
    """
    Chain Mail Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Chain Mail",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=16,
                         stealth_disadvantage=True)


class Splint(armors.Armor):
    """
    Splint Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Splint",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=17,
                         stealth_disadvantage=True)


class Plate(armors.Armor):
    """
    Plate Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Plate",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=18,
                         stealth_disadvantage=True)


class Shield(armors.Armor):
    """
    Shield
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Shield",
                         training_needed=ArmorTraining.SHIELD,
                         armor_class=2)


class AcidArrow(spells.Spell):
    """
    Acid Arrow Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Acid Arrow",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="powdered rhubarb leaf and an adder's stomach",
                         duration="Instantaneous",
                         description="A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage and no damage at the end of its next turn.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, the damage (both initial and later) increases by 1d4 for each slot level above 2nd.")


class AcidSplash(spells.Spell):
    """
    Acid Splash Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Acid Splash",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=0,
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Instantaneous",
                         description="You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage. This spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).",
                         at_higher_levels="")


class Aid(spells.Spell):
    """
    Aid Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Aid",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a tiny strip of white cloth",
                         duration="8 hours",
                         description="Your spell bolsters your allies with toughness and resolve. Choose up to three creatures within range. Each target's hit point maximum and current hit points increase by 5 for the duration.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, a target's hit points increase by an additional 5 for each slot level above 2nd.")


class Alarm(spells.Spell):
    """
    Alarm Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Alarm",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=1,
                         ritual=True,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a tiny bell and a piece of fine silver wire",
                         duration="8 hours",
                         description="You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible. A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping. An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.",
                         at_higher_levels="")


class AlterSelf(spells.Spell):
    """
    Alter Self Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Alter Self",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 hour",
                         description="You assume a different form. When you cast the spell, choose one of the following options, the effects of which last for the duration of the spell. While the spell lasts, you can end one option as an action to gain the benefits of a different one. Aquatic Adaptation. You adapt your body to an aquatic environment, sprouting gills and growing webbing between your fingers. You can breathe underwater and gain a swimming speed equal to your walking speed. Change Appearance. You transform your appearance. You decide what you look like, including your height, weight, facial features, sound of your voice, hair length, coloration, and distinguishing characteristics, if any. You can make yourself appear as a member of another race, though none of your statistics change. You also can't appear as a creature of a different size than you, and your basic shape stays the same; if you're bipedal, you can't use this spell to become quadrupedal, for instance. At any time for the duration of the spell, you can use your action to change your appearance in this way again. Natural Weapons. You grow claws, fangs, spines, horns, or a different natural weapon of your choice. Your unarmed strikes deal 1d6 bludgeoning, piercing, or slashing damage, as appropriate to the natural weapon you chose, and you are proficient with your unarmed strikes. Finally, the natural weapon is magic and you have a +1 bonus to the attack and damage rolls you make using it.",
                         at_higher_levels="")


class AnimalFriendship(spells.Spell):
    """
    Animal Friendship Spell
    SRD p. 115
    """

    def __init__(self):
        super().__init__(name="Animal Friendship",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.ENCHANTMENT,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a morsel of food",
                         duration="24 hours",
                         description="This spell lets you convince a beast that you mean it no harm. Choose a beast "
                                     "that you can see within range. It must see and hear you. If the beast's "
                                     "Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed "
                                     "on a Wisdom saving throw or be charmed by you for the spell's duration. If you "
                                     "or one of your companions harms the target, the spells ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you can affect one additional beast t level above 1st.")


class AnimalMessenger(spells.Spell):
    """
    Animal Messenger Spell
    SRD p. 115
    """

    def __init__(self):
        super().__init__(name="Animal Messenger",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ENCHANTMENT,
                         ritual=True,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a morsel of food",
                         duration="24 hours",
                         description="By means of this spell, you use an animal to deliver a message. Choose a Tiny "
                                     "beast you can see within range, such as a squirrel, a blue jay, or a bat. You "
                                     "specify a location, which you must have visited, and a recipient who matches a "
                                     "general description, such as “a man or woman dressed in the uniform of the town "
                                     "guard” or “a red-haired dwarf wearing a pointed hat.” You also speak a "
                                     "message of up to twenty-five words. The target beast travels for the duration "
                                     "of the spell toward the specified location, covering about 50 miles per 24 "
                                     "hours for a flying messenger, or 25 miles for other animals.\n"
                                     "When the messenger arrives, it delivers your message to the creature that you "
                                     "described, replicating the sound of your voice. The messenger speaks only to a "
                                     "creature matching the description you gave. If the messenger doesn't reach its "
                                     "destination before the spell ends, the message is lost, and the beast makes its "
                                     "way back to where you cast this spell.",
                         at_higher_levels="If you cast this spell using a spell slot of 3nd level or higher, "
                                          "the duration of the spell increases by 48 hours for each slot level above "
                                          "2nd.")


class AnimalShapes(spells.Spell):
    """
    Animal Shapes Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Animal Shapes",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=8,
                         ritual=False,
                         school=SpellSchools.Transmutation,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 24 hours",
                         description="Your magic turns others into beasts. Choose any number of willing creatures that you can see within range. You transform each target into the form of a Large or smaller beast with a challenge rating of 4 or lower. On subsequent turns, you can use your action to transform affected creatures into new forms. The transformation lasts for the duration for each target, or until the target drops to 0 hit points or dies. You can choose a different form for each target. A target's game statistics are replaced by the statistics of the chosen beast, though the target retains its alignment and Intelligence, Wisdom, and Charisma scores. The target assumes the hit points of its new form, and when it reverts to its normal form, it returns to the number of hit points it had before it transformed. If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form. As long as the excess damage doesn't reduce the creature's normal form to 0 hit points, it isn't knocked unconscious. The creature is limited in the actions it can perform by the nature of its new form, and it can't speak or cast spells. The target's gear melds into the new form. The target can't activate, wield, or otherwise benefit from any of its equipment.",
                         at_higher_levels="")


class AnimateDead(spells.Spell):
    """
    Animate Dead Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Animate Dead",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=3,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="10 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a drop of blood, a piece of flesh, and a pinch of bone dust",
                         duration="Instantaneous",
                         description="This spell creates an undead servant. Choose a pile of bones or a corpse of a Medium or Small humanoid within range. Your spell imbues the target with a foul mimicry of life, raising it as an undead creature. The target becomes a skeleton if you chose bones or a zombie if you chose a corpse (the GM has the creature's game statistics). On each of your turns, you can use a bonus action to mentally command any creature you made with this spell if the creature is within 60 feet of you (if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one). You decide what action the creature will take and where it will move during its next turn, or you can issue a general command, such as to guard a particular chamber or corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete. The creature is under your control for 24 hours, after which it stops obeying any command you've given it. To maintain control of the creature for another 24 hours, you must cast this spell on the creature again before the current 24-hour period ends. This use of the spell reasserts your control over up to four creatures you have animated with this spell, rather than animating a new one.",
                         at_higher_levels="When you cast this spell using a spell slot of 4th level or higher, you animate or reassert control over two additional undead creatures for each slot level above 3rd. Each of the creatures must come from a different corpse or pile of bones.")


class AnimateObjects(spells.Spell):
    """
    Animate Objects Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Animate Objects",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Transmutation,
                         spell_range="120 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 minute",
                         description="Objects come to life at your command. Choose up to ten nonmagical objects within range that are not being worn or carried. Medium targets count as two objects, Large targets count as four objects, Huge targets count as eight objects. You can't animate any object larger than Huge. Each target animates and becomes a creature under your control until the spell ends or until reduced to 0 hit points. As a bonus action, you can mentally command any creature you made with this spell if the creature is within 500 feet of you (if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one). You decide what action the creature will take and where it will move during its next turn, or you can issue a general command, such as to guard a particular chamber or corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete. Animated Object Statistics Size HP AC Attack Str Dex Tiny 20 18 +8 to hit, 1d4 + 4 damage 4 18 Small 25 16 +6 to hit, 1d8 + 2 damage 6 14 Medium 40 13 +5 to hit, 2d6 + 1 damage 10 12 Large 50 10 +6 to hit, 2d10 + 2 damage 14 10 Huge 80 10 +8 to hit, 2d12 + 4 damage 18 6 An animated object is a construct with AC, hit points, attacks, Strength, and Dexterity determined by its size. Its Constitution is 10 and its Intelligence and Wisdom are 3, and its Charisma is 1. Its speed is 30 feet; if the object lacks legs or other appendages it can use for locomotion, it instead has a flying speed of 30 feet and can hover. If the object is securely attached to a surface or a larger object, such as a chain bolted to a wall, its speed is 0. It has blindsight with a radius of 30 feet and is blind beyond that distance. When the animated object drops to 0 hit points, it reverts to its original object form, and any remaining damage carries over to its original object form. If you command an object to attack, it can make a single melee attack against a creature within 5 feet of it. It makes a slam attack with an attack bonus and bludgeoning damage determined by its size. The GM might rule that a specific object inflicts slashing or piercing damage based on its form.",
                         at_higher_levels="If you cast this spell using a spell slot of 6th level or higher, you can animate two additional objects for each slot level above 5th.")


class AntilifeShell(spells.Spell):
    """
    Antilife Shell Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Antilife Shell",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="Self (10-foot radius)",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 hour",
                         description="A shimmering barrier extends out from you in a 10- foot radius and moves with you, remaining centered on you and hedging out creatures other than undead and constructs. The barrier lasts for the duration. The barrier prevents an affected creature from passing or reaching through. An affected creature can cast spells or make attacks with ranged or reach weapons through the barrier. If you move so that an affected creature is forced to pass through the barrier, the spell ends.",
                         at_higher_levels="")


class AntimagicField(spells.Spell):
    """
    Antimagic Field Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Antimagic Field",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=8,
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="Self (10-foot-radius sphere)",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a pinch of powdered iron or iron filings",
                         duration="Concentration, up to 1 hour",
                         description="A 10-foot-radius invisible sphere of antimagic surrounds you. This area is divorced from the magical energy that suffuses the multiverse. Within the sphere, spells can't be cast, summoned creatures disappear, and even magic items become mundane. Until the spell ends, the sphere moves with you, centered on you. Spells and other magical effects, except those created by an artifact or a deity, are suppressed in the sphere and can't protrude into it. A slot expended to cast a suppressed spell is consumed. While an effect is suppressed, it doesn't function, but the time it spends suppressed counts against its duration. Targeted Effects. Spells and other magical effects, such as magic missile and charm person, that target a creature or an object in the sphere have no effect on that target. Areas of Magic. The area of another spell or magical effect, such as fireball, can't extend into the sphere. If the sphere overlaps an area of magic, the part of the area that is covered by the sphere is suppressed. For example, the flames created by a wall of fire are suppressed within the sphere, creating a gap in the wall if the overlap is large enough. Spells. Any active spell or other magical effect on a creature or an object in the sphere is suppressed while the creature or object is in it. Magic Items. The properties and powers of magic items are suppressed in the sphere. For example, a +1 longsword in the sphere functions as a nonmagical longsword. A magic weapon's properties and powers are suppressed if it is used against a target in the sphere or wielded by an attacker in the sphere. If a magic weapon or a piece of magic ammunition fully leaves the sphere (for example, if you fire a magic arrow or throw a magic spear at a target outside the sphere), the magic of the item ceases to be suppressed as soon as it exits. Magical Travel. Teleportation and planar travel fail to work in the sphere, whether the sphere is the destination or the departure point for such magical travel. A portal to another location, world, or plane of existence, as well as an opening to an extradimensional space such as that created by the rope trick spell, temporarily closes while in the sphere. Creatures and Objects. A creature or object summoned or created by magic temporarily winks out of existence in the sphere. Such a creature instantly reappears once the space the creature occupied is no longer within the sphere. Dispel Magic. Spells and magical effects such as dispel magic have no effect on the sphere. Likewise, the spheres created by different antimagic field spells don't nullify each other.",
                         at_higher_levels="")


class AntipathySympathy(spells.Spell):
    """
    Antipathy/Sympathy Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Antipathy/Sympathy",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=8,
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="either a lump of alum soaked in vinegar for the antipathy effect or a drop of honey for the sympathy effect",
                         duration="10 days",
                         description="This spell attracts or repels creatures of your choice. You target something within range, either a Huge or smaller object or creature or an area that is no larger than a 200-foot cube. Then specify a kind of intelligent creature, such as red dragons, goblins, or vampires. You invest the target with an aura that either attracts or repels the specified creatures for the duration. Choose antipathy or sympathy as the aura's effect. Antipathy. The enchantment causes creatures of the kind you designated to feel an intense urge to leave the area and avoid the target. When such a creature can see the target or comes within 60 feet of it, the creature must succeed on a Wisdom saving throw or become frightened. The creature remains frightened while it can see the target or is within 60 feet of it. While frightened by the target, the creature must use its movement to move to the nearest safe spot from which it can't see the target. If the creature moves more than 60 feet from the target and can't see it, the creature is no longer frightened, but the creature becomes frightened again if it regains sight of the target or moves within 60 feet of it. Sympathy. The enchantment causes the specified creatures to feel an intense urge to approach the target while within 60 feet of it or able to see it. When such a creature can see the target or comes within 60 feet of it, the creature must succeed on a Wisdom saving throw or use its movement on each of its turns to enter the area or move within reach of the target. When the creature has done so, it can't willingly move away from the target. If the target damages or otherwise harms an affected creature, the affected creature can make a Wisdom saving throw to end the effect, as described below. Ending the Effect. If an affected creature ends its turn while not within 60 feet of the target or able to see it, the creature makes a Wisdom saving throw. On a successful save, the creature is no longer affected by the target and recognizes the feeling of repugnance or attraction as magical. In addition, a creature affected by the spell is allowed another Wisdom saving throw every 24 hours while the spell persists. A creature that successfully saves against this effect is immune to it for 1 minute, after which time it can be affected again.",
                         at_higher_levels="")


class ArcaneEye(spells.Spell):
    """
    Arcane Eye Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Eye",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=4,
                         ritual=False,
                         school=SpellSchools.Divination,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a bit of bat fur",
                         duration="Concentration, up to 1 hour",
                         description="You create an invisible, magical eye within range that hovers in the air for the duration. You mentally receive visual information from the eye, which has normal vision and darkvision out to 30 feet. The eye can look in every direction. As an action, you can move the eye up to 30 feet in any direction. There is no limit to how far away from you the eye can move, but it can't enter another plane of existence. A solid barrier blocks the eye's movement, but the eye can pass through an opening as small as 1 inch in diameter.",
                         at_higher_levels="")


class ArcaneHand(spells.Spell):
    """
    Arcane Hand Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Hand",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="an eggshell and a snakeskin glove",
                         duration="Concentration, up to 1 minute",
                         description="You create a Large hand of shimmering, translucent force in an unoccupied space that you can see within range. The hand lasts for the spell's duration, and it moves at your command, mimicking the movements of your own hand. The hand is an object that has AC 20 and hit points equal to your hit point maximum. If it drops to 0 hit points, the spell ends. It has a Strength of 26 (+8) and a Dexterity of 10 (+0). The hand doesn't fill its space. When you cast the spell and as a bonus action on your subsequent turns, you can move the hand up to 60 feet and then cause one of the following effects with it. Clenched Fist. The hand strikes one creature or object within 5 feet of it. Make a melee spell attack for the hand using your game statistics. On a hit, the target takes 4d8 force damage. Forceful Hand. The hand attempts to push a creature within 5 feet of it in a direction you choose. Make a check with the hand's Strength contested by the Strength (Athletics) check of the target. If the target is Medium or smaller, you have advantage on the check. If you succeed, the hand pushes the target up to 5 feet plus a number of feet equal to five times your spellcasting ability modifier. The hand moves with the target to remain within 5 feet of it. Grasping Hand. The hand attempts to grapple a Huge or smaller creature within 5 feet of it. You use the hand's Strength score to resolve the grapple. If the target is Medium or smaller, you have advantage on the check. While the hand is grappling the target, you can use a bonus action to have the hand crush it. When you do so, the target takes bludgeoning damage equal to 2d6 + your spellcasting ability modifier. Interposing Hand. The hand interposes itself between you and a creature you choose until you give the hand a different command. The hand moves to stay between you and the target, providing you with half cover against the target. The target can't move through the hand's space if its Strength score is less than or equal to the hand's Strength score. If its Strength score is higher than the hand's Strength score, the target can move toward you through the hand's space, but that space is difficult terrain for the target.",
                         at_higher_levels="When you cast this spell using a spell slot of 6th level or higher, the damage from the clenched fist option increases by 2d8 and the damage from the grasping hand increases by 2d6 for each slot level above 5th.")


class ArcaneLock(spells.Spell):
    """
    Arcane Lock Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Lock",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="gold dust worth at least 25 gp, which the spell consumes",
                         duration="Until dispelled",
                         description="You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. You and the creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute. Otherwise, it is impassable until it is broken or the spell is dispelled or suppressed. Casting knock on the object suppresses arcane lock for 10 minutes. While affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.",
                         at_higher_levels="")


class ArcaneSword(spells.Spell):
    """
    Arcane Sword Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcane Sword",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=True,
                         level=7,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a miniature platinum sword with a grip and pommel of copper and zinc, worth 250 gp",
                         duration="Concentration, up to 1 minute",
                         description="You create a sword-shaped plane of force that hovers within range. It lasts for the duration. When the sword appears, you make a melee spell attack against a target of your choice within 5 feet of the sword. On a hit, the target takes 3d10 force damage. Until the spell ends, you can use a bonus action on each of your turns to move the sword up to 20 feet to a spot you can see and repeat this attack against the same target or a different one.",
                         at_higher_levels="")


class ArcanistsMagicAura(spells.Spell):
    """
    Arcanist's Magic Aura Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Arcanist's Magic Aura",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Illusion,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a small square of silk",
                         duration="24 hours",
                         description="You place an illusion on a creature or an object you touch so that divination spells reveal false information about it. The target can be a willing creature or an object that isn't being carried or worn by another creature. When you cast the spell, choose one or both of the following effects. The effect lasts for the duration. If you cast this spell on the same creature or object every day for 30 days, placing the same effect on it each time, the illusion lasts until it is dispelled. False Aura. You change the way the target appears to spells and magical effects, such as detect magic, that detect magical auras. You can make a nonmagical object appear magical, a magical object appear nonmagical, or change the object's magical aura so that it appears to belong to a specific school of magic that you choose. When you use this effect on an object, you can make the false magic apparent to any creature that handles the item. Mask. You change the way the target appears to spells and magical effects that detect creature types, such as a paladin's Divine Sense or the trigger of a symbol spell. You choose a creature type and other spells and magical effects treat the target as if it were a creature of that type or of that alignment.",
                         at_higher_levels="")


class AstralProjection(spells.Spell):
    """
    Astral Projection Spell
    SRD p. 0
    Generated
    """

    def __init__(self):
        super().__init__(name="Astral Projection",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=9,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="10 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="for each creature you affect with this spell, you must provide one jacinth worth at least 1,000 gp and one ornately carved bar of silver worth at least 100 gp, all of which the spell consumes",
                         duration="Special",
                         description="You and up to eight willing creatures within range project your astral bodies into the Astral Plane (the spell fails and the casting is wasted if you are already on that plane). The material body you leave behind is unconscious and in a state of suspended animation; it doesn't need food or air and doesn't age. Your astral body resembles your mortal form in almost every way, replicating your game statistics and possessions. The principal difference is the addition of a silvery cord that extends from between your shoulder blades and trails behind you, fading to invisibility after 1 foot. This cord is your tether to your material body. As long as the tether remains intact, you can find your way home. If the cord is cut—something that can happen only when an effect specifically states that it does—your soul and body are separated, killing you instantly. Your astral form can freely travel through the Astral Plane and can pass through portals there leading to any other plane. If you enter a new plane or return to the plane you were on when casting this spell, your body and possessions are transported along the silver cord, allowing you to re-enter your body as you enter the new plane. Your astral form is a separate incarnation. Any damage or other effects that apply to it have no effect on your physical body, nor do they persist when you return to it. The spell ends for you and your companions when you use your action to dismiss it. When the spell ends, the affected creature returns to its physical body, and it awakens. The spell might also end early for you or one of your companions. A successful dispel magic spell used against an astral or physical body ends the spell for that creature. If a creature's original body or its astral form drops to 0 hit points, the spell ends for that creature. If the spell ends and the silver cord is intact, the cord pulls the creature's astral form back to its body, ending its state of suspended animation. If you are returned to your body prematurely, your companions remain in their astral forms and must find their own way back to their bodies, usually by dropping to 0 hit points.",
                         at_higher_levels="")


class Augury(spells.Spell):
    """
    Augury Spell
    SRD p. 120
    """

    def __init__(self):
        super().__init__(name="Augury",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         casting_time="1 minute",
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="specially marked sticks, bones, or similar tokens worth at least "
                                                  "25 gp",
                         description="By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, "
                                     "or employing some other divining tool, you receive an omen from an otherworldly "
                                     "entity about the results of a specific course of action that you plan to take "
                                     "within the next 30 minutes. The DM chooses from the following possible omens:\n"
                                     "• Weal, for good results\n"
                                     "• Woe, for bad results\n"
                                     "• Weal and woe, for both good and bad results\n"
                                     "• Nothing, for results that aren't especially good or bad\n"
                                     "The spell doesn't take into account any possible circumstances that might "
                                     "change the outcome, such as the casting of additional spells or the loss or "
                                     "gain of a companion.\n"
                                     "If you cast the spell two or more times before completing your next long rest, "
                                     "there is a cumulative 25 percent chance for each casting after the first that "
                                     "you get a random reading. The DM makes this roll in secret.")


class Awaken(spells.Spell):
    """
    Awaken Spell
    SRD p. 121
    Generated
    """

    def __init__(self):
        super().__init__(name="Awaken",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=False,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Transmutation,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="an agate worth at least 1,000 gp, which the spell consumes",
                         duration="Instantaneous",
                         description="After spending the casting time tracing magical pathways within a precious gemstone, you touch a Huge or smaller beast or plant. The target must have either no Intelligence score or an Intelligence of 3 or less. The target gains an Intelligence of 10. The target also gains the ability to speak one language you know. If the target is a plant, it gains the ability to move its limbs, roots, vines, creepers, and so forth, and it gains senses similar to a human's. Your GM chooses statistics appropriate for the awakened plant, such as the statistics for the awakened shrub or the awakened tree. The awakened beast or plant is charmed by you for 30 days or until you or your companions do anything harmful to it. When the charmed condition ends, the awakened creature chooses whether to remain friendly to you, based on how you treated it while it was charmed.",
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
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a drop of blood",
                         duration="Concentration, up to 1 minute",
                         description="Up to three creatures of your choice that you can see within range must make Charisma saving throws. Whenever a target that fails this saving throw makes an attack roll or a saving throw before the spell ends, the target must roll a d4 and subtract the number rolled from the attack roll or saving throw.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.")


class Banishment(spells.Spell):
    """
    Banishment Spell
    SRD p. 121-122
    Generated
    """

    def __init__(self):
        super().__init__(name="Banishment",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=4,
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="an item distasteful to the target",
                         duration="Concentration, up to 1 minute",
                         description="You attempt to send one creature that you can see within range to another plane of existence. The target must succeed on a Charisma saving throw or be banished. If the target is native to the plane of existence you're on, you banish the target to a harmless demiplane. While there, the target is incapacitated. The target remains there until the spell ends, at which point the target reappears in the space it left or in the nearest unoccupied space if that space is occupied. If the target is native to a different plane of existence than the one you're on, the target is banished with a faint popping noise, returning to its home plane. If the spell ends before 1 minute has passed, the target reappears in the space it left or in the nearest unoccupied space if that space is occupied. Otherwise, the target doesn't return.",
                         at_higher_levels="When you cast this spell using a spell slot of 5th level or higher, you can target one additional creature for each slot level above 4th.")


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
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 minute",
                         description="This spell bestows hope and vitality. Choose any number of creatures within range. For the duration, each target has advantage on Wisdom saving throws and death saving throws, and regains the maximum number of hit points possible from any healing.",
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
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 minute",
                         description="You touch a creature, and that creature must succeed on a Wisdom saving throw or become cursed for the duration of the spell. When you cast this spell, choose the nature of the curse from the following options: • Choose one ability score. While cursed, the target has disadvantage on ability checks and saving throws made with that ability score. • While cursed, the target has disadvantage on attack rolls against you. • While cursed, the target must make a Wisdom saving throw at the start of each of its turns. If it fails, it wastes its action that turn doing nothing. • While the target is cursed, your attacks and spells deal an extra 1d8 necrotic damage to the target. A remove curse spell ends this effect. At the GM's option, you may choose an alternative curse effect, but it should be no more powerful than those described above. The GM has final say on such a curse's effect.",
                         at_higher_levels="If you cast this spell using a spell slot of 4th level or higher, the duration is concentration, up to 10 minutes. If you use a spell slot of 5th level or higher, the duration is 8 hours. If you use a spell slot of 7th level or higher, the duration is 24 hours. If you use a 9th level spell slot, the spell lasts until it is dispelled. Using a spell slot of 5th level or higher grants a duration that doesn't require concentration.")


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
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a piece of tentacle from a giant octopus or a giant squid",
                         duration="Concentration, up to 1 minute",
                         description="Squirming, ebony tentacles fill a 20-foot square on ground that you can see within range. For the duration, these tentacles turn the ground in the area into difficult terrain. When a creature enters the affected area for the first time on a turn or starts its turn there, the creature must succeed on a Dexterity saving throw or take 3d6 bludgeoning damage and be restrained by the tentacles until the spell ends. A creature that starts its turn in the area and is already restrained by the tentacles takes 3d6 bludgeoning damage. A creature restrained by the tentacles can use its action to make a Strength or Dexterity check (its choice) against your spell save DC. On a success, it frees itself.",
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
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 10 minutes",
                         description="You create a vertical wall of whirling, razor-sharp blades made of magical energy. The wall appears within range and lasts for the duration. You can make a straight wall up to 100 feet long, 20 feet high, and 5 feet thick, or a ringed wall up to 60 feet in diameter, 20 feet high, and 5 feet thick. The wall provides three-quarters cover to creatures behind it, and its space is difficult terrain. When a creature enters the wall's area for the first time on a turn or starts its turn there, the creature must make a Dexterity saving throw. On a failed save, the creature takes 6d10 slashing damage. On a successful save, the creature takes half as much damage.",
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
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a sprinkling of holy water",
                         duration="Concentration, up to 1 minute",
                         description="You bless up to three creatures of your choice within range. Whenever a target makes an attack roll or a saving throw before the spell ends, the target can roll a d4 and add the number rolled to the attack roll or saving throw.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.")


class Blight(spells.Spell):
    """
    Blight Spell
    SRD p. 123
    Generated
    """

    def __init__(self):
        super().__init__(name="Blight",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=4,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Instantaneous",
                         description="Necromantic energy washes over a creature of your choice that you can see within range, draining moisture and vitality from it. The target must make a Constitution saving throw. The target takes 8d8 necrotic damage on a failed save, or half as much damage on a successful one. This spell has no effect on undead or constructs. If you target a plant creature or a magical plant, it makes the saving throw with disadvantage, and the spell deals maximum damage to it. If you target a nonmagical plant that isn't a creature, such as a tree or shrub, it doesn't make a saving throw; it simply withers and dies.",
                         at_higher_levels="When you cast this spell using a spell slot of 5th level or higher, the damage increases by 1d8 for each slot level above 4th.")


class BlindnessDeafness(spells.Spell):
    """
    Blindness/Deafness Spell
    SRD p. 123
    Generated
    """

    def __init__(self):
        super().__init__(name="Blindness/Deafness",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="False",
                         material_components_list="",
                         duration="1 minute",
                         description="You can blind or deafen a foe. Choose one creature that you can see within range to make a Constitution saving throw. If it fails, the target is either blinded or deafened (your choice) for the duration. At the end of each of its turns, the target can make a Constitution saving throw. On a success, the spell ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.")


class Blink(spells.Spell):
    """
    Blink Spell
    SRD p. 123-124
    Generated
    """

    def __init__(self):
        super().__init__(name="Blink",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=3,
                         ritual=False,
                         school=SpellSchools.Transmutation,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="1 minute",
                         description="Roll a d20 at the end of each of your turns for the duration of the spell. On a roll of 11 or higher, you vanish from your current plane of existence and appear in the Ethereal Plane (the spell fails and the casting is wasted if you were already on that plane). At the start of your next turn, and when the spell ends if you are on the Ethereal Plane, you return to an unoccupied space of your choice that you can see within 10 feet of the space you vanished from. If no unoccupied space is available within that range, you appear in the nearest unoccupied space (chosen at random if more than one space is equally near). You can dismiss this spell as an action. While on the Ethereal Plane, you can see and hear the plane you originated from, which is cast in shades of gray, and you can't see anything there more than 60 feet away. You can only affect and be affected by other creatures on the Ethereal Plane. Creatures that aren't there can't perceive you or interact with you, unless they have the ability to do so.",
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
                         ritual=False,
                         school=SpellSchools.Illusion,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="False",
                         material_components_list="",
                         duration="Concentration, up to 1 minute",
                         description="Your body becomes blurred, shifting and wavering to all who can see you. For the duration, any creature has disadvantage on attack rolls against you. An attacker is immune to this effect if it doesn't rely on sight, as with blindsight, or can see through illusions, as with truesight.",
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
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="False",
                         material_components_list="",
                         duration="Concentration, up to 1 minute",
                         description="The next time you hit a creature with a weapon attack before this spell ends, the weapon gleams with astral radiance as you strike. The attack deals an extra 2d6 radiant damage to the target, which becomes visible if it's invisible, and the target sheds dim light in a 5-foot radius and can't become invisible until the spell ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, the extra damage increases by 1d6 for each slot level above 2nd.")


class BurningHands(spells.Spell):
    """
    Burning Hands Spell
    SRD p. 124
    Generated
    """

    def __init__(self):
        super().__init__(name="Burning Hands",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=1,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="Self (15-foot cone)",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Instantaneous",
                         description="As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one. The fire ignites any flammable objects in the area that aren't being worn or carried.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.")


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
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="120 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 10 minutes",
                         description="A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 60-foot radius, centered on a point you can see 100 feet directly above you. The spell fails if you can't see a point in the air where the storm cloud could appear (for example, if you are in a room that can't accommodate the cloud). When you cast the spell, choose a point you can see within range. A bolt of lightning flashes down from the cloud to that point. Each creature within 5 feet of that point must make a Dexterity saving throw. A creature takes 3d10 lightning damage on a failed save, or half as much damage on a successful one. On each of your turns until the spell ends, you can use your action to call down lightning in this way again, targeting the same point or a different one. If you are outdoors in stormy conditions when you cast this spell, the spell gives you control over the existing storm instead of creating a new one. Under such conditions, the spell's damage increases by 1d10.",
                         at_higher_levels="When you cast this spell using a spell slot of 4th or higher level, the damage increases by 1d10 for each slot level above 3rd.")


class CalmEmotions(spells.Spell):
    """
    Calm Emotions Spell
    SRD p. 124-125
    Generated
    """

    def __init__(self):
        super().__init__(name="Calm Emotions",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 minute",
                         description="You attempt to suppress strong emotions in a group of people. Each humanoid in a 20-foot-radius sphere centered on a point you choose within range must make a Charisma saving throw; a creature can choose to fail this saving throw if it wishes. If a creature fails its saving throw, choose one of the following two effects. You can suppress any effect causing a target to be charmed or frightened. When this spell ends, any suppressed effect resumes, provided that its duration has not expired in the meantime. Alternatively, you can make a target indifferent about creatures of your choice that it is hostile toward. This indifference ends if the target is attacked or harmed by a spell or if it witnesses any of its friends being harmed. When the spell ends, the creature becomes hostile again, unless the GM rules otherwise.",
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
                         concentration=False,
                         level=6,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="150 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a bit of fur; a piece of amber, glass, or a crystal rod; and three silver pins",
                         duration="Instantaneous",
                         description="You create a bolt of lightning that arcs toward a target of your choice that you can see within range. Three bolts then leap from that target to as many as three other targets, each of which must be within 30 feet of the first target. A target can be a creature or an object and can be targeted by only one of the bolts. A target must make a Dexterity saving throw. The target takes 10d8 lightning damage on a failed save, or half as much damage on a successful one.",
                         at_higher_levels="When you cast this spell using a spell slot of 7th level or higher, one additional bolt leaps from the first target to another target for each slot level above 6th.")


class CharmPerson(spells.Spell):
    """
    Charm Person Spell
    SRD p. 125
    Generated
    """

    def __init__(self):
        super().__init__(name="Charm Person",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=1,
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="1 hour",
                         description="You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, and does so with advantage if you or your companions are fighting it. If it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it. The charmed creature regards you as a friendly acquaintance. When the spell ends, the creature knows it was charmed by you.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.")


class CircleOfDeath(spells.Spell):
    """
    Circle of Death Spell
    SRD p. 125
    Generated
    """

    def __init__(self):
        super().__init__(name="Circle of Death",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=6,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="150 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="the powder of a crushed black pearl worth at least 500 gp",
                         duration="Instantaneous",
                         description="A sphere of negative energy ripples out in a 60-footradius sphere from a point within range. Each creature in that area must make a Constitution saving throw. A target takes 8d6 necrotic damage on a failed save, or half as much damage on a successful one.",
                         at_higher_levels="When you cast this spell using a spell slot of 7th level or higher, the damage increases by 2d6 for each slot level above 6th.")


class Clairvoyance(spells.Spell):
    """
    Clairvoyance Spell
    SRD p. 125-126
    Generated
    """

    def __init__(self):
        super().__init__(name="Clairvoyance",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=True,
                         level=3,
                         ritual=False,
                         school=SpellSchools.Divination,
                         spell_range="1 mile",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for seeing",
                         duration="Concentration, up to 10 minutes",
                         description="You create an invisible sensor within range in a location familiar to you (a place you have visited or seen before) or in an obvious location that is unfamiliar to you (such as behind a door, around a corner, or in a grove of trees). The sensor remains in place for the duration, and it can't be attacked or otherwise interacted with. When you cast the spell, you choose seeing or hearing. You can use the chosen sense through the sensor as if you were in its space. As your action, you can switch between seeing and hearing. A creature that can see the sensor (such as a creature benefiting from see invisibility or truesight) sees a luminous, intangible orb about the size of your fist.",
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
                         concentration=False,
                         level=8,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a diamond worth at least 1,000 gp and at least 1 cubic inch of flesh of the creature that is to be cloned, which the spell consumes, and a vessel worth at least 2,000 gp that has a sealable lid and is large enough to hold a Medium creature, such as a huge urn, coffin, mudfilled cyst in the ground, or crystal container filled with salt water",
                         duration="Instantaneous",
                         description="This spell grows an inert duplicate of a living creature as a safeguard against death. This clone forms inside a sealed vessel and grows to full size and maturity after 120 days; you can also choose to have the clone be a younger version of the same creature. It remains inert and endures indefinitely, as long as its vessel remains undisturbed. At any time after the clone matures, if the original creature dies, its soul transfers to the clone, provided that the soul is free and willing to return. The clone is physically identical to the original and has the same personality, memories, and abilities, but none of the original's equipment. The original creature's physical remains, if they still exist, become inert and can't thereafter be restored to life, since the creature's soul is elsewhere.",
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
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="120 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 10 minutes",
                         description="You create a 20-foot-radius sphere of poisonous, yellow-green fog centered on a point you choose within range. The fog spreads around corners. It lasts for the duration or until strong wind disperses the fog, ending the spell. Its area is heavily obscured. When a creature enters the spell's area for the first time on a turn or starts its turn there, that creature must make a Constitution saving throw. The creature takes 5d8 poison damage on a failed save, or half as much damage on a successful one. Creatures are affected even if they hold their breath or don't need to breathe. The fog moves 10 feet away from you at the start of each of your turns, rolling along the surface of the ground. The vapors, being heavier than air, sink to the lowest level of the land, even pouring down openings.",
                         at_higher_levels="When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th.")


class ColorSpray(spells.Spell):
    """
    Color Spray Spell
    SRD p. 126
    Generated
    """

    def __init__(self):
        super().__init__(name="Color Spray",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=1,
                         ritual=False,
                         school=SpellSchools.Illusion,
                         spell_range="Self (15-foot cone)",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a pinch of powder or sand that is colored red, yellow, and blue",
                         duration="1 round",
                         description="A dazzling array of flashing, colored light springs from your hand. Roll 6d10; the total is how many hit points of creatures this spell can effect. Creatures in a 15-foot cone originating from you are affected in ascending order of their current hit points (ignoring unconscious creatures and creatures that can't see). Starting with the creature that has the lowest current hit points, each creature affected by this spell is blinded until the spell ends. Subtract each creature's hit points from the total before moving on to the creature with the next lowest hit points. A creature's hit points must be equal to or less than the remaining total for that creature to be affected.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, roll an additional 2d10 for each slot level above 1st.")


class Command(spells.Spell):
    """
    Command Spell
    SRD p. 126-127
    Generated
    """

    def __init__(self):
        super().__init__(name="Command",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=1,
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="False",
                         material_components_list="",
                         duration="1 round",
                         description="You speak a one-word command to a creature you can see within range. The target must succeed on a Wisdom saving throw or follow the command on its next turn. The spell has no effect if the target is undead, if it doesn't understand your language, or if your command is directly harmful to it. Some typical commands and their effects follow. You might issue a command other than one described here. If you do so, the GM determines how the target behaves. If the target can't follow your command, the spell ends. Approach. The target moves toward you by the shortest and most direct route, ending its turn if it moves within 5 feet of you. Drop. The target drops whatever it is holding and then ends its turn. Flee. The target spends its turn moving away from you by the fastest available means. Grovel. The target falls prone and then ends its turn. Halt. The target doesn't move and takes no actions. A flying creature stays aloft, provided that it is able to do so. If it must move to stay aloft, it flies the minimum distance needed to remain in the air.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.")


class Commune(spells.Spell):
    """
    Commune Spell
    SRD p. 127
    Generated
    """

    def __init__(self):
        super().__init__(name="Commune",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=5,
                         ritual=True,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="incense and a vial of holy or unholy water",
                         duration="1 minute",
                         description="You contact your deity or a divine proxy and ask up to three questions that can be answered with a yes or no. You must ask your questions before the spell ends. You receive a correct answer for each question. Divine beings aren't necessarily omniscient, so you might receive “unclear” as an answer if a question pertains to information that lies beyond the deity's knowledge. In a case where a one-word answer could be misleading or contrary to the deity's interests, the GM might offer a short phrase as an answer instead. If you cast the spell two or more times before finishing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get no answer. The GM makes this roll in secret.",
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
                         concentration=False,
                         level=5,
                         ritual=True,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Instantaneous",
                         description="You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. The spell doesn't function where nature has been replaced by construction, such as in dungeons and towns. You instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area: • terrain and bodies of water • prevalent plants, minerals, animals, or peoples • powerful celestials, fey, fiends, elementals, or undead • influence from other planes of existence • buildings For example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns.",
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
                         concentration=False,
                         level=1,
                         ritual=True,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a pinch of soot and salt",
                         duration="1 hour",
                         description="For the duration, you understand the literal meaning of any spoken language that you hear. You also understand any written language that you see, but you must be touching the surface on which the words are written. It takes about 1 minute to read one page of text. This spell doesn't decode secret messages in a text or a glyph, such as an arcane sigil, that isn't part of a written language.",
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
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 minute",
                         description="Creatures of your choice that you can see within range and that can hear you must make a Wisdom saving throw. A target automatically succeeds on this saving throw if it can't be charmed. On a failed save, a target is affected by this spell. Until the spell ends, you can use a bonus action on each of your turns to designate a direction that is horizontal to you. Each affected target must use as much of its movement as possible to move in that direction on its next turn. It can take its action before it moves. After moving in this way, it can make another Wisdom saving to try to end the effect. A target isn't compelled to move into an obviously deadly hazard, such as a fire or pit, but it will provoke opportunity attacks to move in the designated direction.",
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
                         concentration=False,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="Self (60-foot cone)",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a small crystal or glass cone",
                         duration="Instantaneous",
                         description="A blast of cold air erupts from your hands. Each creature in a 60-foot cone must make a Constitution saving throw. A creature takes 8d8 cold damage on a failed save, or half as much damage on a successful one. A creature killed by this spell becomes a frozen statue until it thaws.",
                         at_higher_levels="When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th.")


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
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="three nut shells",
                         duration="Concentration, up to 1 minute",
                         description="This spell assaults and twists creatures' minds, spawning delusions and provoking uncontrolled action. Each creature in a 10-foot-radius sphere centered on a point you choose within range must succeed on a Wisdom saving throw when you cast this spell or be affected by it. An affected target can't take reactions and must roll a d10 at the start of each of its turns to determine its behavior for that turn. d10 Behavior 1 The creature uses all its movement to move in a random direction. To determine the direction, roll a d8 and assign a direction to each die face. The creature doesn't take an action this turn. 2–6 The creature doesn't move or take actions this turn. 7–8 The creature uses its action to make a melee attack against a randomly determined creature within its reach. If there is no creature within its reach, the creature does nothing this turn. 9–10 The creature can act and move normally. At the end of each of its turns, an affected target can make a Wisdom saving throw. If it succeeds, this effect ends for that target.",
                         at_higher_levels="When you cast this spell using a spell slot of 5th level or higher, the radius of the sphere increases by 5 feet for each slot level above 4th.")


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
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 hour",
                         description="You summon fey spirits that take the form of beasts and appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears: • One beast of challenge rating 2 or lower • Two beasts of challenge rating 1 or lower • Four beasts of challenge rating 1/2 or lower • Eight beasts of challenge rating 1/4 or lower Each beast is also considered fey, and it disappears when it drops to 0 hit points or when the spell ends. The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions. The GM has the creatures' statistics.",
                         at_higher_levels="When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 5th-level slot, three times as many with a 7th-level slot, and four times as many with a 9th-level slot.")


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
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 hour",
                         description="You summon a celestial of challenge rating 4 or lower, which appears in an unoccupied space that you can see within range. The celestial disappears when it drops to 0 hit points or when the spell ends. The celestial is friendly to you and your companions for the duration. Roll initiative for the celestial, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you), as long as they don't violate its alignment. If you don't issue any commands to the celestial, it defends itself from hostile creatures but otherwise takes no actions. The GM has the celestial's statistics.",
                         at_higher_levels="When you cast this spell using a 9th-level spell slot, you summon a celestial of challenge rating 5 or lower.")


class ConjureElemental(spells.Spell):
    """
    Conjure Elemental Spell
    SRD p. 129
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Elemental",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="burning incense for air, soft clay for earth, sulfur and phosphorus for fire, or water and sand for water",
                         duration="Concentration, up to 1 hour",
                         description="You call forth an elemental servant. Choose an area of air, earth, fire, or water that fills a 10-foot cube within range. An elemental of challenge rating 5 or lower appropriate to the area you chose appears in an unoccupied space within 10 feet of it. For example, a fire elemental emerges from a bonfire, and an earth elemental rises up from the ground. The elemental disappears when it drops to 0 hit points or when the spell ends. The elemental is friendly to you and your companions for the duration. Roll initiative for the elemental, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the elemental, it defends itself from hostile creatures but otherwise takes no actions. If your concentration is broken, the elemental doesn't disappear. Instead, you lose control of the elemental, it becomes hostile toward you and your companions, and it might attack. An uncontrolled elemental can't be dismissed by you, and it disappears 1 hour after you summoned it. The GM has the elemental's statistics.",
                         at_higher_levels="When you cast this spell using a spell slot of 6th level or higher, the challenge rating increases by 1 for each slot level above 5th.")


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
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 hour",
                         description="You summon a fey creature of challenge rating 6 or lower, or a fey spirit that takes the form of a beast of challenge rating 6 or lower. It appears in an unoccupied space that you can see within range. The fey creature disappears when it drops to 0 hit points or when the spell ends. The fey creature is friendly to you and your companions for the duration. Roll initiative for the creature, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you), as long as they don't violate its alignment. If you don't issue any commands to the fey creature, it defends itself from hostile creatures but otherwise takes no actions. If your concentration is broken, the fey creature doesn't disappear. Instead, you lose control of the fey creature, it becomes hostile toward you and your companions, and it might attack. An uncontrolled fey creature can't be dismissed by you, and it disappears 1 hour after you summoned it. The GM has the fey creature's statistics.",
                         at_higher_levels="When you cast this spell using a spell slot of 7th level or higher, the challenge rating increases by 1 for each slot level above 6th.")


class ConjureMinorElementals(spells.Spell):
    """
    Conjure Minor Elementals Spell
    SRD p. 129-130
    Generated
    """

    def __init__(self):
        super().__init__(name="Conjure Minor Elementals",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="90 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 1 hour",
                         description="You summon elementals that appear in unoccupied spaces that you can see within range. You choose one the following options for what appears: • One elemental of challenge rating 2 or lower • Two elementals of challenge rating 1 or lower • Four elementals of challenge rating 1/2 or lower • Eight elementals of challenge rating 1/4 or lower. An elemental summoned by this spell disappears when it drops to 0 hit points or when the spell ends. The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions. The GM has the creatures' statistics.",
                         at_higher_levels="When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot.")


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
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="one holly berry per creature summoned",
                         duration="Concentration, up to 1 hour",
                         description="You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears: • One fey creature of challenge rating 2 or lower • Two fey creatures of challenge rating 1 or lower • Four fey creatures of challenge rating 1/2 or lower • Eight fey creatures of challenge rating 1/4 or lower A summoned creature disappears when it drops to 0 hit points or when the spell ends. The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which have their own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions. The GM has the creatures' statistics.",
                         at_higher_levels="When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot.")


class ContactOtherPlane(spells.Spell):
    """
    Contact Other Plane Spell
    SRD p. 130
    Generated
    """

    def __init__(self):
        super().__init__(name="Contact Other Plane",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=5,
                         ritual=True,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="False",
                         material_components_list="",
                         duration="1 minute",
                         description="You mentally contact a demigod, the spirit of a longdead sage, or some other mysterious entity from another plane. Contacting this extraplanar intelligence can strain or even break your mind. When you cast this spell, make a DC 15 Intelligence saving throw. On a failure, you take 6d6 psychic damage and are insane until you finish a long rest. While insane, you can't take actions, can't understand what other creatures say, can't read, and speak only in gibberish. A greater restoration spell cast on you ends this effect. On a successful save, you can ask the entity up to five questions. You must ask your questions before the spell ends. The GM answers each question with one word, such as “yes,” “no,” “maybe,” “never,” “irrelevant,” or “unclear” (if the entity doesn't know the answer to the question). If a one-word answer would be misleading, the GM might instead offer a short phrase as an answer.",
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
                         concentration=False,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="7 days",
                         description="Your touch inflicts disease. Make a melee spell attack against a creature within your reach. On a hit, you afflict the creature with a disease of your choice from any of the ones described below. At the end of each of the target's turns, it must make a Constitution saving throw. After failing three of these saving throws, the disease's effects last for the duration, and the creature stops making these saves. After succeeding on three of these saving throws, the creature recovers from the disease, and the spell ends. Since this spell induces a natural disease in its target, any effect that removes a disease or otherwise ameliorates a disease's effects apply to it. Blinding Sickness. Pain grips the creature's mind, and its eyes turn milky white. The creature has disadvantage on Wisdom checks and Wisdom saving throws and is blinded. Filth Fever. A raging fever sweeps through the creature's body. The creature has disadvantage on Strength checks, Strength saving throws, and attack rolls that use Strength. Flesh Rot. The creature's flesh decays. The creature has disadvantage on Charisma checks and vulnerability to all damage. Mindfire. The creature's mind becomes feverish. The creature has disadvantage on Intelligence checks and Intelligence saving throws, and the creature behaves as if under the effects of the confusion spell during combat. Seizure. The creature is overcome with shaking. The creature has disadvantage on Dexterity checks, Dexterity saving throws, and attack rolls that use Dexterity. Slimy Doom. The creature begins to bleed uncontrollably. The creature has disadvantage on Constitution checks and Constitution saving throws. In addition, whenever the creature takes damage, it is stunned until the end of its next turn.",
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
                         concentration=False,
                         level=6,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a statuette of yourself carved from ivory and decorated with gems worth at least 1,500 gp",
                         duration="10 days",
                         description="Choose a spell of 5th level or lower that you can cast, that has a casting time of 1 action, and that can target you. You cast that spell—called the contingent spell—as part of casting contingency, expending spell slots for both, but the contingent spell doesn't come into effect. Instead, it takes effect when a certain circumstance occurs. You describe that circumstance when you cast the two spells. For example, a contingency cast with water breathing might stipulate that water breathing comes into effect when you are engulfed in water or a similar liquid. The contingent spell takes effect immediately after the circumstance is met for the first time, whether or not you want it to, and then contingency ends. The contingent spell takes effect only on you, even if it can normally target others. You can use only one contingency spell at a time. If you cast this spell again, the effect of another contingency spell on you ends. Also, contingency ends on you if its material component is ever not on your person.",
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
                         concentration=False,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="ruby dust worth 50 gp, which the spell consumes",
                         duration="Until dispelled",
                         description="A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The effect looks like a regular flame, but it creates no heat and doesn't use oxygen. A continual flame can be covered or hidden but not smothered or quenched.",
                         at_higher_levels="")


class ControlWater(spells.Spell):
    """
    Control Water Spell
    SRD p. 131-132
    Generated
    """

    def __init__(self):
        super().__init__(name="Control Water",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=4,
                         ritual=False,
                         school=SpellSchools.Transmutation,
                         spell_range="300 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a drop of water and a pinch of dust",
                         duration="Concentration, up to 10 minutes",
                         description="Until the spell ends, you control any freestanding water inside an area you choose that is a cube up to 100 feet on a side. You can choose from any of the following effects when you cast this spell. As an action on your turn, you can repeat the same effect or choose a different one. Flood. You cause the water level of all standing water in the area to rise by as much as 20 feet. If the area includes a shore, the flooding water spills over onto dry land. If you choose an area in a large body of water, you instead create a 20-foot tall wave that travels from one side of the area to the other and then crashes down. Any Huge or smaller vehicles in the wave's path are carried with it to the other side. Any Huge or smaller vehicles struck by the wave have a 25 percent chance of capsizing. The water level remains elevated until the spell ends or you choose a different effect. If this effect produced a wave, the wave repeats on the start of your next turn while the flood effect lasts. Part Water. You cause water in the area to move apart and create a trench. The trench extends across the spell's area, and the separated water forms a wall to either side. The trench remains until the spell ends or you choose a different effect. The water then slowly fills in the trench over the course of the next round until the normal water level is restored. Redirect Flow. You cause flowing water in the area to move in a direction you choose, even if the water has to flow over obstacles, up walls, or in other unlikely directions. The water in the area moves as you direct it, but once it moves beyond the spell's area, it resumes its flow based on the terrain conditions. The water continues to move in the direction you chose until the spell ends or you choose a different effect. Whirlpool. This effect requires a body of water at least 50 feet square and 25 feet deep. You cause a whirlpool to form in the center of the area. The whirlpool forms a vortex that is 5 feet wide at the base, up to 50 feet wide at the top, and 25 feet tall. Any creature or object in the water and within 25 feet of the vortex is pulled 10 feet toward it. A creature can swim away from the vortex by making a Strength (Athletics) check against your spell save DC. When a creature enters the vortex for the first time on a turn or starts its turn there, it must make a Strength saving throw. On a failed save, the creature takes 2d8 bludgeoning damage and is caught in the vortex until the spell ends. On a successful save, the creature takes half damage, and isn't caught in the vortex. A creature caught in the vortex can use its action to try to swim away from the vortex as described above, but has disadvantage on the Strength (Athletics) check to do so. The first time each turn that an object enters the vortex, the object takes 2d8 bludgeoning damage; this damage occurs each round it remains in the vortex.",
                         at_higher_levels="")


class ControlWeather(spells.Spell):
    """
    Control Weather Spell
    SRD p. 132
    Generated
    """

    def __init__(self):
        super().__init__(name="Control Weather",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=True,
                         level=8,
                         ritual=False,
                         school=SpellSchools.Transmutation,
                         spell_range="Self (5-mile radius)",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="burning incense and bits of earth and wood mixed in water",
                         duration="Concentration, up to 8 hours",
                         description="You take control of the weather within 5 miles of you for the duration. You must be outdoors to cast this spell. Moving to a place where you don't have a clear path to the sky ends the spell early. When you cast the spell, you change the current weather conditions, which are determined by the GM based on the climate and season. You can change precipitation, temperature, and wind. It takes 1d4 × 10 minutes for the new conditions to take effect. Once they do so, you can change the conditions again. When the spell ends, the weather gradually returns to normal. When you change the weather conditions, find a current condition on the following tables and change its stage by one, up or down. When changing the wind, you can change its direction. Precipitation Stage Condition 1 Clear 2 Light clouds 3 Overcast or ground fog 4 Rain, hail, or snow 5 Torrential rain, driving hail, or blizzard Temperature Stage Condition 1 Unbearable heat 2 Hot 3 Warm 4 Cool 5 Cold 6 Arctic cold Wind Stage Condition 1 Calm 2 Moderate wind 3 Strong wind 4 Gale 5 Storm",
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
                         concentration=False,
                         level=3,
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="60 feet",
                         verbal_components="False",
                         somatic_components="True",
                         material_components_list="",
                         duration="Instantaneous",
                         description="You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a success, the creature's spell fails and has no effect.",
                         at_higher_levels="When you cast this spell using a spell slot of 4th level or higher, the interrupted spell has no effect if its level is less than or equal to the level of the spell slot you used.")


class CreateFoodAndWater(spells.Spell):
    """
    Create Food and Water Spell
    SRD p. 132-133
    Generated
    """

    def __init__(self):
        super().__init__(name="Create Food and Water",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=3,
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Instantaneous",
                         description="You create 45 pounds of food and 30 gallons of water on the ground or in containers within range, enough to sustain up to fifteen humanoids or five steeds for 24 hours. The food is bland but nourishing, and spoils if uneaten after 24 hours. The water is clean and doesn't go bad.",
                         at_higher_levels="")


class ChillTouch(spells.Spell):
    """
    Chill Touch Spell
    SRD p. 124
    """

    def __init__(self):
        super().__init__(name="Chill Touch",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.NECROMANCY,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         duration="1 round",
                         description="You create a ghostly, skeletal hand in the space of a creature within range. "
                                     "Make a ranged spell attack against the creature to assail it with the chill of "
                                     "the grave. On a hit, the target takes 1d8 necrotic damage, and it can't regain "
                                     "hit points until the start of your next turn. Until then, the hand clings to "
                                     "the target.\n"
                                     "If you hit an undead target, it also has disadvantage on attack rolls against "
                                     "you until the end of your next turn.\n"
                                     "This spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level "
                                     "(3d8), and 17th level (4d8).")


class CreateOrDestroyWater(spells.Spell):
    """
    Create or Destroy Water Spell
    SRD p. 132
    """

    def __init__(self):
        super().__init__(name="Create or Destroy Water",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of water if creating water or a few grains of sand if "
                                                  "destroying it",
                         description="You either create or destroy water.\n"
                                     "Create Water. You create up to 10 gallons of clean water within range in an "
                                     "open container. Alternatively, the water falls as rain in a 30-foot cube within "
                                     "range, extinguishing exposed flames in the area.\n"
                                     "Destroy Water. You destroy up to 10 gallons of water in an open container "
                                     "within range. Alternatively, you destroy fog in a 30-foot cube within range.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you create or destroy 10 additional gallons of water, or the size of the "
                                          "cube increases by 5 feet, for each slot level above 1st.")


class CreateUndead(spells.Spell):
    """
    Create Undead Spell
    SRD p. 133
    Generated
    """

    def __init__(self):
        super().__init__(name="Create Undead",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=6,
                         ritual=False,
                         school=SpellSchools.Necromancy,
                         spell_range="10 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="one clay pot filled with grave dirt, one clay pot filled with brackish water, and one 150 gp black onyx stone for each corpse",
                         duration="Instantaneous",
                         description="You can cast this spell only at night. Choose up to three corpses of Medium or Small humanoids within range. Each corpse becomes a ghoul under your control. (The GM has game statistics for these creatures.) As a bonus action on each of your turns, you can mentally command any creature you animated with this spell if the creature is within 120 feet of you (if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one). You decide what action the creature will take and where it will move during its next turn, or you can issue a general command, such as to guard a particular chamber or corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete. The creature is under your control for 24 hours, after which it stops obeying any command you have given it. To maintain control of the creature for another 24 hours, you must cast this spell on the creature before the current 24-hour period ends. This use of the spell reasserts your control over up to three creatures you have animated with this spell, rather than animating new ones.",
                         at_higher_levels="When you cast this spell using a 7th-level spell slot, you can animate or reassert control over four ghouls. When you cast this spell using an 8th-level spell slot, you can animate or reassert control over five ghouls or two ghasts or wights. When you cast this spell using a 9th-level spell slot, you can animate or reassert control over six ghouls, three ghasts or wights, or two mummies.")


class Creation(spells.Spell):
    """
    Creation Spell
    SRD p. 133
    Generated
    """

    def __init__(self):
        super().__init__(name="Creation",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=5,
                         ritual=False,
                         school=SpellSchools.Illusion,
                         spell_range="30 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a tiny piece of matter of the same type of the item you plan to create",
                         duration="Special",
                         description="You pull wisps of shadow material from the Shadowfell to create a nonliving object of vegetable matter within range: soft goods, rope, wood, or something similar. You can also use this spell to create mineral objects such as stone, crystal, or metal. The object created must be no larger than a 5- foot cube, and the object must be of a form and material that you have seen before. The duration depends on the object's material. If the object is composed of multiple materials, use the shortest duration. Material Duration Vegetable matter 1 day Stone or crystal 12 hours Precious metals 1 hour Gems 10 minutes Adamantine or mithral 1 minute Using any material created by this spell as another spell's material component causes that spell to fail.",
                         at_higher_levels="When you cast this spell using a spell slot of 6th level or higher, the cube increases by 5 feet for each slot level above 5th.")


class CureWounds(spells.Spell):
    """
    Cure Wounds Spell
    SRD p. 132-133
    """

    def __init__(self):
        super().__init__(name="Cure Wounds",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.ABJURATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         description="A creature you touch regains a number of hit points equal to 1d8 + your "
                                     "spellcasting ability modifier. This spell has no effect on undead or "
                                     "constructs.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the healing increases by 1d8 for each slot level above 1st.")


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
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="120 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a bit of phosphorus or wychwood, or a glowworm",
                         duration="Concentration, up to 1 minute",
                         description="You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10- foot radius. As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range.",
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
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="False",
                         material_components_list="bat fur and a drop of pitch or piece of coal",
                         duration="Concentration, up to 10 minutes",
                         description="Magical darkness spreads from a point you choose within range to fill a 15-foot-radius sphere for the duration. The darkness spreads around corners. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it. If the point you choose is on an object you are holding or one that isn't being worn or carried, the darkness emanates from the object and moves with it. Completely covering the source of the darkness with an opaque object, such as a bowl or a helm, blocks the darkness. If any of this spell's area overlaps with an area of light created by a spell of 2nd level or lower, the spell that created the light is dispelled.",
                         at_higher_levels="")


class Darkvision(spells.Spell):
    """
    Darkvision Spell
    SRD p. 133
    """

    def __init__(self):
        super().__init__(name="Darkvision",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="either a pinch of dried carrot or an agate",
                         duration="8 hours",
                         description="You touch a willing creature to grant it the ability to see in the dark. For "
                                     "the duration, that creature has darkvision out to a range of 60 feet.")


class Daylight(spells.Spell):
    """
    Daylight Spell
    SRD p. 134
    Generated
    """

    def __init__(self):
        super().__init__(name="Daylight",
                         spell_lists=[SpellLists.PRIMAL],
                         concentration=False,
                         level=3,
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="1 hour",
                         description="A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet. If you chose a point on an object you are holding or one that isn't being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light. If any of this spell's area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled.",
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
                         concentration=False,
                         level=4,
                         ritual=False,
                         school=SpellSchools.Abjuration,
                         spell_range="Touch",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="8 hours",
                         description="You touch a creature and grant it a measure of protection from death. The first time the target would drop to 0 hit points as a result of taking damage, the target instead drops to 1 hit point, and the spell ends. If the spell is still in effect when the target is subjected to an effect that would kill it instantaneously without dealing damage, that effect is instead negated against the target, and the spell ends.",
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
                         ritual=False,
                         school=SpellSchools.Evocation,
                         spell_range="150 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="a tiny ball of bat guano and sulfur",
                         duration="Concentration, up to 1 minute",
                         description="A beam of yellow light flashes from your pointing finger, then condenses to linger at a chosen point within range as a glowing bead for the duration. When the spell ends, either because your concentration is broken or because you decide to end it, the bead blossoms with a low roar into an explosion of flame that spreads around corners. Each creature in a 20-foot-radius sphere centered on that point must make a Dexterity saving throw. A creature takes fire damage equal to the total accumulated damage on a failed save, or half as much damage on a successful one. The spell's base damage is 12d6. If at the end of your turn the bead has not yet detonated, the damage increases by 1d6. If the glowing bead is touched before the interval has expired, the creature touching it must make a Dexterity saving throw. On a failed save, the spell ends immediately, causing the bead to erupt in flame. On a successful save, the creature can throw the bead up to 40 feet. When it strikes a creature or a solid object, the spell ends, and the bead explodes. The fire damages objects in the area and ignites flammable objects that aren't being worn or carried.",
                         at_higher_levels="When you cast this spell using a spell slot of 8th level or higher, the base damage increases by 1d6 for each slot level above 7th.")


class Demiplane(spells.Spell):
    """
    Demiplane Spell
    SRD p. 135
    Generated
    """

    def __init__(self):
        super().__init__(name="Demiplane",
                         spell_lists=[SpellLists.ARCANE],
                         concentration=False,
                         level=8,
                         ritual=False,
                         school=SpellSchools.Conjuration,
                         spell_range="60 feet",
                         verbal_components="False",
                         somatic_components="True",
                         material_components_list="",
                         duration="1 hour",
                         description="You create a shadowy door on a flat solid surface that you can see within range. The door is large enough to allow Medium creatures to pass through unhindered. When opened, the door leads to a demiplane that appears to be an empty room 30 feet in each dimension, made of wood or stone. When the spell ends, the door disappears, and any creatures or objects inside the demiplane remain trapped there, as the door also disappears from the other side. Each time you cast this spell, you can create a new demiplane, or have the shadowy door connect to a demiplane you created with a previous casting of this spell. Additionally, if you know the nature and contents of a demiplane created by a casting of this spell by another creature, you can have the shadowy door connect to its demiplane instead.",
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
                         ritual=False,
                         school=SpellSchools.Divination,
                         spell_range="Self",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="Concentration, up to 10 minutes",
                         description="For the duration, you know if there is an aberration, celestial, elemental, fey, fiend, or undead within 30 feet of you, as well as where the creature is located. Similarly, you know if there is a place or object within 30 feet of you that has been magically consecrated or desecrated. The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.",
                         at_higher_levels="")


class DetectMagic(spells.Spell):
    """
    Detect Magic Spell
    SRD p. 134
    """

    def __init__(self):
        super().__init__(name="Detect Magic",
                         spell_lists=[SpellLists.ARCANE,
                                      SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="For the duration, you sense the presence of magic within 30 feet of you. If you "
                                     "sense magic in this way, you can use your action to see a faint aura around any "
                                     "visible creature or object in the area that bears magic, and you learn its "
                                     "school of magic, if any.\n"
                                     "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, "
                                     "1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.")


class DetectPoisonAndDisease(spells.Spell):
    """
    Detect Poison and Disease Spell
    SRD p. 134
    """

    def __init__(self):
        super().__init__(name="Detect Poison and Disease",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a yew leaf",
                         concentration=True,
                         duration="10 minutes",
                         description="For the duration, you can sense the presence and location of poisons, poisonous "
                                     "creatures, and diseases within 30 feet of you. You also identify the kind of "
                                     "poison, poisonous creature, or disease in each case.\n"
                                     "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, "
                                     "1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.")


class DetectThoughts(spells.Spell):
    """
    False Life Spell
    SRD p. 135
    """

    def __init__(self):
        super().__init__(name="Detect Thoughts",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.DIVINATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a copper piece",
                         concentration=True,
                         duration="1 minute",
                         description="For the duration, you can read the thoughts of certain creatures. When you cast "
                                     "the spell and as your action on each turn until the spell ends, you can focus "
                                     "your mind on any one creature that you can see within 30 feet of you. If the "
                                     "creature you choose has an Intelligence of 3 or lower or doesn't speak any "
                                     "language, the creature is unaffected.\n"
                                     "You initially learn the surface thoughts of the creature—what is most on its "
                                     "mind in that moment. As an action, you can either shift your attention to "
                                     "another creature's thoughts or attempt to probe deeper into the same creature's "
                                     "mind. If you probe deeper, the target must make a Wisdom saving throw. If it "
                                     "fails, you gain insight into its reasoning (if any), its emotional state, "
                                     "and something that looms large in its mind (such as something it worries over, "
                                     "loves, or hates). If it succeeds, the spell ends. Either way, the target knows "
                                     "that you are probing into its mind, and unless you shift your attention to "
                                     "another creature's thoughts, the creature can use its action on its turn to "
                                     "make an Intelligence check contested by your Intelligence check; if it "
                                     "succeeds, the spell ends.\n"
                                     "Questions verbally directed at the target creature naturally shape the course "
                                     "of its thoughts, so this spell is particularly effective as part of an "
                                     "interrogation.\n"
                                     "You can also use this spell to detect the presence of thinking creatures you "
                                     "can't see. When you cast the spell or as your action during the duration, "
                                     "you can search for thoughts within 30 feet of you. The spell can penetrate "
                                     "barriers, but 2 feet of rock, 2 inches of any metal other than lead, "
                                     "or a thin sheet of lead blocks you. You can't detect a creature with an "
                                     "Intelligence of 3 or lower or one that doesn't speak any language.\n"
                                     "Once you detect the presence of a creature in this way, you can read its "
                                     "thoughts for the rest of the duration as described above, even if you can't see "
                                     "it, but it must still be within range.")


class Druidcraft(spells.Spell):
    """
    Druidcraft Spell
    SRD p. 138-139
    """

    def __init__(self):
        super().__init__(name="Druidcraft",
                         spell_lists=[SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="Whispering to the spirits of nature, you create one of the following effects "
                                     "within range:\n"
                                     "• You create a tiny, harmless sensory effect that predicts what the weather "
                                     "will be at your location for the next 24 hours. The effect might manifest as a "
                                     "golden orb for clear skies, a cloud for rain, falling snowflakes for snow, "
                                     "and so on. This effect persists for 1 round.\n"
                                     "• You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.\n"
                                     "• You create an instantaneous, harmless sensory effect, such as falling leaves, "
                                     "a puff of wind, the sound of a small animal, or the faint odor of skunk. The "
                                     "effect must fit in a 5-foot cube.\n"
                                     "• You instantly light or snuff out a candle, a torch, or a small campfire.")


class EnhanceAbility(spells.Spell):
    """
    Enhance Ability Spell
    SRD p. 139
    """

    def __init__(self):
        super().__init__(name="Longstrider",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="(fur or a feather from a beast",
                         concentration=True,
                         duration="1 hour",
                         description="You touch a creature and bestow upon it a magical enhancement. Choose one of "
                                     "the following effects; the target gains that effect until the spell ends.\n"
                                     "Bear's Endurance. The target has advantage on Constitution checks. It also "
                                     "gains 2d6 temporary hit points, which are lost when the spell ends.\n"
                                     "Bull's Strength. The target has advantage on Strength checks, and his or her "
                                     "carrying capacity doubles.\n"
                                     "Cat's Grace. The target has advantage on Dexterity checks. It also doesn't take "
                                     "damage from falling 20 feet or less if it isn't incapacitated.\n"
                                     "Eagle's Splendor. The target has advantage on Charisma checks.\n"
                                     "Fox's Cunning. The target has advantage on Intelligence checks.\n"
                                     "Owl's Wisdom. The target has advantage on Wisdom checks.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "you can target one additional creature for each slot level above 2nd.")


class EnlargeReduce(spells.Spell):
    """
    Enlarge/Reduce Spell
    SRD p. 140
    """

    def __init__(self):
        super().__init__(name="Enlarge/Reduce",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of powdered iron",
                         concentration=True,
                         duration="1 minute",
                         description="You cause a creature or an object you can see within range to grow larger or "
                                     "smaller for the duration. Choose either a creature or an object that is neither "
                                     "worn nor carried. If the target is unwilling, it can make a Constitution saving "
                                     "throw. On a success, the spell has no effect.\n"
                                     "If the target is a creature, everything it is wearing and carrying changes size "
                                     "with it. Any item dropped by an affected creature returns to normal size at "
                                     "once.\n"
                                     "Enlarge. The target's size doubles in all dimensions, and its weight is "
                                     "multiplied by eight. This growth increases its size by one category-- from "
                                     "Medium to Large, for example. If there isn't enough room for the target to "
                                     "double its size, the creature or object attains the maximum possible size in "
                                     "the space available. Until the spell ends, the target also has advantage on "
                                     "Strength checks and Strength saving throws. The target's weapons also grow to "
                                     "match its new size. While these weapons are enlarged, the target's attacks with "
                                     "them deal 1d4 extra damage.\n"
                                     "Reduce. The target's size is halved in all dimensions, and its weight is "
                                     "reduced to one-eighth of normal. This reduction decreases its size by one "
                                     "category--from Medium to Small, for example. Until the spell ends, the target "
                                     "also has disadvantage on Strength checks and Strength saving throws. The "
                                     "target's weapons also shrink to match its new size. While these weapons are "
                                     "reduced, the target's attacks with them deal 1d4 less damage (this can't reduce "
                                     "the damage below 1).")


class Entangle(spells.Spell):
    """
    Entangle Spell
    SRD p. 140
    """

    def __init__(self):
        super().__init__(name="Entangle",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.CONJURATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="Grasping weeds and vines sprout from the ground in a 20-foot square starting "
                                     "from a point within range. For the duration, these plants turn the ground in "
                                     "the area into difficult terrain.\n"
                                     "A creature in the area when you cast the spell must succeed on a Strength "
                                     "saving throw or be restrained by the entangling plants until the spell ends. A "
                                     "creature restrained by the plants can use its action to make a Strength check "
                                     "against your spell save DC. On a success, it frees itself.\n"
                                     "When the spell ends, the conjured plants wilt away.")


class FalseLife(spells.Spell):
    """
    False Life Spell
    SRD p. 142
    """

    def __init__(self):
        super().__init__(name="False Life",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.NECROMANCY,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small amount of alcohol or distilled spirits",
                         duration="1 hour",
                         description="Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4 "
                                     "temporary hit points for the duration.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you gain 5 additional temporary hit points for each slot level above 1st.")


class FindTraps(spells.Spell):
    """
    Find Traps Spell
    SRD p. 144
    """

    def __init__(self):
        super().__init__(name="Find Traps",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.DIVINATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You sense the presence of any trap within range that is within line of sight. A "
                                     "trap, for the purpose of this spell, includes anything that would inflict a "
                                     "sudden or unexpected effect you consider harmful or undesirable, "
                                     "which was specifically intended as such by its creator. Thus, the spell would "
                                     "sense an area affected by the alarm spell, a glyph of warding, or a mechanical "
                                     "pit trap, but it would not reveal a natural weakness in the floor, an unstable "
                                     "ceiling, or a hidden sinkhole.\n"
                                     "This spell merely reveals that a trap is present. You don't learn the location "
                                     "of each trap, but you do learn the general nature of the danger posed by a trap "
                                     "you sense.")


class FogCloud(spells.Spell):
    """
    Fog Cloud Spell
    SRD p. 146
    """

    def __init__(self):
        super().__init__(name="Fog Cloud",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.CONJURATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 hour",
                         description="You create a 20-foot-radius sphere of fog centered on a point within range. The "
                                     "sphere spreads around corners, and its area is heavily obscured. It lasts for "
                                     "the duration or until a wind of moderate or greater speed (at least 10 miles "
                                     "per hour) disperses it.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the radius of the fog increases by 20 feet for each slot level above 1st.")


class GentleRepose(spells.Spell):
    """
    Gentle Repose Spell
    SRD p. 148-149
    """

    def __init__(self):
        super().__init__(name="Gentle Repose",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.NECROMANCY,
                         ritual=True,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of salt and one copper piece placed on each of the "
                                                  "corpse's eyes, which must remain there for the duration",
                         duration="10 days",
                         description="You touch a corpse or other remains. For the duration, the target is protected "
                                     "from decay and can't become undead.\n"
                                     "The spell also effectively extends the time limit on raising the target from "
                                     "the dead, since days spent under the influence of this spell don't count "
                                     "against the time limit of spells such as raise dead.")


class Goodberry(spells.Spell):
    """
    Goodberry Spell
    SRD p. 150
    """

    def __init__(self):
        super().__init__(name="Goodberry",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a sprig of mistletoe",
                         description="Up to ten berries appear in your hand and are infused with magic for the "
                                     "duration. A creature can use its action to eat one berry. Eating a berry "
                                     "restores 1 hit point, and the berry provides enough nourishment to sustain a "
                                     "creature for one day.\n"
                                     "The berries lose their potency if they have not been consumed within 24 hours "
                                     "of the casting of this spell.")


class HealingWord(spells.Spell):
    """
    Healing Word Spell
    SRD p. 153
    """

    def __init__(self):
        super().__init__(name="Healing Word",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.ABJURATION,
                         casting_time="1 bonus action",
                         spell_range="60 feet",
                         verbal_components=True,
                         description="A creature of your choice that you can see within range regains hit points "
                                     "equal to 1d4 + your spellcasting ability modifier. This spell has no effect on "
                                     "undead or constructs.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the healing increases by 1d4 for each slot level above 1st.")


class HeatMetal(spells.Spell):
    """
    Heat Metal Spell
    SRD p. 153-154
    """

    def __init__(self):
        super().__init__(name="Heat Metal",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of iron and a flame",
                         concentration=True,
                         duration="1 minute",
                         description="Choose a manufactured metal object, such as a metal weapon or a suit of heavy "
                                     "or medium metal armor, that you can see within range. You cause the object to "
                                     "glow red-hot. Any creature in physical contact with the object takes 2d8 fire "
                                     "damage when you cast the spell. Until the spell ends, you can use a bonus "
                                     "action on each of your subsequent turns to cause this damage again.\n"
                                     "If a creature is holding or wearing the object and takes the damage from it, "
                                     "the creature must succeed on a Constitution saving throw or drop the object if "
                                     "it can. If it doesn't drop the object, it has disadvantage on attack rolls and "
                                     "ability checks until the start of your next turn.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "the damage increases by 1d8 for each slot level above 2nd.")


class HuntersMark(spells.Spell):
    """
    Hunter's Mark Spell
    SRD p. 155
    """

    def __init__(self):
        super().__init__(name="Hunter's Mark",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         casting_time="1 bonus action",
                         school=SpellSchools.DIVINATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         concentration=True,
                         duration="1 hour",
                         description="You choose a creature you can see within range and mystically mark it as your "
                                     "quarry. Until the spell ends, you deal an extra 1d6 damage to the target "
                                     "whenever you hit it with a weapon attack, and you have advantage on any Wisdom "
                                     "(Perception) or Wisdom (Survival) check you make to find it. If the target "
                                     "drops to 0 hit points before this spell ends, you can use a bonus action on a "
                                     "subsequent turn of yours to mark a new creature.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd or 4th level, you can "
                                          "maintain your concentration on the spell for up to 8 hours. When you use a "
                                          "spell slot of 5th level or higher, you can maintain your concentration on "
                                          "the spell for up to 24 hours.")


class Jump(spells.Spell):
    """
    Jump Spell
    SRD p. 158
    """

    def __init__(self):
        super().__init__(name="Jump",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a grasshopper's hind leg",
                         duration="1 minute",
                         description="You touch a creature. The creature's jump distance is tripled until the spell "
                                     "ends.")


class LesserRestoration(spells.Spell):
    """
    Lesser Restoration Spell
    SRD p. 158
    """

    def __init__(self):
        super().__init__(name="Lesser Restoration",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         description="You touch a creature and can end either one disease or one condition afflicting "
                                     "it. The condition can be blinded, deafened, paralyzed, or poisoned.")


class Light(spells.Spell):
    """
    Light Spell
    SRD p. 159
    """

    def __init__(self):
        super().__init__(name="Light",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=0,
                         school=SpellSchools.EVOCATION,
                         spell_range="Touch",
                         verbal_components=True,
                         material_components_list="a firefly or phosphorescent moss",
                         duration="1 hour",
                         description="You touch one object that is no larger than 10 feet in any dimension. Until the "
                                     "spell ends, the object sheds bright light in a 20-foot radius and dim light "
                                     "for an additional 20 feet. The light can be colored as you like. Completely "
                                     "covering the object with something opaque blocks the light. The spell ends if "
                                     "you cast it again or dismiss it as an action.\n"
                                     "If you target an object held or worn by a hostile creature, that creature must "
                                     "succeed on a Dexterity saving throw to avoid the spell.")


class LocateObject(spells.Spell):
    """
    Locate Object Spell
    SRD p. 159-160
    """

    def __init__(self):
        super().__init__(name="Locate Object",
                         spell_lists=[SpellLists.ARCANE,
                                      SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a forked twig",
                         concentration=True,
                         duration="10 minutes",
                         description="Describe or name an object that is familiar to you. You sense the direction to "
                                     "the object's location, as long as that object is within 1,000 feet of you. If "
                                     "the object is in motion, you know the direction of its movement.\n"
                                     "The spell can locate a specific object known to you, as long as you have seen "
                                     "it up close--within 30 feet--at least once. Alternatively, the spell can locate "
                                     "the nearest object of a particular kind, such as a certain kind of apparel, "
                                     "jewelry, furniture, tool, or weapon.\n"
                                     "This spell can't locate an object if any thickness of lead, even a thin sheet, "
                                     "blocks a direct path between you and the object.")


class Longstrider(spells.Spell):
    """
    Longstrider Spell
    SRD p. 160
    """

    def __init__(self):
        super().__init__(name="Longstrider",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of dirt",
                         duration="1 hour",
                         description="You touch a creature. The target's speed increases by 10 feet until the spell "
                                     "ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you can target one additional creature for each slot level above 1st.")


class Mending(spells.Spell):
    """
    Mending Spell
    SRD p. 164
    """

    def __init__(self):
        super().__init__(name="Mending",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="two lodestones",
                         description="This spell repairs a single break or tear in an object you touch, such as a "
                                     "broken chain link, two halves of a broken key, a torn cloak, or a leaking "
                                     "wineskin. As long as the break or tear is no larger than 1 foot in any "
                                     "dimension, you mend it, leaving no trace of the former damage.\n"
                                     "This spell can physically repair a magic item or construct, but the spell can't "
                                     "restore magic to such an object.")


class Message(spells.Spell):
    """
    Message Spell
    SRD p. 164
    """

    def __init__(self):
        super().__init__(name="Message",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a short piece of copper wire",
                         duration="1 round",
                         description="You point your finger toward a creature within range and whisper a message. The "
                                     "target (and only the target) hears the message and can reply in a whisper that "
                                     "only you can hear.\n"
                                     "You can cast this spell through solid objects if you are familiar with the "
                                     "target and know it is beyond the barrier. Magical silence, 1 foot of stone, "
                                     "1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the "
                                     "spell. The spell doesn't have to follow a straight line and can travel freely "
                                     "around corners or through openings.")


class PassWithoutTrace(spells.Spell):
    """
    Pas Without Trace Spell
    SRD p. 167
    """

    def __init__(self):
        super().__init__(name="Pass Without Trace",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="ashes from a burned leaf of mistletoe and a sprig of spruce",
                         concentration=True,
                         duration="1 hour",
                         description="A veil of shadows and silence radiates from you, masking you and your "
                                     "companions from detection. For the duration, each creature you choose within 30 "
                                     "feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and "
                                     "can't be tracked except by magical means. A creature that receives this bonus "
                                     "leaves behind no tracks or other traces of its passage.")


class PoisonSpray(spells.Spell):
    """
    Poison Spray Spell
    SRD p. 169
    """

    def __init__(self):
        super().__init__(name="Poison Spray",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.CONJURATION,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You extend your hand toward a creature you can see within range and project a "
                                     "puff of noxious gas from your palm. The creature must succeed on a Constitution "
                                     "saving throw or take 1d12 poison damage.\n"
                                     "This spell's damage increases by 1d12 when you reach 5th level (2d12), "
                                     "11th level (3d12), and 17th level (4d12).")


class ProtectionFromPoison(spells.Spell):
    """
    Protection From Poison Spell
    SRD p. 173
    """

    def __init__(self):
        super().__init__(name="Protection From Poison",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         duration="1 hour",
                         description="You touch a creature. If it is poisoned, you neutralize the poison. If more "
                                     "than one poison afflicts the target, you neutralize one poison that you know is "
                                     "present, or you neutralize one at random.\n"
                                     "For the duration, the target has advantage on saving throws against being "
                                     "poisoned, and it has resistance to poison damage.")


class PurifyFoodAndDrink(spells.Spell):
    """
    Purify Food and Drink Spell
    SRD p. 173
    """

    def __init__(self):
        super().__init__(name="Purify Food and Drink",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         ritual=True,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="All nonmagical food and drink within a 5-foot-radius sphere centered on a point "
                                     "of your choice within range is purified and rendered free of poison and "
                                     "disease.")


class RayOfEnfeeblement(spells.Spell):
    """
    Ray of Enfeeblement Spell
    SRD p. 174
    """

    def __init__(self):
        super().__init__(name="Ray of Enfeeblement",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.NECROMANCY,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="A black beam of enervating energy springs from your finger toward a creature "
                                     "within range. Make a ranged spell attack against the target. On a hit, "
                                     "the target deals only half damage with weapon attacks that use Strength until "
                                     "the spell ends.\n"
                                     "At the end of each of the target's turns, it can make a Constitution saving "
                                     "throw against the spell. On a success, the spell ends.")


class Resistance(spells.Spell):
    """
    Resistance Spell
    SRD p. 175
    """

    def __init__(self):
        super().__init__(name="Resistance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a miniature cloak",
                         concentration=True,
                         duration="1 minute",
                         description="You touch one willing creature. Once before the spell ends, the target can roll "
                                     "a d4 and add the number rolled to one saving throw of its choice. It can roll "
                                     "the die before or after making the saving throw. The spell then ends.")


class Shillelagh(spells.Spell):
    """
    Shillelagh Spell
    SRD p. 179
    """

    def __init__(self):
        super().__init__(name="Shillelagh",
                         spell_lists=[SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="1 bonus action",
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="(mistletoe, a shamrock leaf, and a club or quarterstaff",
                         duration="1 minute",
                         description="The wood of a club or quarterstaff you are holding is imbued with nature's "
                                     "power. For the duration, you can use your spellcasting ability instead of "
                                     "Strength for the attack and damage rolls of melee attacks using that weapon, "
                                     "and the weapon's damage die becomes a d8. The weapon also becomes magical, "
                                     "if it isn't already. The spell ends if you cast it again or if you let go of "
                                     "the weapon.")


class Silence(spells.Spell):
    """
    Silence Spell
    SRD p. 179
    """

    def __init__(self):
        super().__init__(name="Silence",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ILLUSION,
                         ritual=True,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="For the duration, no sound can be created within or pass through a "
                                     "20-foot-radius sphere centered on a point you choose within range. Any creature "
                                     "or object entirely inside the sphere is immune to thunder damage, and creatures "
                                     "are deafened while entirely inside it. Casting a spell that includes a verbal "
                                     "component is impossible there.")


class SpareTheDying(spells.Spell):
    """
    Spare the Dying Spell
    SRD p. 181
    """

    def __init__(self):
        super().__init__(name="Spare the Dying",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.NECROMANCY,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         description="You touch a living creature that has 0 hit points. The creature becomes stable. "
                                     "This spell has no effect on undead or constructs.")


class SpeakWithAnimals(spells.Spell):
    """
    Speak with Animals Spell
    SRD p. 181
    """

    def __init__(self):
        super().__init__(name="Speak with Animals",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         duration="10 minutes",
                         description="You gain the ability to comprehend and verbally communicate with beasts for the "
                                     "duration. The knowledge and awareness of many beasts is limited by their "
                                     "intelligence, but at minimum, beasts can give you information about nearby "
                                     "locations and monsters, including whatever they can perceive or have perceived "
                                     "within the past day. You might be able to persuade a beast to perform a small "
                                     "favor for you, at the GM's discretion.")


class SpikeGrowth(spells.Spell):
    """
    Spike Growth Spell
    SRD p. 182
    """

    def __init__(self):
        super().__init__(name="Spike Growth",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="seven sharp thorns or seven small twigs, each sharpened to a point",
                         concentration=True,
                         duration="10 minutes",
                         description="The ground in a 20-foot radius centered on a point within range twists and "
                                     "sprouts hard spikes and thorns. The area becomes difficult terrain for the "
                                     "duration. When a creature moves into or within the area, it takes 2d4 piercing "
                                     "damage for every 5 feet it travels.\n"
                                     "The transformation of the ground is camouflaged to look natural. Any creature "
                                     "that can't see the area at the time the spell is cast must make a Wisdom ("
                                     "Perception) check against your spell save DC to recognize the terrain as "
                                     "hazardous before entering it.")


class Thaumaturgy(spells.Spell):
    """
    Thaumaturgy Spell
    SRD p. 187
    """

    def __init__(self):
        super().__init__(name="Thaumaturgy",
                         spell_lists=[SpellLists.DIVINE],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         duration="Up to 1 minute",
                         description="You manifest a minor wonder, a sign of supernatural power, within range. You "
                                     "create one of the following magical effects within range:\n"
                                     "• Your voice booms up to three times as loud as normal for 1 minute\n"
                                     "• You cause flames to flicker, brighten, dim, or change color for 1 minute.\n"
                                     "• You cause harmless tremors in the ground for 1 minute.\n"
                                     "• You create an instantaneous sound that originates from a point of your choice "
                                     "within range, such as a rumble of thunder, the cry of a raven, or ominous "
                                     "whispers.\n"
                                     "• You instantaneously cause an unlocked door or window to fly open or slam "
                                     "shut.\n"
                                     "• You alter the appearance of your eyes for 1 minute.\n"
                                     "If you cast this spell multiple times, you can have up to three of its 1-minute "
                                     "effects active at a time, and you can dismiss such an effect as an action.")


class Thunderwave(spells.Spell):
    """
    Thunderwave Spell
    SRD p. 187
    """

    def __init__(self):
        super().__init__(name="Thunderwave",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Self (15-foot cube)",
                         verbal_components=True,
                         somatic_components=True,
                         description="A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube "
                                     "originating from you must make a Constitution saving throw. On a failed save, "
                                     "a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a "
                                     "successful save, the creature takes half as much damage and isn't pushed.\n"
                                     "In addition, unsecured objects that are completely within the area of effect "
                                     "are automatically pushed 10 feet away from you by the spell's effect, "
                                     "and the spell emits a thunderous boom audible out to 300 feet.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the damage increases by 1d8 for each slot level above 1st.")


class Dagger(weapons.Weapon):
    """
    Dagger Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Dagger",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.SIMPLE,
                         damage_dice="1d4",
                         damage_type=DamageTypes.PIERCING,
                         finesse=True,
                         light=True,
                         thrown=True,
                         attack_range=(20, 60),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Rapier(weapons.Weapon):
    """
    Rapier Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Rapier",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d8",
                         damage_type=DamageTypes.PIERCING,
                         finesse=True,
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Shortsword(weapons.Weapon):
    """
    Shortsword Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Shortsword",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d6",
                         damage_type=DamageTypes.PIERCING,
                         finesse=True,
                         light=True,
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class HandCrossbow(weapons.Weapon):
    """
    Hand Crossbow Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Hand Crossbow",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d6",
                         damage_type=DamageTypes.PIERCING,
                         ammunition=True,
                         light=True,
                         loading=True,
                         attack_range=(30, 120),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Longbow(weapons.Weapon):
    """
    Longbow Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Longbow",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d8",
                         damage_type=DamageTypes.PIERCING,
                         ammunition=True,
                         heavy=True,
                         two_handed=True,
                         attack_range=(150, 600),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class ZoneOfTruth(spells.Spell):
    """
    Zone of Truth Spell
    SRD p. 0
    """

    def __init__(self):
        super().__init__(name="Zone of Truth",
                         spell_lists=[SpellLists.DIVINE],
                         concentration=False,
                         level=2,
                         ritual=False,
                         school=SpellSchools.Enchantment,
                         spell_range="60 feet",
                         verbal_components="True",
                         somatic_components="True",
                         material_components_list="",
                         duration="10 minutes",
                         description="You create a magical zone that guards against deception in a 15-foot-radius sphere centered on a point of your choice within range. Until the spell ends, a creature that enters the spell's area for the first time on a turn or starts its turn there must make a Charisma saving throw. On a failed save, a creature can't speak a deliberate lie while in the radius. You know whether each creature succeeds or fails on its saving throw. An affected creature is aware of the spell and can thus avoid answering questions to which it would normally respond with a lie. Such a creature can be evasive in its answers as long as it remains within the boundaries of the truth",
                         at_higher_levels="")


CONTENT = {
    "Armors": {
        "Padded": Padded,
        "Leather": Leather,
        "Studded Leather": StuddedLeather,
        "Hide": Hide,
        "Chain Shirt": ChainShirt,
        "Scale Mail": ScaleMail,
        "Breastplate": Breastplate,
        "Half Plate": HalfPlate,
        "Ring Mail": RingMail,
        "Chain Mail": ChainMail,
        "Splint": Splint,
        "Plate": Plate,
        "Shield": Shield,
    },
    "Classes": {
        # TODO The rest of the subclasses
        # "Berserker Barbarian": BerserkerBarbarian,
        "Lore Bard": "OBSOLETE",
        # "Life Cleric": LifeCleric,
        # "Land Druid": LandDruid,
        # "Champion Fighter": ChampionFighter,
        # "Open Hand Monk": OpenHandMonk,
        # "Devotion Paladin": DevotionPaladin,
        "Hunter Ranger": "OBSOLETE",
        "Thief Rogue": "OBSOLETE",
        # "Draconic Sorcerer": DraconicSorcerer,
        # "Fiend Warlock": FiendWarlock,
        # "Evocation Wizard": EvocationWizard,
    },
    "Feats": {
        "Grappler": "OBSOLETE",
    },
    "Magic Items": {
        # TODO All Magic Items
    },
    "Races": {
        "Dwarf": "OBSOLETE",
        "High Elf": "OBSOLETE",
        "Halfling": "OBSOLETE",
        "Human": "OBSOLETE",
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
        "Rock Gnome": "OBSOLETE",
        "Half-Elf": "OBSOLETE",
        "Half-Orc": "OBSOLETE",
        "Infernal Tiefling": "OBSOLETE",
    },
    "Spells": {
        # TODO The rest of the spells
        "Acid Arrow": AcidArrow,
        "Acid Splash": AcidSplash,
        "Aid": Aid,
        "Alarm": Alarm,
        "Alter Self": AlterSelf,
        "Animal Friendship": AnimalFriendship,
        "Animal Messenger": AnimalMessenger,
        "Animal Shapes": AnimalShapes,
        "Animate Dead": AnimateDead,
        "Animate Objects": AnimateObjects,
        "Antilife Shell": AntilifeShell,
        "Antimagic Field": AntimagicField,
        "Antipathy/Sympathy": AntipathySympathy,
        "Arcane Eye": ArcaneEye,
        "Arcane Hand": ArcaneHand,
        "Arcane Lock": ArcaneLock,
        "Arcane Sword": ArcaneSword,
        "Arcanist's Magic Aura": ArcanistsMagicAura,
        "Astral Projection": AstralProjection,
        "Augury": Augury,
        "Awaken": Awaken,
        "Bane": Bane,
        "Banishment": Banishment,
        "Barkskin": "OBSOLETE",
        "Beacon of Hope": BeaconOfHope,
        "Bestow Curse": BestowCurse,
        "Black Tentacles": BlackTentacles,
        "Blade Barrier": BladeBarrier,
        "Bless": Bless,
        "Blight": Blight,
        "Blindness/Deafness": BlindnessDeafness,
        "Blink": Blink,
        "Blur": Blur,
        "Branding Smite": BrandingSmite,
        "Burning Hands": BurningHands,
        "Call Lightning": CallLightning,
        "Calm Emotions": CalmEmotions,
        "Chain Lightning": ChainLightning,
        "Charm Person": CharmPerson,
        "Chill Touch": ChillTouch,
        "Circle of Death": CircleOfDeath,
        "Clairvoyance": Clairvoyance,
        "Clone": Clone,
        "Cloudkill": Cloudkill,
        "Color Spray": ColorSpray,
        "Command": Command,
        "Commune": Commune,
        "Commune with Nature": CommuneWithNature,
        "Comprehend Languages": ComprehendLanguages,
        "Compulsion": Compulsion,
        "Cone of Cold": ConeOfCold,
        "Confusion": Confusion,
        "Conjure Animals": ConjureAnimals,
        "Conjure Celestial": ConjureCelestial,
        "Conjure Elemental": ConjureElemental,
        "Conjure Fey": ConjureFey,
        "Conjure Minor Elementals": ConjureMinorElementals,
        "Conjure Woodland Beings": ConjureWoodlandBeings,
        "Contact Other Plane": ContactOtherPlane,
        "Contagion": Contagion,
        "Contingency": Contingency,
        "Continual Flame": ContinualFlame,
        "Control Water": ControlWater,
        "Control Weather": ControlWeather,
        "Counterspell": Counterspell,
        "Create Food and Water": CreateFoodAndWater,
        "Create or Destroy Water": CreateOrDestroyWater,
        "Create Undead": CreateUndead,
        "Creation": Creation,
        "Cure Wounds": CureWounds,
        "Dancing Lights": DancingLights,
        "Darkness": Darkness,
        "Darkvision": Darkvision,
        "Daylight": Daylight,
        "Death Ward": DeathWard,
        "Delayed Blast Fireball": DelayedBlastFireball,
        "Demiplane": Demiplane,
        "Detect Evil and Good": DetectEvilAndGood,
        "Detect Magic": DetectMagic,
        "Detect Poison and Disease": DetectPoisonAndDisease,
        "Detect Thoughts": DetectThoughts,
        # "Dimension Door": DimensionDoor,
        # "Disguise Self": DisguiseSelf,
        # "Disintegrate": Disintegrate,
        # "Dispel Evil and Good": DispelEvilAndGood,
        # "Dispel Magic": DispelMagic,
        # "Divination": Divination,
        # "Divine Favor": DivineFavor,
        # "Divine Word": DivineWord,
        # "Dominate Beast": DominateBeast,
        # "Dominate Monster": DominateMonster,
        # "Dominate Person": DominatePerson,
        # "Dream": Dream,
        "Druidcraft": Druidcraft,
        # "Earthquake": Earthquake,
        # "Eldritch Blast": EldritchBlast,
        "Enhance Ability": EnhanceAbility,
        "Enlarge/Reduce": EnlargeReduce,
        "Entangle": Entangle,
        # "Enthrall": Enthrall,
        # "Etherealness": Etherealness,
        # "Expeditious Retreat": ExpeditiousRetreat,
        # "Eyebite": Eyebite,
        # "Fabricate": Fabricate,
        # "Faerie Fire": FaerieFire,
        # "Faithful Hound": FaithfulHound,
        "False Life": FalseLife,
        # "Fear": Fear,
        # "Feather Fall": FeatherFall,
        # "Feeblemind": Feeblemind,
        # "Find Familiar": FindFamiliar,
        # "Find Steed": FindSteed,
        # "Find the Path": FindThePath,
        "Find Traps": FindTraps,
        # "Finger of Death": FingerOfDeath,
        # "Fireball": Fireball,
        # "Fire Bolt": FireBolt,
        # "Fire Shield": FireShield,
        # "Fire Storm": FireStorm,
        # "Flame Blade": FlameBlade,
        # "Flame Strike": FlameStrike,
        # "Flaming Sphere": FlamingSphere,
        # "Flesh to Stone": FleshToStone,
        # "Floating Disk": FloatingDisk,
        # "Fly": Fly,
        "Fog Cloud": FogCloud,
        # "Forbiddance": Forbiddance,
        # "Forcecage": Forcecage,
        # "Foresight": Foresight,
        # "Freedom of Movement": FreedomOfMovement,
        # "Freezing Sphere": FreezingSphere,
        # "Gaseous Form": GaseousForm,
        # "Gate": Gate,
        # "Geas": Geas,
        "Gentle Repose": GentleRepose,
        # "Giant Insect": GiantInsect,
        # "Glibness": Glibness,
        # "Globe of Invulnerability": GlobeOfInvulnerability,
        # "Glyph of Warning": GlyphOfWarning,
        "Goodberry": Goodberry,
        # "Grease": Grease,
        # "Greater Invisibility": GreaterInvisibility,
        # "Greater Restoration": GreaterRestoration,
        # "Guardian of Faith": GuardianOfFaith,
        # "Guards and Wards": GuardsAndWards,
        "Guidance": "OBSOLETE",
        # "Guiding Bolt": GuidingBolt,
        # "Gust of Wind": GustOfWind,
        # "Hallow": Hallow,
        # "Hallucinatory Terrain": HallucinatoryTerrain,
        # "Harm": Harm,
        # "Haste": Haste,
        # "Heal": Heal,
        "Healing Word": HealingWord,
        "Heat Metal": HeatMetal,
        # "Hellish Rebuke": HellishRebuke,
        # "Heroes' Feast": HeroesFeast,
        # "Heroism": Heroism,
        # "Hideous Laughter": HideousLaughter,
        # "Hold Monster": HoldMonster,
        # "Hold Person": HoldPerson,
        # "Holy Aura": HolyAura,
        "Hunter's Mark": HuntersMark,
        # "Hypnotic Pattern": HypnoticPattern,
        # "Ice Storm": IceStorm,
        # "Identify": Identify,
        # "Illusory Script": IllusoryScript,
        # "Imprisonment": Imprisonment,
        # "Incendiary Cloud": IncendiaryCloud,
        # "Inflict Wounds": InflictWounds,
        # "Insect Plague": InsectPlague,
        # "Instant Summons": InstantSummons,
        # "Invisibility": Invisibility,
        # "Irresistible Dance": IrresistibleDance,
        "Jump": Jump,
        # "Knock": Knock,
        # "Legend Lore": LegendLore,
        "Lesser Restoration": LesserRestoration,
        # "Levitate": Levitate,
        "Light": Light,
        # "Lightning Bolt": LightningBolt,
        # "Locate Animals or Plants": LocateAnimalsOrPlants,
        # "Locate Creature": LocateCreature,
        "Locate Object": LocateObject,
        "Longstrider": Longstrider,
        # "Mage Armor": MageArmor,
        # "Mage Hand": MageHand,
        # "Magic Circle": MagicCircle,
        # "Magic Jar": MagicJar,
        # "Magic Missile": MagicMissile,
        # "Magic Mouth": MagicMouth,
        # "Magic Weapon": MagicWeapon,
        # "Magnificent Mansion": MagnificentMansion,
        # "Major Image": MajorImage,
        # "Mass Cure Wounds": MassCureWounds,
        # "Mass Heal": MassHeal,
        # "Mass Healing Word": MassHealingWord,
        # "Mass Suggestion": MassSuggestion,
        # "Maze": Maze,
        # "Meld into Stone": MeldIntoStone,
        "Mending": Mending,
        "Message": Message,
        # "Meteor Swarm": MeteorSwarm,
        # "Mind Blank": MindBlank,
        # "Minor Illusion": MinorIllusion,
        # "Mirage Arcane": MirageArcane,
        # "Mirror Image": MirrorImage,
        # "Mislead": Mislead,
        # "Misty Step": MistyStep,
        # "Modify Memory": ModifyMemory,
        # "Moonbeam": Moonbeam,
        # "Move Earth": MoveEarth,
        # "Nondetection": Nondetection,
        "Pass Without Trace": PassWithoutTrace,
        # "Passwall": Passwall,
        # "Phantasmal Killer": PhantasmalKiller,
        # "Phantom Steed": PhantomSteed,
        # "Planar Ally": PlanarAlly,
        # "Planar Binding": PlanarBinding,
        # "Plane Shift": PlaneShift,
        # "Plant Growth": PlantGrowth,
        "Poison Spray": PoisonSpray,
        # "Polymorph": Polymorph,
        # "Power Word Kill": PowerWordKill,
        # "Power Word Stun": PowerWordStun,
        # "Prayer of Healing": PrayerOfHealing,
        # "Prestidigitation": Prestidigitation,
        # "Prismatic Spray": PrismaticSpray,
        # "Prismatic Wall": PrismaticWall,
        # "Private Sanctum": PrivateSanctum,
        # "Produce Flame": ProduceFlame,
        # "Programmed Illusion": ProgrammedIllusion,
        # "Project Image": ProjectImage,
        # "Protection from Energy": ProtectionFromEnergy,
        # "Protection from Good and Evil": ProtectionFromGoodAndEvil,
        "Protection from Poison": ProtectionFromPoison,
        "Purify Food and Drink": PurifyFoodAndDrink,
        # "Raise Dead": RaiseDead,
        "Ray of Enfeeblement": RayOfEnfeeblement,
        # "Ray of Frost": RayOfFrost,
        # "Regenerate": Regenerate,
        # "Reincarnate": Reincarnate,
        # "Remove Curse": RemoveCurse,
        # "Resilient Sphere": ResilientSphere,
        "Resistance": Resistance,
        # "Resurrection": Resurrection,
        # "Reverse Gravity": ReverseGravity,
        # "Revivify": Revivify,
        # "Rope Trick": RopeTrick,
        # "Sacred Flame": SacredFlame,
        # "Sanctuary": Sanctuary,
        # "Scorching Ray": ScorchingRay,
        # "Scrying": Scrying,
        # "Secret Chest": SecretChest,
        # "See Invisibility": SeeInvisibility,
        # "Seeming": Seeming,
        # "Sending": Sending,
        # "Sequester": Sequester,
        # "Shapechange": Shapechange,
        # "Shatter": Shatter,
        # "Shield": ShieldSpell,
        # "Shield of Faith": ShieldOfFaith,
        "Shillelagh": Shillelagh,
        # "ShockingGrasp": ShockingGrasp,
        "Silence": Silence,
        # "Silent Image": SilentImage,
        # "Simulacrum": Simulacrum,
        # "Sleep": Sleep,
        # "Sleet Storm": SleetStorm,
        # "Slow": Slow,
        "Spare the Dying": SpareTheDying,
        "Speak with Animals": SpeakWithAnimals,
        # "Speak with Dead": SpeakWithDead,
        # "Speak with Plants": SpeakWithPlants,
        # "Spider Climb": SpiderClimb,
        "Spike Growth": SpikeGrowth,
        # "Spirit Guardians": SpiritGuardians,
        # "Spiritual Weapon": SpiritualWeapon,
        # "Stinking Cloud": StinkingCloud,
        # "Stone Shape": StoneShape,
        # "Stoneskin": Stoneskin,
        # "Storm of Vengeance": StormOfVengeance,
        # "Suggestion": Suggestion,
        # "Sunbeam": Sunbeam,
        # "Sunburst": Sunburst,
        # "Symbol": Symbol,
        # "Telekinesis": Telekinesis,
        # "Telepathic Bond": TelepathicBond,
        # "Teleport": Teleport,
        # "Teleportation Circle": TeleportationCircle,
        "Thaumaturgy": Thaumaturgy,
        "Thunderwave": Thunderwave,
        # "Time Stop": TimeStop,
        # "Tiny Hut": TinyHut,
        # "Tongues": Tongues,
        # "Transport via Plants": TransportViaPlants,
        # "Tree Stride": TreeStride,
        # "True Polymorph": TruePolymorph,
        # "True Resurrection": TrueResurrection,
        # "True Seeing": TrueSeeing,
        # "True Strike": TrueStrike,
        # "Unseen Servant": UnseenServant,
        # "Vampiric Touch": VampiricTouch,
        # "Vicious Mockery": ViciousMockery,
        # "Wall of Fire": WallOfFire,
        # "Wall of Force": WallOfForce,
        # "Wall of Ice": WallOfIce,
        # "Wall of Stone": WallOfStone,
        # "Wall of Thorns": WallOfThorns,
        # "Warding Bond": WardingBond,
        # "Water Breathing": WaterBreathing,
        # "Water Walk": WaterWalk,
        # "Web": Web,
        # "Weird": Weird,
        # "Wind Walk": WindWalk,
        # "Wind Wall": WindWall,
        # "Wish": Wish,
        # "Word of Recall": WordOfRecall,
        # "Zone of Truth": ZoneOfTruth,
    },
    "Weapons": {
        # TODO The rest of the weapons
        # "Club": Club,
        "Dagger": Dagger,
        # "Greatclub": Greatclub,
        # "Handaxe": Handaxe,
        # "Javelin": Javelin,
        # "Light Hammer": LightHammer,
        # "Mace": Mace,
        # "Quarterstaff": Quarterstaff,
        # "Sickle": Sickle,
        # "Spear": Spear,
        # "Light Crossbow": LightCrossbow,
        # "Dart": Dart,
        # "Shortbow": Shortbow,
        # "Sling": Sling,
        # "Battleaxe": Battleaxe,
        # "Flail": Flail,
        # "Glaive": Glaive,
        # "Greataxe": Greataxe,
        # "Greatsword": Greatsword,
        # "Halberd": Halberd,
        # "Lance": Lance,
        # "Longsword": Longsword,
        # "Maul": Maul,
        # "Morningstar": Morningstar,
        # "Pike": Pike,
        "Rapier": Rapier,
        # "Scimitar": Scimitar,
        "Shortsword": Shortsword,
        # "Trident": Trident,
        # "War Pick": WarPick,
        # "Warhammer": Warhammer,
        # "Whip": Whip,
        # "Blowgun": Blowgun,
        "Hand Crossbow": HandCrossbow,
        # "Heavy Crossbow": HeavyCrossbow,
        "Longbow": Longbow,
        # "Net": Net
    },
}
