from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description', 'date', 'completed')
        read_only_fields = ('id', 'date')

    def validate_title(self, value):
        if ToDo.objects.filter(title=value).exists():
            raise serializers.ValidationError("A ToDo with this title already exists.")
        return value