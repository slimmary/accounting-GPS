# Generated by Django 2.2.13 on 2021-04-17 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0012_auto_20210304_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additions',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 4, 17), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 4, 17), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
    ]
