# Generated by Django 4.2.1 on 2023-06-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_employee_business_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='business_account',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
