from django.shortcuts import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer, ReviewListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
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


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
def review_detail_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if request.method == 'GET':
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    review.delete()
    return Response({'message': f'{review_pk}번 글이 정상적으로 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)