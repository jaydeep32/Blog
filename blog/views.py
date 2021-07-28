from blog.models import Post
from django.shortcuts import render, redirect
from comment_app.forms import CommentForm
from comment_app.models import Comment


def index_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts, 
    }
    return render(request, 'index.html', context)


def post_detail(request, slug):
    comment_form = CommentForm(request.POST or None)
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all()[:3]
    if request.method == 'POST':
        if comment_form.is_valid():
            comment_id = request.POST.get('commentid')
            res = comment_form.save(commit=False)
            res.post = post
            if request.user.is_authenticated:
                res.user = request.user
            if comment_id:
                try:
                    comment = Comment.objects.get(id=comment_id)
                except:
                    pass
                else:
                    res.reply = comment
            res.save()
            return redirect('blog:post-detail', slug=slug)
    context = {
        'posts': posts, 
        'post': post, 
        'comments': post.comments.filter(reply__isnull=True)[:4],
        'form': comment_form,
    }
    return render(request, 'post-detail.html', context)


