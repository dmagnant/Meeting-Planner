from datetime import time
from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    floorNumber = models.IntegerField(default=1)
    roomNumber = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.name}, room # {self.roomNumber}, on floor # {self.floorNumber}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    startTime = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} at {self.startTime} on {self.date}"