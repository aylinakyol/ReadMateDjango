from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'description']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'description']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']