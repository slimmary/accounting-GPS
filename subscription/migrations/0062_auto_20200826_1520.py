# Generated by Django 2.2.13 on 2020-08-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0061_auto_20200826_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='date_payment',
            field=models.DateField(blank=True, help_text='Заповниться автоматично', null=True, verbose_name='Дата оплати'),
        ),
    ]