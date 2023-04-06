from django.db import models
import uuid
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, blank=False, editable=False, primary_key=True)
    first_name = models.CharField(max_length=250, null=False, verbose_name = 'Имя')
    last_name = models.CharField(max_length=250, null=False, verbose_name = 'Фамилия')
    designation = models.CharField(max_length=250, null=False, verbose_name = 'Должность')
    photo = models.ImageField(upload_to='photo/account/%Y/%m/%d', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    text_feedback = models.CharField(max_length=500, null=False, verbose_name = 'Отзыв')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'