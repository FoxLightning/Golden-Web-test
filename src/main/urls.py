from django.urls import path
from .views import Index
from django.views.generic import TemplateView

urlpatterns = [
    path('',  Index.as_view())
]