from django.urls import path
from .views import DetailTodo, ListTodo, CreateTodo, DeleteTodo


urlpatterns = [
	path('<int:pk>/', DetailTodo.as_view()),
	path('api/', ListTodo.as_view()),
	path('create/', CreateTodo.as_view()),
	path('delete/<int:pk>/', DeleteTodo.as_view()),
]

