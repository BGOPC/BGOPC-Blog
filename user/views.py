from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView

from blog.models import Post
from .forms import *



# Create your views here.
def login(request):
    return render(request, 'user/login.html')


class SignupView(View):
    def get(self, request):
        lf = NewUserForm()
        return render(request, 'user/signup.html', {
            'lf': lf,
            'error': None
        })

    def post(self, request):
        lf = NewUserForm(data=request.POST, files=request.FILES)
        print(request.FILES)

        if lf.is_valid() and lf:
            user = lf.save()
            return redirect(reverse('profile-page', kwargs={'uid': user.nickname}))
        else:
            return render(request, 'user/signup.html', {
                'lf': lf,
                'error': """Please Fill All of the required fields,
                 and if still doesn't work Your nickname exist and u should change it"""
            })


class PageView(TemplateView):
    template_name = 'user/page.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data()
        uid = kwargs['uid']
        user = get_object_or_404(BlogUser, nickname=uid)
        all_posts = Post.objects.filter(author_id=user.id).order_by("date")
        context["user"] = user
        context["posts"] = all_posts
        return context


class NpView(View):
    def get(self, request, unc):
        user = get_object_or_404(BlogUser, nickname=unc)
        return render(request, 'user/new_post.html', {"user": user})

    def post(self, request, unc):
        user = get_object_or_404(BlogUser, nickname=unc)
        return render(request, 'user/new_post.html', {"user": user})
