# Generated by Django 2.2.13 on 2021-03-03 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_auto_20210303_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinvoice',
            name='client',
            field=models.ForeignKey(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proj_invoice', to='clients.Client', verbose_name='Клієнт'),
        ),
    ]