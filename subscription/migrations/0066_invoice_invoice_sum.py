# Generated by Django 2.2.13 on 2020-10-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0065_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_sum',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Введіть суму рахунку', null=True, verbose_name='сума рахунку грн'),
        ),
    ]
