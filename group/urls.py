from django.urls import path

from . import views

urlpatterns= [
        path('', views.index, name='index'),
        path('create', views.create_group),
        path('<int:group_id>', views.get_group_by_id),
]
