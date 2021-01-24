from django.db import models
from datetime import date
from clients.models import Client
from staff.models import Staff
from vehicle.models import Vehicle
from projects.models import Project

from products.models import Equipment, Service, Gps, FuelSensor


class WorkOrder(models.Model):
    date = models.DateField(verbose_name='Дата ЗН',
                            help_text='Введіть дату',
                            )
    number = models.PositiveIntegerField(null=True,
                                         verbose_name='№',
                                         help_text='Номер ЗН',
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
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='№ проекту до якого відноситься ЗН',
                                related_name='work_orders',
                                blank=True
                                )

    executor = models.ForeignKey(Staff,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='виконавець',
                                 related_name='work_orders',
                                 blank=True
                                 )
    client = models.ForeignKey(Client,
                               null=True,
                               on_delete=models.CASCADE,
                               verbose_name='клієнт',
                               related_name='work_orders',
                               blank=True,
                               )

    price_of_completed_works = models.PositiveIntegerField(null=True,
                                                           verbose_name='сума за виконані роботи',
                                                           help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                                           blank=True
                                                           )
    price_of_used_equipment = models.PositiveIntegerField(null=True,
                                                          verbose_name='Сума за використане обладнання',
                                                          help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                                          blank=True
                                                          )

    info = models.CharField(max_length=100, verbose_name='додаткова інформація з протоколу огляду')

    class PayForm:
        taxfree = 'БК'
        invoice = 'РФ'

    PAY_CHOICE = (
        (PayForm.taxfree, 'КО'),
        (PayForm.invoice, 'РФ'),
    )
    pay_form = models.CharField(max_length=100,
                                default=PayForm.taxfree,
                                choices=PAY_CHOICE,
                                verbose_name='Форма оплати',
                                help_text='Оберіть форму оплати',
                                blank=True
                                )
    milege = models.PositiveIntegerField(null=True,
                                         verbose_name='пробіг (км)',
                                         blank=True
                                         )
    milege_price_executor = models.PositiveIntegerField(null=True,
                                                        verbose_name='грн за км монтажнику',
                                                        help_text='Сума компенсації за пробіг монтажнику\nПоле '
                                                                  'заповниться автоматично, вводити нічого не '
                                                                  'потрібно',
                                                        blank=True
                                                        )

    milege_price_client = models.PositiveIntegerField(null=True,
                                                      verbose_name='грн за км клієнту',
                                                      help_text='Вартість пробігу для клієнта\nПоле заповниться '
                                                                'автоматично, вводити нічого не потрібно',
                                                      blank=True
                                                      )

    add_costs_executor = models.PositiveIntegerField(null=True,
                                                     verbose_name='грн за ДВ монтажнику',
                                                     help_text='Сума коомпенсації за додаткові витрати '
                                                               'монтажнику\nПоле заповниться автоматично, '
                                                               'вводити нічого не потрібно',
                                                     blank=True
                                                     )
    add_costs_client = models.PositiveIntegerField(null=True,
                                                   verbose_name='грн за км монтажнику',
                                                   help_text='Вартість додаткових витрат для клієнта\nПоле '
                                                             'заповниться автоматично, вводити нічого не потрібно',
                                                   blank=True
                                                   )
    description_add_costs = models.CharField(null=True,
                                             max_length=100,
                                             verbose_name='Список додаткових витрат',
                                             help_text='',
                                             blank=True
                                             )
    month_executor_pay = models.DateField(verbose_name='місяць/рік',
                                          help_text='місяць нарахування ЗП монтажнику',
                                          )
    sum_price_client = models.PositiveIntegerField(null=True,
                                                   verbose_name='сума рахунку',
                                                   help_text='сума рахунку для клієнта\nПоле заповниться автоматично, '
                                                             'вводити нічого не потрібно',
                                                   blank=True
                                                   )
    # invoice =
    # date_payment:
    # def save(self,*args, **kwargs):


class CompletedProjectWorks(models.Model):
    work_order_project = models.ForeignKey(WorkOrder,
                                           null=True,
                                           on_delete=models.CASCADE,
                                           verbose_name='ЗН',
                                           related_name='list_project_works',
                                           blank=True
                                           )

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
                                     related_name='completed_project_works'
                                     )

    gps = models.ForeignKey(Gps,
                            null=True,
                            on_delete=models.CASCADE,
                            verbose_name='БР',
                            related_name='gps_project_works',
                            blank=True
                            )

    fuel_sensor = models.ForeignKey(FuelSensor,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='ДВРП',
                                    related_name='fuel_sensor_project_works',
                                    blank=True
                                    )


class CompletedServiceWorks(CompletedProjectWorks):
    work_order_service = models.ForeignKey(WorkOrder,
                                           null=True,
                                           on_delete=models.CASCADE,
                                           verbose_name='ЗН',
                                           related_name='list_service_works',
                                           blank=True
                                           )

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
