from rest_framework_mongoengine import viewsets
from .models import Attendee
from .serializers import AttendeeSerializer
from events.models import Event


class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

    def perform_create(self, serializer):
        attendee = serializer.save()
        event_id = self.request.data.get('event_id')
        if event_id:
            try:
                event = Event.objects.get(id=event_id)
                event.attendees.append(attendee)
                event.save()
            except Event.DoesNotExist:
                pass