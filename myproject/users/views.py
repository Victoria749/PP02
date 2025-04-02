from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    