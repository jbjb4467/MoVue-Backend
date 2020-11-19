from django.urls import path
from . import views


urlpatterns = [
  path('reviews/', views.review_list_create),
  path('reviews/<int:review_pk>/', views.review_detail_update_delete),
  path('reviews/<int:review_pk>/comment/', views.create_read_comment),
  path('reviews/<int:review_pk>/comment/<int:comment_pk>/', views.comment_detail_update_delete),
]
