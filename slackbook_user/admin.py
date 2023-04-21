from django.contrib import admin

from .models import User, Channel, Topic, Post, Chat
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Post)
# admin.site.register(Channel)
admin.site.register(Chat)


@admin.register(Channel)
class ChannelAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'host']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description',)

# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):

#     list_display = ('title', 'slug', 'status', 'created_on')
#     search_fields = ['title', 'content']
#     list_filter = ('status', 'created_on')
#     prepopulated_fields = {'slug': ('title',)}
#     summernote_fields = ('content',)
