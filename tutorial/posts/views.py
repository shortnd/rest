from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializers
from django.shortcuts import render

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializers
