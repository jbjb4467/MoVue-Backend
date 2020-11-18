from .models import Review
from .serializers import ReviewSerializer, ReviewListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def review_list_create(request):
  if request.method == 'GET':
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
  
  else:
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)