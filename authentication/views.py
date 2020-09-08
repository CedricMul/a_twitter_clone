from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from twitteruser.models import MyTwitterUser
from tweet.models import Tweet
from notification.models import Notification
from authentication.forms import UserCreateForm, SignInForm

def create_user_view(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyTwitterUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password')
            )
            new_user.following.add(new_user)
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('home'))
    form = UserCreateForm()
    return render(request, 'auth_forms.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            log_user = authenticate(
                username=data.get('username'),
                password=data.get('password')
            )
            if log_user:
                login(request, log_user)
                return HttpResponseRedirect(reverse('home'))
    form = SignInForm()
    return render(request, 'auth_forms.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def home_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        following = current_user.following.all()
        follow_int = len(following) - 1
        # Remember to add User to own follow list
        posts = Tweet.objects.filter(user_tweeted__in=following).order_by('-date_and_time')
        notes = Notification.objects.filter(notify_user=current_user
        ).filter(is_seen=False).count()
        return render(
            request,
            'homepage.html',
            {
                'current_user': current_user,
                'posts': posts,
                'notes': notes,
                'follow_int': follow_int
            }
        )
    else:
        return HttpResponseRedirect(reverse('login'))
