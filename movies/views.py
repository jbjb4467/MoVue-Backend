import operator

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Movie, Review, Genre
from .serializers import MovieDetailSerializer, MovieListSerializer, ReviewSerializer, ReviewListSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
 

@api_view(['GET'])
def movie_list(request):
  movies = Movie.objects.all()[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
  movie = Movie.objects.get(pk=movie_id)
  serializer = MovieDetailSerializer(movie)
  return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  user = request.user
  print(user)
  if movie.like_user.filter(pk=user.pk).exists():
    movie.like_user.remove(user.pk)
    liked = False
  else:
    movie.like_user.add(user.pk)
    liked = True
    
  like_status = {
    'liked': liked,
    'count': movie.like_user.count()
  }
  return JsonResponse(like_status)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_id):
  if request.method == 'GET':
    reviews = Review.objects.filter(movie_id_id=movie_id)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
  
  else:
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      # print(serializer)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail_update_delete(request, movie_id, review_pk):
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
    return Response({'message': f'{review_pk}번 댓글이 정상적으로 삭제되었습니다.', 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_recommend(request):
  recommendee = get_object_or_404(get_user_model(), username=request.user)
  his_reviews = recommendee.review_set.all()
  his_genre = {}
  for review in his_reviews:
    review_genres = review.movie_id.genres.all()
    for review_genre in review_genres:
      genre = review_genre.name
      if genre in his_genre:
        his_genre[genre] += 1
      else:
        his_genre[genre] = 1
  movies = Movie.objects.order_by('-popularity')
  rec_vote_avg = []
  rec_genre = []
  cnt = 0
  temp = []
  for his_review in his_reviews:
    temp.append(his_review.movie_id.pk)
  if his_genre:
    max_genre = max(his_genre.items(), key=operator.itemgetter(1))[0]
    for movie in movies:
      target_genre = Genre.objects.get(name=max_genre)
      if target_genre in movie.genres.all():
        if movie.pk not in temp:
          if movie not in rec_genre:
            rec_genre.append(movie)
          cnt += 1
      if cnt == 10:
        break
  serializer = MovieListSerializer(rec_genre, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)