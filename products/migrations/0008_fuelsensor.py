# Generated by Django 2.2.4 on 2020-03-20 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200320_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=128, verbose_name='Серія')),
                ('number', models.PositiveIntegerField(help_text='Введіть номер', verbose_name='Номер')),
                ('date_manufacturing', models.DateField(blank=True, help_text='Оберіть дату', verbose_name='Дата виробництва')),
                ('gps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuel_sensor', to='products.Gps', verbose_name='ДУТ')),
            ],
        ),
    ]