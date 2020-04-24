# Generated by Django 2.2.4 on 2020-04-24 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20200424_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='vehicle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gps', to='vehicle.Vehicle', verbose_name='Транспортний засіб'),
        ),
    ]
