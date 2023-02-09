from django.shortcuts import render

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'about.html'
    
class Post_detail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# Create your views here.
