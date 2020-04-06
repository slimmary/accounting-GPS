# Generated by Django 2.2.4 on 2020-04-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200401_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='sim',
            name='rate_price',
            field=models.CharField(help_text='Змініть вартість', max_length=100, null=True, verbose_name='Вартість'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='rate_sim',
            field=models.FloatField(blank=True, help_text='Введіть суму', max_length=5, null=True, verbose_name='Тариф оператора грн/міс'),
        ),
    ]