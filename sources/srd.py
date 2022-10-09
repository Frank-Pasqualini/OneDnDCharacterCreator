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
        "Animal Messenger": AnimalMessenger,
        # "Barkskin": Barkskin,
        # "Chill Touch": ChillTouch,
        # "Cure Wounds": CureWounds,
        # "Dancing Lights": DancingLights,
        # "Darkness": Darkness,
        # "Detect Magic": DetectMagic,
        # "Divine Favor": DivineFavor,
        # "Druidcraft": Druidcraft,
        # "Faerie Fire: FaerieFire,
        # "False Life": FalseLife,
        # "Fire Bolt": FireBolt,
        # "Guidance": Guidance,
        # "Healing Word": HealingWord,
        # "Hellish Rebuke": HellishRebuke,
        # "Hold Person": HoldPerson,
        # "Lesser Restoration": LesserRestoration,
        "Light": Light,
        # "Longstrider": Longstrider,
        # "Mending": Mending,
        # "Minor Illusion": MinorIllusion,
        # "Misty Step": MistyStep,
        # "Pass Without Trace": PassWithoutTrace,
        # "Poison Spray": PoisonSpray,
        # "Prestidigitation": Prestidigitation,
        # "Ray of Enfeeblement": RayOfEnfeeblement,
        # "Ray of Sickness": RayOfSickness,
        # "Speak with Animals": SpeakWithAnimals,
        # "Thaumaturgy": Thaumaturgy,
        # "Zone of Truth": ZoneOfTruth,
    },
    # TODO Other things from SRD
}
