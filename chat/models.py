from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Schnap(models.Model):
    image = models.ImageField()
    sender = models.ForeignKey(User)
    sent_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{}'s Schnap".format(self.sender.username)


class Friendship(models.Model):
    creator = models.ForeignKey(User, related_name="friendship_creator")
    receiver = models.ForeignKey(User, related_name="friendship_receiver")
    created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField()


