from django.shortcuts import render
from .models import Post
# Create your views here.


def index_page(request):
    posts = Post.objects.all()
    print(locals)
    return render(request, 'index.html', {'posts': posts})

def detail_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'detail_post.html', {'post': post})
    
