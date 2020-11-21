from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieDetailSerializer, MovieListSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def movie_list(request):
  # movies = Movie.objects.all()
  movies = Movie.objects.all()[:10]
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
  movie = Movie.objects.get(movie_id=movie_id)
  serializer = MovieDetailSerializer(movie)
  return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def like(request, movie_id):
  movie = get_object_or_404(Movie, movie_id=movie_id)
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
  # print(like_status)
  # print(request.user)
  return JsonResponse(like_status)
