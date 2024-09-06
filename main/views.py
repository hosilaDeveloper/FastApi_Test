from rest_framework import generics
from .serializer import CategorySerializer, PostSerializer
from .models import Category, Post


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
