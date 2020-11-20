from .models import Genre, Movie
from rest_framework import serializers

class MovieListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = ('title', 'poster_path', 'movie_id',)


class MovieDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = '__all__'