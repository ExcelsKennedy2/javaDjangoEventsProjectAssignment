from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    start_time = models.DateField()
    end_time = models.DateField()
    organizer = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name