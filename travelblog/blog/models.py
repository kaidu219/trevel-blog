from django.db import models
import uuid 
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class Tag(models.Model):
    
    slug = models.CharField(max_length=150, unique=True, primary_key=True)
    title = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
    def __str__(self) -> str:
        return self.title

class Category(models.Model):

    slug = models.CharField(max_length=150, unique=True, primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    text = RichTextField()
    photo = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    tags = models.ManyToManyField(Tag, related_query_name='tags+', related_name='tags')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.author.first_name} {self.author.last_name} commented on {self.blog.title}'