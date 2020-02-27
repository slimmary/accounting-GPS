# Generated by Django 2.2.4 on 2020-02-27 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0007_auto_20200227_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(choices=[('1', 'Абонплата'), ('2', 'Поставки'), ('3', 'Обслуговування')], help_text='Оберіть вид договору', max_length=1)),
                ('provider', models.CharField(choices=[('1', 'Абонплата'), ('2', 'Поставки'), ('3', 'Обслуговування')], help_text='Оберіть вид договору', max_length=1)),
                ('number', models.IntegerField(help_text='Введіть номер договору')),
                ('contract_date', models.DateField(help_text='Дата заключеня договору')),
                ('status', models.CharField(choices=[('1', 'Абонплата'), ('2', 'Поставки'), ('3', 'Обслуговування')], help_text='Оберіть статус договору', max_length=1)),
                ('status_date', models.DateField(help_text='Дата статусу(створення/відправки/отримання)', null=True)),
                ('contract_image', models.ImageField(blank=True, upload_to='images/contracts', verbose_name='Скан-копія')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='clients.Client')),
            ],
        ),
    ]
