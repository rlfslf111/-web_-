from rest_framework import serializers
from accounts.serializers import UserSerializer
from movies.serializers import MovieListSerializer
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    movie = MovieListSerializer()
    created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")

    class Meta:
        model = Article
        fields = ('id', 'title', 'user','created_at','updated_at','movie')# movie{ title:ddd , poste"...}//


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    movie = MovieListSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S",required=False)
    updated_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S",required=False)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer()
    created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'article', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S",required=False)
    updated_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S",required=False)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'user', 'article', 'created_at', 'updated_at')
