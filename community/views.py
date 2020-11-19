from django.shortcuts import get_object_or_404
from .models import Comment, Review
from .serializers import CommentListSerializer, CommentSerializer, ReviewSerializer, ReviewListSerializer
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


@api_view(['GET','POST'])
def create_read_comment(request, review_pk):
  if request.method == 'POST':
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(review=review, user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, review_pk, comment_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)
  if request.method == 'GET':
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
  else:
    comment.delete()
    return Response({'message': f'{comment_pk}번 댓글이 정상적으로 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)