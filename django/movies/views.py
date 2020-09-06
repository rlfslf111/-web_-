import random

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie,Genre,Rating,UserGenre
from .serializers import MovieListSerializer, MovieSerializer, GenreSerializer, MovieSearchSerializer



@api_view(['GET'])
def count(request):
    cnt = Movie.objects.count()
    page = 12
    total_page = cnt//page if cnt%page==0 else cnt//page+1
    res={"end_index":total_page}
    return Response(res)

@api_view(['GET','POST'])
def list_or_create(request):
    if request.method=='GET':
        p = request.GET.get('page',1)
        movies = Paginator(Movie.objects.order_by('-vote_average'),12)
        serializer = MovieListSerializer(movies.page(p), many=True)
        return Response(serializer.data)
    else:
        if request.user.is_superuser:
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"status":"OK",**serializer.data})
        else:
            return Response({"status":"FAIL","user_error":"관리자만 생성할 수 있습니다."},status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','DELETE','PUT'])
def detail_or_update_or_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method=='GET':
        serializer = MovieSerializer(movie)
        genre = movie.genres.all()
        genre_srlzr=GenreSerializer(genre, many=True)  
        return Response({"status":"OK",**serializer.data,"genre":[x["name"] for x in genre_srlzr.data]})
    
    elif request.method=='DELETE':
        if request.user.is_superuser:
            movie.delete()
            return Response({"status":"OK"})
        else:
            return Response({"status":"FAIL","user_error":"관리자만 삭제할 수 있습니다."},status=status.HTTP_403_FORBIDDEN)

    else:
        if request.user.is_superuser:
            movie.title = request.data.get('title')
            movie.poster_path = request.data.get('poster_path')
            movie.backdrop_path = request.data.get('backdrop_path')
            movie.overview = request.data.get('overview')
            movie.release_date = request.data.get('release_date')
            movie.vote_average = request.data.get('vote_average')
            movie.save()
            genre_ids=request.data.get('genre_ids')
            for genre_id in genre_ids:
                movie.genres.add(genre_id)
            serializer = MovieSerializer(movie)
            return Response({"status":"OK",**serializer.data})

        else:
            return Response({"status":"FAIL","user_error":"관리자만 수정할 수 있습니다."},status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def rate(request,movie_id):
    if request.method == 'GET':
        if Rating.objects.filter(movie_id=movie_id,user_id=request.user.id).exists():
            rating = Rating.objects.get(movie_id=movie_id,user_id=request.user.id)
            return Response({"status":"OK","point":rating.point})
        else:
            return Response({"status":"FAIL"},status=status.HTTP_404_NOT_FOUND)
    elif request.method=='POST':
        if Rating.objects.filter(movie_id=movie_id,user_id=request.user.id).exists():
            rating = Rating.objects.get(movie_id=movie_id,user_id=request.user.id)
        else:
            rating = Rating(movie_id=movie_id,user_id=request.user.id)
            movie = Movie.objects.get(id=movie_id)
            for genre in movie.genres.all():
                if UserGenre.objects.filter(genre_id=genre.id,user_id=request.user.id).exists():
                    cnt = UserGenre.objects.get(genre_id=genre.id,user_id=request.user.id)                
                    cnt.count+=1
                else:
                    cnt = UserGenre(genre_id=genre.id,user_id=request.user.id)
                    cnt.count=1            
                cnt.save()
            best_genre_id = UserGenre.objects.filter(user_id=request.user.id).order_by('-count')
            request.user.best_genre_id=best_genre_id[0].genre_id
            request.user.save()

        rating.point = request.data.get('point')
        rating.save()
        return Response({"status":"OK", "point":rating.point})
    else:
        rating = get_object_or_404(Rating,movie_id=movie_id,user_id=request.user.id)
        rating.delete()
        return Response({"status":"OK"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
    # 유저가 평점을 낸 영화가 있을 경우
    # 유저가 평점을 낸 영화의 장르 추출
    # 카운트를 통해 가장 많이 추천한 장르의 영화중 랜덤으로 10개
    if request.user.best_genre_id is None:
        movies = Paginator(Movie.objects.order_by('-vote_average'),8)
        serializer = MovieListSerializer(movies.page(1), many=True)
        return Response(serializer.data)
    else:
        best_genre = Genre.objects.get(id=request.user.best_genre_id)
        movies = best_genre.movies.all()
        movie_ids = []
        for movie in movies:
            movie_ids.append(movie.id)
        recommend_movie_ids = random.sample(movie_ids,8)
        res=[]
        for movie_id in recommend_movie_ids:
            serializer = MovieListSerializer(Movie.objects.get(id=movie_id))
            res.append(serializer.data)
        return Response(res)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):
    Movies = Movie.objects.all()
    serializer = MovieSearchSerializer(Movies,many=True)
    return Response(serializer.data)