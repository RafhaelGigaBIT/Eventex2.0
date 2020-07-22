from django.urls import path

from . import views

urlpatterns= [
    path('',  views.index, name='index'),
    path('event/<str:pk>', views.event, name='event'),
    path('activity/<str:pk>', views.actEvent, name='act'),
]