from rest_framework import serializers
from blog.models import Blog,Blogger

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ('title','blogger','content','created_on','topics')
    read_only_fields = ('blogger','topics')