from .models import Review, Comment
from rest_framework import serializers


class ReviewListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    exclude = ('user', 'like_users',)


class CommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('review',)
