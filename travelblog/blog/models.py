from django.db import models
import uuid 
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class Tag(models.Model):
    title = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    def __str__(self) -> str:
        return self.title

class Categories(models.Model):
    category_choice = [
        ['Travel','Travel'],
        ['Tour', 'Tour'],
        ['Destination', 'Destination'],
        ['Drinks', 'Drinks'],
        ['Food', 'Food'],
    ]

    name = MultiSelectField(choices=category_choice, max_length=40)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    text = RichTextField()
    photo = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/', null=True, blank=True)
    categories = models.ManyToManyField(Categories)
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    tags = models.ManyToManyField(Tag, related_query_name='tags+', related_name='tags')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['created_date']