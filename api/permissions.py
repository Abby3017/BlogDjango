from rest_framework.permissions import BasePermission
from blog.models import Comment

class IsUser(BasePermission):

  def has_object_permission(self, request, view, obj):
    if isinstance(obj, BucketList):
      return obj.user == request.user
    return obj.user == request.user 