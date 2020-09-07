from django.db.models import Count
from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import MyTwitterUser
from tweet.models import Tweet
from notification.models import Notification

def user_detail_view(request, id):
    # If a user is signed in
    if request.user:
        current_user = request.user
        # Gets number of notifications for current user
        notes = len(Notification.objects.filter(notify_user=current_user.id))
    else:
        current_user = None
        notes = 0
    detail_user = MyTwitterUser.objects.get(id=id)
    posts = Tweet.objects.filter(user_tweeted=detail_user)
    post_count = len(posts)
    follows = MyTwitterUser.objects.filter(following=detail_user).count() - 1
    return render(
        request,
        'user_detail.html',
        {
            'current_user': current_user,
            'notes': notes,
            'viewed_user': detail_user,
            'posts': posts,
            'post_count': post_count,
            'follow_int': follows
        }
    )

def user_profile_view(request):
    current_user = request.user
    posts = Tweet.objects.filter(user_tweeted=current_user)
    post_count = len(posts)
    notes = Notification.objects.filter(notify_user=current_user.id).count()
    follow_int = current_user.following.count() - 1
    return render(
        request,
        'user_home.html',
        {
            'current_user': current_user,
            'posts': posts,
            'notes': notes,
            'post_count': post_count,
            'follow_int': follow_int
        }
    )

def follow_view(request, id):
    if request.user.is_authenticated:
        follower = request.user
        followed = MyTwitterUser.objects.get(id=id)
        follower.following.add(followed)
    return HttpResponseRedirect(reverse('home'))
