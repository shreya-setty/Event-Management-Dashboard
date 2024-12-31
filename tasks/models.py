from mongoengine import Document, StringField, DateTimeField, ReferenceField
from django.db import models

class Task(Document):
    name = StringField(required=True, max_length=100)
    deadline = DateTimeField()
    status = StringField(choices=['Pending', 'Completed'])
    assigned_to = ReferenceField('Attendee')

class TaskProxy(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
