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
                                     "golden orb for clear skies, a cloud fo r rain, falling snowflakes for snow, "
                                     "and so on. This effect persists for 1 round.\n"
                                     "• You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.\n"
                                     "• You create an instantaneous, harmless sensory effect, such as falling leaves, "
                                     "a puff of wind, the sound of a small animal, or the faint odor of skunk. The "
                                     "effect must fit in a 5-foot cube.\n"
                                     "• You instantly light or snuff out a candle, a torch, or a small campfire.")


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
                         material_components_list="a firefly or phosphorescent moss",
                         duration="1 hour",
                         description="You touch one object that is no larger than 10 feet in any dimension. Until the "
                                     "spell ends, the object sheds bright light in a 20-foot radius and dim light "
                                     "for an additional 20 feet. The light can be colored as you like. Completely "
                                     "covering the object with something opaque blocks the light. The spell ends if "
                                     "you cast it again or dismiss it as an action.\n"
                                     "If you target an object held or worn by a hostile creature, that creature must "
                                     "succeed on a Dexterity saving throw to avoid the spell.")


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
                         material_components=True,
                         material_components_list="a pinch of dirt",
                         duration="1 hour",
                         description="You touch a creature. The target's speed increases by 10 feet until the spell "
                                     "ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you can target one additional creature for each slot level above 1st.")


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
                         material_components=True,
                         material_components_list="ashes from a burned leaf of mistletoe and a sprig of spruce",
                         concentration=True,
                         duration="1 hour",
                         description="A veil of shadows and silence radiates from you, masking you and your "
                                     "companions from detection. For the duration, each creature you choose within 30 "
                                     "feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and "
                                     "can't be tracked except by magical means. A creature that receives this bonus "
                                     "leaves behind no tracks or other traces of its passage.")


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
        # TODO All subclasses from SRD
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
        # TODO All spells from SRD
        # "Acid Arrow": AcidArrow,
        # "Acid Splash": AcidSplash,
        # "Aid": Aid,
        # "Alarm": Alarm,
        # "Alter Self", AlterSelf,
        "Animal Friendship": AnimalFriendship,
        "Animal Messenger": AnimalMessenger,
        # "Animal Shapes": AnimalShapes,
        # "Animate Dead": AnimateDead,
        # "Animate Objects": AnimateObjects,
        # "Antilife Shell": AntilifeShell,
        # "Antimagic Field": AntimagicField,
        # "Antipathy/Sympathy": AntipathySympathy,
        # "Arcane Eye": ArcaneEye,
        # "Arcane Hand": ArcaneHand,
        # "Arcane Lock": ArcaneLock,
        # "Arcane Sword": ArcaneSword,
        # "Arcanist's Magic Aura": ArcanistsMagicAura,
        # "Astral Projection": AstralProjection,
        "Augury": Augury,
        # "Awaken": Awaken,
        # "Bane": Bane,
        # "Banishment": Banishment,
        "Barkskin": "OBSOLETE",
        # "Beacon of Hope": BeaconOfHope,
        # "Bestow Curse": BestowCurse,
        # "Black Tentacles": BlackTentacles,
        # "Blade Barrier": BladeBarrier,
        # "Bless": Bless,
        # "Blight": Blight,
        # "Blindness/Deafness": BlindnessDeafness,
        # "Blink": Blink,
        # "Blur": Blur,
        # "Branding Smite": BrandingSmite,
        # "Burning Hands": BurningHands,
        # "Call Lightning": CallLightning,
        # "Calm Emotions": CalmEmotions,
        # "Chain Lightning": ChainLightning,
        # "Charm Person": CharmPerson,
        "Chill Touch": ChillTouch,
        # "Circle of Death": CircleOfDeath,
        # "Clairvoyance": Clairvoyance,
        # "Clone": Clone,
        # "Cloudkill": Cloudkill,
        # "Color Spray": ColorSpray,
        # "Command": Command,
        # "Commune": Commune,
        # "Commune with Nature": CommuneWithNature,
        # "Comprehend Languages": ComprehendLanguages,
        # "Compulsion": Compulsion,
        # "Cone of Cold": ConeOfCold,
        # "Confusion": Confusion,
        # "Conjure Animals": ConjureAnimals,
        # "Conjure Celestial": ConjureCelestial,
        # "Conjure Elemental": ConjureElemental,
        # "Conjure Fey": ConjureFey,
        # "Conjure Minor Elementals": ConjureMinorElementals,
        # "Conjure Woodland Beings": ConjureWoodlandBeings,
        # "Contact Other Plane": ConjureOtherPlane,
        # "Contagion": Contagion,
        # "Contingency": Contingency,
        # "Continual Flame": ContinualFlame,
        # "Control Water": ControlWater,
        # "Control Weather": ControlWeather,
        # "Counterspell": Counterspell,
        # "Create Food and Water": CreateFoodAndWater,
        "Create or Destroy Water": CreateOrDestroyWater,
        # "Create Undead": CreateUndead,
        # "Creation": Creation,
        "Cure Wounds": CureWounds,
        # "Dancing Lights": DancingLights,
        # "Darkness": Darkness,
        "Darkvision": Darkvision,
        # "Daylight": Daylight,
        # "Death Ward": DeathWard,
        # "Delayed Blast Fireball": DelayedBlastFireball,
        # "Demiplane": Demiplane,
        # "Detect Evil and Good": DetectEvilAndGood,
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
        # TODO All weapons from SRD
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
