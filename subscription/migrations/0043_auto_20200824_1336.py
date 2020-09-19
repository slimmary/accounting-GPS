# Generated by Django 2.2.13 on 2020-08-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0042_auto_20200824_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='price',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='rate_own_sim',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='rate_pause',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='rate_ua',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='rate_ua_world',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='rate_world',
        ),
        migrations.AddField(
            model_name='subscription',
            name='all_1m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='жовтень - Всього'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='all_2m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='листопад - Всього'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='all_3m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='грудень - Всього'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price_1m',
            field=models.IntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Вартість грн/жовтень'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price_2m',
            field=models.IntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Вартість грн/листопад'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price_3m',
            field=models.IntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Вартість грн/грудень'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price_quarter',
            field=models.IntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Вартість грн/квартал'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_own_sim_1m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='жовтень - Власна Сім'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_own_sim_2m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='листопад - Власна Сім'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_own_sim_3m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='грудень - Власна Сім'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_pause_1m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='жовтень - Пауза'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_pause_2m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='листопад - Пауза'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_pause_3m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='грудень - Пауза'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_ua_1m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='жовтень - Ураїна'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_ua_2m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='листопад - Ураїна'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_ua_3m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='грудень - Ураїна'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_ua_world_1m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='жовтень - Україна+Світ'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_ua_world_2m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='листопад - Україна+Світ'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_ua_world_3m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='грудень - Україна+Світ'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_world_1m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='жовтень - Світ'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_world_2m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='листопад - Світ'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate_world_3m',
            field=models.CharField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', max_length=100, null=True, verbose_name='грудень - Світ'),
        ),
    ]