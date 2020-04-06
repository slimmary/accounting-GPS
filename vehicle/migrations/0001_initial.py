# Generated by Django 2.2.4 on 2020-02-28 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_auto_20200228_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Тягач'), ('2', 'Легкове авто'), ('3', 'Мікроавтобус'), ('4', 'Екскаватор'), ('5', 'Навантажувач'), ('6', 'Трактор'), ('7', 'Оприскувач'), ('8', 'Комбайн'), ('9', 'Асфальтоукладник'), ('10', 'Фреза'), ('11', 'Каток'), ('12', 'Інше')], help_text='Оберіть тип Транспортного Засобу', max_length=1, verbose_name='Тип ТЗ')),
                ('make', models.CharField(max_length=50, verbose_name='Марка')),
                ('model', models.CharField(blank=True, max_length=50, verbose_name='Модель')),
                ('number', models.CharField(max_length=50, verbose_name=' Ідентефікатор (держ.номер)')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='clients.Client', verbose_name='Власник')),
            ],
            options={
                'verbose_name_plural': 'транспортні засоби',
            },
        ),
    ]