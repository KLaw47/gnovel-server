from django.db import models

class User_Comic(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    comic = models.ForeignKey("Comic", on_delete=models.CASCADE, related_name="joined_comics")
