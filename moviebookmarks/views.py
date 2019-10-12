from django.shortcuts import render

from django.core import exceptions

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import UserSerializer, MovieBookmarkSerializer, AppUserSerializer
from .models import MovieBookmarks, AppUser



class MovieBookmarkView(generics.ListCreateAPIView):
    queryset = MovieBookmarks.objects.all()
    serializer_class = MovieBookmarkSerializer


class MovieBookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieBookmarks.objects.all()
    serializer_class = MovieBookmarkSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                appUser = AppUser.objects.get(email=serializer.data['email'])
                if (appUser.email == serializer.data['email'] and appUser.password == serializer.data['password']):
                    return Response({
                        'id': appUser.id
                    }, status=status.HTTP_200_OK)
                else:
                    return HttpResponseForbidden()
            except Exception:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()

class RegisterView(APIView):
    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                appUser = serializer.save()
                appUser = AppUser.save(appUser)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()


# class MovieBookmarkView(APIView):
#     def get(self):
#         bookmarks = MovieBookmarks.objects.all()
#         serializer = MovieBookmarkSerializer(bookmarks, many = True)

#     def post(self):
#         pass
