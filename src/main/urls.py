from django.urls import path
from django.views.generic import RedirectView

from .views import Index


urlpatterns = [
    path('',  RedirectView.as_view(url='/ru'), name='auto-leng'),
    path('<pk>',  Index.as_view(), name='index'),
]
