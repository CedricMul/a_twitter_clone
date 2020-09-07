from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Reads contents of tweet for a name following an @
from tweet.reg_helper import read_reggie

from tweet.forms import PostTweetForm

from tweet.models import Tweet
from notification.models import Notification
from twitteruser.models import MyTwitterUser

@login_required
def post_tweet_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        notes = len(Notification.objects.filter(notify_user=current_user.id))
    else:
        notes = 0
    if request.method == "POST":
        form = PostTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet(
                user_tweeted=data.get('user_tweeted'),
                content=data.get('content'),
                #date_and_time=data.get('date_and_time')
            )
            new_tweet.save()
            # Either gets after "@" or returns false
            notify = read_reggie(data.get('content'))
            if notify:
                # Gets user being "@" @ by the username in the mention
                #note_user = MyTwitterUser.objects.get(username=notify)
                Notification.objects.create(
                    # Attributes user
                    notify_user=MyTwitterUser.objects.get(username=notify).id,
                    # Gets tweet obj
                    tweet=new_tweet,
                    is_seen=False
                ).save()
            return HttpResponseRedirect(reverse('home'))
    form = PostTweetForm()
    return render(request, 'tweet_form.html', {'form': form, 'notes': notes})

def tweet_detail_view(request, id):
    if request.user:
        current_user = request.user
        notes = Notification.objects.filter(notify_user=current_user.id).count()
    else:
        notes = 0
    tweet = Tweet.objects.get(id=id)
    return render(
        request,
        'tweet_detail.html',
        {
            'tweet': tweet,
            'notes': notes
        })
