# Generated by Django 2.2.13 on 2021-01-26 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210126_1247'),
        ('workorders', '0002_auto_20210125_2056'),
        ('invoices', '0002_subinvoice_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='work_order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_workorder', to='workorders.WorkOrder', verbose_name='ЗН'),
        ),
        migrations.AddField(
            model_name='projectinvoice',
            name='project_to',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_invoice', to='projects.Project', verbose_name='РФ/КО'),
        ),
    ]
