# Generated by Django 2.2.13 on 2020-08-28 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_auto_20200828_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='sim_1',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gps_1', to='products.Sim', verbose_name='Сім_1'),
        ),
        migrations.AlterField(
            model_name='gps',
            name='sim_2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gps_2', to='products.Sim', verbose_name='Сім_2'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='operator',
            field=models.CharField(choices=[('Київстар', 'Київстар'), ('Лайфсел', 'Лайфсел'), ('Тревел-сім', 'Тревел-сім')], default='Київстар', help_text='Оберіть оператора', max_length=100, verbose_name='Оператор'),
        ),
    ]
