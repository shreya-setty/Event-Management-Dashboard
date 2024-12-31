from rest_framework_mongoengine import viewsets
from .models import Task
from .serializers import TaskSerializer
from attendees.models import Attendee


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        attendee_id = self.request.data.get('attendee_id')
        if attendee_id:
            try:
                attendee = Attendee.objects.get(id=attendee_id)
                attendee.tasks.append(task)
                attendee.save()
            except Attendee.DoesNotExist:
                pass