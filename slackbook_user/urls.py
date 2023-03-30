from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('channel/<str:pk>/', views.channel, name='channel'),
    path('topics/', views.topics, name='topics'),
    path('account/<str:pk>/', views.account, name='account'),
    path(
     'delete-comment/<str:pk>/', views.deleteComment, name='delete-comment'),

]
