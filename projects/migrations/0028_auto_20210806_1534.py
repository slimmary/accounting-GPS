# Generated by Django 2.2.20 on 2021-08-06 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20210805_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateField(default=datetime.date(2021, 8, 6), verbose_name='Дата створення проекту'),
        ),
    ]
