import uuid
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gnovelapi.models import Comic_Image
from gnovelapi.models import Comic
from gnovelapi.models import User
from django.core.files.base import ContentFile
import base64

class ImageView(ViewSet):

  def list(self, request):
    image = Comic_Image.objects.all()
    comic = request.query_params.get('comic_id', None)
    user = request.query_params.get('user_id', None)

    if comic is not None and user is not None:
        image = Comic_Image.objects.filter(comic=comic, user=user)
    elif comic is not None:
        image = Comic_Image.objects.filter(comic=comic)
    elif user is not None:
        image = Comic_Image.objects.filter(user=user)

    serializer = ImageSerializer(image, many=True)
    return Response(serializer.data)


  def create(self, request):
    user = User.objects.get(pk=request.data['user_id'])
    comic = Comic.objects.get(pk=request.data["comic_id"])
    format, imgstr = request.data["image"].split(';base64,')
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["comic_id"]}-{uuid.uuid4()}.{ext}')
    pic = Comic_Image.objects.create(
      comic=comic,
      user=user,
      image=data
    )
    pic.save()
    serializer = ImageSerializer(pic)
    return Response(serializer.data)

class ImageSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comic_Image
    fields = ('id', 'comic', 'user', 'image')
    depth = 1
