from rest_framework_mongoengine import serializers
from .models import Attendee
from tasks.serializers import TaskSerializer


class AttendeeSerializer(serializers.DocumentSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Attendee
        fields = '__all__'