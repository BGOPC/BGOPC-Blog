from django.urls import path


from . import views

urlpatterns = [
    path('', views.login),
    # path('signup/', views.signup),
    path('signup/', views.SignupView.as_view()),
    # path('user/<uid>', views.page, name='profile-page'),
    path('user/<str:uid>', views.PageView.as_view(), name='profile-page'),
    path('upload/', views.NpView.as_view(), name='new-post'),
]
