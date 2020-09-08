from django.db import models
from twitteruser.models import MyTwitterUser
from tweet.models import Tweet

class Notification(models.Model):
    notify_user = models.ForeignKey(
        MyTwitterUser,
        on_delete=models.CASCADE
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE
    )
    # For changing status of whether it is seen or not
    # so they can be filtered before and after the
    # notification page is loaded
    is_seen = models.BooleanField(default=False)
