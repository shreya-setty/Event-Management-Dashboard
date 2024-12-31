from mongoengine import Document, StringField, ListField, ReferenceField
from django.db import models

class Attendee(Document):
    name = StringField(required=True, max_length=100)
    tasks = ListField(ReferenceField('Task'))

class AttendeeProxy(models.Model):
    class Meta:
        verbose_name = 'Attendee'
        verbose_name_plural = 'Attendees'