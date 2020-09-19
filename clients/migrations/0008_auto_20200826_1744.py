# Generated by Django 2.2.13 on 2020-08-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20200424_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='IBAN',
            field=models.PositiveIntegerField(default=0, help_text='Введіть IBAN клієнта', max_length=29, null=True, verbose_name='IBAN'),
        ),
        migrations.AddField(
            model_name='client',
            name='IPN',
            field=models.PositiveIntegerField(default=0, help_text='Введіть ІПН клієнта', max_length=12, null=True, verbose_name='ІПН'),
        ),
        migrations.AddField(
            model_name='client',
            name='director',
            field=models.CharField(blank=True, help_text='Введіть ПІП директора', max_length=100, null=True, verbose_name='Директор'),
        ),
        migrations.AddField(
            model_name='client',
            name='edrpou',
            field=models.PositiveIntegerField(default=0, help_text='Введіть ЄДРПОУ клієнта', max_length=8, null=True, verbose_name='ЄДРПОУ'),
        ),
        migrations.AlterField(
            model_name='client',
            name='provider',
            field=models.CharField(choices=[('ТОВ "Системи Контролю Транспорту"', 'ТОВ "Системи Контролю Транспорту"'), ('ФОП Шевчук С.І.', 'ФОП Шевчук С.І.'), ('ФОП Дячук Л.В.', 'ФОП Демченко К.В.'), ('ФОП Демченко К.В.', 'ФОП Дячук Л.В.'), ('БК/ІНШЕ', 'БК/ІНШЕ')], default='ФОП Шевчук С.І.', help_text='Оберіть постачальника з абонплати', max_length=100, null=True, verbose_name='Постачальник з абонплати'),
        ),
    ]