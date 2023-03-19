from django.db import models
import uuid 
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.

class Blog(models.Model):
    category_choice = (
        ('Travel','Travel'),
        ('Tour', 'Tour'),
        ('Destination', 'Destination'),
        ('Drinks', 'Drinks'),
        ('Food', 'Food'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    text = RichTextField()
    photo = models.ImageField(upload_to='photos/blogs/%Y/%m/%d/', null=True, blank=True)
    categories = MultiSelectField(choices=category_choice, max_length=255)
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['created_date']