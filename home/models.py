from django.db import models

# Create your models here.
class Home(models.Model):
    room = models.CharField(max_length=30)

    def __str__(self):
        return self.room
