from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_index, name='movies_index'),
    path('genres/', views.genres_index, name="genres_index"),
    path('<int:movie_pk>/', views.detail, name='detail'),
    # path('<int:movie_pk>/ratings/new/', views.rating_create, name='rating_create'),
    # path('<int:movie_pk>/ratings/<int:rating_pk>/delete/', views.rating_delete, name='rating_delete'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    # path('<int:rating_pk>/update_score/', views.update_score, name="update_score"),
    path('<int:movie_pk>/ratings/<int:rating_pk>/update/', views.rating_update, name='rating_update'),
    path('<int:movie_pk>/ratings/<int:rating_pk>/delete/', views.rating_delete, name='rating_delete'),
    path('<int:movie_pk>/ratings/new/', views.create_rating, name='create_rating'),
    path('genreslist/', views.genres_list),
    path('actors/', views.actors_list),
    path('<int:movie_pk>/rating/<int:rating_pk>/', views.rating_update_and_delete),
    path('<int:movie_pk>/rating/', views.rating_create),
    # path('<int:movie_pk>/', views.movie_detail),
    path('posts/', views.movies_list), 
]