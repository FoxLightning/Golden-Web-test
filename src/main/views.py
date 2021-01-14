from django.views.generic import ListView, RedirectView

from .models import ItemMenu, ItemName

from . import choices

from .utils import choice_to_str, choice_to_int


class AutoLeng(RedirectView):
    pass


def hesh_from_queryset(queryset, leng: str) -> dict:
    hesh = {}
    for element in queryset:
        # group elements by perents
        '''
        target: make fast structured dict from queryset
        complexity: O(n)
        '''
        # 1. element data
        leng_name = element.get_leng_name[:]
        if leng_name != leng:
            continue
        item_id = element.item_menu_id_id
        link_data = element.item_menu_id.link_data
        name = element.name
        parent = element.item_menu_id.parent_id

        # 2 create hesh
        # 2.1 find place to insert element
        # 2.1.1 insert only name in existing item
        if parent in hesh and item_id in hesh[parent]:
            hesh[parent][item_id]['name'][leng_name] = name
        # 2.1.2 insert fool element
        else:
            # 2.1.2.1 create dict of items with same parent if not exist
            if parent not in hesh:
                hesh[parent] = {}
            # 2.1.2.1 insert element data in dict
            hesh[parent][item_id] = {
                'link': link_data,
                'name': {
                    leng_name: name
                },
                'childs': {}
            }
    return hesh


class Index(ListView):
    queryset = ItemName.objects.select_related('item_menu_id').all()

    def get_context_data(self, **kwargs):
        # define lenguage
        leng_name = self.kwargs.get('pk', 'ru')
        leng_id = choice_to_int(leng_name, choices.LENG_CHOICE)
        # generate context current lenguage
        kwargs['lang_name'] = leng_name
        context_names = [
            'title', 'menu'
        ]
        kwargs['title'] = choice_to_str(leng_id, choices.TITLE)
        kwargs['menu'] = choice_to_str(leng_id, choices.TITLE)
        # create hesh
        kwargs['hesh'] = hesh_from_queryset(self.queryset, leng_name)
        # breakpoint()
        return super().get_context_data(**kwargs)
