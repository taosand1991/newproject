from django.db import models
from django.conf import settings
from accounts.models import  Profile


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
STATUS = (

    ('draft', 'draft'),
    ('publish', 'published')

)
CATEGORIES = (
    ('RO', 'Romance'),
    ('CR', 'Crime'),
    ('TR', 'Travel')
)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(max_length=200, choices=CATEGORIES, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS, default='draft')
    blog_views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Category, related_name='cattys', default=1)
    cover = models.ImageField(upload_to='img/', blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author