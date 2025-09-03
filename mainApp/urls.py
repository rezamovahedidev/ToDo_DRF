from django.urls import path
from .views import ListTodo, DetailTodo, CreateTodo, DeleteTodo

urlpatterns = [
    path('todos/', ListTodo.as_view(), name='todo-list'),
    path('todos/<int:pk>/', DetailTodo.as_view(), name='todo-detail'),
    path('todos/create/', CreateTodo.as_view(), name='todo-create'),
    path('todos/<int:pk>/delete/', DeleteTodo.as_view(), name='todo-delete'),
]
]

