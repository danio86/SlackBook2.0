from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('channel/<str:pk>/', views.channel, name='channel'),
    path('topics', views.topics, name='topics'),
    path('recently-active', views.recentlyActive, name='recently-active'),
    path('chat/<str:pk>/', views.chat, name='chat'),
    path('account/<str:pk>/', views.account, name='account'),
    path(
     'delete-comment/<str:pk>/', views.deleteComment, name='delete-comment'),
    # path('create-channel/', views.createChannel, name='create-channel'),
    path('<slug:slug>/', views.createChannel, name='create-channel'),
    # path('create-channel/', views.createChannel, name='create-channel'),
    path('add-members/<str:pk>/', views.addMembers, name='add-members'),
    path('create-personal-channel/', views.createPersonalChannel,
         name='personal-channel'),
    path('channel-member/<str:pk>/', views.channelMember,
         name='member'),
    path(
     'update-channel/<str:pk>/', views.updateChannel, name='update-channel'),
    path(
     'delete-channel/<str:pk>/', views.deleteChannel, name='delete-channel'),
    path('user-settings/', views.userSettings, name='user-settings'),
    # path('account/logout/', views.logoutUser, name='logout'),

]
