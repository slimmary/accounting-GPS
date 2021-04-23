# Generated by Django 2.2.20 on 2021-04-20 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0019_auto_20210417_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrderProxy',
            fields=[
            ],
            options={
                'verbose_name_plural': 'зведені дані сервісного відділу',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('workorders.workorder',),
        ),
        migrations.AddField(
            model_name='workorder',
            name='trip_day',
            field=models.FloatField(blank=True, default=0, help_text='Кількість днів нарахування добових монтажнику', null=True, verbose_name='Добові дні'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='trip_day_costs_executor',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Сума коомпенсації монтажнику\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн добових \nмонтажнику'),
        ),
        migrations.AlterField(
            model_name='serviceplan',
            name='date_create',
            field=models.DateField(default=datetime.date(2021, 4, 20), help_text='Введіть дату', verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='add_costs_client',
            field=models.IntegerField(blank=True, help_text='Вартість додаткових витрат для клієнта', null=True, verbose_name='грн за ДВ \nклієнту'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='milege_price_client',
            field=models.IntegerField(blank=True, help_text='Вартість пробігу для клієнта\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за км клієнту'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='type_of_work',
            field=models.CharField(choices=[('Проект', 'Проект'), ('Сервіс', 'Сервіс')], default='Сервіс', help_text='Оберіть тип', max_length=100, verbose_name='Тип ЗН'),
        ),
    ]
