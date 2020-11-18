from django.urls import path
from . import views


urlpatterns = [
  path('reviews/', views.review_list_create),
]
