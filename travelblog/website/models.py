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

class Tours(models.Model):
    country = (
        ('USA', 'USA'),
        ('IND','Indonesia'),
        ('IN','India'),
        ('RF','Russia'),
        ('GB','Great Britain'),
        ('KZ','Kazakhstan'),
        ('KG','Kyrgyzstan'),
        ('EG','Egypt'),
        ('KT','Katar'),
        ('TR','Turkey'),
        ('GR','Georgia'),
        ('SA','Saudi Arabia'),
        ('BZ','Brazil'),
    )
    near = (
        ('M', 'Mountains'),
        ('B', 'Beach'),
        ('S', 'Skiing'),
        ('SF','Safari')
    )


    id = models.UUIDField(default=uuid.uuid4, blank=False, editable=False, primary_key=True)
    tour_name = models.CharField(max_length=255, verbose_name='Название тура')
    price = models.IntegerField(verbose_name='Стоимость тура')
    duration_tour = models.IntegerField(default=1, verbose_name='Длительность тура')
    city = models.CharField(max_length=255, verbose_name='Город')
    country = models.CharField(choices=country, max_length=100, verbose_name='Страна')
    hotel = models.CharField(max_length=255, verbose_name='Название отеля')
    numb_seats_room = models.IntegerField(verbose_name='Количество мест в номере')
    numb_bath_room = models.IntegerField(verbose_name='Количество ванн в номере')
    nearby = MultiSelectField(choices = near, max_length=255, verbose_name='Поблизости есть: ')
    main_photo = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', null=True, blank=True, verbose_name='Главное фото')
    description = RichTextField(blank=True, null=True, verbose_name='Описание тура')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление тура', editable=False)
    start_date = models.DateField(verbose_name='Дата начала тура', blank=True)


    def __str__(self) -> str:
        return self.city + ' ' + self.country
    
    class Meta:
        ordering = ['created_date']
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours' 


class Tour_Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    tour_photo = models.ForeignKey(Tours, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to = 'photos/tour/tour_photos/%Y/%m/%d/')
    
    def __str__(self) -> str:
        return str(self.tour_photo)
        
    class Meta:
        verbose_name = 'Tour photo'
        verbose_name_plural = 'Tour photos'        




