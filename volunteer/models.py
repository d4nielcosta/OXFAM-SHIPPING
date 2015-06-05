from django.db import models

# Create your models here.

class Text(models.Model):
    id = models.IntegerField(primary_key=True, default=1)  # Variable for flexibility in future updates
    mission = models.TextField()
    description = models.TextField()
    donate = models.TextField()
    getinvolved = models.TextField()