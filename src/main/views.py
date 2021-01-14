from django.views.generic import ListView, RedirectView

from . import choices
from .models import ItemName
from .utils import choice_to_int, choice_to_str


class AutoLeng(RedirectView):
    pass


def hesh_from_queryset(queryset, leng: str) -> dict:
    hesh = {}
    for element in queryset:
        '''
        target: make fast structured dict from queryset
        method: group element by parent
        result: create hesh complexity = O(n)
                create template from hesh complexity = O(n)
        '''
        # element data
        leng_name = element.get_leng_name[:]
        if leng_name != leng:
            continue
        item_id = element.item_menu_id_id
        link_data = element.item_menu_id.link_data
        name = element.name
        parent = element.item_menu_id.parent_id
        parent = parent if parent else 0

        # add item to hesh
        if parent not in hesh:
            hesh[parent] = []
        hesh[parent].append((item_id, name, link_data))

    return hesh


class Index(ListView):
    queryset = ItemName.objects.select_related('item_menu_id').all()

    def get_context_data(self, **kwargs):
        # define lenguage
        leng_name = self.kwargs.get('pk', 'ru')
        leng_id = choice_to_int(leng_name, choices.LENG_CHOICE)

        # generate context current lenguage
        kwargs['lang_name'] = leng_name

        context_names = ('TITLE', 'MENU', 'LENG_NAMES')
        for name in context_names:
            kwargs[name] = choice_to_str(leng_id, getattr(choices, name))

        kwargs['lengs'] = (
            (choice_to_str(leng_id, choices.LENG_CHOICE), name,)
            for leng_id, name in choices.LENG_NAMES
        )

        kwargs['hesh'] = hesh_from_queryset(self.queryset, leng_name)

        return super().get_context_data(**kwargs)
