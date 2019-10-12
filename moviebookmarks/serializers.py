from rest_framework import serializers
from .models import MovieBookmarks
from django.contrib.auth.models import User

class MovieBookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieBookmarks
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'