# Generated by Django 2.2.4 on 2020-06-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20200622_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='rate_price',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='Вартість грн/міс'),
        ),
    ]
