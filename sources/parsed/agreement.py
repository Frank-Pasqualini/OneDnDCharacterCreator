import json
from textwrap import indent
from tkinter.font import names
odnd2 = json.loads(open('sources/parsed/odnd2.json').read())
srd = json.loads(open('sources/parsed/srd.json').read())

odnd2_names = {x['name'] for x in odnd2}
srd_names = {x['name'] for x in srd}


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

names_map = names_map | {names_map[x]: x for x in names_map}

odnd2_exclusive = [
    x for x in odnd2_names if x not in srd_names and x not in names_map]
srd_exclusive = [
    x for x in srd_names if x not in odnd2_names and x not in names_map]
#print('odnd_2 not in srd:')
# print(sorted(odnd2_exclusive))
#print('srd not in odnd_2')
# print(sorted(srd_exclusive))
#print('len odnd2_exclusive')
# print(len(odnd2_exclusive))
#print('len srd')
# print(len(srd_exclusive))
#raise Exception('odnd and source do not agree on names')

odnd2 = {x['name']: x for x in odnd2}
srd = {x['name']: x for x in srd}


def merge():
    ret = []
    for name in odnd2:
        if name in srd and name in odnd2:
            srd_spell_info = srd[name]
            odnd2_spell_info = odnd2[name]
            shared_fields = ['name', 'school', 'level']
            if any(odnd2_spell_info[x] != srd_spell_info[x] for x in shared_fields):
                # Default to odnd2, that's why it's 2nd
                new_spell_info = srd_spell_info | odnd2_spell_info
                # TODO: Fix
                ret.append(odnd2_spell_info | srd_spell_info)
            else:
                ret.append(odnd2_spell_info | srd_spell_info)
        elif name in srd and name in names_map:
            ret.append(odnd2[names_map[name]] | srd[name])
        elif name in odnd2 and name in names_map:
            ret.append(odnd2[name] | srd[names_map[name]])
        else:
            ret.append(odnd2[name])
    return ret


r = merge()
open('sources/parsed/odnd2_srd.json', 'w+').write(json.dumps(r, indent=4))
