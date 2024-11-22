from django.urls import path
from . import views

urlpatterns = [
    path('add_event/', views.add, name='add_event'),
    path('', views.events, name='event'),
    path('delete_event/<id>/', views.delete_event, name='delete_event'),
    path('update_event/<id>/', views.update_event, name='update_event'),
    path('participants/', views.participants, name='participants'),
    path('add_participant/', views.add_participant, name='add_participant'),
    path('update_participant/<id>/', views.update_participant, name='update_participant'),
    path('delete_participant/<id>/', views.delete_participant, name='delete_participant'),
]