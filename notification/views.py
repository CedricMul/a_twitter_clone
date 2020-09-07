from django.shortcuts import render

from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import MyTwitterUser

def notification_view(request):
    current_user = request.user
    #c_notes = Notification.objects.filter(
        # Filter by user
        #notify_user=current_user
        #).filter(
            # and by only unseen notifications
            #is_seen=False
        #)
    # Update status of each notification to seen
    c_notes = Notification.objects.all()
    for n in c_notes:
        n.update(is_seen=True)
    return render(
        request,
        'notification.html',
        {
            'current_user': current_user,
            'notifications': c_notes
        }
        )
