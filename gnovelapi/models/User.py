from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=400)
    uid = models.CharField(max_length=50)
    comics = models.ManyToManyField("Comic", through="User_Comic")
