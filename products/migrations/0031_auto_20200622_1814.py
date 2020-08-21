# Generated by Django 2.2.4 on 2020-06-22 18:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20200424_1449'),
        ('products', '0030_auto_20200424_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sim',
            name='rate_client',
        ),
        migrations.RemoveField(
            model_name='sim',
            name='rate_price',
        ),
        migrations.AddField(
            model_name='gps',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gps', to='clients.Client', verbose_name='Власник'),
        ),
        migrations.AddField(
            model_name='gps',
            name='rate_client',
            field=models.CharField(choices=[('Україна', 'Україна'), ('Світ', 'Світ'), ('Україна+Світ', 'Україна+Світ'), ('Пауза', 'Пауза'), ('Власна сім', 'Власна сім')], default='Україна', help_text='Оберіть тариф для клієнта', max_length=100, verbose_name='Тариф'),
        ),
        migrations.AddField(
            model_name='gps',
            name='rate_price',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='Вартість грн/міс'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='number',
            field=models.CharField(help_text='Введіть номер', max_length=11, validators=[django.core.validators.RegexValidator('^\\d{0,11}$')], verbose_name='Номер SIM'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='operator',
            field=models.CharField(choices=[('Київстар', 'Київстар'), ('Лайфсел', 'Лайфсел'), ('Тревел-сім', 'Тревел-сім')], default='Київстар', help_text='Оберіть оператора', max_length=100, verbose_name='Оператор'),
        ),
    ]
