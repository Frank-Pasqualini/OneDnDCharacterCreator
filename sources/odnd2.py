from rules import classes, spells
from rules.enums import SpellLists, SpellSchools


class Rogue(classes.CharacterClass):
    # TODO
    def __init__(self):
        super().__init__(name="Rogue")


class Barkskin(spells.Spell):
    def __init__(self):
        super().__init__(name="Barkskin",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="Bonus Action",
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components=True,
                         material_components_list="a handful of bark",
                         concentration=True,
                         duration="1 hour",
                         description="You touch one willing creature to protect it with regenerating bark. Until the "
                                     "Spell ends, the target’s skin assumes a bark-like appearance, and at the start "
                                     "of each of the target’s turns, the target gains a number of Temporary Hit "
                                     "Points equal to your Spellcasting Ability Modifier plus your Proficiency Bonus.",
                         at_higher_levels="When you cast this Spell using a Spell Slot of 3rd level or higher, "
                                          "you can target one additional willing creature for each slot level above "
                                          "2nd.")


class Guidance(spells.Spell):
    def __init__(self):
        super().__init__(name="Guidance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.DIVINATION,
                         casting_time="Reaction, which you take in response to you or an ally within 30 feet of you "
                                      "failing an Ability Check",
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You channel magical insight to the creature who failed the Ability Check. That "
                                     "creature can roll a d4 and add the number rolled to the check, potentially "
                                     "turning it into a success.\n"
                                     "Once a creature rolls the die for this Spell,that creature can’t benefit from "
                                     "the Spell again until the creature finishes a Long Rest.")


CONTENT = {
    #  TODO
    "Classes": {
        "Rogue": Rogue,
    },
    "Spells": {
        "Barkskin": Barkskin,
        "Guidance": Guidance,
    },
}
