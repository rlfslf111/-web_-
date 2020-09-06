from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_or_create),
    path('<int:movie_id>/', views.detail_or_update_or_delete),
    path('<int:movie_id>/rate/', views.rate),
    path('recommend/', views.recommend),
    path('search/', views.search),
    path('count/', views.count),

]