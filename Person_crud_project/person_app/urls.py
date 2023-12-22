from django.urls import path
from .views import create_person, show_person, retrive_person, update_person, delete_person

urlpatterns = [
    path('create-person/', create_person),
    path('show-person/', show_person ),
    path('retrive-person/<int:pk>/', retrive_person),
    path('update-person/<int:pk>/', update_person),
    path('delete-person/<int:pk>/', delete_person),
]