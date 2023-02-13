from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gnovelapi.models import Comic, Review, User

class ReviewView(ViewSet):

    def retrieve(self, request, pk):

        try:
            review = Review.objects.get(pk=pk)

            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        reviews = Review.objects.all()
        review_comic = request.query_params.get('comic', None)
        if review_comic is not None:
            reviews.filter(comic=review_comic)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def create(self, request):

        comic = Comic.objects.get(pk=request.data['comic'])
        user = User.objects.get(pk=request.data['user'])

        review = Review.objects.create(
            rating=request.data["rating"],
            text=request.data["text"],
            user=user,
            comic=comic,
        )
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=request.data["user"])
        comic = Comic.objects.get(pk=request.data["comic"])

        review = Review.objects.get(pk=pk)
        review.rating=request.data["rating"]
        review.text=request.data["text"]
        user=user
        comic=comic
        review.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'rating', 'text', 'user', 'comic')
        depth = 1
