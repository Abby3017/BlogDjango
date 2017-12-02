from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer
from blog.models import Blog,Blogger

# Create your views here.
class BlogsView(generics.ListCreateAPIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.all()

  def perform_create(self, serializer):
    serializer.save()

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.all()