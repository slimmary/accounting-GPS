# Generated by Django 2.2.4 on 2020-03-09 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractSupplementary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='Введіть номер', verbose_name='Номер ДУ')),
                ('date', models.DateField(help_text='Оберіть дату', verbose_name='Дата заключеня договору')),
                ('contract_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplementary', to='contracts.Contract', verbose_name='Додаткові угоди')),
            ],
        ),
    ]