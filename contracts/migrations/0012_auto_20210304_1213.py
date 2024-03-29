# Generated by Django 2.2.13 on 2021-03-04 12:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0011_auto_20210303_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additions',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 3, 4), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts_all', to='clients.Client', verbose_name='Покупець/Абонент'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(default=datetime.date(2021, 3, 4), help_text='Оберіть дату', verbose_name='Дата заключеня'),
        ),
    ]
