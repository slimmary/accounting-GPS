# Generated by Django 2.2.4 on 2020-03-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_sim_rate_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sim',
            name='rate',
            field=models.FloatField(blank=True, help_text='Введіть суму', max_length=5, null=True, verbose_name='Тариф грн/міс'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='packet_volume',
            field=models.PositiveIntegerField(blank=True, help_text='Введіть кількість', null=True, verbose_name="Об'єм пакетних даних Мб/міс"),
        ),
        migrations.AlterField(
            model_name='sim',
            name='rate_client',
            field=models.CharField(choices=[('Україна', 'Україна'), ('Світ', 'Світ'), ('Пауза', 'Пауза'), ('Власна сім', 'Власна сім')], default=models.FloatField(blank=True, help_text='Введіть суму', max_length=5, null=True, verbose_name='Тариф грн/міс'), help_text='Оберіть тариф для клієнта', max_length=100, verbose_name='Тариф'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='rate_volume',
            field=models.FloatField(blank=True, help_text='Введіть суму', max_length=5, null=True, verbose_name='Тариф за 1Мб поза пакетом'),
        ),
    ]