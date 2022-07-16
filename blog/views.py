from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from pyrsistent import s

from user.models import BlogUser

from .models import Post


# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        latest = Post.objects.order_by('date')[:3]
        context['posts'] = latest
        request = self.request
        unc = request.session.get("unc", None)
        user = None
        if unc:
            user = get_object_or_404(BlogUser, nickname=unc)
        context['user'] = user
        return context


class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        unc = request.session.get("unc", None)
        user = None
        if unc:
            user = get_object_or_404(BlogUser, nickname=unc)
        context['user'] = user
        return context

class PostView(DetailView):
    template_name = "blog/post.html"
    module = Post
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        request = self.request
        unc = request.session.get("unc", None)
        user = None
        if unc:
            user = get_object_or_404(BlogUser, nickname=unc)
        context['user'] = user
        return context