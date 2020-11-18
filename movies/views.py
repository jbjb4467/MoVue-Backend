from .models import Movie
from .serializers import MovieDetailSerializer, MovieListSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def movie_list(request):
  movies = Movie.objects.all()
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
  movie = Movie.objects.get(movie_id=movie_id)
  serializer = MovieDetailSerializer(movie)
  return Response(serializer.data)