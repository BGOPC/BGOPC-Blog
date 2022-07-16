from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView

from .forms import *


# Create your views here.
def red(request):
    unc = request.session.get("unc", None)
    if unc:
        user = get_object_or_404(BlogUser, nickname=unc)
        return redirect(reverse("profile-page", kwargs={'uid':unc}))
    return redirect(reverse("login"))
class LoginView(View):
    def get(self):
        pass

    def post(self):
        pass

class SignupView(View):
    def get(self, request):
        lf = NewUserForm()
        return render(request, 'user/signup.html', {
            'lf': lf,
            'error': None,
            'user': None,
        })

    def post(self, request):
        lf = NewUserForm(data=request.POST, files=request.FILES)

        if lf.is_valid() and lf:
            user = lf.save()
            request.session["unc"] = str(user.nickname)
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
        request = self.request
        unc = request.session.get("unc", None)
        checkuser = None
        if unc:
            checkuser = BlogUser.objects.get(nickname=unc)
        user = get_object_or_404(BlogUser, nickname=uid)
        all_posts = Post.objects.filter(author_id=user.id).order_by("date")
        context["user"] = user
        context["checkuser"] = user == checkuser
        context["posts"] = all_posts
        return context


class NpView(View):
    def get(self, request):
        unc = request.session.get("unc", None)
        if unc:
            user = get_object_or_404(BlogUser, nickname=unc)
            return render(request, 'user/new_post.html', {"user": user, "form": NewPostForm()})
        res = HttpResponse("Client Unauthorized")
        res.status_code = 401
        return res

    def post(self, request):
        unc = request.session.get("unc", None)
        if unc and BlogUser.objects.filter(nickname=unc).exists():
            Postform = NewPostForm(request.POST, request.FILES)
            if Postform.is_valid():
                NewPost: Post = Postform.save()
                NewPost.author = BlogUser.objects.get(nickname=unc)
                NewPost.save()
                return redirect(reverse("post-detail", kwargs={"slug": NewPost.slug}))
            user = get_object_or_404(BlogUser, nickname=unc)
            return render(request, 'user/new_post.html', {"user": user, "form": Postform})

        return HttpResponse("Client Unauthorized", status=401)
