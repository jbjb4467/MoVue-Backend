from django.urls import path
from . import views


urlpatterns = [
  path('<int:category>/article/', views.article_create_read, name="list"),
  path('<int:category>/article/<int:article_pk>/', views.article_detail_update_delete),
  path('<int:category>/article/<int:article_pk>/comment/', views.comment_create_read),
  path('<int:category>/article/<int:article_pk>/comment/<int:comment_pk>/', views.comment_detail_update_delete),
]