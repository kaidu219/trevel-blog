# Generated by Django 4.1.6 on 2023-04-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_alter_tours_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/countries/%Y/%m/%d/'),
        ),
    ]
