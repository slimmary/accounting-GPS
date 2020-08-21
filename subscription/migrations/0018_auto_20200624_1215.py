# Generated by Django 2.2.4 on 2020-06-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0017_auto_20200622_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letters',
            old_name='old_rate',
            new_name='gps_rate',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.IntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Вартість грн/міс'),
        ),
    ]