# Generated by Django 2.2.13 on 2020-08-27 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20200827_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='notification_contact_1',
            field=models.ForeignKey(blank=True, default=None, help_text='Оберіть контактну особу яку повідомлятимуть по рахунках', on_delete=django.db.models.deletion.CASCADE, related_name='client_notification_field_1', to='clients.ContactProfile', verbose_name='Контактна особи для повідомлень'),
        ),
    ]