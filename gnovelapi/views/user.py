from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gnovelapi.models import User, Comic, User_Comic

class UserView(ViewSet):

    def retrieve(self, request, pk):
        user = User.objects.get(pk=pk)
        comics = Comic.objects.filter(joined_comics__user_id=user)
        user.comics.set(comics)
        serializer = UserSerializer(user, context={'user': user})
        return Response(serializer.data)

    def list(self, request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class UserComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Comic
        fields = ('id',)
class ComicSerializer(serializers.ModelSerializer):

    joined_comics = serializers.SerializerMethodField()

    class Meta:
        model = Comic
        fields = ('id', 'title', 'description', 'thumbnail', 'joined_comics')

    def get_joined_comics(self, obj):
        user = self.context.get('user')
        user_comics = obj.joined_comics.filter(user=user)
        serializer = UserComicSerializer(user_comics, many=True)
        return serializer.data

class UserSerializer(serializers.ModelSerializer):
    comics=ComicSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'image_url', 'uid', 'comics')
        depth = 2
