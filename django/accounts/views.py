from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


# Create your views here.
@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def detail_or_delete_or_update(request,user_id):
    User=get_user_model()
    user=get_object_or_404(User,id=user_id)
    serializer = UserSerializer(user)
    if request.method=='GET':
        return Response(serializer.data)
    elif request.method=='DELETE':
        if request.user==user:
            request.user.delete()
            return Response({"status":"OK",**serializer.data})
        else:
            return Response({"status":"FAIL","user_error":"삭제 권한이 없습니다."},status=status.HTTP_403_FORBIDDEN)
    else:
        if request.user == user:
            user.email = request.data.get('email')
            user.save()
            serializer = UserSerializer(user)
            return Response({"status":"OK",**serializer.data})

        else:
            return Response({"status":"FAIL","user_error":"수정 권한이 없습니다."},status=status.HTTP_403_FORBIDDEN)
