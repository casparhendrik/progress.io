from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='rooms', default='no_picture.png')
    room = models.CharField(max_length=50)
    progression = models.IntegerField()
    status = models.CharField(max_length=40)
