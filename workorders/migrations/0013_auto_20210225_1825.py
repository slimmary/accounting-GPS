# Generated by Django 2.2.13 on 2021-02-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0012_auto_20210225_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='month_executor_pay',
            field=models.DateField(blank=True, help_text='місяць нарахування ЗП монтажнику', null=True, verbose_name='місяць/рік ЗП'),
        ),
    ]
