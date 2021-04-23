# Generated by Django 2.2.20 on 2021-04-20 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0011_auto_20210417_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinvoice',
            name='project_to',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_invoice', to='projects.Project', verbose_name='Проект'),
        ),
    ]
