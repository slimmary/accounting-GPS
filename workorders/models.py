from django.db import models
from datetime import date
from vehicle.models import Vehicle
from projects.models import Project
from products.models import Equipment, Service, Gps, FuelSensor


class WorkOrder(models.Model):
    date = models.DateField(verbose_name='Дата ЗН',
                            help_text='Введіть дату',
                            )
    number = models.PositiveIntegerField(null=True,
                                         verbose_name='№',
                                         help_text='Номер PY',
                                         blank=True
                                         )

    class TypeWork:
        project = 'Проект'
        service = 'Сервіс'

    TYPE_WORK_CHOICE = (
        (TypeWork.project, 'Проект'),
        (TypeWork.service, 'Сервіс'),
    )
    type_of_work = models.CharField(max_length=100,
                                    default=TypeWork.project,
                                    choices=TYPE_WORK_CHOICE,
                                    verbose_name='Тип ЗН (Проект/Серві',
                                    help_text='Оберіть тип',

                                    )
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                verbose_name='№ проекту до якого відноситься ЗН',
                                related_name='work_orders'
                                )

    # executor =
    # +client: Foreignkey(Client)
    # +client_login:
    # +list_of_completed_works:
    # +price_of_completed_works:
    # +price_of_used_equipment:
    # +list_of_used_equipment:
    # +info:
    # +pay_form:
    # +milege:
    # +milege_price_executor:
    # +milege_price_client:
    # +add_costs_executor:
    # +add_costs_client:
    # +description_add_costs:
    # +month_executor_pay:
    # +sum_price_client:
    # +invoice:
    # +date_payment:


class CompletedProjectWorks(models.Model):
    car = models.ForeignKey(Vehicle,
                            null=True,
                            on_delete=models.CASCADE,
                            verbose_name='ТЗ',
                            related_name='service_works',
                            blank=True
                            )
    type_service = models.ForeignKey(Service,
                                     on_delete=models.CASCADE,
                                     verbose_name='виконані роботи',
                                     related_name='completed_service_works'
                                     )

    gps = models.ForeignKey(Gps,
                            on_delete=models.CASCADE,
                            verbose_name='БР',
                            related_name='gps_service_works',
                            )

    fuel_sensor = models.ForeignKey(FuelSensor,
                                    on_delete=models.CASCADE,
                                    verbose_name='ДВРП',
                                    related_name='fuel_sensor_service_works',
                                    )


class CompletedServiceWorks(CompletedProjectWorks):
    used_equipment = models.ManyToManyField(Equipment,
                                            verbose_name='використане обладнання',
                                            related_name='used_equipment'
                                            )

    class Payer:
        client = 'Клієнт'
        ckt = 'СКТ'
        executor = 'монтажник'
        manufacturer = 'виробник'

    PAYER_CHOICE = (
        (Payer.client, 'Клієнт'),
        (Payer.ckt, 'ЛайСКТфсел'),
        (Payer.executor, 'Тревел-монтажник'),
        (Payer.manufacturer, 'виробник-сім'),
    )
    payer = models.CharField(max_length=100,
                             default=Payer.client,
                             choices=PAYER_CHOICE,
                             verbose_name='Платник',
                             help_text='Оберіть платника'
                             )

    class Meta:
        verbose_name_plural = "Виконані сервісні роботи та використане обладнання"

    def __str__(self):
        return '{}{}{}{}{}{}'.format(self.car, self.type_service, self.used_equipment, self.gps, self.fuel_sensor,
                                     self.payer)
