# Generated by Django 2.2.20 on 2021-04-24 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20210423_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateField(default=datetime.date(2021, 4, 24), verbose_name='Дата створення проекту'),
        ),
    ]
