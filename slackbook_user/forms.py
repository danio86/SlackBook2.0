from django.forms import ModelForm
from .models import User
from .models import Channel


class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = '__all__'
        # exclude = ['host', 'content', 'guests', 'status', 'slug', 'excerpt']
        

# this shows the model(Channel) i want to create a form for and the
# writable fields. Alternatively: ['body', 'title',...]
# These are Metadata from the Channel-Model
# the form itself is from Django


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['username', 'email']
        # exclude = ['', '']
