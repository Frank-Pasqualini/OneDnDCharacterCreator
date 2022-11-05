import json

spell_info = json.loads(open('sources/parsed/odnd2_srd.json').read())

spell_fields = [
    'name',
    'spell_lists',
    'level',
    'school',
    'spell_range',
    'description',
    'ritual',
    'casting_time',
    'verbal_components',
    'somatic_components',
    'material_components_list',
    'concentration',
    'duration',
    'at_higher_levels'
]

spell_template = """
class {class_name}(spells.Spell):
    \"""
    {name} Spell
    SRD p. {pages}
    Generated
    \"""

    def __init__(self):
        super().__init__(name="{name}",
                         spell_lists={spells_type},{concentration}{ritual}
                         level={level},
                         school=SpellSchools.{school},
                         spell_range="{range}",
                         verbal_components={verbal_components},
                         somatic_components={somatic_components},
                         material_components_list={material_components_list},
                         duration="{duration}",
                         description={description},
                         at_higher_levels={at_higher_levels})
"""


def concentration(conc: bool) -> str:
    if conc:
        return '\n                         concentration=True,'
    else:
        return ''


def ritual(rit: bool) -> str:
    if rit:
        return '\n                         ritual=True,'
    else:
        return ''


def class_name(name: str) -> str:
    name = name.replace('/', ' ')
    for x in "/\\'":
        name = name.replace(x, '')
    name = name.title()
    name = name.replace(' ', '')
    return name


def spell_list(s: list[str]) -> str:
    s = ['SpellLists.' + x.upper() for x in s]
    return '[' + ', '.join(s) + "]"


def material_components_list(text: str):
    if text == '':
        return None
    else:
        return '"' + text + '"'


def duration(text: str) -> str:
    if 'Concentration, up to ' in text:
        return text.replace('Concentration, up to ', '').strip()
    else:
        return text


def line_limit(text: str, limit: int, offset: int) -> str:
    if len(text) < limit:
        if text == '':
            return '""'
        else:
            return text
    wraps = []
    cur = ''
    text = text.split(' ')
    print(text)
    for i, word in enumerate(text):
        if len(cur) + len(word) - 3 < limit:
            # can add to cur
            cur += word + ' '
        else:
            to_append = '"' + cur + '"'

            if len(wraps) != 0:
                to_append = ' ' * offset + to_append
            wraps.append(to_append)
            cur = word + ' '

        if i == len(text) - 1:
            # print(word)
            wraps.append(' ' * offset + '"' + cur + '"')
    return ' +\n'.join(wraps)


def generate_spell(spell_json) -> str:
    if 'description' not in spell_json:
        return None

    start, end = spell_json['pages']

    if start == end:
        pages = str(start)
    else:
        pages = str(start) + '-' + str(end)
    return spell_template.format(class_name=class_name(spell_json['name']),
                                 pages=pages,
                                 concentration=concentration(
                                     'oncentration' in spell_json['duration']),
                                 name=spell_json['name'],
                                 spells_type=spell_list(
                                     spell_json['spell_list']),
                                 ritual=ritual(spell_json['is_ritual']),
                                 level=spell_json['level'],
                                 school=spell_json['school'],
                                 range=spell_json['spell_range'],
                                 verbal_components=spell_json['verbal_components'],
                                 somatic_components=spell_json['somatic_components'],
                                 material_components_list=material_components_list(
                                     spell_json['material_components_list']),
                                 duration=duration(spell_json['duration']),
                                 description=line_limit(
                                     spell_json['description'], 60, 36),
                                 at_higher_levels=line_limit(
                                     spell_json['at_higher_levels'], 60, 42)
                                 )


res = [generate_spell(x) for x in sorted(spell_info, key=lambda x: x['name'])]

open('sources/parsed/generated_spells.py', 'w+',
     encoding='utf-8').write('\n'.join([x for x in res if x != None]))
