# Generated by Django 4.2.1 on 2023-07-05 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0002_alter_petsagramuser_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PetsagramUser',
            new_name='PetstagramUser',
        ),
    ]
