# Generated by Django 2.2.13 on 2021-01-23 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_auto_20210123_1749'),
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, help_text='Номер РФ', null=True, verbose_name='№')),
                ('date', models.DateField(help_text='Оберіть дату', null=True, verbose_name='Дата створення')),
                ('invoice_sum', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='сума до сплати')),
                ('status_payment', models.CharField(blank=True, choices=[('Сплачено', 'Сплачено'), ('НЕ сплачено', 'НЕ сплачено'), ('Частково сплачено', 'Частково сплачено')], default='НЕ сплачено', help_text='Оберіть статус оплати', max_length=100, verbose_name='Статус оплати')),
                ('sum_payment', models.PositiveIntegerField(blank=True, default=0, help_text='Ведіть суму, якщо оплата часткова', null=True, verbose_name='сума оплати')),
                ('date_payment', models.DateField(blank=True, help_text='Заповниться автоматично', null=True, verbose_name='Дата оплати')),
                ('provider', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='Постачальник')),
                ('client', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='Клієнт')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_invoice', to='subscription.Subscription', verbose_name='АП')),
            ],
            options={
                'verbose_name_plural': 'АП рахунки фактури ',
            },
        ),
        migrations.CreateModel(
            name='ProjectInvoiceTaxfree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, help_text='Номер РФ', null=True, verbose_name='№')),
                ('date', models.DateField(help_text='Оберіть дату', null=True, verbose_name='Дата створення')),
                ('invoice_sum', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='сума до сплати')),
                ('status_payment', models.CharField(blank=True, choices=[('Сплачено', 'Сплачено'), ('НЕ сплачено', 'НЕ сплачено'), ('Частково сплачено', 'Частково сплачено')], default='НЕ сплачено', help_text='Оберіть статус оплати', max_length=100, verbose_name='Статус оплати')),
                ('sum_payment', models.PositiveIntegerField(blank=True, default=0, help_text='Ведіть суму, якщо оплата часткова', null=True, verbose_name='сума оплати')),
                ('date_payment', models.DateField(blank=True, help_text='Заповниться автоматично', null=True, verbose_name='Дата оплати')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_invoice_taxfree', to='projects.Project', verbose_name='Проект')),
            ],
            options={
                'verbose_name_plural': 'Касові Ордера (КО)',
            },
        ),
        migrations.CreateModel(
            name='ProjectInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, help_text='Номер РФ', null=True, verbose_name='№')),
                ('date', models.DateField(help_text='Оберіть дату', null=True, verbose_name='Дата створення')),
                ('invoice_sum', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='сума до сплати')),
                ('status_payment', models.CharField(blank=True, choices=[('Сплачено', 'Сплачено'), ('НЕ сплачено', 'НЕ сплачено'), ('Частково сплачено', 'Частково сплачено')], default='НЕ сплачено', help_text='Оберіть статус оплати', max_length=100, verbose_name='Статус оплати')),
                ('sum_payment', models.PositiveIntegerField(blank=True, default=0, help_text='Ведіть суму, якщо оплата часткова', null=True, verbose_name='сума оплати')),
                ('date_payment', models.DateField(blank=True, help_text='Заповниться автоматично', null=True, verbose_name='Дата оплати')),
                ('provider', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='Постачальник')),
                ('client', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='Клієнт')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_invoice', to='projects.Project', verbose_name='Проект')),
            ],
            options={
                'verbose_name_plural': 'Проекти рахунки фактури ',
            },
        ),
    ]
