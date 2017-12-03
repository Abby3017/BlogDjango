from rest_framework import serializers
from blog.models import Blog, Blogger, Comment

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ('title','blogger','content','created_on','topics')
    read_only_fields = ('blogger','topics')

class CommentSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source='user.username')

  class Meta:
    model = Comment
    fields =('created_on','blog','comment','user')
    read_only_fields = ('created_on',)