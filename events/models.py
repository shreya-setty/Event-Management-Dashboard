from mongoengine import Document, StringField, DateTimeField, ListField, ReferenceField
from django.db import models

class Event(Document):
    name = StringField(required=True, max_length=100)
    description = StringField()
    location = StringField()
    date = DateTimeField()
    attendees = ListField(ReferenceField('Attendee'))

# Django proxy model for admin
class EventProxy(models.Model):
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'