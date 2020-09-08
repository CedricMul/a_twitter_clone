"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import twitteruser.views
import tweet.views
import authentication.views
import notification.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.home_view, name='home'),
    path('tweet_detail/<int:id>/', tweet.views.tweet_detail_view),
    path('login/', authentication.views.LoginView.as_view(), name='login'),
    path('logout/', authentication.views.logout_view),
    path('make_tweet/', tweet.views.post_tweet_view),
    path('notifications/', notification.views.NotificationView.as_view()),
    path('profile/', twitteruser.views.user_profile_view),
    path('view_user/<int:id>/', twitteruser.views.user_detail_view),
    path('new_user/', authentication.views.CreateUserView.as_view()),
    path('following/<int:id>/', twitteruser.views.follow_view)
]
