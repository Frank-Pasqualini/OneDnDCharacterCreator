"""
Code to generate the class definitions from the json files
"""
import json

spell_info = json.loads(
    open('sources/parsed/odnd2_srd.json', 'r', encoding='utf-8').read())


SPELL_TEMPLATE = """
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
                         material_components_list={material_components_list},{duration}
                         description={description},
                         at_higher_levels={at_higher_levels})
"""


def concentration(conc: bool) -> str:
    """
    format concentration string
    """
    if conc:
        return '\n                         concentration=True,'
    else:
        return ''


def ritual(rit: bool) -> str:
    """
    format ritual string 
    """
    if rit:
        return '\n                         ritual=True,'
    else:
        return ''


def class_name(name: str) -> str:
    """
    format class name string
    """
    name = name.replace('/', ' ')
    for x in "/\\'":
        name = name.replace(x, '')
    name = name.title()
    name = name.replace(' ', '')
    return name


def spell_list(spell_lists: list[str]) -> str:
    """
    format spell list text
    """
    spell_lists = ['SpellLists.' + x.upper() for x in spell_lists]
    return '[' + ', '.join(spell_lists) + ']'


def material_components_list(text: str):
    """
    format material components string
    """
    if text == '':
        return None
    else:
        return '"' + text + '"'


def duration(text: str) -> str:
    """
    format duration string
    """
    fmt = '\n                         duration="{duration}",'
    if 'Concentration, up to ' in text:
        return fmt.format(duration=text.replace('Concentration, up to ', '').strip())
    elif text == 'Instantaneous':
        return ''
    else:
        return fmt.format(duration=text)


def line_limit(text: str, limit: int, offset: int) -> str:
    """
    format strings with newlines < limit
    """
    indices = [i for i, x in enumerate(text) if x == '\n']
    text = list(text)
    padding = ' ' * offset
    # remove formatting newlines
    for index in reversed(indices):
        if text[index-1] != '.':
            text[index] = ' '

    text = ''.join(x for x in text if x != '')
    if len(text) < limit:
        if text == '':
            return '""'
        else:
            return text
    wraps = []
    cur = ''
    text = text.split(' ')
    for i, word in enumerate(text):
        if len(cur) + len(word) - 3 < limit:
            # can add to cur
            if '\n' in word:
                first, second = word.split('\n')
                cur += first + '\n'
                if len(wraps) != 0:
                    cur = padding + '"' + cur + '"'
                wraps.append(cur)
                cur = second + ''
            else:
                cur += word + ' '
        else:
            to_append = '"' + cur + '"'

            if len(wraps) != 0:
                to_append = padding + to_append
            wraps.append(to_append)
            cur = word + ' '

        if i == len(text) - 1:
            # print(word)
            wraps.append(padding + '"' + cur + '"')
    wraps = [x.replace('\n', '\\n') for x in wraps]
    wraps = [x.replace('.\\n', '.\\n" +\n' + padding + '"') for x in wraps]
    return ' +\n'.join(wraps)


def generate_spell_code(spell_json) -> str:
    """
    generate and format spell class def using helper functions
    """
    if 'description' not in spell_json:
        return None

    start, end = spell_json['pages']

    if start == end:
        pages = str(start)
    else:
        pages = str(start) + '-' + str(end)
    return SPELL_TEMPLATE.format(class_name=class_name(spell_json['name']),
                                 pages=pages,
                                 concentration=concentration(
                                     'oncentration' in spell_json['duration']),
                                 name=spell_json['name'],
                                 spells_type=spell_list(
                                     spell_json['spell_list']),
                                 ritual=ritual(spell_json['is_ritual']),
                                 level=spell_json['level'],
                                 school=spell_json['school'].upper(),
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


res = [generate_spell_code(x)
       for x in sorted(spell_info, key=lambda x: x['name'])]

open('sources/parsed/generated_spells.py', 'w+',
     encoding='utf-8').write('\n'.join([x for x in res if x is not None]))
