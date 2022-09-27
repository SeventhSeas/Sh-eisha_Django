from importlib.resources import contents
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.utils import timezone
from django.urls import reverse
from .helpers import *


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
        
class Comment(models.Model):
    post = models.ForeignKey(
    BlogModel, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="author")
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post")

    def __str__(self):
        return  (str(self.author))

        