from django.conf.urls import url

from . import views

urlpatterns = [
  url('^$',views.index,name='index'),
  url('^blogs/$',views.BlogListView.as_view(),name="blogs"),
  url('^blog/(?P<pk>\d+)$',views.BlogDetailView.as_view(),name="blog-detail"),
  url('^blogger/(?P<pk>\d+)$', views.BloggerDetailView.as_view(),name='blogger-detail'),
  url('^bloggers/$',views.BloggerListView.as_view(),name='bloggers')
]