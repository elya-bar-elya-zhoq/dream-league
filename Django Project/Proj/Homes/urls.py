from django.urls import path, include
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('', views.index, name='Homes'),

    path('', auth_login, name='login'),
    path('register', views.registerView.as_view(), name="registration"),
    path('userprofile/', views.profile, name='profile'),

]

