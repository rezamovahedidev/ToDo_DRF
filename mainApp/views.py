from rest_framework import generics
from .serializers import *
from .models import *

 #CRUD Operations

class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializers_class = ToDoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset =  ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer