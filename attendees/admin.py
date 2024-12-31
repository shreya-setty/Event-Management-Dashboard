from django.contrib import admin
from .models import Attendee, AttendeeProxy

@admin.register(AttendeeProxy)
class AttendeeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Attendee.objects.all()