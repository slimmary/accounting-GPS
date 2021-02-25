from django.db import models
from datetime import date
from clients.models import Client, ContactProfile
from users.models import User
from vehicle.models import Vehicle
from projects.models import Project
from products.models import Equipment, Service, Gps, FuelSensor
from django.core.exceptions import ValidationError


def get_first_name(self):
    return self.first_name


User.add_to_class("__str__", get_first_name)


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
                                    verbose_name='Тип ЗН (Проект/Сервіc)',
                                    help_text='Оберіть тип',

                                    )
    project = models.ForeignKey(Project,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='Проект',
                                related_name='work_orders',
                                blank=True
                                )

    executor = models.ForeignKey(User,
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
                                                           help_text='Поле заповниться автоматично, вводити нічого не '
                                                                     'потрібно',
                                                           blank=True
                                                           )
    price_of_used_equipment = models.PositiveIntegerField(null=True,
                                                          verbose_name='Сума за використане обладнання',
                                                          help_text='Поле заповниться автоматично, вводити нічого не '
                                                                    'потрібно',
                                                          blank=True
                                                          )

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
                                         default=0,
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
                                                     verbose_name='грн за ДВ \nмонтажнику',
                                                     help_text='Сума коомпенсації за додаткові витрати монтажнику',
                                                     blank=True
                                                     )
    add_costs_client = models.PositiveIntegerField(null=True,
                                                   verbose_name='грн за ДВ \nклієнту',
                                                   help_text='Вартість додаткових витрат для клієнта',
                                                   blank=True
                                                   )
    description_add_costs = models.CharField(null=True,
                                             max_length=100,
                                             verbose_name='Список додаткових витрат',
                                             help_text='',
                                             blank=True
                                             )
    month_executor_pay = models.DateField(null=True,
                                          verbose_name='місяць/рік ЗП',
                                          help_text='місяць нарахування ЗП монтажнику',
                                          blank=True
                                          )
    sum_price_client = models.PositiveIntegerField(null=True,
                                                   verbose_name='сума рахунку',
                                                   help_text='сума рахунку для клієнта\nПоле заповниться автоматично, '
                                                             'вводити нічого не потрібно',
                                                   blank=True
                                                   )

    amount_gps = models.PositiveIntegerField(null=True,
                                             default=0,
                                             verbose_name='кіл-ть СКТ',
                                             help_text='введіть кількість ТІЛЬКИ ЯКЩО ПРОЕКТ',
                                             blank=True
                                             )
    amount_fuel_sensor = models.PositiveIntegerField(null=True,
                                                     default=0,
                                                     verbose_name='кіл-ть ДВРП',
                                                     help_text='введіть кількість ТІЛЬКИ ЯКЩО ПРОЕКТ',
                                                     blank=True
                                                     )

    # date_payment:
    def clean(self):
        if (self.amount_gps != 0 or self.amount_fuel_sensor != 0) and self.type_of_work != self.TypeWork.project:
            raise ValidationError('Кількість СКТ да ДВРП не потрібно рахувати якщо ЗН не Проект')
        if self.type_of_work != self.TypeWork.project and self.project:
            raise ValidationError('Не можливо приєднати проект, якщо тип ЗН не Проект')

    def save(self, *args, **kwargs):
        self.milege_price_executor = self.milege * 4.5
        if self.pay_form == self.PayForm.taxfree:
            self.milege_price_client = self.milege * 4.5
        else:
            self.milege_price_client = self.milege * 5.4

        super(WorkOrder, self).save(*args, **kwargs)

    def __str__(self):
        return 'ЗН №{}, від {}'.format(
            self.number,
            self.date,
        )

    class Meta:
        verbose_name_plural = "Заказ-Наряди"


class CompletedWorks(models.Model):
    work_order = models.ForeignKey(WorkOrder,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   verbose_name='ЗН',
                                   related_name='list_works',
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
                                     related_name='completed_works'
                                     )

    used_equipment = models.ManyToManyField(Equipment,
                                            null=True,
                                            verbose_name='використане обладнання',
                                            related_name='used_equipment',
                                            blank=True
                                            )

    class Payer:
        client = 'Клієнт'
        ckt = 'СКТ'
        executor = 'монтажник'
        manufacturer = 'виробник'

    PAYER_CHOICE = (
        (Payer.client, 'Клієнт'),
        (Payer.ckt, 'СКТ'),
        (Payer.executor, 'монтажник'),
        (Payer.manufacturer, 'виробник'),
    )
    payer = models.CharField(max_length=100,
                             default=Payer.client,
                             choices=PAYER_CHOICE,
                             verbose_name='Платник',
                             help_text='Оберіть платника'
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
    info = models.CharField(max_length=100,
                            null=True,
                            verbose_name='додаткова інформація\nз протоколу огляду',
                            blank=True
                            )

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.car,
            self.type_service,
            self.gps,
            self.fuel_sensor,
            self.used_equipment,
            self.payer
        )

    class Meta:
        verbose_name_plural = "Список виконаних робіт"


class ServicePlan(models.Model):
    date_create = models.DateField(verbose_name='Дата',
                                   default=date.today(),
                                   help_text='Введіть дату',
                                   )

    class TypeService:
        install = 'монтаж'
        disinstall = 'демонтаж'
        dis_install = 'демонтаж+монтаж'
        send = 'отправка'
        fix = 'ремонт'
        dis_fix = 'демонтаж+ремонт'
        install_fix = 'монтаж+ремонт'

    TYPE_SERVICE_CHOICE = (
        (TypeService.install, 'монтаж'),
        (TypeService.disinstall, 'демонтаж'),
        (TypeService.dis_install, 'демонтаж+монтаж'),
        (TypeService.send, 'отправка'),
        (TypeService.fix, 'ремонт'),
        (TypeService.dis_fix, 'демонтаж+ремонт'),
        (TypeService.install_fix, 'монтаж+ремонт'),
    )
    type_of_service = models.CharField(max_length=100,
                                       choices=TYPE_SERVICE_CHOICE,
                                       verbose_name='Тип робіт',
                                       help_text='Оберіть тип',
                                       )

    class City:
        kyiv = 'Київ'
        vinnytsia = 'Вінниця'
        lutsk = 'Луцьк'
        dnipro = 'Дніпро'
        zhytomir = 'Житомир'
        uzhgorod = 'Ужгород'
        zaporizhzhia = 'Запоріжжя'
        iv_frankivsk = 'Івано-Франківськ'
        kropivnitskiy = 'Кропивницький'
        lviv = 'Львів'
        mykolaiv = 'Миколаїв'
        odessa = 'Одеса'
        poltava = 'Полтава'
        sumy = 'Суми'
        rivne = 'Рівне'
        ternopil = 'Тернопіль'
        harkiv = 'Харків'
        herson = 'Херсон'
        hmelnitskiy = 'Хмельницький'
        cherkassy = 'Черкаси'
        chernihiv = 'Чернігів'
        chernivtsi = 'Чернівці'

    CITY_CHOICE = (
        (City.kyiv, 'Київ'),
        (City.vinnytsia, 'Вінниця'),
        (City.lutsk, 'Луцьк'),
        (City.dnipro, 'Дніпро'),
        (City.zhytomir, 'Житомир'),
        (City.uzhgorod, 'Ужгород'),
        (City.zaporizhzhia, 'Запоріжжя'),
        (City.iv_frankivsk, 'Івано-Франківськ'),
        (City.kropivnitskiy, 'Кропивницький'),
        (City.lviv, 'Львів'),
        (City.mykolaiv, 'Миколаїв'),
        (City.odessa, 'Одеса'),
        (City.poltava, 'Полтава'),
        (City.sumy, 'Суми'),
        (City.rivne, 'Рівне'),
        (City.ternopil, 'Тернопіль'),
        (City.harkiv, 'Харків'),
        (City.herson, 'Херсон'),
        (City.hmelnitskiy, 'Хмельницький'),
        (City.cherkassy, 'Черкаси'),
        (City.chernihiv, 'Чернігів'),
        (City.chernivtsi, 'Чернівці'),
    )
    city = models.CharField(max_length=100,
                            null=True,
                            choices=CITY_CHOICE,
                            verbose_name='місто',
                            help_text='Оберіть місто',
                            blank=True
                            )

    class District:
        kyiv = 'Київська'
        vinnytsia = 'Вінницька'
        volyn = 'Волинська'
        dnipro = 'Дніпропетровьска'
        zhytomir = 'Житомирська'
        zakarpattya = 'Закарпатська'
        zaporizhzhia = 'Запоріжська'
        iv_frankivsk = 'Івано-Франківська'
        kropivnitskiy = 'Кіровоградська'
        lviv = 'Львівська'
        mykolaiv = 'Миколаївська'
        odessa = 'Одеська'
        poltava = 'Полтавська'
        rivne = 'Рівненська'
        sumy = 'Сумська'
        ternopil = 'Тернопільська'
        harkiv = 'Харківська'
        herson = 'Херсонська'
        hmelnitskiy = 'Хмельницька'
        cherkassy = 'Черкаська'
        chernihiv = 'Чернігівська'
        chernivtsi = 'Чернівецька'

    DISTRICT_CHOICE = (
        (District.kyiv, 'Київська'),
        (District.vinnytsia, 'Вінницька'),
        (District.volyn, 'Волинська'),
        (District.dnipro, 'Дніпропетровьска'),
        (District.zhytomir, 'Житомирська'),
        (District.zakarpattya, 'Закарпатська'),
        (District.zaporizhzhia, 'Запоріжська'),
        (District.iv_frankivsk, 'Івано-Франківська'),
        (District.kropivnitskiy, 'Кіровоградська'),
        (District.lviv, 'Львівська'),
        (District.mykolaiv, 'Миколаївська'),
        (District.odessa, 'Одеська'),
        (District.poltava, 'Полтавська'),
        (District.rivne, 'Рівненська'),
        (District.sumy, 'Сумська'),
        (District.ternopil, 'Тернопільська'),
        (District.harkiv, 'Харківська'),
        (District.herson, 'Херсонська'),
        (District.hmelnitskiy, 'Хмельницька'),
        (District.cherkassy, 'Черкаська'),
        (District.chernihiv, 'Чернігівська'),
        (District.chernivtsi, 'Чернівецька'),
    )
    district = models.CharField(max_length=100,
                                null=True,
                                choices=DISTRICT_CHOICE,
                                verbose_name='область',
                                help_text='Оберіть область',
                                blank=True
                                )

    class Delivery:
        personal_car = 'власний автомобіль'
        client = 'силами замовника'
        carrier = 'перевізник'

    DELIVERY_CHOICE = (
        (Delivery.personal_car, 'власний автомобіль'),
        (Delivery.client, 'силами замовника'),
        (Delivery.carrier, 'перевізник'),
    )

    type_of_delivery = models.CharField(max_length=100,
                                        null=True,
                                        default=Delivery.personal_car,
                                        choices=DELIVERY_CHOICE,
                                        verbose_name='Спосіб проїду',
                                        )

    tasks = models.TextField(max_length=1000,
                             null=True,
                             verbose_name='Задачі',
                             help_text='Опишіть перелік запланованих робіт',
                             )

    date_planing = models.DateField(verbose_name='Строк з / Дата',
                                    help_text='Введіть дату',
                                    )

    time = models.CharField(max_length=100,
                            verbose_name='Строк до / Час',
                            help_text='Введіть дату або час вручну',
                            )

    client = models.ForeignKey(Client,
                               null=True,
                               on_delete=models.CASCADE,
                               verbose_name='клієнт',
                               related_name='work_orders_plan',
                               )
    adress = models.CharField(max_length=100,
                              null=True,
                              verbose_name='Адреса',
                              )
    contact = models.ForeignKey(ContactProfile,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='Контактна особа',
                                related_name='wo_plan_contact',
                                )
    contact_2 = models.ForeignKey(ContactProfile,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  verbose_name='Дод. контактна особа',
                                  related_name='wo_plan_contact_2',
                                  blank=True,
                                  )
    respons_manager = models.ForeignKey(User,
                                        null=True,
                                        on_delete=models.CASCADE,
                                        verbose_name='Відповідальний',
                                        related_name='wo_plan_response',
                                        )

    wo_numb = models.PositiveIntegerField(null=True,
                                          verbose_name='№',
                                          help_text='Номер ЗН',
                                          blank=True
                                          )

    date_ex = models.DateField(verbose_name='Дата виконання',
                               null=True,
                               help_text='Введіть дату',
                               blank=True
                               )

    executor = models.ForeignKey(User,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='виконавець',
                                 related_name='work_orders_plan_ex',
                                 blank=True
                                 )

    class StatusWOPlan:
        executed = 'виконано'
        postponed = 'перенесено'

    STATUSWOPLAN_CHOICE = (
        (StatusWOPlan.executed, 'виконано'),
        (StatusWOPlan.postponed, 'перенесено'),
    )

    status = models.CharField(max_length=100,
                              null=True,
                              choices=STATUSWOPLAN_CHOICE,
                              verbose_name='Статус виконання',
                              blank=True
                              )

    def clean(self):
        if self.city is None and self.district is None:
            raise ValidationError('Оберіть або область або місто')
        elif self.city and self.district:
            raise ValidationError('Оберіть щось одне або область або місто')

    def save(self, *args, **kwargs):
        if self.status == self.StatusWOPlan.executed:
            WorkOrder.objects.create(date=self.date_ex, number=self.wo_numb, executor=self.executor)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "План сервісних робіт"