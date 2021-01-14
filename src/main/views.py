from django.views.generic import ListView, RedirectView

from .models import ItemMenu, ItemName

from .choices import LENG_CHOICE


class AutoLeng(RedirectView):
    pass


def hesh_from_query_list(query_list_list: list):
    hesh = {}
    for element in query_list_list:

        # 1. element data
        item_id = element.item_menu_id_id
        leng_name = element.get_leng_name[:]
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
                }
            }

    return hesh


# def tree_from_hesh(hesh):
#     current_node = None

#     while True:


#     return tree


class Index(ListView):
    queryset = ItemMenu.objects.all()

    def get_context_data(self, **kwargs):
        kwargs['lang_name'] = self.kwargs.get('pk', 'ru')
        kwargs['tree'] = hesh_from_query_list(list(ItemName.objects.select_related('item_menu_id').all()))
        kwargs['len'] = len(kwargs['tree'])
        # breakpoint()
        return super().get_context_data(**kwargs)
