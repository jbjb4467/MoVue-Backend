from .models import Review
from rest_framework import serializers


class ReviewListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    exclude = ('user', 'like_users',)