from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from blog.models import Post
from .models import BlogUser
from .forms import *

# Create your views here.
def login(request):
    return render(request, 'user/login.html')
def signup(request):
    lf = NewUserForm(request.POST or None)
    if request.method == 'POST':
        if lf.is_valid() and lf:
            user = lf.save()
            return redirect(reverse('profile-page', kwargs={'uid':user.nickname}))
        else:
            return render(request,'user/signup.html', {
                    'lf':lf,
                    'error':"Please Fill All of the required fields and if still doesn't work Your nickname exist and u should change it"
                })
    return render(request,'user/signup.html', {
                'lf':lf,
                'error':None
            })


def page(request, uid):
    user = get_object_or_404(BlogUser, nickname=uid)
    all_posts = Post.objects.filter(author_id=user.id).order_by("date")
    return render(request,'user/page.html', {"user":user, "posts":all_posts})

def np(request, unc):
    user = get_object_or_404(BlogUser, nickname=unc)
    return render(request,'user/new_post.html', {"user":user})