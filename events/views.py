from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from django.db import models
from .filters import EventFilter
from .models import Event
from rest_framework import serializers
from attendees.models import Attendee

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EventFilter
    search_fields = ['name', 'description', 'location']
    ordering_fields = ['date', 'name']

    @action(detail=True, methods=['post'])
    def add_attendee(self, request, pk=None):
        event = self.get_object()
        attendee_id = request.data.get('attendee_id')

        try:
            attendee = Attendee.objects.get(id=attendee_id)
            if attendee not in event.attendees:
                event.attendees.append(attendee)
                event.save()
                return Response({'status': 'attendee added'})
            return Response({'status': 'attendee already exists'})
        except Attendee.DoesNotExist:
            return Response({'error': 'attendee not found'}, status=404)
