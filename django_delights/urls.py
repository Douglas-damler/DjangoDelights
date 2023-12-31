from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name = "login_user"),
    path('home/', views.home, name = "home"),
    path('logout/', views.logout_user, name="logout_user")
]
