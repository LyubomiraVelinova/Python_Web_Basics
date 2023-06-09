# Generated by Django 4.2.2 on 2023-06-30 12:08

from django.db import migrations, models
import forms_demos_part_2.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25, validators=[forms_demos_part_2.web.validators.validate_text])),
                ('priority', models.IntegerField(validators=[forms_demos_part_2.web.validators.ValueInRangeValidator(1, 10)])),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
