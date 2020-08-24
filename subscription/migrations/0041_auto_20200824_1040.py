# Generated by Django 2.2.13 on 2020-08-24 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0040_auto_20200824_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letters',
            name='date_letter',
            field=models.DateField(blank=True, help_text='Оберіть дату', null=True, verbose_name='Дата листа'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date_init',
            field=models.DateField(blank=True, default=datetime.date.today, help_text='Оберіть дату', null=True, verbose_name='Дата створення'),
        ),
    ]
