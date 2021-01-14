from .choices import LENG_CHOICE


def leng_name(input_id: int) -> str:
    leng_name = ''
    for leng_id, leng_neme_choice in LENG_CHOICE:
        if leng_id == input_id:
            leng_name = leng_neme_choice
            break
    return leng_name
