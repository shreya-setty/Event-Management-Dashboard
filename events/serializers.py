from rest_framework_mongoengine import serializers
from .models import Event
from attendees.serializers import AttendeeSerializer


class EventSerializer(serializers.DocumentSerializer):
    attendees = AttendeeSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
