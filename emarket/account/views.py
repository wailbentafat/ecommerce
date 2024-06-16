from django.shortcuts import render # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore
from rest_framework.response import Response # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.hashers import make_password # type: ignore
from rest_framework import status # type: ignore
from .serializer import signupserializer 
from rest_framework.permissions import IsAuthenticated # type: ignore

@api_view(['POST'])
def register(request):
    data=request.data
    user=signupserializer(data=data)
    if user.is_valid():
        if not User.objects.filter(email=data['email']).exists():
            user=User.objects.create(first_name=data['first_name'],
                                    last_name=data['last_name'],
                                    email=data['email'],
                                    password=make_password(data['password']),
                                    username=data['email']
                                    )
            return Response({'message':'success'},status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'email already exists'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user=signupserializer(request.user,many=False)
    return Response(user.data)

   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user=request.user
    data=request.data
    user.first_name=data['first_name']
    user.last_name=data['last_name']
    user.email=data['email']
    user.username=data['email']
    if data['password'] != '':
        user.password=make_password(data['password'])
    user.save()
    return Response({"message":"user updated"})
