# Generated by Django 2.2.13 on 2020-08-25 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0058_auto_20200825_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='date_init',
            field=models.DateField(default=datetime.date(2020, 8, 25), help_text='Дата заповниться автоматично', null=True, verbose_name='Дата створення'),
        ),
    ]
