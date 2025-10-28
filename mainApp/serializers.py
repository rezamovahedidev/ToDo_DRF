from rest_framework import serializers
from models import *

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

    # def validate_title(self, value):
    #     if ToDo.objects.filter(title=value).exists():
    #         raise serializers.ValidationError("A ToDo with this title already exists.")
    #     return value