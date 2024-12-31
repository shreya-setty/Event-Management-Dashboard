from django.contrib import admin
from .models import Task, TaskProxy

@admin.register(TaskProxy)
class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Task.objects.all()