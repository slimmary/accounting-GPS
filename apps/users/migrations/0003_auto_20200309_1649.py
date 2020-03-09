# Generated by Django 2.2.4 on 2020-03-09 16:49

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200228_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Електронна адреса'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_2',
            field=phone_field.models.PhoneField(max_length=31, null=True, verbose_name='Власний номер телефону співробітника'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, null=True, verbose_name='Робочий номер телефону співробітника'),
        ),
    ]
