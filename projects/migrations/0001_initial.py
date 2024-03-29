# Generated by Django 2.2.13 on 2021-01-25 20:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoices', '0001_initial'),
        ('contracts', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, help_text='Номер проекту', null=True, verbose_name='№')),
                ('project_status', models.CharField(blank=True, choices=[('Завершено', 'Завершено'), ('НЕ завершено', 'НЕ завершено')], default='НЕ завершено', help_text='Оберіть статус проекту', max_length=100, verbose_name='Статус проекту')),
                ('date_start', models.DateField(default=datetime.date(2021, 1, 25), verbose_name='Дата створення проекту')),
                ('amount_gps', models.PositiveIntegerField(blank=True, default=0, help_text='введіть кількість', null=True, verbose_name='кіл-ть СКТ')),
                ('amount_fuel_sensor', models.PositiveIntegerField(blank=True, default=0, help_text='введіть кількість', null=True, verbose_name='кіл-ть ДВРП')),
                ('add_costs', models.PositiveIntegerField(blank=True, default=0, help_text='введіть суму', null=True, verbose_name='дод. витрати грн')),
                ('sum', models.PositiveIntegerField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='загальна сума проекту')),
                ('date_receipt_contract', models.DateField(blank=True, help_text='Введіть дату', null=True, verbose_name='Дата отримання договору')),
                ('date_receipt_sale_invoice', models.DateField(blank=True, help_text='Введіть дату', null=True, verbose_name='Дата отримання видаткової накладної')),
                ('execution_status', models.CharField(blank=True, choices=[('Виконано', 'Виконано'), ('НЕ виконано', 'НЕ виконано'), ('Частково виконано', 'Частково виконано')], default='НЕ виконано', help_text='Оберіть статус', max_length=100, verbose_name='Статус виконання робіт')),
                ('notes', models.CharField(blank=True, max_length=100, verbose_name='Приміки')),
                ('additions', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_to_additions', to='contracts.Additions', verbose_name='ДУ до даного проекту')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='clients.Client', verbose_name='клієнт')),
                ('contract', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_to_contract', to='contracts.Contract', verbose_name='Договір до даного проекту')),
                ('invoice', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_invoice', to='invoices.ProjectInvoice', verbose_name='РФ/КО')),
            ],
            options={
                'verbose_name_plural': 'Проекти',
            },
        ),
    ]
