# Generated by Django 2.2.13 on 2020-08-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_auto_20200826_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='IBAN',
            field=models.IntegerField(default=0, help_text='Введіть IBAN клієнта', max_length=29, null=True, verbose_name='IBAN'),
        ),
    ]