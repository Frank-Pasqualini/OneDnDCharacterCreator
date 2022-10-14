"""
Content from the Dungeons and Dragons System Reference Document v5.1.
https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf
"""

from rules import spells, armors
from rules.enums import ArmorTraining, SpellLists, SpellSchools


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
                         material_components=True,
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
                         material_components=True,
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
                         material_components=True,
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
                         material_components=True,
                         material_components_list="a small amount of alcohol or distilled spirits",
                         duration="1 hour",
                         description="Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4 "
                                     "temporary hit points for the duration.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you gain 5 additional temporary hit points for each slot level above 1st.")


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
                         material_components=True,
                         material_components_list="(a firefly or phosphorescent moss",
                         duration="1 hour",
                         description="You touch one object that is no larger than 10 feet in any dimension. Until the "
                                     "spell ends, the object sheds bright light in a 20-foot radius and dim light "
                                     "for an additional 20 feet. The light can be colored as you like. Completely "
                                     "covering the object with something opaque blocks the light. The spell ends if "
                                     "you cast it again or dismiss it as an action.\n "
                                     "If you target an object held or worn by a hostile creature, that creature must "
                                     "succeed on a Dexterity saving throw to avoid the spell.")


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
                                     "the spell ends.\n "
                                     "At the end of each of the target's turns, it can make a Constitution saving "
                                     "throw against the spell. On a success, the spell ends.")


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
                                     "shut.\n "
                                     "• You alter the appearance of your eyes for 1 minute.\n"
                                     "If you cast this spell multiple times, you can have up to three of its 1-minute "
                                     "effects active at a time, and you can dismiss such an effect as an action.")


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
    "Spells": {
        # TODO All spells from SRD
        "Animal Friendship": AnimalFriendship,
        "Animal Messenger": AnimalMessenger,
        "Augury": Augury,
        "Barkskin": "OBSOLETE",
        "Beast Sense": BeastSense,
        "Chill Touch": ChillTouch,
        "Cordon of Arrows": CordonOfArrows,
        "Create or Destroy Water": CreateOrDestroyWater,
        "Cure Wounds": CureWounds,
        # "Dancing Lights": DancingLights,
        # "Darkness": Darkness,
        "Darkvision": Darkvision,
        "Detect Magic": DetectMagic,
        "Detect Poison and Disease": DetectPoisonAndDisease,
        "Detect Thoughts": DetectThoughts,
        # "Divine Favor": DivineFavor,
        "Druidcraft": Druidcraft,
        "Enhance Ability": EnhanceAbility,
        "Enlarge/Reduce": EnlargeReduce,
        "Ensnaring Strike": EnsnaringStrike,
        "Entangle": Entangle,
        # "Faerie Fire": FaerieFire,
        "False Life": FalseLife,
        "Find Traps": FindTraps,
        # "Fire Bolt": FireBolt,
        "Fog Cloud": FogCloud,
        "Gentle Repose": GentleRepose,
        "Goodberry": Goodberry,
        "Guidance": "OBSOLETE",
        "Hail of Thorns": HailOfThorns,
        "Healing Word": HealingWord,
        "Heat Metal": HeatMetal,
        # "Hellish Rebuke": HellishRebuke,
        # "Hold Person": HoldPerson,
        "Hunter's Mark": HuntersMark,
        "Jump": Jump,
        "Lesser Restoration": LesserRestoration,
        "Light": Light,
        "Locate Animals or Plants": LocateAnimalsOrPlants,
        "Locate Object": LocateObject,
        "Longstrider": Longstrider,
        "Mending": Mending,
        "Message": Message,
        # "Minor Illusion": MinorIllusion,
        # "Misty Step": MistyStep,
        "Pass Without Trace": PassWithoutTrace,
        "Poison Spray": PoisonSpray,
        # "Prestidigitation": Prestidigitation,
        "Protection from Poison": ProtectionFromPoison,
        "Purify Food and Drink": PurifyFoodAndDrink,
        "Ray of Enfeeblement": RayOfEnfeeblement,
        # "Ray of Sickness": RayOfSickness,
        "Resistance": Resistance,
        "Shillelagh": Shillelagh,
        "Silence": Silence,
        "Spare the Dying": SpareTheDying,
        "Speak with Animals": SpeakWithAnimals,
        "Spike Growth": SpikeGrowth
        "Thaumaturgy": Thaumaturgy,
        "Thorn Whip": ThornWhip,
        "Thunderwave": Thunderwave,
        # "Zone of Truth": ZoneOfTruth,
    },
    # TODO Other things from SRD
}
