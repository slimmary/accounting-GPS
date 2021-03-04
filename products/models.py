from django.db import models
from django.core.validators import RegexValidator
from vehicle.models import Vehicle
from clients.models import Client
from django.core.exceptions import ValidationError


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
    owner = models.ForeignKey(Client,
                              null=True,
                              on_delete=models.CASCADE,
                              verbose_name='Власник',
                              related_name='gps',
                              blank=True
                              )
    vehicle = models.OneToOneField(Vehicle,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   verbose_name='Транспортний засіб',
                                   related_name='gps',
                                   blank=True
                                   )

    class Rate:
        ua = 'Україна'
        world = 'Світ'
        pause = 'Пауза'
        own_sim = 'Власна сім'

    RATE_CHOICE = (
        (Rate.ua, 'Україна'),
        (Rate.world, 'Світ'),
        (Rate.pause, 'Пауза'),
        (Rate.own_sim, 'Власна сім'),
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
    rate_client = models.CharField(null=True,
                                   choices=RATE_CHOICE,
                                   max_length=100,
                                   verbose_name='Тариф',
                                   help_text='Тариф заповниться автоматично нічого не потрібно вводити',
                                   blank=True
                                   )

    rate_price = models.IntegerField(null=True,
                                     default=0,
                                     verbose_name='Вартість грн/міс',
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )

    def clean(self):
        if self.sim_1:
            if self.sim_2:
                if self.sim_2.operator == self.sim_2.Operator.lifecell or self.sim_2.operator == self.sim_2.Operator.kiyvstar:
                    raise ValidationError('Сім 2 може бути тільки операторів Тревелсім або Гудлайн')
                elif self.sim_1.operator == self.sim_1.Operator.travelsim or self.sim_1.operator == self.sim_1.Operator.goodline:
                    raise ValidationError('Сім 1 не може бути операторів Тревелсім або Гудлайн, якщо Сім 2 додана')
        else:
            if self.sim_2:
                raise ValidationError('Сім 2 може бути додана якщо Сім 1 не додана')
        # if self.sim_1.gps_sim_1 or self.sim_1.gps_sim_2:
        #     raise ValidationError('Сім 1 вже закріплена за іншим реєстратором')
        # elif self.sim_2.gps_sim_1 or self.sim_2.gps_sim_2:
        #     raise ValidationError('Сім 2 вже закріплена за іншим реєстратором')

    def save(self, *args, **kwargs):
        if self.owner is None:
            self.rate_client = 0
        else:
            if self.rate_client is None:
                if self.sim_1 is None and self.sim_2 is None:
                    self.rate_client = self.Rate.own_sim
                    if self.owner.provider == self.owner.Provider.dyachuk or self.owner.provider == self.owner.Provider.card:
                        self.rate_price = 60
                    else:
                        self.rate_price = 72
                else:
                    if self.sim_2 is None:
                        if self.owner.provider == self.owner.Provider.dyachuk or self.owner.provider == self.owner.Provider.card:
                            if self.sim_1.operator == self.sim_1.Operator.travelsim or self.sim_1.operator ==  self.sim_1.Operator.goodline:
                                self.rate_client = self.Rate.world
                                self.rate_price = 270
                            else:
                                self.rate_client = self.Rate.ua
                                self.rate_price = 120
                        else:
                            if self.sim_1.operator == self.sim_1.Operator.travelsim or self.sim_1.operator == self.sim_1.Operator.goodline:
                                self.rate_client = self.Rate.world
                                self.rate_price =324
                            else:
                                self.rate_client = self.Rate.ua
                                self.rate_price = 144
                    else:
                        self.rate_client = self.Rate.world
                        if self.owner.provider == self.owner.Provider.dyachuk or self.owner.provider == self.owner.Provider.card:
                            self.rate_price = 270
                        else:
                            self.rate_price = 324
            else:
                if self.owner.provider == self.owner.Provider.dyachuk or self.owner.provider == self.owner.Provider.card:
                    if self.rate_client == self.Rate.pause:
                        self.rate_price = 30
                    elif self.rate_client == self.Rate.world:
                        self.rate_price = 270
                    elif self.rate_client == self.Rate.ua:
                        self.rate_price = 120
                    elif self.rate_client == self.Rate.own_sim:
                        self.rate_price = 60
                    else:
                        self.rate_price = 0

                else:
                    if self.rate_client == self.Rate.pause:
                        self.rate_price = 36
                    elif self.rate_client == self.Rate.world:
                        self.rate_price = 324
                    elif self.rate_client == self.Rate.ua:
                        self.rate_price = 144
                    elif self.rate_client == self.Rate.own_sim:
                        self.rate_price = 72
                    else:
                        self.rate_price = 0

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
    gps = models.ForeignKey(Gps,
                            null=True,
                            on_delete=models.CASCADE,
                            verbose_name='БР',
                            related_name='fuel_sensor',
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
