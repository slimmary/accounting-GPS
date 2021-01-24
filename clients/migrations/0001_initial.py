# Generated by Django 2.2.13 on 2021-01-23 21:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_start', models.DateField(help_text='Оберіть дату', null=True, verbose_name='Дата початку роботи')),
                ('name', models.CharField(max_length=128, verbose_name='Назва клієнта')),
                ('login', models.CharField(max_length=128, verbose_name="Ім'я користувача (login)")),
                ('status', models.CharField(choices=[('1', 'активний'), ('2', 'видалений')], default='активний', help_text='Оберіть статус клієнта', max_length=1, null=True, verbose_name='Статус')),
                ('edrpou', models.CharField(default=12345678, help_text='Введіть ЄДРПОУ клієнта', max_length=8, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,10}$'), django.core.validators.MinLengthValidator(8)], verbose_name='ЄДРПОУ')),
                ('provider', models.CharField(choices=[('ТОВ "Системи Контролю Транспорту"', 'ТОВ "Системи Контролю Транспорту"'), ('ФОП Шевчук С.І.', 'ФОП Шевчук С.І.'), ('ФОП Дячук Л.В.', 'ФОП Демченко К.В.'), ('ФОП Демченко К.В.', 'ФОП Дячук Л.В.'), ('БК/ІНШЕ', 'БК/ІНШЕ')], default='ФОП Шевчук С.І.', help_text='Оберіть постачальника з абонплати', max_length=100, null=True, verbose_name='Постачальник з АП')),
                ('type_notification_1', models.CharField(choices=[('SMS', 'SMS'), ('VIBER', 'VIBER'), ('Email', 'Email'), ('M.E.D.O.C.', 'M.E.D.O.C.'), ('Дзвінок', 'Дзвінок')], default='M.E.D.O.C.', help_text='Оберіть спосіб повідомлення клієнта по рахунках', max_length=100, null=True, verbose_name='Тип повідомлень 1')),
                ('type_notification_2', models.CharField(blank=True, choices=[('SMS', 'SMS'), ('VIBER', 'VIBER'), ('Email', 'Email'), ('M.E.D.O.C.', 'M.E.D.O.C.'), ('Дзвінок', 'Дзвінок')], help_text='Оберіть спосіб повідомлення клієнта по рахунках', max_length=100, null=True, verbose_name='Тип повідомлень 2')),
            ],
            options={
                'verbose_name_plural': 'Клієнти',
            },
        ),
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(verbose_name='Пштовий індекс')),
                ('region', models.CharField(max_length=50, verbose_name='Область')),
                ('district', models.CharField(blank=True, max_length=50, verbose_name='Район')),
                ('city', models.CharField(max_length=50, verbose_name='Місто')),
                ('street', models.CharField(max_length=200, verbose_name='Вулиця')),
                ('house', models.CharField(max_length=50, verbose_name='Номер будинку')),
                ('office', models.CharField(max_length=50, verbose_name='Номер офісу або квартири')),
            ],
            options={
                'verbose_name_plural': 'Поштові адреси',
            },
        ),
        migrations.CreateModel(
            name='ContactProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Прізвище')),
                ('surname', models.CharField(max_length=50, verbose_name="І'мя")),
                ('patronymic', models.CharField(max_length=50, verbose_name='По батькові')),
                ('position', models.CharField(default='менеджер', max_length=50, verbose_name='Посада')),
                ('phone', phone_field.models.PhoneField(max_length=31, null=True, verbose_name='№ телефону')),
                ('phone_2', phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='додатковий № телефону')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='електронна адреса')),
            ],
            options={
                'verbose_name_plural': 'Контактні особи клієнтів',
            },
        ),
        migrations.CreateModel(
            name='ClientLegalDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPN', models.CharField(blank=True, default=123456789012, help_text='Введіть ІПН клієнта', max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,100}$'), django.core.validators.MinLengthValidator(10)], verbose_name='ІПН')),
                ('director', models.CharField(blank=True, help_text='Введіть ПІП директора', max_length=100, null=True, verbose_name='Директор')),
                ('IBAN', models.CharField(blank=True, default=12345678912345678901234567890, help_text='Введіть IBAN клієнта', max_length=29, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,100}$'), django.core.validators.MinLengthValidator(29)], verbose_name='IBAN')),
                ('bank_account', models.CharField(blank=True, default=1234567890, help_text='Введіть р/р', max_length=20, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,100}$')], verbose_name='№ р/р')),
                ('MFO', models.CharField(blank=True, default=12345, help_text='Введіть IBAN клієнта', max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,100}$'), django.core.validators.MinLengthValidator(5)], verbose_name='IBAN')),
                ('bank', models.CharField(blank=True, help_text='Введіть назву банку', max_length=100, null=True, verbose_name='Банк>')),
                ('client', models.ForeignKey(blank=True, default=None, help_text='Оберіть клєнта якому належать ці реквізити', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_legal_detail', to='clients.Client', verbose_name='Клієнт')),
                ('legal_address', models.OneToOneField(blank=True, help_text='Оберіть юридичну адресу клієнта', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_legal_address', to='clients.ClientAddress', verbose_name='Юридична адреса')),
                ('post_address', models.OneToOneField(blank=True, help_text='Оберіть поштову адресу клієнта, якщо вона не співпадає з юридичною', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_post_address', to='clients.ClientAddress', verbose_name='Поштова адреса')),
            ],
            options={
                'verbose_name_plural': 'Реквізити клієнтів',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='contacts',
            field=models.ManyToManyField(related_name='client_field', to='clients.ContactProfile', verbose_name='Контактні особи'),
        ),
        migrations.AddField(
            model_name='client',
            name='notification_contact_1',
            field=models.ForeignKey(blank=True, default=None, help_text='Оберіть контактну особу яку повідомлятимуть по рахунках', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_notification_field_1', to='clients.ContactProfile', verbose_name='Контактна особи для повідомлень'),
        ),
        migrations.AddField(
            model_name='client',
            name='notification_contact_2',
            field=models.ForeignKey(blank=True, default=None, help_text='Оберіть контактну особу, яку повідомлятимуть по рахунках', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_notification_field_2', to='clients.ContactProfile', verbose_name='Контактна особи для повідомлень'),
        ),
    ]
