# Generated by Django 2.2.13 on 2021-02-25 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0007_auto_20210205_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additions',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 2, 25), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 2, 25), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
    ]
