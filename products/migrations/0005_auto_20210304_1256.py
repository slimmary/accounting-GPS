# Generated by Django 2.2.13 on 2021-03-04 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210304_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gps',
            name='sim',
        ),
        migrations.AddField(
            model_name='gps',
            name='sim_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gps_sim_1', to='products.Sim', verbose_name='Сім 1'),
        ),
        migrations.AddField(
            model_name='gps',
            name='sim_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gps_sim_2', to='products.Sim', verbose_name='Сім 2'),
        ),
    ]
