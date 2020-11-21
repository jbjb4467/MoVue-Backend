from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    movie_id = models.IntegerField(unique=True)
    backdrop_path = models.CharField(max_length=200)
    original_language = models.CharField(max_length=20)
    original_title = models.CharField(max_length=200)
    adult = models.BooleanField()
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movie", default=None)


    def __str__(self):
        return self.title


class Review(models.Model):
  title = models.CharField(max_length=100)
  movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, to_field="movie_id")
  rank = models.IntegerField()
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

  def __str__(self):
    return self.title


    