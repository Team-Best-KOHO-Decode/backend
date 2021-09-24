from django.urls import path

from . import views

urlpatterns= [
        path('<int:group_id>', views.get_events)
]

