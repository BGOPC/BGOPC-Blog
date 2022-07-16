from django.urls import path


from . import views

urlpatterns = [
    path('', views.red),
    path('login', views.LoginView.as_view(), name="login"),
    # path('signup/', views.signup),
    path('signup/', views.SignupView.as_view(), name="signup"),
    # path('user/<uid>', views.page, name='profile-page'),
    path('user/<str:uid>', views.PageView.as_view(), name='profile-page'),
    path('upload/', views.NpView.as_view(), name='new-post'),
]
