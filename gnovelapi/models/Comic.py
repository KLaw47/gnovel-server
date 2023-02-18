from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=500, null=True)
    thumbnail = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)

