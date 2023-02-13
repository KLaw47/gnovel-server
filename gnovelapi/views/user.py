from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gnovelapi.models import User, Comic, User_Comic

class UserView(ViewSet):

    def retrieve(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        # try:
        #     user = User.objects.get(pk=pk)
        #     this_user_comics = User_Comic.objects.filter(user=user)
        #     comics = []

        #     for user_comic in this_user_comics:
        #         try:
        #             comics = Comic.objects.get(id=user_comic.comic_id)
        #         except:
        #             pass
        #     serializer = UserSerializer(user)
        #     return Response(serializer.data)
        # except User.DoesNotExist as ex:
        #     return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'image_url', 'uid', 'comics')
        depth = 1
