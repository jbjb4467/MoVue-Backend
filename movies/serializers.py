from .models import Genre, Movie, Review
from rest_framework import serializers

class MovieListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = ('title', 'poster_path', 'movie_id',)


class MovieDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    exclude = ('user', 'like_users',)