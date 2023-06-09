# Generated by Django 4.2.1 on 2023-06-28 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_remove_department_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
