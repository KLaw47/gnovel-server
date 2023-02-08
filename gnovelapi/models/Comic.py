from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    thumbnail = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    
