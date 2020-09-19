# Generated by Django 2.2.13 on 2020-08-21 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0033_auto_20200821_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letters',
            name='client',
            field=models.ForeignKey(blank=True, help_text='Оберіть клієнта від якого реєструється звернення', max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Client', verbose_name='Покупець/Абонент'),
        ),
        migrations.AlterField(
            model_name='letters',
            name='gps',
            field=models.ForeignKey(default=None, help_text='Оберіть реєстратор для зміни', limit_choices_to={'owner': models.ForeignKey(blank=True, help_text='Оберіть клієнта від якого реєструється звернення', max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Client', verbose_name='Покупець/Абонент')}, on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='products.Gps', verbose_name='БР'),
        ),
    ]