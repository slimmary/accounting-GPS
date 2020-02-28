# Generated by Django 2.2.4 on 2020-02-28 16:58

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientPostAddress',
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
                ('position', models.CharField(max_length=50, verbose_name='Посада')),
                ('phone', phone_field.models.PhoneField(max_length=31, null=True, verbose_name='Контактний номер телефону')),
                ('phone_2', phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='додатковий контактний номер телефону')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Контактна електронна адреса')),
            ],
            options={
                'verbose_name_plural': 'Контактні особи клієнтів',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_form', models.CharField(choices=[('1', 'Безнал'), ('2', 'Нал'), ('3', 'БК'), ('4', 'Безнал/Нал'), ('5', 'Безнал/БК')], help_text='Оберіть форму оплати', max_length=1, verbose_name='форма оплати')),
                ('name', models.CharField(max_length=128, verbose_name='Назва')),
                ('login', models.CharField(max_length=128, verbose_name="Ім'я користувача")),
                ('status', models.CharField(choices=[('1', 'активний'), ('2', 'видалений')], help_text='Оберіть статус клієнта', max_length=1, null=True, verbose_name='Статус')),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='clients.ClientPostAddress', verbose_name='Поштова адреса')),
                ('contacts', models.ManyToManyField(related_name='client_field', to='clients.ContactProfile', verbose_name='Контактні особи')),
            ],
            options={
                'verbose_name_plural': 'Клієнти',
            },
        ),
    ]
