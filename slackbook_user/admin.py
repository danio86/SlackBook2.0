from django.contrib import admin

from .models import User, Channel, Topic, Post, Chat
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(User)
# admin.site.register(Topic)
# admin.site.register(Post)
# admin.site.register(Channel)
# admin.site.register(Chat)


@admin.register(Channel)
class ChannelAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'host']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description',)


@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):

    search_fields = ['title']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['user', 'channel']
    list_filter = ('user', 'created_on')


@admin.register(Chat)
class ChatAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'host']
    list_filter = ('title', 'host', 'created_on')
