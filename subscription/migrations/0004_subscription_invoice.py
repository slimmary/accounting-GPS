# Generated by Django 2.2.20 on 2021-08-09 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_remove_subinvoice_subscription'),
        ('subscription', '0003_letters_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='invoices.SubInvoice', verbose_name='РФ'),
        ),
    ]
