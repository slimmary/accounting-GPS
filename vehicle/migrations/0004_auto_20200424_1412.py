# Generated by Django 2.2.4 on 2020-04-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20200311_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(blank=True, choices=[('1', 'Тягач'), ('2', 'Легкове авто'), ('3', 'Мікроавтобус'), ('4', 'Екскаватор'), ('5', 'Навантажувач'), ('6', 'Трактор'), ('7', 'Оприскувач'), ('8', 'Комбайн'), ('9', 'Асфальтоукладник'), ('10', 'Фреза'), ('11', 'Каток'), ('12', 'Інше')], help_text='Оберіть тип Транспортного Засобу', max_length=1, verbose_name='Тип ТЗ'),
        ),
    ]
