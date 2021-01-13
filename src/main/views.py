from django.views.generic import ListView

from .models import ItemMenu


class Index(ListView):
    queryset = ItemMenu.objects.all()
