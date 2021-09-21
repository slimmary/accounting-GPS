from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from vehicle.models import Vehicle


class ServiceAndEquipment(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Назва',
                            help_text='Введіть назву товару або послуги',
                            )
    price_client_taxfree = models.PositiveIntegerField(null=True,
                                                       default=0,
                                                       verbose_name="Вартість для клієнта БЕЗ ПДВ",
                                                       help_text='Введіть вартість',
                                                       blank=True
                                                       )
    price_client_tax = models.PositiveIntegerField(null=True,
                                                   default=0,
                                                   verbose_name="Вартість для клієнта з ПДВ",
                                                   help_text='Введіть вартість',
                                                   blank=True
                                                   )
    price_taxfree = models.PositiveIntegerField(null=True,
                                                default=0,
                                                verbose_name="Собівартість БЕЗ ПДВ",
                                                help_text='Введіть вартість',
                                                blank=True
                                                )
    price_tax = models.PositiveIntegerField(null=True,
                                            default=0,
                                            verbose_name="Собівартість з ПДВ",
                                            help_text='Введіть вартість',
                                            blank=True
                                            )

    class Meta:
        abstract = True


class Equipment(ServiceAndEquipment):
    class Meta:
        verbose_name_plural = "Комплектуючі"

    def __str__(self):
        return '{}'.format(self.name)


class Service(ServiceAndEquipment):
    salary_installer = models.PositiveIntegerField(null=True,
                                                   default=0,
                                                   verbose_name="Вартість роботи монтажника",
                                                   help_text='Введіть вартість',
                                                   blank=True
                                                   )

    class Meta:
        verbose_name_plural = "Послуги"

    def __str__(self):
        return '{}'.format(self.name)


class Sim(models.Model):
    class Operator:
        kiyvstar = 'Київстар'
        lifecell = 'Лайфсел'
        travelsim = 'Тревел-сім'
        goodline = 'Гудлайн'

    OPERATOR_CHOICE = (
        (Operator.kiyvstar, 'Київстар'),
        (Operator.lifecell, 'Лайфсел'),
        (Operator.travelsim, 'Тревел-сім'),
        (Operator.goodline, 'Гудлайн'),
    )
    operator = models.CharField(max_length=100,
                                default=Operator.kiyvstar,
                                choices=OPERATOR_CHOICE,
                                verbose_name='Оператор',
                                help_text='Оберіть оператора'
                                )
    number = models.CharField(max_length=11,
                              verbose_name='Номер SIM',
                              help_text='Введіть номер',
                              validators=[RegexValidator(r'^\d{0,11}$')]
                              )
    account_number = models.CharField(max_length=5,
                                      verbose_name='Рахунок',
                                      help_text='Введіть номер рахунку',
                                      validators=[RegexValidator(r'^\d{0,10}$')]
                                      )
    date_receive = models.DateField(null=True,
                                    verbose_name='Дата отримання',
                                    help_text='Оберіть дату'
                                    )
    rate_sim = models.FloatField(null=True,
                                 max_length=5,
                                 verbose_name='Тариф оператора грн/міс',
                                 help_text='Введіть суму',
                                 blank=True
                                 )
    packet_volume = models.PositiveIntegerField(null=True,
                                                verbose_name="Об'єм пакетних даних Мб/міс",
                                                help_text='Введіть кількість', blank=True
                                                )
    rate_volume = models.FloatField(null=True,
                                    max_length=5,
                                    verbose_name='Тариф за 1Мб поза пакетом',
                                    help_text='Введіть суму',
                                    blank=True
                                    )

    INSTALLER_CHOICE = (
        ('1', 'Герус В.'),
        ('2', 'Деміденко Ю.'),
        ('3', 'Ігнатенко М.'),
    )
    installer = models.CharField(max_length=1,
                                 choices=INSTALLER_CHOICE,
                                 verbose_name='Монтажник',
                                 help_text='Оберіть монтажника, якому видано сім',
                                 blank=True
                                 )
    date_given = models.DateField(null=True,
                                  verbose_name='Дата видачі монтажнику сім',
                                  help_text='Оберіть дату',
                                  blank=True
                                  )

    class Meta:
        verbose_name_plural = "Сім-картки"

    def __str__(self):
        return '{} {}'.format(self.get_operator_display(), self.number)


class Gps(models.Model):
    number = models.CharField(verbose_name='Номер',
                              help_text='Введіть номер',
                              max_length=6,
                              validators=[RegexValidator(r'^\d{0,10}$')]
                              )

    sim_1 = models.ForeignKey(Sim,
                              null=True,
                              on_delete=models.CASCADE,
                              verbose_name='Сім 1',
                              related_name='gps_sim_1',
                              blank=True
                              )

    sim_2 = models.ForeignKey(Sim,
                              null=True,
                              on_delete=models.CASCADE,
                              verbose_name='Сім 2',
                              related_name='gps_sim_2',
                              blank=True
                              )
    vehicle = models.OneToOneField(Vehicle,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   verbose_name='ТЗ',
                                   related_name='gps',
                                   blank=True
                                   )

    def clean(self):
        if self.sim_1:
            if self.sim_2:
                if self.sim_2.operator == self.sim_2.Operator.lifecell or self.sim_2.operator == self.sim_2.Operator.kiyvstar:
                    raise ValidationError({'sim_2': 'Сім 2 може бути тільки операторів Тревелсім або Гудлайн'})
                elif self.sim_1.operator == self.sim_1.Operator.travelsim or self.sim_1.operator == self.sim_1.Operator.goodline:
                    raise ValidationError(
                        {'sim_1': 'Сім 1 не може бути операторів Тревелсім або Гудлайн, якщо Сім 2 додана'})
        else:
            if self.sim_2:
                raise ValidationError({'sim_2': 'Сім 2 може бути додана якщо Сім 1 не додана'})

    def save(self,*args, **kwargs):
        if self.vehicle:
            Vehicle.save(self.vehicle, *args, **kwargs)
        super(Gps, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Бортові Реєстратори (БР)"

    def __str__(self):
        return 'БР №{}'.format(self.number)


class FuelSensor(models.Model):
    class Fuel_Type:
        analog = 'аналоговый'
        chastot = 'частотный'
        cyfra = 'цифровой'

    FUEL_TYPE = (
        (Fuel_Type.analog, 'аналоговый'),
        (Fuel_Type.chastot, 'частотный'),
        (Fuel_Type.cyfra, 'цифровой'),
    )
    type = models.CharField(null=True,
                            default=Fuel_Type.cyfra,
                            choices=FUEL_TYPE,
                            max_length=100,
                            verbose_name='Тип датчика',
                            help_text='Оберіть тип',
                            blank=True
                            )

    class Serial:
        h2 = '2'
        h4 = '4'
        h7 = '7'
        h10 = '10'
        h15 = '15'
        h20 = '20'

    FUEL_SERIAL = (
        (Serial.h2, '2'),
        (Serial.h4, '4'),
        (Serial.h7, '7'),
        (Serial.h10, '10'),
        (Serial.h15, '15'),
        (Serial.h20, '20'),
    )
    serial = models.CharField(null=True,
                              default=Serial.h7,
                              choices=FUEL_SERIAL,
                              max_length=100,
                              verbose_name='Серія',
                              help_text='Оберіть серію (висоту)',
                              blank=True
                              )
    number = models.PositiveIntegerField(verbose_name="Номер", help_text='Введіть номер', )
    date_manufacturing = models.DateField(verbose_name='Дата виробництва', null=True, help_text='Оберіть дату',
                                          blank=True)
    vehicle = models.ForeignKey(Vehicle,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='ТЗ',
                                related_name='fuel_sensor',
                                blank=True
                                )
    comments = models.CharField(null=True,
                                verbose_name='Висота та інше',
                                max_length=200,
                                blank=True
                                )

    class Meta:
        verbose_name_plural = "Датчики Вимірювання Рівня Пального (ДВРП)"

    def __str__(self):
        if self.type == self.Fuel_Type.cyfra:
            return 'D{}-{}'.format(self.serial, self.number)
        elif self.type == self.Fuel_Type.chastot:
            return 'H{}-{}'.format(self.serial, self.number)
        return 'стріла{}-{}'.format(self.serial, self.number)
