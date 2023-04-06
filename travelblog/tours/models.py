from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.

class Country(models.Model):

    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class Nearby(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Nearby'
        verbose_name_plural = 'Nearbies'

class Tours(models.Model):

    id = models.UUIDField(default=uuid.uuid4, blank=False, editable=False, primary_key=True)
    tour_name = models.CharField(max_length=255, verbose_name='Название тура')
    price = models.IntegerField(verbose_name='Стоимость тура')
    duration_tour = models.IntegerField(default=1, verbose_name='Длительность тура')
    city = models.CharField(max_length=255, verbose_name='Город')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
    hotel = models.CharField(max_length=255, verbose_name='Название отеля')
    numb_seats_room = models.IntegerField(verbose_name='Количество мест в номере')
    numb_bath_room = models.IntegerField(verbose_name='Количество ванн в номере')
    nearby = models.ForeignKey(Nearby, on_delete=models.CASCADE, null=True, blank=True, max_length=255, verbose_name='Поблизости есть: ')
    main_photo = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', null=True, blank=True, verbose_name='Главное фото')
    description = RichTextField(blank=True, null=True, verbose_name='Описание тура')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление тура', editable=False)
    start_date = models.DateField(verbose_name='Дата начала тура', blank=True)


    def __str__(self) -> str:
        return self.tour_name
    
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
