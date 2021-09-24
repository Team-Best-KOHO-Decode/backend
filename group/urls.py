from django.urls import path

from . import views

urlpatterns= [
        path('', views.index, name='index'),
        path('create', views.add_group),
        path('<str:group_name>', views.get_group_name)
]
