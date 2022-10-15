"""
Content from the Dungeons and Dragons Elemental Evil Player's Companion.
"""

from rules import spells
from rules.enums import SpellLists, SpellSchools


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
                         material_components=True,
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
                                     "• You cause simple shapes—such as the vague form of a creature, an inanimate "
                                     "object, or a location—to appear within the flames and animate as you like. The "
                                     "shapes last for 1 hour.\n"
                                     "If you cast this spell multiple times, you can have up to three of its "
                                     "non-instantaneous effects active at a time, and you can dismiss such an effect "
                                     "as an action.")


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
                                     "ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire’s "
                                     "space when you cast the spell must succeed on a Dexterity saving throw or take "
                                     "1d8 fire damage. A creature must also make the saving throw when it moves into "
                                     "the bonfire’s space for the first time on a turn or ends its turn there.\n"
                                     "The bonfire ignites flammable objects in its area that aren’t being worn or "
                                     "carried.\n"
                                     "The spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level "
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
                         material_components=True,
                         material_components_list="a pinch of dust",
                         concentration=True,
                         duration="1 minute",
                         description="Choose an unoccupied 5-foot cube of air that you can see within range. An "
                                     "elemental force that resembles a dust devil appears in the cube and lasts for "
                                     "the spell's duration.\n"
                                     "Any creature that ends its turn within 5 feet of the dust devil must make a "
                                     "Strength saving throw. On a failed save, the creature takes 1d8 bludgeoning "
                                     "damage and is pushed 10 feet away. On a successful save, the creature takes "
                                     "half as much damage and isn’t pushed.\n"
                                     "As a bonus action, you can move the dust devil up to 30 feet in any direction. "
                                     "If the dust devil moves over sand, dust, loose dirt, or small gravel, "
                                     "it sucks up the material and forms a 10-foot-radius cloud of debris around "
                                     "itself that lasts until the start of your next turn. The cloud heavily obscures "
                                     "its area.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "the damage increases by 1d8 for each slot level above 2nd.")


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
                         material_components=True,
                         material_components_list="a drop of water or a piece of ice",
                         description="You create a shard of ice and fling it at one creature within range. Make a "
                                     "ranged spell attack against the target. On a hit, the target takes 1d10 "
                                     "piercing damage. Hit or miss, the shard then explodes. The target and each "
                                     "creature within 5 feet of it must succeed on a Dexterity saving throw or take "
                                     "2d6 cold damage.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the cold damage increases by 1d6 for each slot level above 1st.")


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
                                     "not the attacker’s, to the attack roll. On a hit, the target takes bludgeoning "
                                     "damage equal to 1d6 + your spellcasting ability modifier. Hit or miss, "
                                     "the spell then ends on the stone.\n"
                                     "If you cast this spell again, the spell ends early on any pebbles still "
                                     "affected by it.")


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


CONTENT = {
    "Spells": {
        # TODO the rest of the spells
        # "Abi-Dalzim's Horrid Wilting": HorridWilting,
        "Absorb Elements": AbsorbElements,
        # "Aganazzar's Scorcher": AganazzarsScorcher,
        "Beast Bond": BeastBond,
        # "Bones of the Earth": BonesOfTheEarth,
        # "Catapult": Catapult,
        "Control Flames": ControlFlames,
        # "Control Winds": ControlWinds,
        "Create Bonfire": CreateBonfire,
        "Dust Devil": DustDevil,
        # "Earth Tremor": EarthTremor,
        "Earthbind": Earthbind,
        # "Elemental Bane": ElementalBane,
        # "Erupting Earth": EruptingEarth,
        # "Flame Arrows": FlameArrows,
        # "Frostbite": Frostbite,
        "Gust": Gust,
        "Ice Knife": IceKnife,
        # "Immolation": Immolation,
        # "Investiture of Flame": InvestitureOfFlame,
        # "Investiture of Ice": InvestitureOfIce,
        # "Investiture of Stone": InvestitureOfStone,
        # "Investiture of Wind": InvestitureOfWind,
        # "Maelstrom": Maelstrom,
        "Magic Stone": MagicStone,
        # "Maximilian's Earthen Grasp": MaximiliansEarthenGrasp,
        # "Melf's Minute Meteors": MelfsMinuteMeteors,
        "Mold Earth": MoldEarth,
        # "Primordial Ward": PrimordialWard,
        # "Pyrotechnics": Pyrotechnics,
        "Shape Water": ShapeWater,
        "Skywrite": Skywrite,
        # "Snilloc's Snowball Swarm": SnillocsSnowballSwarm,
        # "Storm Sphere": StormSphere,
        # "Thunderclap": Thunderclap,
        # "Tidal Wave": TidalWave,
        # "Transmute Rock": TransmuteRock,
        # "Vitriolic Sphere": VitriolicSphere,
        # "Wall of Sand": WallOfSand,
        # "Wall of Water": WallOfWater,
        # "Warding Wind": WardingWind,
        # "Watery Sphere": WaterySphere,
        # "Whirlwind": Whirlwind,
    }
    # TODO the rest
}
