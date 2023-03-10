
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gnovelapi.models import Comic, Review


class ComicView(ViewSet):

    def retrieve(self, request, pk):
        try:
            comic = Comic.objects.get(pk=pk)
            reviews = Review.objects.filter(comic=comic.id)
            serializer = ComicSerializer(comic)
            data = serializer.data
            data['reviews'] = ReviewSerializer(reviews, many=True).data
            return Response(data)
        except Comic.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        comics = Comic.objects.all()
        serializer = ComicSerializer(comics, many=True)
        return Response(serializer.data)
class ComicSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Comic
        fields = ('id', 'title', 'description', 'thumbnail', 'average_rating')
        depth = 1

    def get_average_rating(self, comic):
        reviews = Review.objects.filter(comic=comic)
        if reviews:
            ratings = [review.rating for review in reviews]
            return sum(ratings) / len(ratings)
        else:
            return 0


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'rating', 'text', 'user', 'comic')
        depth = 1
