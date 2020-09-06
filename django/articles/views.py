from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer,CommentListSerializer

# Articles



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def list_or_create(request):
    if request.method=='GET':
        p = request.GET.get('page',1)
        articles = Paginator(Article.objects.order_by('-id'),10)
        serializer = ArticleListSerializer(articles.page(p), many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie_id = request.data.get('movie_id')
            if movie_id is None:
                return Response({"status":"FAIL"},status=status.HTTP_400_BAD_REQUEST)
            serializer.save(user=request.user,movie_id=request.data.get('movie_id'))
            return Response({"status":"OK",**serializer.data})



@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def detail_or_update_or_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method=='GET':
        serializer = ArticleSerializer(article)
        return Response({"status":"OK",**serializer.data})
    elif request.method=='DELETE':
        if request.user == article.user:
            article.delete()
            return Response({"status":"OK"})
        else:
            return Response({"status":"FAIL","user_error":"본인 글만 삭제할 수 있습니다."},status=status.HTTP_403_FORBIDDEN)
    else:
        if request.user == article.user:
            article.title = request.data.get('title')
            article.content = request.data.get('content')
            article.save()
            serializer = ArticleSerializer(article)
            return Response({"status":"OK",**serializer.data})

        else:
            return Response({"status":"FAIL","user_error":"본인 글만 수정할 수 있습니다."},status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def count(request):
    cnt = Article.objects.count()
    page = 10
    total_page = cnt//page if cnt%page==0 else cnt//page+1
    res={"end_index":total_page}
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def article_user_valid(request,article_id):
    article = get_object_or_404(Article,id=article_id)
    if request.user.id==article.user_id:
        return Response({"status":"OK"})
    return Response({"status":"FAIL"})
    
# Comments

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comment_list_or_create(request,article_id):
    if request.method=='GET':
        comments = Comment.objects.filter(article_id=article_id)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = CommentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=get_object_or_404(Article,id=article_id))
            return Response(serializer.data)


@api_view(['DELETE','PUT'])
@permission_classes([IsAuthenticated])
def comment_update_or_delete(request,article_id,comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method=='DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response({"status":"OK"})
        else:
            return Response({"status":"FAIL","user_error":"본인 댓글만 삭제할 수 있습니다."},status=status.HTTP_403_FORBIDDEN)
    else:
        if request.user == comment.user:
            comment.content = request.data.get('content')
            comment.save()
            serializer = CommentSerializer(comment)
            return Response({"status":"OK",**serializer.data})

        else:
            return Response({"status":"FAIL","user_error":"본인 댓글만 수정할 수 있습니다."},status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_user_valid(request,article_id,comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    if request.user.id==comment.user_id:
        return Response({"status":"OK"})
    return Response({"status":"FAIL"})