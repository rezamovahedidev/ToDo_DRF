from django.urls import path
from .views import *
from rest_framework import routers

app_name='todo_drf'
urlpatterns = [
    path('todos/', ListTodo.as_view(), name='todo-list'),
    path('todos/<int:pk>/', DetailTodo.as_view(), name='todo-detail'),
    path('todos/create/', CreateTodo.as_view(), name='todo-create'),
    path('todos/<int:pk>/delete/', DeleteTodo.as_view(), name='todo-delete'),
]


