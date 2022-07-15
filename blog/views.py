from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Post


# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        latest = Post.objects.order_by('date')[:3]
        context['posts'] = latest
        return context


class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = 'posts'


def post(request, slug):
    p = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post.html", {'post': p})


class PostView(DetailView):
    template_name = "blog/post.html"
    module = Post
