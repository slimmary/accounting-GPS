# Generated by Django 2.2.20 on 2021-04-22 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0015_auto_20210421_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additions',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 4, 22), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 4, 22), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
    ]
