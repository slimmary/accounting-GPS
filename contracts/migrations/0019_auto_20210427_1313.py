# Generated by Django 2.2.20 on 2021-04-27 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0018_auto_20210424_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additions',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 4, 27), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 4, 27), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
    ]
