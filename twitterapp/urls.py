from django.urls import path

from . import views


app_name = 'twitterapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>', views.details, name='details'),
    path('profile', views.profile, name='profile'),
]