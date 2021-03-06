# Generated by Django 2.2.13 on 2021-01-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_auto_20210123_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additions',
            name='status',
            field=models.CharField(choices=[('Створений', 'Створений'), ('Відправлений укрпоштою', 'Відправлений укрпоштою'), ('Відправлений НП', 'Відправлений НП'), ('Відправлений на електронну пошту', 'Відправлений на електронну пошту'), ('В наявності', 'В наявності')], default='Створений', help_text='Оберіть статус договору', max_length=100, verbose_name='Статус'),
        ),
    ]
