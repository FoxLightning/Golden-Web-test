def choice_to_str(input_id: int, choices) -> str:
    string = ''
    for choice_id, str_choice in choices:
        if choice_id == input_id:
            string = str_choice
            break
    return string


def choice_to_int(input_str: str, choices) -> int:
    integer = 0
    for choice_id, str_choice in choices:
        if str_choice == input_str:
            integer = choice_id
            break
    return integer


def hesh_from_queryset(queryset, leng: str) -> dict:
    '''
    target: make fast structured dict from queryset
    method: group element by parent
    result: create hesh complexity = O(n)
            create template from hesh complexity = O(n)
    '''
    hesh = {}
    for element in queryset:
        # element data
        leng_name = element.get_leng_name[:]
        if leng_name != leng:
            continue
        item_id = element.item_menu_id_id
        link_data = element.item_menu_id.link_data
        link_data = link_data if link_data else ''
        name = element.name
        parent = element.item_menu_id.parent_id
        parent = parent if parent else 0

        # add item to hesh
        if parent not in hesh:
            hesh[parent] = []
        hesh[parent].append((item_id, name, link_data))

    return hesh
