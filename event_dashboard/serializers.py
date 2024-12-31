from rest_framework import serializers
from .models import Event, Attendee, Task

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event  # The model this serializer is for
        fields = '__all__'  # You can list specific fields here, or use '__all__' to include all model fields

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee  # The model this serializer is for
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # The model this serializer is for
        fields = '__all__'
