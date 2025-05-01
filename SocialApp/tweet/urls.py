"""
URL configuration for SocialApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.tweetList, name='tweetList'),
    path('create/',views.tweetCreate, name='tweetCreate'),
    path('<int:tweet_id>/edit/',views.tweetEdit, name='tweetEdit'),
    path('<int:tweet_id>/delete/',views.tweetDelete, name='tweetDelete'),
    path('register/',views.Register, name='Register'),
    path('search/',views.Search,name='Search'),
    path('profile/',views.Profile,name='Profile'),
    path('aboutus/',views.AboutUs,name='AboutUs')
    # path('',views.tweetList, name='tweetList'),
]


    