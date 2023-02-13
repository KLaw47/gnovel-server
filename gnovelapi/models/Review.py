from django.db import models


class Review(models.Model):
    rating = models.IntegerField()
    text = models.CharField(max_length=500)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comic = models.ForeignKey('Comic', on_delete=models.CASCADE)
