from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<str:movie_title>/', views.movie_detail_by_title),
    path('<int:movie_id>/like/', views.like),
    path('<int:movie_id>/review/', views.review_list_create),
    path('<int:movie_id>/review/<int:review_pk>/', views.review_detail_update_delete),
    path('review_recommend/', views.review_recommend),
]
