# Generated by Django 2.2.20 on 2021-05-12 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0029_auto_20210429_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceplan',
            name='date_create',
            field=models.DateField(default=datetime.date(2021, 5, 12), help_text='Введіть дату', verbose_name='Дата'),
        ),
    ]
