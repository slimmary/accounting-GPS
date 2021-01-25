# Generated by Django 2.2.13 on 2021-01-25 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('staff', '0001_initial'),
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Введіть дату', verbose_name='Дата ЗН')),
                ('number', models.PositiveIntegerField(blank=True, help_text='Номер ЗН', null=True, verbose_name='№')),
                ('type_of_work', models.CharField(choices=[('Проект', 'Проект'), ('Сервіс', 'Сервіс')], default='Проект', help_text='Оберіть тип', max_length=100, verbose_name='Тип ЗН (Проект/Серві')),
                ('price_of_completed_works', models.PositiveIntegerField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума за виконані роботи')),
                ('price_of_used_equipment', models.PositiveIntegerField(blank=True, help_text='Поле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='Сума за використане обладнання')),
                ('info', models.CharField(max_length=100, verbose_name='додаткова інформація з протоколу огляду')),
                ('pay_form', models.CharField(blank=True, choices=[('БК', 'КО'), ('РФ', 'РФ')], default='БК', help_text='Оберіть форму оплати', max_length=100, verbose_name='Форма оплати')),
                ('milege', models.PositiveIntegerField(blank=True, null=True, verbose_name='пробіг (км)')),
                ('milege_price_executor', models.PositiveIntegerField(blank=True, help_text='Сума компенсації за пробіг монтажнику\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за км монтажнику')),
                ('milege_price_client', models.PositiveIntegerField(blank=True, help_text='Вартість пробігу для клієнта\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за км клієнту')),
                ('add_costs_executor', models.PositiveIntegerField(blank=True, help_text='Сума коомпенсації за додаткові витрати монтажнику\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за ДВ \nмонтажнику')),
                ('add_costs_client', models.PositiveIntegerField(blank=True, help_text='Вартість додаткових витрат для клієнта\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='грн за ДВ \nклієнту')),
                ('description_add_costs', models.CharField(blank=True, max_length=100, null=True, verbose_name='Список додаткових витрат')),
                ('month_executor_pay', models.DateField(help_text='місяць нарахування ЗП монтажнику', verbose_name='місяць/рік ЗП')),
                ('sum_price_client', models.PositiveIntegerField(blank=True, help_text='сума рахунку для клієнта\nПоле заповниться автоматично, вводити нічого не потрібно', null=True, verbose_name='сума рахунку')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to='clients.Client', verbose_name='клієнт')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to='staff.Staff', verbose_name='виконавець')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to='projects.Project', verbose_name='№ проекту до якого відноситься ЗН')),
            ],
            options={
                'verbose_name_plural': 'Зака-Наряди',
            },
        ),
        migrations.CreateModel(
            name='CompletedWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(choices=[('Клієнт', 'Клієнт'), ('СКТ', 'ЛайСКТфсел'), ('монтажник', 'Тревел-монтажник'), ('виробник', 'виробник-сім')], default='Клієнт', help_text='Оберіть платника', max_length=100, verbose_name='Платник')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_works', to='vehicle.Vehicle', verbose_name='ТЗ')),
                ('fuel_sensor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuel_sensor_project_works', to='products.FuelSensor', verbose_name='ДВРП')),
                ('gps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gps_project_works', to='products.Gps', verbose_name='БР')),
                ('type_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_works', to='products.Service', verbose_name='виконані роботи')),
                ('used_equipment', models.ManyToManyField(related_name='used_equipment', to='products.Equipment', verbose_name='використане обладнання')),
                ('work_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_works', to='workorders.WorkOrder', verbose_name='ЗН')),
            ],
            options={
                'verbose_name_plural': 'Список виконаних робіт',
            },
        ),
    ]
