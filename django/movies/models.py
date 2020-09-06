import requests
from django.conf import settings
from django.db import models


# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    poster_path=models.CharField(max_length=100,null=True)
    backdrop_path=models.CharField(max_length=100,null=True)
    overview=models.TextField()
    release_date=models.DateField()    
    vote_average=models.FloatField()
    rating_users=models.ManyToManyField(settings.AUTH_USER_MODEL, through='Rating',related_name='rating_movies')
    

    @classmethod
    def get_movie(cls):
        TMDB_URL='https://api.themoviedb.org/3/movie/now_playing'
        API_KEY='bfb5c7f19282ed6f7fd887a13cc2ce86'
        for i in range(1,26):
            params={'api_key':API_KEY,'language':'ko','page':i}
            movies=requests.get(TMDB_URL,params=params).json()
            for movie in movies["results"]:
                tmp=cls.objects.create(
                    title=movie["title"],
                    poster_path=movie["poster_path"],
                    backdrop_path=movie["backdrop_path"],
                    overview=movie["overview"],
                    release_date=movie["release_date"],
                    vote_average=movie["vote_average"]
                )
                genres=movie["genre_ids"]
                for genre in genres:
                    tmp.genres.add(genre)

class Genre(models.Model):
    name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie,related_name='genres')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='genres', through= 'UserGenre')


    @classmethod
    def get_genre(cls):
        GENRE_URL='https://api.themoviedb.org/3/genre/movie/list?api_key=bfb5c7f19282ed6f7fd887a13cc2ce86&language=ko'
        genres=requests.get(GENRE_URL).json()
        for genre in genres["genres"]:
            cls.objects.create(
                id=genre["id"],
                name=genre["name"]
            )

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    point = models.IntegerField()

class UserGenre(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    count = models.IntegerField()