from rest_framework import serializers
from .models import Movie, Genre


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path','vote_average')

class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','name')