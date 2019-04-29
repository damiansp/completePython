# inefficent:
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x = 1)


def indented_list_sort(indented_list, indent=' '):
    KEY, ITEM, CHILDREN = range(3)

    def add_entry(key, item, children):
        #if level == 0:
        #    children.append((key, item, []))
        #else:
        #    add_entry(level - 1, key, item, children[-1][CHILDREN])
        nonlocal level
        if level == 0:
            children.append((key, item, []))
        else:
            level -= 1
            add_entry(key, item, children[-1][CHILDREN])

    def update_indented_list(entry):
        indented_list.append(entry[ITEM])
        for subentry in sorted(entry[CHILDREN]):
            update_indented_list(subentry)

    entries = []
    for item in indented_list:
        level = 0
        i = 0
        while item.startswith(indent, i):
            i += len(indent)
            level += 1
        key = item.strip().lower()
        add_entry(key, item, entries)
    indented_list = []
    for entry in sorted(entries):
        update_indented_list(entry)
    return indented_list


elements = ['Nonmetals',
            '    H',
            '    C',
            '    N',
            '    O',
            'Inner Transitionals',
            '    Lanthanides',
            '        Ce',
            '        Eu',
            '    Actinides',
            '        U',
            '        Cm',
            '        Pl',
            'Alkali Metals',
            '    Li',
            '    Na',
            '    K']
elem_sorted = indented_list_sort(elements, indent='    ')
for e in elem_sorted:
    print(e)
