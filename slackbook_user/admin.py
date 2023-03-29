from django.contrib import admin

from .models import User, Channel, Topic
# from django_summernote.admin import SummernoteModelAdmin


# admin.site.register(Channel)


admin.site.register(User)
admin.site.register(Channel)
admin.site.register(Topic)
