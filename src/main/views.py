from django.views.generic import ListView, RedirectView

from .models import ItemMenu


class AutoLeng(RedirectView):
    pass


class Index(ListView):
    queryset = ItemMenu.objects.all()

    def get_context_data(self, **kwargs):
        kwargs['lang_name'] = self.kwargs.get('pk', 'ru')
        return super().get_context_data(**kwargs)
