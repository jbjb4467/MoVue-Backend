from django.urls import path
from . import views


urlpatterns = [
  path('article/', views.article_create_read, name="list"),
  path('article/<int:article_pk>/', views.article_detail_update_delete),
  path('article/<int:article_pk>/comment/', views.comment_create_read),
  path('article/<int:article_pk>/comment/<int:comment_pk>/', views.comment_detail_update_delete),
]