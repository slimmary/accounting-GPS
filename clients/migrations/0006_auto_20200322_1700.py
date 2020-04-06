# Generated by Django 2.2.4 on 2020-03-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='provider',
            field=models.CharField(choices=[('ТОВ "Системи Контролю Транспорту"', 'ТОВ "Системи Контролю Транспорту"'), ('ФОП Шевчук С.І.', 'ФОП Шевчук С.І.'), ('ФОП Дячук Л.В.', 'ФОП Дячук Л.В.'), ('БК/ІНШЕ', 'БК/ІНШЕ')], default='ФОП Шевчук С.І.', help_text='Оберіть постачальника з абонплати', max_length=100, null=True, verbose_name='Постачальник з абонплати'),
        ),
    ]