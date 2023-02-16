from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('signup',views.Signup.as_view(),name="sign"),
    path('login',views.Loginuser.as_view(),name="login"),
    path('signout',views.logout,name="signout"),
    path('action',views.Home.as_view()),
]