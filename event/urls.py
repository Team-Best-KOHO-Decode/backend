from django.urls import path

from . import views

urlpatterns= [
        path('create', views.create_event),
        path('<int:event_id>', views.get_event_by_id),
        path('updateBudget', views.update_event_budget),
]

