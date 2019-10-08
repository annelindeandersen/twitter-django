from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

from .models import *


@login_required
def index(request):
    if request.method == 'GET':
        tweet_items = TweetItem.objects.all()
        context = {
            'tweets': tweet_items
        }
        return render(request, 'twitterapp/index.html', context)

    if request.method == 'POST':
        tweet_item = TweetItem()
        tweet_item.title = request.POST['title']
        tweet_item.description = request.POST['description']
        tweet_item.status = False
        tweet_item.user = request.user
        tweet_item.save()
        return HttpResponseRedirect(reverse('twitterapp:index'))

    return HttpResponseBadRequest()


@login_required
def profile(request):
    if request.method == 'GET':
        tweet_items = TweetItem.objects.filter(user=request.user)
        context = {
            'tweets': tweet_items
        }
        return render(request, 'twitterapp/profile.html', context)

    if request.method == 'POST':
        tweet_item = TweetItem()
        tweet_item.title = request.POST['title']
        tweet_item.description = request.POST['description']
        tweet_item.status = False
        tweet_item.user = request.user
        tweet_item.save()
        return HttpResponseRedirect(reverse('twitterapp:profile'))

    return HttpResponseBadRequest()

@login_required
def details(request, pk):
    tweet = get_object_or_404(TweetItem, pk=pk, user=request.user)

    if request.method == 'GET':
        context = {
            'tweet': tweet
        }
        return render(request, 'twitterapp/details.html', context)

    if request.method == 'POST':
        tweet.title = request.POST['title']
        tweet.description = request.POST['description']
        status = request.POST.getlist('status')
        if len(status) > 0:
            tweet.status = True
        else:
            tweet.status = False
        tweet.save()
        return HttpResponseRedirect(reverse('twitterapp:index'))

    return HttpResponseBadRequest()