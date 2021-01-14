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
