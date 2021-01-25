# Generated by Django 2.2.13 on 2021-01-25 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_init', models.DateField(auto_now_add=True, help_text='Дата заповниться автоматично', null=True, verbose_name='Дата створення')),
                ('year', models.CharField(blank=True, help_text='Заповниться автоматично', max_length=10, null=True, verbose_name='Рік')),
                ('quarter', models.CharField(choices=[('Перший', 'Перший'), ('Другий', 'Другий'), ('Третій', 'Третій'), ('Четвертий', 'Четвертий')], default='Перший', max_length=100, verbose_name='Квартал')),
                ('price_quarter', models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='нараховано')),
                ('sum_payment', models.PositiveIntegerField(blank=True, default=0, help_text='Введть суму, що сплатив клієнт', null=True, verbose_name='сплачено')),
                ('sum_to_pay', models.IntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='залишок')),
                ('status', models.CharField(blank=True, choices=[('Сплачено', 'Сплачено'), ('НЕ сплачено', 'НЕ сплачено'), ('Частково сплачено', 'Частково сплачено')], default='НЕ сплачено', help_text='Оберіть статус оплати', max_length=100, verbose_name='Статус оплати')),
                ('date_payment', models.DateField(blank=True, help_text='Заповниться автоматично', null=True, verbose_name='Дата оплати')),
                ('activation', models.BooleanField(default=False, verbose_name='активація')),
                ('activation_sum', models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Сума активації')),
                ('rate_ua_1m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='1 міс - Укр')),
                ('rate_world_1m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='1 міс - Св')),
                ('rate_pause_1m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='1 міс - П')),
                ('rate_own_sim_1m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='1 міс - ВС')),
                ('all_1m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='1 міс - БР')),
                ('rate_ua_2m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='2 міс - Укр')),
                ('rate_world_2m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='2 міс - Св')),
                ('rate_pause_2m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='2 міс - П')),
                ('rate_own_sim_2m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='2 міс - ВС')),
                ('all_2m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='2 міс - БР')),
                ('rate_ua_3m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='3 міс - Укр')),
                ('rate_world_3m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='3 міс - Св')),
                ('rate_pause_3m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='3 міс - П')),
                ('rate_own_sim_3m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='3 міс - ВС')),
                ('all_3m', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='3 міс - БР')),
                ('price_1m', models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн/1 міс')),
                ('price_2m', models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн/2 міс')),
                ('price_3m', models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн/3 міс')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='clients.Client', verbose_name='Платник')),
            ],
            options={
                'verbose_name_plural': 'АП звітність ',
            },
        ),
        migrations.CreateModel(
            name='Letters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_letter', models.DateField(help_text='Оберіть дату', null=True, verbose_name='Дата листа')),
                ('action', models.CharField(choices=[('Видалення', 'Видалення'), ('Зміна тарифу', 'Зміна тарифу')], help_text='Оберіть дію', max_length=100, verbose_name='Дія')),
                ('gps_rate', models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='з тарифу')),
                ('new_rate', models.CharField(blank=True, choices=[('Україна', 'Україна'), ('Світ', 'Світ'), ('Україна+Світ', 'Україна+Світ'), ('Пауза', 'Пауза'), ('Власна сім', 'Власна сім')], help_text='Оберіть тариф на який змінюється', max_length=100, null=True, verbose_name='на тариф')),
                ('client', models.ForeignKey(blank=True, help_text='Оберіть клієнта від якого реєструється звернення', max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='clients.Client', verbose_name='Покупець/Абонент')),
                ('gps', models.ForeignKey(default=None, help_text='Оберіть реєстратор для зміни', on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='products.Gps', verbose_name='БР')),
            ],
            options={
                'verbose_name_plural': 'Звернення/листи',
            },
        ),
    ]
