from django import forms

from tweet.models import Tweet

class PostTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            #'user_tweeted',
            'content',
            #'date_and_time'
        ]
