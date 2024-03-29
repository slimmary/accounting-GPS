# Generated by Django 2.2.13 on 2021-04-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20210304_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientproxypayment',
            options={'verbose_name_plural': 'Клієнт зведені дані'},
        ),
        migrations.AlterField(
            model_name='client',
            name='provider',
            field=models.CharField(choices=[('ТОВ "Системи Контролю Транспорту"', 'ТОВ "Системи Контролю Транспорту"'), ('ФОП Шевчук С.І.', 'ФОП Шевчук С.І.'), ('ФОП Дячук Л.В.', 'ФОП Демченко К.В.'), ('ФОП Демченко К.В.', 'ФОП Дячук Л.В.'), ('БК/ІНШЕ', 'БК/ІНШЕ')], default='БК/ІНШЕ', help_text='Оберіть постачальника з абонплати', max_length=100, null=True, verbose_name='Постачальник з АП'),
        ),
    ]
