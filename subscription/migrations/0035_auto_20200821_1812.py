# Generated by Django 2.2.13 on 2020-08-21 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0034_auto_20200821_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letters',
            name='gps',
            field=models.ForeignKey(default=None, help_text='Оберіть реєстратор для зміни', on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='products.Gps', verbose_name='БР'),
        ),
    ]