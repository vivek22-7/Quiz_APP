from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username = username).exists():
        return Response({'error':'Username already exists'}, status=400)
    
    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'User created successfully'}, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    return Response({'message': f'Welcome, {request.user.username}!'})