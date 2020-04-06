# Generated by Django 2.2.4 on 2020-04-06 19:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20200406_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='date_given',
            field=models.DateField(blank=True, help_text='Оберіть дату', null=True, verbose_name='Дата видачі монтажнику сім'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='date_receive',
            field=models.DateField(help_text='Оберіть дату', null=True, verbose_name='Дата отримання'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='number',
            field=models.CharField(help_text='Введіть номер, якщо сім клієнта введіть 8 нулів', max_length=11, validators=[django.core.validators.RegexValidator('^\\d{0,11}$')], verbose_name='Номер SIM'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='operator',
            field=models.CharField(choices=[('Київстар', 'Київстар'), ('Лайфсел', 'Лайфсел'), ('Тревел-сім', 'Тревел-сім'), ('Клієнтська сім', 'Клієнтська сім')], default='Київстар', help_text='Оберіть оператора', max_length=100, verbose_name='Оператор'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='rate_client',
            field=models.CharField(choices=[('Україна', 'Україна'), ('Світ', 'Світ'), ('Пауза', 'Пауза'), ('Власна сім', 'Власна сім')], default='Україна', help_text='Оберіть тариф для клієнта', max_length=100, verbose_name='Тариф'),
        ),
    ]
