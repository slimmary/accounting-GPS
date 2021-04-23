# Generated by Django 2.2.20 on 2021-04-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0024_auto_20210423_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executorpayment',
            name='milege_price_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Сума компенсації за пробіг монтажнику\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за км 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='milege_price_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Сума компенсації за пробіг монтажнику\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за км 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='milege_price_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Сума компенсації за пробіг монтажнику\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за км 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='premium_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума премії 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='premium_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума премії 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='premium_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума премії 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_payment_works_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='сума ЗП за роботи \nзаповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума ЗП 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_payment_works_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='сума ЗП за роботи \nзаповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума ЗП 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_payment_works_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='сума ЗП за роботи \nзаповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума ЗП 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_payment_works_sum',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='сума ЗП за роботи \nзаповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума ЗП сумарно'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_work_orders_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='к-ть ЗН 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_work_orders_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='к-ть ЗН 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_work_orders_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='к-ть ЗН 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_works_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість виконаних робіт співробітником заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='к-ть вик. робіт 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_works_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість виконаних робіт співробітником заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='к-ть вик. робіт 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='qua_works_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість виконаних робіт співробітником заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='к-ть вик. робіт 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='total_payment_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='загальна сума ЗП 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='total_payment_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='загальна сума ЗП 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='total_payment_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='загальна сума ЗП 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='trip_day_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість днів на які нараховано добові\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='добові 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='trip_day_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість днів на які нараховано добові\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='добові 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='trip_day_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість днів на які нараховано добові\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='добові 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість робочих днів(окрім вихідних)\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='роб.д. 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість робочих днів(окрім вихідних)\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='р.д. 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_3',
            field=models.PositiveIntegerField(blank=True, help_text='кількість робочих днів(окрім вихідних)\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='р.д. 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_sum',
            field=models.PositiveIntegerField(blank=True, help_text='кількість робочих днів(окрім вихідних)\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='р.д. сумарно'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_weekend_1',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість робочих днів у вихідних\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='р.д.вих 1'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_weekend_2',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість робочих днів у вихідних\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='р.д.вих 2'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_weekend_3',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість робочих днів у вихідних\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='р.д.вих 3'),
        ),
        migrations.AlterField(
            model_name='executorpayment',
            name='work_days_weekend_sum',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='кількість робочих днів у вихідних\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='р.д.вих сумарно'),
        ),
    ]
