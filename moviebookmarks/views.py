from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import UserSerializer, MovieBookmarkSerializer
from .models import MovieBookmarks
from django.contrib.auth.models import User

class MovieBookmarkView(generics.ListCreateAPIView):
    queryset = MovieBookmarks.objects.all()
    serializer_class = MovieBookmarkSerializer


class MovieBookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieBookmarks.objects.all()
    serializer_class = MovieBookmarkSerializer

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class MovieBookmarkView(APIView):
#     def get(self):
#         bookmarks = MovieBookmarks.objects.all()
#         serializer = MovieBookmarkSerializer(bookmarks, many = True)

#     def post(self):
#         pass