from .models import Article, Comment
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Article
    exclude = ('user',)
    # fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Article
    fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Comment
    exclude = ('user',)
    read_only_fields = ('article',)


class CommentListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = '__all__'
