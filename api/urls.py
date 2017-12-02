from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import BlogsView, BlogDetailView

urlpatterns = [
  url('^v1/blogs/$',BlogsView.as_view(),name='blogs-list'),
  url('^v1/blog/(?P<pk>[0-9]+)/$',BlogDetailView.as_view(),name='blog-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)