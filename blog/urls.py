from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='main-page'),
    path('posts/', views.posts, name="posts-page"),
    path("post/<slug>", views.post , name="post-detail"),

]
