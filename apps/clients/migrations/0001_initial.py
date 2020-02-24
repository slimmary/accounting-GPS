# Generated by Django 2.2.4 on 2020-02-13 15:43

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
                ('pay_form', models.CharField(choices=[('1', 'Безнал'), ('2', 'Нал'), ('3', 'БК'), ('4', 'Безнал/Нал'), ('5', 'Безнал/БК')], help_text='Оберіть форму оплати', max_length=1)),
                ('name', models.CharField(max_length=128)),
                ('login', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ContactProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='Прізвище', max_length=50)),
                ('surname', models.CharField(help_text="І'мя", max_length=50)),
                ('patronymic', models.CharField(help_text='По батькові', max_length=50)),
                ('position', models.CharField(help_text='Посада', max_length=50)),
                ('client_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(help_text='Контактний номер телефону', max_length=31)),
                ('contact_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='clients.ContactProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Контактна електронна адреса', max_length=254)),
                ('contact_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='clients.ContactProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ClientPostAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(help_text='Пштовий індекс')),
                ('region', models.CharField(help_text='Область', max_length=50)),
                ('district', models.CharField(help_text='Район', max_length=50)),
                ('city', models.CharField(help_text='Місто', max_length=50)),
                ('street', models.CharField(help_text='Вулиця', max_length=200)),
                ('house', models.CharField(help_text='Номер будинку', max_length=50)),
                ('office', models.CharField(help_text='Номер офісу або квартири', max_length=50)),
                ('client_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adress', to='clients.Client')),
            ],
        ),
    ]
