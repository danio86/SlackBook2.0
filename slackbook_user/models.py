from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    biography = models.TextField(null=True)
    id = models.AutoField(primary_key=True)
    # avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Channel(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # if the Topic Class would be below the this(Channel) Class
    # Topic wouldt need quotes ('Topic')
    # if the topic is deleted, the Channel is not deleted (SET_NULL)
    # title = models.CharField(max_length=200)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    guests = models.ManyToManyField(User, related_name='guests', blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    # excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    privat = models.BooleanField()
    keywords = models.TextField(blank=True)
    permission = models.TextField(blank=True)
    # likes = models.ManyToManyField(
    #     User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title