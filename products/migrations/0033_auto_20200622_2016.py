# Generated by Django 2.2.4 on 2020-06-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20200622_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='rate_price',
            field=models.IntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Вартість грн/міс'),
        ),
    ]
