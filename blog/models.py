from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from datetime import datetime


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, unique=True, verbose_name='What is the category name ?')
    category_slug = models.SlugField(unique=True, max_length=150, blank=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)

        return super().save(*args, **kwargs)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True, verbose_name='Title of the Post')
    body = models.TextField(verbose_name='Blog content')
    picture_location = models.ImageField(upload_to='images/', max_length=200)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now())
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    blog_slug = models.SlugField(blank=True, )
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(self.title)

        return super().save(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Fullname')
    comment = models.TextField(verbose_name='Comment')
    timestamp = models.DateTimeField(default=datetime.now())
    blog_post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name







