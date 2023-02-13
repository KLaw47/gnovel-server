from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gnovelapi.models import Comic, User, User_Comic

class UserComicView(ViewSet):

    def list(self, request):

        user_comics = User_Comic.objects.all()
        comic_user = request.query_params.get('user', None)
        if comic_user is not None:
            user_comics.filter(user=comic_user)
        serializer = UserComicSerializer(user_comics, many=True)
        return Response(serializer.data)

    def create(self, request):

        comic = Comic.objects.get(pk=request.data['comic_id'])
        user = User.objects.get(pk=request.data['user_id'])

        user_comic = User_Comic.objects.create(
            comic=comic,
            user=user
        )
        serializer = UserComicSerializer(user_comic)
        return Response(serializer.data)

    def destroy(self, request, pk):
        user_comic = User_Comic.objects.get(pk=pk)
        user_comic.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserComicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Comic
        fields = ('id', 'comic', 'user')
        depth = 1
