from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Created a model that stored the user's friend inside 
class Friends(models.Model):
    Amigo = models.ForeignKey(User, on_delete=models.CASCADE)
    requestPending = models.BooleanField(default = True)
    viewable = models.BooleanField(default = True)

# Created a model that stores all of the user information, including their friends
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #notifications = models.ManyToManyField(Notifications, related_name='users', blank=True)
    friendList = models.ManyToManyField(Friends, related_name='users', blank=True)
    isViewer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
