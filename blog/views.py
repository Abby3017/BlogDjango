from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.
def index(request):
  return render(request,'index.html')

class BlogListView(generic.ListView):
  model = Blog
  paginate_by = 5

class BlogDetailView(generic.DetailView):
  model = Blog

  def get_context_data(self, **kwargs):
    context = super(BlogDetailView,self).get_context_data(**kwargs)
    context['comment'] = Comment.objects.filter(blog = self.get_object())
    return context

class BloggerDetailView(generic.DetailView):
  model = Blogger

class BloggerListView(generic.ListView):
  model = Blogger
  paginate_by = 5

# class CommentCreateView(generic.Cre)