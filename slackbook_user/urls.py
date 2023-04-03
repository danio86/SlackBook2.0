from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('channel/<str:pk>/', views.channel, name='channel'),
    # path('topics/', views.topics, name='topics'),
    path('account/<str:pk>/', views.account, name='account'),
    path(
     'delete-comment/<str:pk>/', views.deleteComment, name='delete-comment'),
    path('create-channel/', views.createChannel, name='create-channel'),
    path(
     'update-channel/<str:pk>/', views.updateChannel, name='update-channel'),
    path(
     'delete-channel/<str:pk>/', views.deleteChannel, name='delete-channel'),
    path('user-settings/', views.userSettings, name='user-settings'),

]
