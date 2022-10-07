from rules import spells, armors
from rules.enums import ArmorTraining, SpellLists, SpellSchools


class Padded(armors.Armor):
    def __init__(self,
                 name: str = "Padded",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=11+magic_bonus,
                         stealth_disadvantage=True)


class Leather(armors.Armor):
    def __init__(self,
                 name: str = "Leather",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=11+magic_bonus)


class StuddedLeather(armors.Armor):
    def __init__(self,
                 name: str = "Studded Leather",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=12+magic_bonus)


class Hide(armors.Armor):
    def __init__(self,
                 name: str = "Hide",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=12+magic_bonus)


class ChainShirt(armors.Armor):
    def __init__(self,
                 name: str = "Chain Shirt",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=13+magic_bonus)


class ScaleMail(armors.Armor):
    def __init__(self,
                 name: str = "Scale Mail",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=14+magic_bonus,
                         stealth_disadvantage=True)


class Breastplate(armors.Armor):
    def __init__(self,
                 name: str = "Breastplate",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=14+magic_bonus)


class HalfPlate(armors.Armor):
    def __init__(self,
                 name: str = "Half Plate",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=15+magic_bonus,
                         stealth_disadvantage=True)


class RingMail(armors.Armor):
    def __init__(self,
                 name: str = "Ring Mail",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=14+magic_bonus,
                         stealth_disadvantage=True)


class ChainMail(armors.Armor):
    def __init__(self,
                 name: str = "Chain Mail",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=16+magic_bonus,
                         stealth_disadvantage=True)


class Splint(armors.Armor):
    def __init__(self,
                 name: str = "Splint",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=17+magic_bonus,
                         stealth_disadvantage=True)


class Plate(armors.Armor):
    def __init__(self,
                 name: str = "Plate",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=18+magic_bonus,
                         stealth_disadvantage=True)


class Shield(armors.Shield):
    def __init__(self,
                 name: str = "Shield",
                 magic_bonus: int = 0):
        super().__init__(name=name,
                         armor_class=2+magic_bonus)


class AnimalMessenger(spells.Spell):
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
        # TODO
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
}
