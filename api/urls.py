from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import BlogsView, BlogDetailView, CommentsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  url('^v1/blogs/$',BlogsView.as_view(),name='blogs-list'),
  url('^v1/blog/(?P<pk>[0-9]+)/$',BlogDetailView.as_view(),name='blog-detail'),
  url('v1/comments/$',CommentsView.as_view(), name='comment-list'),
  url('^v1/auth/',include('rest_framework.urls',namespace='rest-framework')),
  url(r'^v1/get-token/',obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)