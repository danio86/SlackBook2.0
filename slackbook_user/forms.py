from django.forms import ModelForm
from .models import User, Channel, Post, Chat


class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        fields = ['avatar', 'username', 'name', 'email']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'image']


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['title', 'body', 'image']
