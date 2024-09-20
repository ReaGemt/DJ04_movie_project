from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.film_create, name='film_create'),
    path('delete/<int:pk>/', views.film_delete, name='film_delete'),  # Новый путь для удаления
    path('', views.film_list, name='film_list'),
]
