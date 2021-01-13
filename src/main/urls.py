from django.urls import path

from .views import AutoLeng, Index


urlpatterns = [
    path('/',  AutoLeng.as_view(), name='auto-leng'),
    path('index/<pk>',  Index.as_view(), name='index'),
]
