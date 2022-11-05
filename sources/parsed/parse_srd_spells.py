from msilib.schema import Component
from msvcrt import kbhit
import json
import re
import string
from weakref import KeyedRef
txt = open('sources\parsed\srd_spells.txt', encoding='utf-8').read()
txt = txt.replace('\t', ' ').replace('’', "'")
starting_page = 115
# txt = txt.split('\n')
# for x in txt[0:150]:
#    print(x)


lines = txt.split('\n')
line_num = 0

schools = ['Abjuration', 'Transmutation', 'Conjuration', 'Divination',
           'Enchantment', 'Illusion', 'Evocation', 'Necromancy']
levels = ['1st-level',
          '2nd-level', '3rd-level', 'th-level']


def find_next_spell(lines):
    levels = ['1st-level',
              '2nd-level', '3rd-level', 'th-level']

    splits = [x + ' ' + y.lower() for x in levels for y in schools]
    splits += [x + ' cantrip' for x in schools]

    for i, x in enumerate(lines):
        if any(kw in x for kw in splits) and lines[i-1][0].isupper():
            return i + 1
    return -1


def get_level_school(level_type: str) -> tuple[int, str]:
    level = -1
    school = ''
    for x in string.digits:
        if level_type.startswith(x):
            level = int(x)
            break
    if 'Cantrip' in level_type or 'cantrip' in level_type:
        level = 0

    for s in schools:
        if s in level_type or s.lower() in level_type:
            school = s.title()
            break

    if level == -1 or school == '':
        print(level_type)
        raise Exception('get level fail')
    return level, school


def split_into_spell_text(lines: list[str]):
    res = []
    cur = lines
    while (line_num < len(lines)):
        next_spell_index = find_next_spell(cur[2:])
        if next_spell_index <= 0:
            res.append('\n'.join(cur))
            break

        to_append = '\n'.join(cur[:next_spell_index])
        res.append(to_append)
        cur = cur[next_spell_index:]
    return res


def handle_pages(raw_spell_texts):
    res = []
    current_page = 115
    for raw_spell_text in raw_spell_texts:
        split_text = raw_spell_text.split('\n')
        page_nums = [int(x[-3:]) for x in raw_spell_text.split(
            '\n') if 'System Reference' in x]
        clean_text = '\n'.join(
            x for x in split_text if 'System Reference' not in x)
        if len(page_nums) > 0:
            # crosses page
            pages = (current_page, page_nums[0]+1)
            current_page += 1
        else:  # same page
            pages = (current_page, current_page)

        res.append((pages, clean_text))
    return res


def get_valid_range(line: str) -> str:
    if 'Range: ' not in line:
        print(line)
        raise Exception('get range fail' + line)
    return line.replace('Range: ', '').strip()


def get_casting_time(text: str) -> str:
    if 'Casting Time:' not in text:
        print(text)
        raise Exception('Casting time not in text')
    return text.replace('Casting Time:', '').strip()


def get_range(text: str) -> str:
    if 'Range:' not in text:
        print('=====')
        print(text)
        print('=====')
        raise Exception('Range not in text')
    return text.replace('Range:', '').strip()


def get_components(text: str) -> tuple[bool, bool, str]:
    if 'Component' not in text:
        print(text)
        raise Exception('Component not in text')

    vsm, *component_list = text.split('(')
    verbal_components = 'V' in vsm
    somatic_components = 'S' in vsm

    return (verbal_components, somatic_components, ''.join(component_list).replace(')', ''))


def get_duration(text: str) -> str:
    if 'Duration' not in text:
        print(text)
        raise Exception('Duration not in text')
    return text.replace('Duration:', '').strip()


def get_desc_higher_levels(lines: list[str]) -> tuple[str, str]:
    text = ' '.join(lines).replace('  ', ' ').replace(" '", "'")
    description, *higher_levels = text.split('At Higher Levels.')
    return (description.strip(), ''.join(higher_levels).strip())


def merge_markers(text: str, start: str, end: str) -> str:
    lines = text.split('\n')
    start_index = -1
    end_index = -1
    for i, line in enumerate(lines):
        if start in line and start_index == -1:
            start_index = i

        if end in line and end_index == -1:
            end_index = i

    if start_index > -1 and end_index > -1 and end_index > start_index:
        lines[start_index:end_index] = [
            ''.join(lines[start_index:end_index])]
        return '\n'.join(x for x in lines if x != '')
    else:
        print('-----')
        print(lines)
        print((start, end))
        print(start_index, end_index)
        raise Exception('start and end not in text')


def nudge_newlines(text: str) -> str:
    #print(' in nudge newlines ')
    splits = ['Casting Time', 'Range', 'Component', 'Duration']
    my_text = text
    for x in splits:
        if x in my_text:
            my_text = my_text.replace(x, '\n' + x)
    my_text = merge_markers(my_text, 'Casting Time', 'Range')
    my_text = merge_markers(my_text, 'Range', 'Component')
    my_text = merge_markers(my_text, 'Component', 'Duration')
    return my_text


def split_spell_entry(text: str):
    text = text.split('\n')
    name = text[0]
    level, school = get_level_school(text[1])
    casting_time = get_casting_time(text[2])
    spell_range = get_range(text[3])
    verbal_components, somatic_components, material_components_list = get_components(
        text[4])
    duration = get_duration(text[5])
    description, at_higher_levels = get_desc_higher_levels(text[6:])

    ret = {
        'name': name,
        'level': level,
        'school': school,
        'casting_time': casting_time,
        'spell_range': spell_range,
        'verbal_components': verbal_components,
        'somatic_components': somatic_components,
        'material_components_list': material_components_list,
        'duration': duration,
        'description': description,
        'at_higher_levels': at_higher_levels
    }
    return ret


def parse_clean_spell_entries(cleaned: list[tuple]):
    ret = []
    for pages, spell_text in cleaned:
        x = nudge_newlines(spell_text)
        x = split_spell_entry(x)
        ret.append(x)
    return ret


raw_spell_texts = split_into_spell_text(lines)
#print([x for x in raw_spell_texts if 'summoning' in x])
spell_text_with_range = handle_pages(raw_spell_texts)
parsed = parse_clean_spell_entries(spell_text_with_range)
# print(handle_pages(raw_spell_texts)[0])
# print(handle_pages(raw_spell_texts)[-1])


open('sources/parsed/srd.json', 'w+').write(json.dumps(parsed, indent=4))
