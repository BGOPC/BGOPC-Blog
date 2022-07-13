from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
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
    return render(request,'user/page.html', {"user":user})