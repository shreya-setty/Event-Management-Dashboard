from django.contrib import admin
from .models import Event, EventProxy

@admin.register(EventProxy)
class EventAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Event.objects.all()