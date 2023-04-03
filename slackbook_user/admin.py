from django.contrib import admin

from .models import User, Channel, Topic, Post
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Channel)


# @admin.register(Channel)
# class ChannelAdmin(SummernoteModelAdmin):
    # admin.site.register(Channel)
    # summernote_fields = ('members',)
