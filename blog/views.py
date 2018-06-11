from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_time=timezone.now()).order_by('published_time')
    return render(request, 'blog/post_list.html', {'posts': posts})
