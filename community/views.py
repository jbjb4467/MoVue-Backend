from django.shortcuts import get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def article_create_read(request):
  if request.method == 'POST':
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
  else:
    article.delete()
    return Response({'message': f'{article_pk}번 댓글이 정상적으로 삭제되었습니다.', 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def comment_create_read(request, article_pk):
  if request.method == 'POST':
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
      serializer.save(article=article, user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, article_pk, comment_pk):
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
    return Response({'message': f'{comment_pk}번 댓글이 정상적으로 삭제되었습니다.', 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)
