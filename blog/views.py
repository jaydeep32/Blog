from blog.models import Post
from django.shortcuts import render

def index_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts, 
    }
    return render(request, 'index.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all()[:3]
    context = {
        'posts': posts, 
        'post': post, 
        'comments': post.comments.all(),
    }
    return render(request, 'post-detail.html', context)


