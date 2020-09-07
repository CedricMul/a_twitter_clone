from django.db import models
from twitteruser.models import MyTwitterUser

class Tweet(models.Model):
    user_tweeted = models.ForeignKey(
        MyTwitterUser,
        related_name='tweeted',
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=140)
    date_and_time = models.DateTimeField(auto_now=True)
    
