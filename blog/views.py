from django.shortcuts import get_object_or_404, render
from .models import Post
from django.urls import reverse


# Create your views here.
def index(request):
    latest = Post.objects.order_by('date')[:3]
    return render(request, "blog/index.html", {
        'posts': latest,
    })


def posts(request):
    context = {'posts': Post.objects.all()}
    return render(request, "blog/posts.html", context=context)


def post(request, slug):
    p = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post.html", {'post': p})
