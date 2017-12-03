from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BlogSerializer, CommentSerializer
from blog.models import Blog,Blogger,Comment
from .permissions import IsUser
# Create your views here.
class BlogsView(generics.ListCreateAPIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.all()

  def perform_create(self, serializer):
    serializer.save()

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.all()

class CommentsView(generics.ListCreateAPIView):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  permission_classes = (permissions.IsAuthenticated,IsUser)

  def perform_create(self,serializer):
    serializer.save(user = self.request.user)
