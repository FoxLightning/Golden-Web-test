from django.views.generic import ListView

from . import choices
from .models import ItemName
from .utils import choice_to_int, choice_to_str, hesh_from_queryset


class Index(ListView):
    queryset = ItemName.objects.select_related('item_menu_id').all()

    def get_context_data(self, **kwargs):
        """
        1. Define lenguage
        2. Push lenguage dependence content into context
        3. Create hesh(dict) with defined lenguage
        """
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
        kwargs['queryset'] = self.queryset.filter(leng=leng_id)

        return super().get_context_data(**kwargs)
