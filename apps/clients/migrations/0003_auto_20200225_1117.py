# Generated by Django 2.2.4 on 2020-02-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20200224_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpostaddress',
            name='district',
            field=models.CharField(blank=True, help_text='Район', max_length=50),
        ),
    ]
