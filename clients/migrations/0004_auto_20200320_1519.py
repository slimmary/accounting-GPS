# Generated by Django 2.2.4 on 2020-03-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20200303_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Назва клієнта'),
        ),
    ]