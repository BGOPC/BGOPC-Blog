from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('signup/', views.signup),
    path('user/<uid>', views.page, name='profile-page'),
    path('upload/<unc>', views.np, name='new-post'),
]
