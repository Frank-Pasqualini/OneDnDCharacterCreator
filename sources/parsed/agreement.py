"""
Merges sources and checks agreement between them
This can probably be refactored out
"""


import json

odnd2 = json.loads(open("sources/parsed/odnd2.json", encoding="utf-8").read())
srd = json.loads(open("sources/parsed/srd.json", encoding="utf-8").read())

odnd2_names = {x["name"] for x in odnd2}
srd_names = {x["namer"] for x in srd}


names_map = {
    "Freezing Sphere": "Otiluke's Freezing Sphere",
    "Irresistible Dance": "Otto's Irresistible Dance",
    "Floating Disk": "Tenser's Floating Disk",
    "Secret Chest": "Leomund's Secret Chest",
    "Arcane Sword": "Mordenkainen's Sword",
    "Black Tentacles": "Evard's Black Tentacles",
    "Arcane Hand": "Bigby's Hand",
    "Acid Arrow": "Melf's Acid Arrow",
    "Hideous Laughter": "Tasha's Hideous Laughter",
    "Faithful Hound": "Mordenkainen's Faithful Hound",
    "Tiny Hut": "Leomund's Tiny Hut",
    "Private Sanctum": "Mordenkainen's Private Sanctum",
    "Arcanist's Magic Aura": "Nystul's Magic Aura",
    "Telepathic Bond": "Rary's Telepathic Bond",
    "Resilient Sphere": "Otiluke's Resilient Sphere",
    "Magnificent Mansion": "Mordenkainen's Magnificent Mansion",
    "Magic Aura": "Arcanist's Magic Aura"
}

names_map = names_map | names_map.items()

odnd2_exclusive = [
    x for x in odnd2_names if x not in srd_names and x not in names_map]
srd_exclusive = [
    x for x in srd_names if x not in odnd2_names and x not in names_map]

odnd2 = {x["name"]: x for x in odnd2}
srd = {x["name"]: x for x in srd}


def merge_sources():
    """
    Method to selectively merge content from srd and odnd2
    """
    ret = []
    for name in odnd2:
        if name in srd and name in odnd2:
            srd_spell_info = srd[name]
            odnd2_spell_info = odnd2[name]
            ret.append(odnd2_spell_info | srd_spell_info)
        elif name in srd and name in names_map:
            ret.append(odnd2[names_map[name]] | srd[name])
        elif name in odnd2 and name in names_map:
            ret.append(odnd2[name] | srd[names_map[name]])
        else:
            ret.append(odnd2[name])
    return ret


r = merge_sources()
open("sources/parsed/odnd2_srd.json", "w+",
     encoding="utf-8").write(json.dumps(r, indent=4))
