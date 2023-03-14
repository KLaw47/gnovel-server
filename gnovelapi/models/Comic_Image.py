from django.db import models
from .Comic import Comic
from .User import User

class Comic_Image(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.DO_NOTHING, related_name='pictures')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(
      upload_to='images', height_field=None,
      width_field=None, max_length=None, null=True)
