# Generated by Django 2.2.13 on 2021-03-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210303_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gps',
            name='rate_client_1',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='rate_client_2',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='sim_1',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='sim_2',
        ),
        migrations.AddField(
            model_name='gps',
            name='rate_client',
            field=models.CharField(blank=True, default='Власна сім', help_text='Тариф заповниться автоматично нічого не потрібно вводити', max_length=100, null=True, verbose_name='Тариф'),
        ),
        migrations.AddField(
            model_name='gps',
            name='sim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gps_sim', to='products.Sim', verbose_name='Сім-картки'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='operator',
            field=models.CharField(choices=[('Київстар', 'Київстар'), ('Лайфсел', 'Лайфсел'), ('Тревел-сім', 'Тревел-сім'), ('Гудлайн', 'Гудлайн')], default='Київстар', help_text='Оберіть оператора', max_length=100, verbose_name='Оператор'),
        ),
    ]
