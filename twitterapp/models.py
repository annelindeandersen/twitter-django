from django.db import models
from django.contrib.auth.models import User


class TweetItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status = models.BooleanField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pk}:{self.title}, by {self.user}"