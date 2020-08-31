# Generated by Django 2.2.13 on 2020-08-31 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_auto_20200829_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='phone_email_contact_1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone_email_contact_2',
        ),
        migrations.AlterField(
            model_name='client',
            name='notification_contact_2',
            field=models.ForeignKey(blank=True, default=None, help_text='Оберіть контактну особу, яку повідомлятимуть по рахунках', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_notification_field_2', to='clients.ContactProfile', verbose_name='Контактна особи для повідомлень'),
        ),
        migrations.AlterField(
            model_name='client',
            name='type_notification_1',
            field=models.CharField(choices=[('SMS', 'SMS'), ('VIBER', 'VIBER'), ('Email', 'Email'), ('M.E.D.O.C.', 'M.E.D.O.C.'), ('Дзвінок', 'Дзвінок')], default='M.E.D.O.C.', help_text='Оберіть спосіб повідомлення клієнта по рахунках', max_length=100, null=True, verbose_name='Тип повідомлень 1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='type_notification_2',
            field=models.CharField(blank=True, choices=[('SMS', 'SMS'), ('VIBER', 'VIBER'), ('Email', 'Email'), ('M.E.D.O.C.', 'M.E.D.O.C.'), ('Дзвінок', 'Дзвінок')], help_text='Оберіть спосіб повідомлення клієнта по рахунках', max_length=100, null=True, verbose_name='Тип повідомлень 2'),
        ),
    ]
