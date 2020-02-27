# Generated by Django 2.2.4 on 2020-02-26 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthday', models.DateField(blank=True, help_text='Дата народження', null=True)),
                ('position', models.CharField(help_text='Посада', max_length=50)),
                ('avatar', models.ImageField(upload_to='images/users', verbose_name='Зображення')),
                ('date_start_work', models.DateField(blank=True, help_text='Дата прийому на роботу', null=True)),
                ('status', models.CharField(choices=[('1', 'на випробному терміні'), ('2', 'прийнятий')], help_text='Оберіть статус', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(help_text='Номер телефону співробітника', max_length=31)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='users.UserProfile')),
            ],
        ),
    ]