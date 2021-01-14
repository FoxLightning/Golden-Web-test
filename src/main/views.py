from django.views.generic import ListView, RedirectView

from .models import ItemMenu, ItemName

from .choices import LENG_CHOICE


class AutoLeng(RedirectView):
    pass

# def tree_from_query_list(query_list:list):
#     '''
#     --prototype--
#     algorithm complexity: O(n**2)
#     TODO try use radix sort expected complexity O(n) bad mamory optimisation
#     TODO or try fast sort O(n*log(n)) and better memory optimisation
#     TODO maybe list is better option for tree
#     '''
#     query_list = query_list[:]
#     tree = {}
#     add_id = set()
#     # first step
#     for element in query_list:
#         if element.item_menu_id.parent is None:
#             tree.add(
#                     {
#                     element.item_menu_id: { 
#                         'name': {
#                             "ru": 
#                             "en":
#                         } 
#                     }
#                 }
#             )
#     return 


def hesh_from_query_list(query_list_list:list):
    hesh = {}
    for element in query_list_list:
        item_id = element.item_menu_id_id
        leng_name = element.item_menu_id.get_leng_name[:]
        link_data = element.item_menu_id.link_data
        parent = element.item_menu_id.parent_id
    
        if item_id in hesh:
            hesh[item_id]['name'][leng_name] = 'asdf'
        else:
            hesh[parent] = {
                'name': {
                    leng_name: element.name,
                },
                'link': link_data,
                'parent': parent
            }
    return hesh

# def tree_from_model():
#     queryset = ItemName.objects.select_related('item_menu_id').all()
#     queryset = list(queryset)
#     tree = tree_from_query_list(queryset)
#     breakpoint()
#     return tree


class Index(ListView):
    queryset = ItemMenu.objects.all()

    def get_context_data(self, **kwargs):
        kwargs['lang_name'] = self.kwargs.get('pk', 'ru')
        kwargs['tree'] = hesh_from_query_list(list(ItemName.objects.select_related('item_menu_id').all()))
        # breakpoint()
        return super().get_context_data(**kwargs)
