from django.urls import path

from . import views

urlpatterns= [
        path('', views.get_events),
        path('<int:budget>', views.get_events_by_budget)
]

