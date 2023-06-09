# Generated by Django 4.2.1 on 2023-06-06 19:16

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_location_alter_photo_pet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pet_image',
            field=models.ImageField(upload_to='mediafiles/photos', validators=[petstagram.photos.validators.image_size_validator]),
        ),
    ]
