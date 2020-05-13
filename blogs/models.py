from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, unique_for_date='created')
    author = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.email