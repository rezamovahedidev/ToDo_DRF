from rest_framework import generics
from .serializers import *
from .models import ToDo
from rest_framework.exceptions import ValidationError

 #CRUD Operations

class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_queryset(self):
        # Custom logic before listing
        queryset = super().get_queryset()
        # Example: filter by a query param
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title=title)
        return queryset

class DetailTodo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_object(self):
        # Custom logic before retrieving
        obj = super().get_object()
        # Example: check permissions or log access
        # log_access(obj)
        return obj

class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if ToDo.objects.filter(title=title).exists():
            raise ValidationError("A ToDo with this title already exists.")
        instance = serializer.save()
        # Custom post-save logic (e.g., send notification)
        # send_notification(instance)

class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def perform_destroy(self, instance):
        # Custom logic before deletion
        # Example: check if ToDo can be deleted
        # if not instance.can_be_deleted():
        #     raise ValidationError("This ToDo cannot be deleted.")
        instance.delete()
        # Custom post-delete logic (e.g., log deletion)
        # log_deletion(instance)
