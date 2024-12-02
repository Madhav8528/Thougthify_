from django.urls import path
from . import views

urlpatterns = [
    path('', views.thought_list, name = 'thought_list'),
    path('create/', views.create_thought, name = 'create_thought'),
    path('<int:thought_id>/edit/', views.edit_thought, name = 'edit_thought'),
    path('<int:thought_id>/delete/', views.thought_delete, name = 'thought_delete'),
    path('register/', views.register, name = 'register'),
]