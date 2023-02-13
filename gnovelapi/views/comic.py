
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gnovelapi.models import Comic

class ComicView(ViewSet):

    def retrieve(self, request, pk):

        try:
            comic = Comic.objects.get(pk=pk)

            serializer = ComicSerializer(comic)
            return Response(serializer.data)
        except Comic.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        comics = Comic.objects.all()

        serializer = ComicSerializer(comics, many=True)
        return Response(serializer.data)

class ComicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comic
        fields = ('id', 'title', 'description', 'thumbnail', 'image')
        depth = 2
