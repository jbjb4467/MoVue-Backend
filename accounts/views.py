from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from movies.serializers import ReviewListSerializer

User = get_user_model()


@api_view(['POST'])
def signup(request):
  password = request.data.get('password')
  password_confirm = request.data.get('passwordConfirm')

  if password != password_confirm:
    return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

  serializer = UserSerializer(data=request.data)
  
  if serializer.is_valid(raise_exception=True):
    user = serializer.save()
    user.set_password(request.data.get('password'))
    user.save()

  return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile(request, username):
  person = get_object_or_404(User, username=username)
  reviews = person.review_set.all()
  serializer = ReviewListSerializer(reviews, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)