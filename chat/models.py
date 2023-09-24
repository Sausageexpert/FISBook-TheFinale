from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Room(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural='Rooms'
        
class Message(models.Model):
    room = models.CharField(max_length=200) # can also use a relationship but don't really need to
    value = models.CharField(max_length=1000)
    user = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)