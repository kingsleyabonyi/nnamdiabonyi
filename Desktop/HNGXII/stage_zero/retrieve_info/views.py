from django.shortcuts import render
from . serializers import UserInfoSerializer
from . models import UserInfo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime, timezone

# Create your views here.
@api_view(['GET'])
def info(request,):
    if request.method == 'GET':
        # users = UserInfo.objects.all()
        # serializer = UserInfoSerializer(users, many=True)
        return Response({
                "email": "kinabonyi@gmail.com",
                "current_date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),  # Convert current time to ISO 8601
                "github_url": "<https://github.com/kingsleyabonyi/HNGXII/tree/master/retrieve_info>"
            }, status=200)
    return Response(status=status.HTTP_404_NOT_FOUND)

