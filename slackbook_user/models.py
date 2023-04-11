from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    biography = models.TextField(null=True)
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    # userImage = models.ImageField(null=True, default="avatar.png")

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
    # slug = models.SlugField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    guests = models.ManyToManyField(User, related_name='guests', blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    # excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    keywords = models.TextField(blank=True)
    private = models.BooleanField(default=False, blank=True)
    permission = models.TextField(blank=True)
    # members = models.ManyToManyField(
    #     User, blank=True, related_name='members',
    #     limit_choices_to={'name': True})

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    # this says to which channel the post belongs
    # all posts are children of the Channel Class/Model.
    # If Channel or User gets deleted, all posts have to get deleted too.
    body = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    image_description = models.TextField(null=True, max_length=200, blank=True)
    # video = models.FileField(upload_to='videos_uploaded',null=True,
    # validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['-updated_on', '-created_on']

    def __str__(self):
        return self.body[0:30]