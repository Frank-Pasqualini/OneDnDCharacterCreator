"""
Content from the Dungeons and Dragons Elemental Evil Player's Companion.
https://media.wizards.com/2015/downloads/dnd/EE_PlayersCompanion.pdf
"""
from rules import spells
from rules.enums import SpellLists, SpellSchools


class HorridWilting(spells.Spell):
    """
    Abi-Dalzim's Horrid Wilting Spell
    EEPC p. 15
    """

    def __init__(self):
        super().__init__(name="Abi-Dalzim's Horrid Wilting",
                         spell_lists=[SpellLists.ARCANE],
                         level=8,
                         school=SpellSchools.NECROMANCY,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of sponge",
                         description="You draw the moisture from every creature in a 30-foot cube centered on a point "
                                     "you choose within range. Each creature in that area must make a Constitution "
                                     "saving throw. Constructs and undead aren't affected, and plants and water "
                                     "elementals make this saving throw with disadvantage. A creature takes 12d8 "
                                     "necrotic damage on a failed save, or half as much damage on a successful one.\n"
                                     "Nonmagical plants in the area that aren't creatures, such as trees and shrubs, "
                                     "wither and die instantly.")


class AbsorbElements(spells.Spell):
    """
    Absorb Elements Spell
    EEPC p. 15
    """

    def __init__(self):
        super().__init__(name="Absorb Elements",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.ABJURATION,
                         casting_time="1 reaction, which you take when you take acid, cold, fire, lightning, "
                                      "or thunder damage",
                         spell_range="Self",
                         somatic_components=True,
                         duration="1 round",
                         description="The spell captures some of the incoming energy, lessening its effect on you and "
                                     "storing it for your next melee attack. You have resistance to the triggering "
                                     "damage type until the start of your next turn. Also, the first time you hit "
                                     "with a melee attack on your next turn, the target takes an extra 1d6 damage of "
                                     "the triggering type, and the spell ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the extra damage increases by 1d6 for each slot level above 1st.")


class AganazzarsScorcher(spells.Spell):
    """
    Aganazzar's Scorcher Spell
    EEPC p. 15
    """

    def __init__(self):
        super().__init__(name="Aganazzar's Scorcher",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.EVOCATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a red dragon's scale",
                         description="A line of roaring flame 30 feet long and 5 feet wide emanates from you in a "
                                     "direction you choose. Each creature in the line must make a Dexterity saving "
                                     "throw. A creature takes 3d8 fire damage on a failed save, or half as much "
                                     "damage on a successful one.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "the damage increases by 1d8 for each slot level above 2nd.")


class BeastBond(spells.Spell):
    """
    Beast Bond Spell
    EEPC p. 15
    """

    def __init__(self):
        super().__init__(name="Beast Bond",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a bit of fur wrapped in a cloth",
                         concentration=True,
                         duration="10 minutes",
                         description="You establish a telepathic link with one beast you touch that is friendly to "
                                     "you or charmed by you. The spell fails if the beast's Intelligence is 4 or "
                                     "higher. Until the spell ends, the link is active while you and the beast are "
                                     "within line of sight of each other. Through the link, the beast can understand "
                                     "your telepathic messages to it, and it can telepathically communicate simple "
                                     "emotions and concepts back to you. While the link is active, the beast gains "
                                     "advantage on attack rolls against any creature within 5 feet of you that you "
                                     "can see.")


class BonesOfTheEarth(spells.Spell):
    """
    Bones of the Earth Spell
    EEPC p. 15
    """

    def __init__(self):
        super().__init__(name="Bones of the Earth",
                         spell_lists=[SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You cause up to six pillars of stone to burst from places on the ground that "
                                     "you can see within range. Each pillar is a cylinder that has a diameter of 5 "
                                     "feet and a height of up to 30 feet. The ground where a pillar appears must be "
                                     "wide enough for its diameter, and you can target the ground under a creature if "
                                     "that creature is Medium or smaller. Each pillar has AC 5 and 30 hit points. "
                                     "When reduced to 0 hit points, a pillar crumbles into rubble, which creates an "
                                     "area of difficult terrain with a 10-foot radius that lasts until the rubble is "
                                     "cleared. Each 5-foot-diameter portion of the area requires at least 1 minute to "
                                     "clear by hand.\n"
                                     "If a pillar is created under a creature, that creature must succeed on a "
                                     "Dexterity saving throw or be lifted by the pillar. A creature can choose to "
                                     "fail the save.\n"
                                     "If a pillar is prevented from reaching its full height because of a ceiling or "
                                     "other obstacle, a creature on the pillar takes 6d6 bludgeoning damage and is "
                                     "restrained, pinched between the pillar and the obstacle. The restrained "
                                     "creature can use an action to make a Strength or Dexterity check (the "
                                     "creature's choice) against the spell's save DC. On a success, the creature is "
                                     "no longer restrained and must either move off the pillar or fall off it.",
                         at_higher_levels="When you cast this spell using a spell slot of 7th level or higher, "
                                          "you can create two additional pillars for each slot level above 6th.")


class Catapult(spells.Spell):
    """
    Catapult Spell
    EEPC p. 15
    """

    def __init__(self):
        super().__init__(name="Catapult",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="150 feet",
                         somatic_components=True,
                         description="Choose one object weighing 1 to 5 pounds within range that isn't being worn or "
                                     "carried. The object flies in a straight line up to 90 feet in a direction you "
                                     "choose before falling to the ground, stopping early if it impacts against a "
                                     "solid surface. If the object would strike a creature, that creature must make a "
                                     "Dexterity saving throw. On a failed save, the object strikes the target and "
                                     "stops moving. When the object strikes something, the object and what it strikes "
                                     "each take 3d8 bludgeoning damage.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the maximum weight of objects that you can target with this spell "
                                          "increases by 5 pounds, and the damage increases by 1d8, for each slot "
                                          "level above 1st.")


class ControlFlames(spells.Spell):
    """
    Control Flames Spell
    EEPC p. 16
    """

    def __init__(self):
        super().__init__(name="Control Flames",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="60 feet",
                         somatic_components=True,
                         duration="Instantaneous or 1 hour",
                         description="You choose nonmagical flame that you can see within range and that fits within "
                                     "a 5-foot cube. You affect it in one of the following ways:\n"
                                     "• You instantaneously expand the flame 5 feet in one direction, provided that "
                                     "wood or other fuel is present in the new location.\n"
                                     "• You instantaneously extinguish the flames within the cube.\n"
                                     "• You double or halve the area of bright light and dim light cast by the flame, "
                                     "change its color, or both. The change lasts for 1 hour.\n"
                                     "• You cause simple shapes-such as the vague form of a creature, an inanimate "
                                     "object, or a location-to appear within the flames and animate as you like. The "
                                     "shapes last for 1 hour.\n"
                                     "If you cast this spell multiple times, you can have up to three of its "
                                     "non-instantaneous effects active at a time, and you can dismiss such an effect "
                                     "as an action.")


class ControlWinds(spells.Spell):
    """
    Control Winds Spell
    EEPC p. 16-17
    """

    def __init__(self):
        super().__init__(name="Control Winds",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=5,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="300 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 hour",
                         description="You take control of the air in a 100-foot cube that you can see within range. "
                                     "Choose one of the following effects when you cast the spell. The effect lasts "
                                     "for the spell's duration, unless you use your action on a later turn to switch "
                                     "to a different effect. You can also use your action to temporarily halt the "
                                     "effect or to restart one you've halted.\n"
                                     "Gusts. A wind picks up within the cube, continually blowing in a horizontal "
                                     "direction you designate. You choose the intensity of the wind: calm, moderate, "
                                     "or strong. If the wind is moderate or strong, ranged weapon attacks that enter "
                                     "or leave the cube or pass through it have disadvantage on their attack rolls. "
                                     "If the wind is strong, any creature moving against the wind must spend 1 extra "
                                     "foot of movement for each foot moved.\n"
                                     "Downdraft. You cause a sustained blast of strong wind to blow downward from the "
                                     "top of the cube. Ranged weapon attacks that pass through the cube or that are "
                                     "made against targets within it have disadvantage on their attack rolls. A "
                                     "creature must make a Strength saving throw if it flies into the cube for the "
                                     "first time on a turn or starts its turn there flying. On a failed save, "
                                     "the creature is knocked prone.\n"
                                     "Updraft. You cause a sustained updraft within the cube, rising upward from the "
                                     "cube's bottom side. Creatures that end a fall within the cube take only half "
                                     "damage from the fall. When a creature in the cube makes a vertical jump, "
                                     "the creature can jump up to 10 feet higher than normal.")


class CreateBonfire(spells.Spell):
    """
    Create Bonfire Spell
    EEPC p. 17
    """

    def __init__(self):
        super().__init__(name="Create Bonfire",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.CONJURATION,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="You create a bonfire on ground that you can see within range. Until the spell "
                                     "ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire's "
                                     "space when you cast the spell must succeed on a Dexterity saving throw or take "
                                     "1d8 fire damage. A creature must also make the saving throw when it moves into "
                                     "the bonfire's space for the first time on a turn or ends its turn there.\n"
                                     "The bonfire ignites flammable objects in its area that aren't being worn or "
                                     "carried.\n"
                                     "The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level "
                                     "(3d8), and 17th level (4d8).")


class DustDevil(spells.Spell):
    """
    Dust Devil Spell
    EEPC p. 17
    """

    def __init__(self):
        super().__init__(name="Dust Devil",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.CONJURATION,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of dust",
                         concentration=True,
                         duration="1 minute",
                         description="Choose an unoccupied 5-foot cube of air that you can see within range. An "
                                     "elemental force that resembles a dust devil appears in the cube and lasts for "
                                     "the spell's duration.\n"
                                     "Any creature that ends its turn within 5 feet of the dust devil must make a "
                                     "Strength saving throw. On a failed save, the creature takes 1d8 bludgeoning "
                                     "damage and is pushed 10 feet away. On a successful save, the creature takes "
                                     "half as much damage and isn't pushed.\n"
                                     "As a bonus action, you can move the dust devil up to 30 feet in any direction. "
                                     "If the dust devil moves over sand, dust, loose dirt, or small gravel, "
                                     "it sucks up the material and forms a 10-foot-radius cloud of debris around "
                                     "itself that lasts until the start of your next turn. The cloud heavily obscures "
                                     "its area.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "the damage increases by 1d8 for each slot level above 2nd.")


class EarthTremor(spells.Spell):
    """
    Earth Tremor Spell
    EEPC p. 17
    """

    def __init__(self):
        super().__init__(name="Earth Tremor",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.EVOCATION,
                         spell_range="Self (10-foot radius)",
                         verbal_components=True,
                         somatic_components=True,
                         description="You cause a tremor in the ground within range. Each creature other than you in "
                                     "that area must make a Dexterity saving throw. On a failed save, a creature "
                                     "takes 1d6 bludgeoning damage and is knocked prone. If the ground in that area "
                                     "is loose earth or stone, it becomes difficult terrain until cleared, "
                                     "with each 5-foot-diameter portion requiring at least 1 minute to clear by hand.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the damage increases by 1d6 for each slot level above 1st.")


class Earthbind(spells.Spell):
    """
    Earthbind Spell
    EEPC p. 17
    """

    def __init__(self):
        super().__init__(name="Earthbind",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="300 feet",
                         verbal_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="Choose one creature you can see within range. Yellow strips of magical energy "
                                     "loop around the creature. The target must succeed on a Strength saving throw, "
                                     "or its flying speed (if any) is reduced to 0 feet for the spell's duration. An "
                                     "airborne creature affected by this spell safely descends at 60 feet per round "
                                     "until it reaches the ground or the spell ends.")


class ElementalBane(spells.Spell):
    """
    Elemental Bane Spell
    EEPC p. 17
    """

    def __init__(self):
        super().__init__(name="Elemental Bane",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=4,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="Choose one creature you can see within range, and choose one of the following "
                                     "damage types: acid, cold, fire, lightning, or thunder. The target must succeed "
                                     "on a Constitution saving throw or be affected by the spell for its duration. "
                                     "The first time each turn the affected target takes damage of the chosen type, "
                                     "the target takes an extra 2d6 damage of that type. Moreover, the target loses "
                                     "any resistance to that damage type until the spell ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 5th level or higher, "
                                          "you can target one additional creature for each slot level above 4th. The "
                                          "creatures must be within 30 feet of each other when you target them.")


class EruptingEarth(spells.Spell):
    """
    Erupting Earth Spell
    EEPC p. 17
    """

    def __init__(self):
        super().__init__(name="Erupting Earth",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of obsidian",
                         description="Choose a point you can see on the ground within range. A fountain of churned "
                                     "earth and stone erupts in a 20-foot cube centered on that point. Each creature "
                                     "in that area must make a Dexterity saving throw. A creature takes 3d12 "
                                     "bludgeoning damage on a failed save, or half as much damage on a successful "
                                     "one. Additionally, the ground in that area becomes difficult terrain until "
                                     "cleared. Each 5-foot-square portion of the area requires at least 1 minute to "
                                     "clear by hand.",
                         at_higher_levels="When you cast this spell using a spell slot of 4th level or higher, "
                                          "the damage increases by 1d12 for each slot level above 3rd.")


class FlameArrows(spells.Spell):
    """
    Flame Arrows Spell
    EEPC p. 18
    """

    def __init__(self):
        super().__init__(name="Flame Arrows",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 hour",
                         description="You touch a quiver containing arrows or bolts. When a target is hit by a ranged "
                                     "weapon attack using a piece of ammunition drawn from the quiver, the target "
                                     "takes an extra 1d6 fire damage. The spell's magic ends on the piece of "
                                     "ammunition when it hits or misses, and the spell ends when twelve pieces of "
                                     "ammunition have been drawn from the quiver.",
                         at_higher_levels="When you cast this spell using a spell slot of 4th level or higher, "
                                          "the number of pieces of ammunition you can affect with this spell "
                                          "increases by two for each slot level above 3rd.")


class Frostbite(spells.Spell):
    """
    Frostbite Spell
    EEPC p. 18
    """

    def __init__(self):
        super().__init__(name="Frostbite",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.EVOCATION,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You cause numbing frost to form on one creature that you can see within range. "
                                     "The target must make a Constitution saving throw. On a failed save, the target "
                                     "takes 1d6 cold damage, and it has disadvantage on the next weapon attack roll "
                                     "it makes before the end of its next turn.\n"
                                     "The spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level "
                                     "(3d6), and 17th level (4d6).")


class Gust(spells.Spell):
    """
    Gust Spell
    EEPC p. 19
    """

    def __init__(self):
        super().__init__(name="Gust",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You seize the air and compel it to create one of the following effects at a "
                                     "point you can see within range:\n"
                                     "• One Medium or smaller creature that you choose must succeed on a Strength "
                                     "saving throw or be pushed up to 5 feet away from you.\n"
                                     "• You create a small blast of air capable of moving one object that is neither "
                                     "held nor carried and that weighs no more than 5 pounds. The object is pushed up "
                                     "to 10 feet away from you. It isn't pushed with enough force to cause damage.\n"
                                     "• You create a harmless sensory effect using air, such as causing leaves to "
                                     "rustle, wind to slam shutters shut, or your clothing to ripple in a breeze.")


class IceKnife(spells.Spell):
    """
    Ice Knife Spell
    EEPC p. 19
    """

    def __init__(self):
        super().__init__(name="Ice Knife",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.CONJURATION,
                         spell_range="60 feet",
                         somatic_components=True,
                         material_components_list="a drop of water or a piece of ice",
                         description="You create a shard of ice and fling it at one creature within range. Make a "
                                     "ranged spell attack against the target. On a hit, the target takes 1d10 "
                                     "piercing damage. Hit or miss, the shard then explodes. The target and each "
                                     "creature within 5 feet of it must succeed on a Dexterity saving throw or take "
                                     "2d6 cold damage.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the cold damage increases by 1d6 for each slot level above 1st.")


class Immolation(spells.Spell):
    """
    Immolation Spell
    EEPC p. 19
    """

    def __init__(self):
        super().__init__(name="Ice Knife",
                         spell_lists=[SpellLists.ARCANE],
                         level=5,
                         school=SpellSchools.EVOCATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="Flames wreathe one creature you can see within range. The target must make a "
                                     "Dexterity saving throw. It takes 8d6 fire damage on a failed save, or half as "
                                     "much damage on a successful one. On a failed save, the target also burns for "
                                     "the spell's duration. The burning target sheds bright light in a 30-foot radius "
                                     "and dim light for an additional 30 feet. At the end of each of its turns, "
                                     "the target repeats the saving throw. It takes 4d6 fire damage on a failed save, "
                                     "and the spell ends on a successful one. These magical flames can't be "
                                     "extinguished by nonmagical means.\n"
                                     "If damage from this spell kills a target, the target is turned to ash.")


class InvestitureOfFlame(spells.Spell):
    """
    Investiture of Flame Spell
    EEPC p. 19
    """

    def __init__(self):
        super().__init__(name="Investiture of Flame",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="Flames race across your body, shedding bright light in a 30-foot radius and dim "
                                     "light for an additional 30 feet for the spell's duration. The flames don't harm "
                                     "you. Until the spell ends, you gain the following benefits:\n"
                                     "• You are immune to fire damage and have resistance to cold damage.\n"
                                     "• Any creature that moves within 5 feet of you for the first time on a turn or "
                                     "ends its turn there takes 1d10 fire damage.\n"
                                     "• You can use your action to create a line of fire 15 feet long and 5 feet wide "
                                     "extending from you in a direction you choose. Each creature in the line must "
                                     "make a Dexterity saving throw. A creature takes 4d8 fire damage on a failed "
                                     "save, or half as much damage on a successful one.")


class InvestitureOfIce(spells.Spell):
    """
    Investiture of Ice Spell
    EEPC p. 19
    """

    def __init__(self):
        super().__init__(name="Investiture of Ice",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="Until the spell ends, ice rimes your body, and you gain the following benefits:\n"
                                     "• You are immune to cold damage and have resistance to fire damage.\n"
                                     "• You can move across difficult terrain created by ice or snow without spending "
                                     "extra movement.\n"
                                     "• The ground in a 10-foot radius around you is icy and is difficult terrain for "
                                     "creatures other than you. The radius moves with you.\n"
                                     "• You can use your action to create a 15-foot cone of freezing wind extending "
                                     "from your outstretched hand in a direction you choose. Each creature in the cone "
                                     "must make a Constitution saving throw. A creature takes 4d6 cold damage on a "
                                     "failed save, or half as much damage on a successful one. A creature that fails "
                                     "its save against this effect has its speed halved until the start of your next "
                                     "turn.")


class InvestitureOfStone(spells.Spell):
    """
    Investiture of Stone Spell
    EEPC p. 19-20
    """

    def __init__(self):
        super().__init__(name="Investiture of Stone",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="Until the spell ends, bits of rock spread across your body, and you gain the "
                                     "following benefits:\n"
                                     "• You have resistance to bludgeoning, piercing, and slashing damage from "
                                     "nonmagical attacks.\n"
                                     "• You can use your action to create a small earthquake on the ground in a "
                                     "15-foot radius centered on you. Other creatures on that ground must succeed on a "
                                     "Dexterity saving throw or be knocked prone.\n"
                                     "• You can move across difficult terrain made of earth or stone without spending "
                                     "extra movement. You can move through solid earth or stone as if it was air and "
                                     "without destabilizing it, but you can't end your movement there. If you do so, "
                                     "you are ejected to the nearest unoccupied space, this spell ends, and you are "
                                     "stunned until the end of your next turn.")


class InvestitureOfWind(spells.Spell):
    """
    Investiture of Wind Spell
    EEPC p. 20
    """

    def __init__(self):
        super().__init__(name="Investiture of Wind",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="Until the spell ends, wind whirls around you, and you gain the following "
                                     "benefits:\n"
                                     "• Ranged weapon attacks made against you have disadvantage on the attack roll.\n"
                                     "• You gain a flying speed of 60 feet. If you are still flying when the spell "
                                     "ends, you fall, unless you can somehow prevent it.\n"
                                     "• You can use your action to create a 15-foot cube of swirling wind centered on "
                                     "a point you can see within 60 feet of you. Each creature in that area must make "
                                     "a Constitution saving throw. A creature takes 2d10 bludgeoning damage on a "
                                     "failed save, or half as much damage on a successful one. If a Large or smaller "
                                     "creature fails the save, that creature is also pushed up to 10 feet away from "
                                     "the center of the cube.")


class Maelstrom(spells.Spell):
    """
    Maelstrom Spell
    EEPC p. 20
    """

    def __init__(self):
        super().__init__(name="Maelstrom",
                         spell_lists=[SpellLists.PRIMAL],
                         level=5,
                         school=SpellSchools.EVOCATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="paper or leaf in the shape of a funnel",
                         concentration=True,
                         duration="1 minute",
                         description="A swirling mass of 5-foot-deep water appears in a 30-foot radius centered on a "
                                     "point you can see within range. The point must be on the ground or in a body of "
                                     "water. Until the spell ends, that area is difficult terrain, and any creature "
                                     "that starts its turn there must succeed on a Strength saving throw or take 6d6 "
                                     "bludgeoning damage and be pulled 10 feet toward the center.")


class MagicStone(spells.Spell):
    """
    Magic Stone Spell
    EEPC p. 20
    """

    def __init__(self):
        super().__init__(name="Magic Stone",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="1 bonus action",
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         duration="1 minute",
                         description="You touch one to three pebbles and imbue them with magic. You or someone else "
                                     "can make a ranged spell attack with one of the pebbles by throwing it or "
                                     "hurling it with a sling. If thrown, it has a range of 60 feet. If someone else "
                                     "attacks with the pebble, that attacker adds your spellcasting ability modifier, "
                                     "not the attacker's, to the attack roll. On a hit, the target takes bludgeoning "
                                     "damage equal to 1d6 + your spellcasting ability modifier. Hit or miss, "
                                     "the spell then ends on the stone.\n"
                                     "If you cast this spell again, the spell ends early on any pebbles still "
                                     "affected by it.")


class MaximiliansEarthenGrasp(spells.Spell):
    """
    Maximilian's Earthen Grasp Spell
    EEPC p. 20
    """

    def __init__(self):
        super().__init__(name="Maximilian's Earthen Grasp",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a miniature hand sculpted from clay",
                         concentration=True,
                         duration="1 minute",
                         description="You choose a 5-foot-square unoccupied space on the ground that you can see "
                                     "within range. A Medium hand made from compacted soil rises there and reaches "
                                     "for one creature you can see within 5 feet of it. The target must make a "
                                     "Strength saving throw. On a failed save, the target takes 2d6 bludgeoning "
                                     "damage and is restrained for the spell's duration.\n"
                                     "As an action, you can cause the hand to crush the restrained target, who must "
                                     "make a Strength saving throw. It takes 2d6 bludgeoning damage on a failed save, "
                                     "or half as much damage on a successful one.\n"
                                     "To break out, the restrained target can use its action to make a Strength check "
                                     "against your spell save DC. On a success, the target escapes and is no longer "
                                     "restrained by the hand.\n"
                                     "As an action, you can cause the hand to reach for a different creature or to "
                                     "move to a different unoccupied space within range. The hand releases a "
                                     "restrained target if you do either.")


class MelfsMinuteMeteors(spells.Spell):
    """
    Melf's Minute Meteors Spell
    EEPC p. 20
    """

    def __init__(self):
        super().__init__(name="Melf's Minute Meteors",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.EVOCATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="niter, sulfur, and pine tar formed into a bead",
                         concentration=True,
                         duration="10 minutes",
                         description="You create six tiny meteors in your space. They float in the air and orbit you "
                                     "for the spell's duration. When you cast the spell - and as a bonus action on "
                                     "each of your turns thereafter - you can expend one or two of the meteors, "
                                     "sending them streaking toward a point or points you choose within 120 feet of "
                                     "you. Once a meteor reaches its destination or impacts against a solid surface, "
                                     "the meteor explodes. Each creature within 5 feet of the point where the meteor "
                                     "explodes must make a Dexterity saving throw. A creature takes 2d6 fire damage "
                                     "on a failed save, or half as much damage on a successful one.",
                         at_higher_levels="When you cast this spell using a spell slot of 4th level or higher, "
                                          "the number of meteors created increases by two for each slot level above "
                                          "3rd.")


class MoldEarth(spells.Spell):
    """
    Mold Earth Spell
    EEPC p. 21
    """

    def __init__(self):
        super().__init__(name="Mold Earth",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         duration="Instantaneous or 1 hour",
                         description="You choose a portion of dirt or stone that you can see within range and that "
                                     "fits within a 5-foot cube. You manipulate it in one of the following ways:\n"
                                     "• If you target an area of loose earth, you can instantaneously excavate it, "
                                     "move it along the ground, and deposit it up to 5 feet away. This movement "
                                     "doesn't have enough force to cause damage.\n"
                                     "• You cause shapes, colors, or both to appear on the dirt or stone, spelling "
                                     "out words, creating images, or shaping patterns. The changes last for 1 hour.\n"
                                     "• If the dirt or stone you target is on the ground, you cause it to become "
                                     "difficult terrain. Alternatively, you can cause the ground to become normal "
                                     "terrain if it is already difficult terrain. This change lasts for 1 hour.\n"
                                     "If you cast this spell multiple times, you can have no more than two of its "
                                     "non-instantaneous effects active at a time, and you can dismiss such an effect "
                                     "as an action.")


class PrimordialWard(spells.Spell):
    """
    Primordial Ward Spell
    EEPC p. 21
    """

    def __init__(self):
        super().__init__(name="Primordial Ward",
                         spell_lists=[SpellLists.PRIMAL],
                         level=6,
                         school=SpellSchools.ABJURATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="You have resistance to acid, cold, fire, lightning, and thunder damage for the "
                                     "spell's duration.\n"
                                     "When you take damage of one of those types, you can use your reaction to gain "
                                     "immunity to that type of damage, including against the triggering damage.\n"
                                     "If you do so, the resistances end, and you have the immunity until the end of "
                                     "your next turn, at which time the spell ends.")


class Pyrotechnics(spells.Spell):
    """
    Pyrotechnics Spell
    EEPC p. 21
    """

    def __init__(self):
        super().__init__(name="Pyrotechnics",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="Choose an area of nonmagical flame that you can see and that fits within a "
                                     "5-foot cube within range. You can extinguish the fire in that area, "
                                     "and you create either fireworks or smoke when you do so.\n"
                                     "Fireworks. The target explodes with a dazzling display of colors. Each creature "
                                     "within 10 feet of the target must succeed on a Constitution saving throw or "
                                     "become blinded until the end of your next turn.\n"
                                     "Smoke. Thick black smoke spreads out from the target in a 20-foot radius, "
                                     "moving around corners. The area of the smoke is heavily obscured. The smoke "
                                     "persists for 1 minute or until a strong wind disperses it.")


class ShapeWater(spells.Spell):
    """
    Shape Water Spell
    EEPC p. 21
    """

    def __init__(self):
        super().__init__(name="Shape Water",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         somatic_components=True,
                         duration="Instantaneous or 1 hour",
                         description="You choose an area of water that you can see within range and that fits within "
                                     "a 5-foot cube. You manipulate it in one of the following ways:\n"
                                     "• You instantaneously move or otherwise change the flow of the water as you "
                                     "direct, up to 5 feet in any direction. This movement doesn't have enough force "
                                     "to cause damage.\n"
                                     "• You cause the water to form into simple shapes and animate at your direction. "
                                     "This change lasts for 1 hour.\n"
                                     "• You change the water's color or opacity. The water must be changed in the "
                                     "same way throughout. This change lasts for 1 hour.\n"
                                     "• You freeze the water, provided that there are no creatures in it. The water "
                                     "unfreezes in 1 hour.\n"
                                     "If you cast this spell multiple times, you can have no more than two of its "
                                     "non-instantaneous effects active at a time, and you can dismiss such an effect "
                                     "as an action.")


class Skywrite(spells.Spell):
    """
    Skywrite Spell
    EEPC p. 22
    """

    def __init__(self):
        super().__init__(name="Skywrite",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         ritual=True,
                         spell_range="Sight",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 hour",
                         description="You cause up to ten words to form in a part of the sky you can see. The words "
                                     "appear to be made of cloud and remain in place for the spell's duration. The "
                                     "words dissipate when the spell ends. A strong wind can disperse the clouds and "
                                     "end the spell early.")


class SnillocsSnowballSwarm(spells.Spell):
    """
    Snilloc's Snowball Swarm Spell
    EEPC p. 22
    """

    def __init__(self):
        super().__init__(name="Snilloc's Snowball Swarm",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.EVOCATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of ice or a small white rock chip",
                         description="A flurry of magic snowballs erupts from a point you choose within range. Each "
                                     "creature in a 5-foot-radius sphere centered on that point must make a Dexterity "
                                     "saving throw. A creature takes 3d6 cold damage on a failed save, or half as "
                                     "much damage on a successful one.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "the damage increases by 1d6 for each slot level above 2nd.")


class StormSphere(spells.Spell):
    """
    Storm Sphere Spell
    EEPC p. 22
    """

    def __init__(self):
        super().__init__(name="Storm Sphere",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.EVOCATION,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="A 20-foot-radius sphere of whirling air springs into existence centered on a "
                                     "point you choose within range. The sphere remains for the spell's duration. "
                                     "Each creature in the sphere when it appears or that ends its turn there must "
                                     "succeed on a Strength saving throw or take 2d6 bludgeoning damage. The sphere's "
                                     "space is difficult terrain.\n"
                                     "Until the spell ends, you can use a bonus action on each of your turns to cause "
                                     "a bolt of lightning to leap from the center of the sphere toward one creature "
                                     "you choose within 60 feet of the center. Make a ranged spell attack. You have "
                                     "advantage on the attack roll if the target is in the sphere. On a hit, "
                                     "the target takes 4d6 lightning damage.\n"
                                     "Creatures within 30 feet of the sphere have disadvantage on Wisdom (Perception) "
                                     "checks made to listen.",
                         at_higher_levels="When you cast this spell using a spell slot of 5th level or higher, "
                                          "the damage increases for each of its effects by 1d6 for each slot level "
                                          "above 4th.")


class Thunderclap(spells.Spell):
    """
    Thunderclap Spell
    EEPC p. 22
    """

    def __init__(self):
        super().__init__(name="Thunderclap",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.EVOCATION,
                         spell_range="Self (5-foot radius)",
                         somatic_components=True,
                         description="You create a burst of thunderous sound that can be heard up to 100 feet away. "
                                     "Each creature within range, other than you, must succeed on a Constitution "
                                     "saving throw or take 1d6 thunder damage.\n"
                                     "The spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level "
                                     "(3d6), and 17th level (4d6).")


class TidalWave(spells.Spell):
    """
    Tidal Wave Spell
    EEPC p. 22
    """

    def __init__(self):
        super().__init__(name="Tidal Wave",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.CONJURATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of water",
                         description="You conjure up a wave of water that crashes down on an area within range. The "
                                     "area can be up to 30 feet long, up to 10 feet wide, and up to 10 feet tall. "
                                     "Each creature in that area must make a Dexterity saving throw. On a failed "
                                     "save, a creature takes 4d8 bludgeoning damage and is knocked prone. On a "
                                     "successful save, a creature takes half as much damage and isn't knocked prone. "
                                     "The water then spreads out across the ground in all directions, extinguishing "
                                     "unprotected flames in its area and within 30 feet of it, and then it vanishes.")


class TransmuteRock(spells.Spell):
    """
    Transmute Rock Spell
    EEPC p. 22-23
    """

    def __init__(self):
        super().__init__(name="Transmute Rock",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=5,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="clay and water",
                         description="You choose an area of stone or mud that you can see that fits within a 40-foot "
                                     "cube and is within range, and choose one of the following effects.\n"
                                     "Transmute Rock to Mud. Nonmagical rock of any sort in the area becomes an equal "
                                     "volume of thick, flowing mud that remains for the spell's duration.\n"
                                     "The ground in the spell's area becomes muddy enough that creatures can sink "
                                     "into it. Each foot that a creature moves through the mud costs 4 feet of "
                                     "movement, and any creature on the ground when you cast the spell must make a "
                                     "Strength saving throw. A creature must also make the saving throw when it moves "
                                     "into the area for the first time on a turn or ends its turn there. On a failed "
                                     "save, a creature sinks into the mud and is restrained, though it can use an "
                                     "action to end the restrained condition on itself by pulling itself free of the "
                                     "mud.\n"
                                     "If you cast the spell on a ceiling, the mud falls. Any creature under the mud "
                                     "when it falls must make a Dexterity saving throw. A creature takes 4d8 "
                                     "bludgeoning damage on a failed save, or half as much damage on a successful "
                                     "one.\n"
                                     "Transmute Mud to Rock. Nonmagical mud or quicksand in the area no more than 10 "
                                     "feet deep transforms into soft stone for the spell's duration. Any creature in "
                                     "the mud when it transforms must make a Dexterity saving throw. On a successful "
                                     "save, a creature is shunted safely to the surface in an unoccupied space. On a "
                                     "failed save, a creature becomes restrained by the rock. A restrained creature, "
                                     "or another creature within reach, can use an action to try to break the rock by "
                                     "succeeding on a DC 20 Strength check or by dealing damage to it. The rock has "
                                     "AC 15 and 25 hit points, and it is immune to poison and psychic damage.")


class VitriolicSphere(spells.Spell):
    """
    Vitriolic Sphere Spell
    EEPC p. 23
    """

    def __init__(self):
        super().__init__(name="Vitriolic Sphere",
                         spell_lists=[SpellLists.ARCANE],
                         level=4,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of giant slug bile",
                         description="You point at a location within range, and a glowing, 1-foot-diameter ball of "
                                     "emerald acid streaks there and explodes in a 20-foot-radius sphere. Each "
                                     "creature in that area must make a Dexterity saving throw. On a failed save, "
                                     "a creature takes 10d4 acid damage and another 5d4 acid damage at the end of its "
                                     "next turn. On a successful save, a creature takes half the initial damage and "
                                     "no damage at the end of its next turn.",
                         at_higher_levels="When you cast this spell using a spell slot of 5th level or higher, "
                                          "the initial damage increases by 2d4 for each slot level above 4th.")


class WallOfSand(spells.Spell):
    """
    Wall of Sand Spell
    EEPC p. 23
    """

    def __init__(self):
        super().__init__(name="Wall of Sand",
                         spell_lists=[SpellLists.ARCANE],
                         level=3,
                         school=SpellSchools.EVOCATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a handful of sand",
                         concentration=True,
                         duration="10 minutes",
                         description="You conjure up a wall of swirling sand on the ground at a point you can see "
                                     "within range. You can make the wall up to 30 feet long, 10 feet high, "
                                     "and 10 feet thick, and it vanishes when the spell ends. It blocks line of sight "
                                     "but not movement. A creature is blinded while in the wall's space and must "
                                     "spend 3 feet of movement for every 1 foot it moves there.")


class WallOfWater(spells.Spell):
    """
    Wall of Water Spell
    EEPC p. 23
    """

    def __init__(self):
        super().__init__(name="Wall of Water",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=3,
                         school=SpellSchools.EVOCATION,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of water",
                         concentration=True,
                         duration="10 minutes",
                         description="You create a wall of water on the ground at a point you can see within range. "
                                     "You can make the wall up to 30 feet long, 10 feet high, and 1 foot thick, "
                                     "or you can make a ringed wall up to 20 feet in diameter, 20 feet high, "
                                     "and 1 foot thick. The wall vanishes when the spell ends. The wall's space is "
                                     "difficult terrain.\n"
                                     "Any ranged weapon attack that enters the wall's space has disadvantage on the "
                                     "attack roll, and fire damage is halved if the fire effect passes through the "
                                     "wall to reach its target. Spells that deal cold damage that pass through the "
                                     "wall cause the area of the wall they pass through to freeze solid (at least a "
                                     "5-foot-square section is frozen). Each 5-foot-square frozen section has AC 5 "
                                     "and 15 hit points. Reducing a frozen section to 0 hit points destroys it. When "
                                     "a section is destroyed, the wall's water doesn't fill it.")


class WardingWind(spells.Spell):
    """
    Warding Wind Spell
    EEPC p. 23
    """

    def __init__(self):
        super().__init__(name="Warding Wind",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.EVOCATION,
                         spell_range="Self",
                         verbal_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="A strong wind (20 miles per hour) blows around you in a 10-foot radius and moves "
                                     "with you, remaining centered on you. The wind lasts for the spell's duration.\n"
                                     "The wind has the following effects:\n"
                                     "• It deafens you and other creatures in its area.\n"
                                     "• It extinguishes unprotected flames in its area that are torch-sized or "
                                     "smaller.\n"
                                     "• It hedges out vapor, gas, and fog that can be dispersed by strong wind.\n"
                                     "• The area is difficult terrain for creatures other than you.\n"
                                     "• The attack rolls of ranged weapon attacks have disadvantage if the attacks "
                                     "pass in or out of the wind.")


class WaterySphere(spells.Spell):
    """
    Watery Sphere Spell
    EEPC p. 23
    """

    def __init__(self):
        super().__init__(name="Watery Sphere",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=4,
                         school=SpellSchools.CONJURATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a droplet of water",
                         concentration=True,
                         duration="1 minute",
                         description="You conjure up a sphere of water with a 5-foot radius at a point you can see "
                                     "within range. The sphere can hover but no more than 10 feet off the ground. The "
                                     "sphere remains for the spell's duration.\n"
                                     "Any creature in the sphere's space must make a Strength saving throw. On a "
                                     "successful save, a creature is ejected from that space to the nearest "
                                     "unoccupied space of the creature's choice outside the sphere. A Huge or larger "
                                     "creature succeeds on the saving throw automatically, and a Large or smaller "
                                     "creature can choose to fail it. On a failed save, a creature is restrained by "
                                     "the sphere and is engulfed by the water. At the end of each of its turns, "
                                     "a restrained target can repeat the saving throw, ending the effect on itself on "
                                     "a success.\n"
                                     "The sphere can restrain as many as four Medium or smaller creatures or one "
                                     "Large creature. If the sphere restrains a creature that causes it to exceed "
                                     "this capacity, a random creature that was already restrained by the sphere "
                                     "falls out of it and lands prone in a space within 5 feet of it.\n"
                                     "As an action, you can move the sphere up to 30 feet in a straight line. If it "
                                     "moves over a pit, a cliff, or other drop-off, it safely descends until it is "
                                     "hovering 10 feet above the ground. Any creature restrained by the sphere moves "
                                     "with it. You can ram the sphere into creatures, forcing them to make the saving "
                                     "throw.\n"
                                     "When the spell ends, the sphere falls to the ground and extinguishes all normal "
                                     "flames within 30 feet of it. Any creature restrained by the sphere is knocked "
                                     "prone in the space where it falls. The water then vanishes.")


class Whirlwind(spells.Spell):
    """
    Whirlwind Spell
    EEPC p. 24
    """

    def __init__(self):
        super().__init__(name="Whirlwind",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=7,
                         school=SpellSchools.EVOCATION,
                         spell_range="300 feet",
                         verbal_components=True,
                         material_components_list="a piece of straw",
                         concentration=True,
                         duration="1 minute",
                         description="A whirlwind howls down to a point that you can see on the ground within range. "
                                     "The whirlwind is a 10-foot-radius, 30-foot-high cylinder centered on that "
                                     "point. Until the spell ends, you can use your action to move the whirlwind up "
                                     "to 30 feet in any direction along the ground. The whirlwind sucks up any Medium "
                                     "or smaller objects that aren't secured to anything and that aren't worn or "
                                     "carried by anyone.\n"
                                     "A creature must make a Dexterity saving throw the first time on a turn that it "
                                     "enters the whirlwind or that the whirlwind enters its space, including when the "
                                     "whirlwind first appears. A creature takes 10d6 bludgeoning damage on a failed "
                                     "save, or half as much damage on a successful one. In addition, a Large or "
                                     "smaller creature that fails the save must succeed on a Strength saving throw or "
                                     "become restrained in the whirlwind until the spell ends. When a creature starts "
                                     "its turn restrained by the whirlwind, the creature is pulled 5 feet higher "
                                     "inside it, unless the creature is at the top. A restrained creature moves with "
                                     "the whirlwind and falls when the spell ends, unless the creature has some means "
                                     "to stay aloft.\n"
                                     "A restrained creature can use an action to make a Strength or Dexterity check "
                                     "against your spell save DC. If successful, the creature is no longer restrained "
                                     "by the whirlwind and is hurled 3d6 × 10 feet away from it in a random "
                                     "direction.")


CONTENT = {
    "Feats": {
        # TODO The rest of the feats
        # "Svirfneblin Magic": SvirfneblinMagic,
    },
    "Species": {
        # TODO The rest of the species,
        # "Aarakocra": Aarakocra,
        # "Deep Gnome": DeepGnome,
        # "Air Genasi": AirGenasi,
        # "Earth Genasi": EarthGenasi,
        # "Fire Genasi": FireGenasi,
        # "Water Genasi": WaterGenasi,
        "Stone Goliath": "OBSOLETE",
    },
    "Spells": {
        "Abi-Dalzim's Horrid Wilting": HorridWilting,
        "Absorb Elements": AbsorbElements,
        "Aganazzar's Scorcher": AganazzarsScorcher,
        "Beast Bond": BeastBond,
        "Bones of the Earth": BonesOfTheEarth,
        "Catapult": Catapult,
        "Control Flames": ControlFlames,
        "Control Winds": ControlWinds,
        "Create Bonfire": CreateBonfire,
        "Dust Devil": DustDevil,
        "Earth Tremor": EarthTremor,
        "Earthbind": Earthbind,
        "Elemental Bane": ElementalBane,
        "Erupting Earth": EruptingEarth,
        "Flame Arrows": FlameArrows,
        "Frostbite": Frostbite,
        "Gust": Gust,
        "Ice Knife": IceKnife,
        "Immolation": Immolation,
        "Investiture of Flame": InvestitureOfFlame,
        "Investiture of Ice": InvestitureOfIce,
        "Investiture of Stone": InvestitureOfStone,
        "Investiture of Wind": InvestitureOfWind,
        "Maelstrom": Maelstrom,
        "Magic Stone": MagicStone,
        "Maximilian's Earthen Grasp": MaximiliansEarthenGrasp,
        "Melf's Minute Meteors": MelfsMinuteMeteors,
        "Mold Earth": MoldEarth,
        "Primordial Ward": PrimordialWard,
        "Pyrotechnics": Pyrotechnics,
        "Shape Water": ShapeWater,
        "Skywrite": Skywrite,
        "Snilloc's Snowball Swarm": SnillocsSnowballSwarm,
        "Storm Sphere": StormSphere,
        "Thunderclap": Thunderclap,
        "Tidal Wave": TidalWave,
        "Transmute Rock": TransmuteRock,
        "Vitriolic Sphere": VitriolicSphere,
        "Wall of Sand": WallOfSand,
        "Wall of Water": WallOfWater,
        "Warding Wind": WardingWind,
        "Watery Sphere": WaterySphere,
        "Whirlwind": Whirlwind,
    }
}
