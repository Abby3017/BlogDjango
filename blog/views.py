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