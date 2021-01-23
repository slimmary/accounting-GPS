from django.db import models
from django.core.validators import RegexValidator
from vehicle.models import Vehicle
from clients.models import Client
from django.core.exceptions import ValidationError


class Equipment(models.Model):
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
        verbose_name_plural = "Комплектуючі"

    def __str__(self):
        return '{}'.format(self.name)


class Service(Equipment):
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

    OPERATOR_CHOICE = (
        (Operator.kiyvstar, 'Київстар'),
        (Operator.lifecell, 'Лайфсел'),
        (Operator.travelsim, 'Тревел-сім'),
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

    sim_1 = models.OneToOneField(Sim,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Сім_1',
                                 related_name='gps_1',
                                 blank=True
                                 )

    sim_2 = models.OneToOneField(Sim,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Сім_2',
                                 related_name='gps_2',
                                 blank=True
                                 )

    rate_client_1 = models.CharField(null=True,
                                     max_length=100,
                                     default=Rate.own_sim,
                                     verbose_name='Тариф 1',
                                     help_text='Тариф заповниться автоматично нічого не потрібно вводити',
                                     blank=True
                                     )

    rate_client_2 = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name='Тариф 2',
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
        # all_gps = Gps.objects.all()
        # for gps in all_gps:
        #     if self.number == gps.number:
        #         raise ValidationError('БР з таким номером вже існує')
        if self.sim_2 is not None:
            if self.sim_1 is None:
                if self.sim_2.operator != self.sim_2.Operator.travelsim:
                    raise ValidationError('Сім_2 може бути тільки оператора "тревел-сім"')
            else:
                if self.sim_2.operator != self.sim_2.Operator.travelsim:
                    raise ValidationError('Сім_2 може бути тільки оператора "тревел-сім" і тоді тариф_2 буде "Світ"')
                elif self.sim_1.operator == self.sim_1.Operator.travelsim and self.sim_2.operator == self.sim_2.Operator.travelsim:
                    raise ValidationError('Сім_1 та Сім_2 не можуть бути одночасно оператора "тревел-сім"')

    def save(self, *args, **kwargs):
        # all_gps = Gps.objects.all()
        try:
            # for gps in all_gps:
            #     if self.number != gps.number:
            if self.rate_client_1 == self.Rate.pause and self.rate_client_2 == self.Rate.pause:
                if self.owner.provider == self.owner.Provider.dyachuk or \
                        self.owner.provider == self.owner.Provider.card:
                    self.rate_price = 30
                else:
                    self.rate_price = 36
            else:
                if self.sim_1 is None and self.sim_2 is None:
                    self.rate_client_1 = self.Rate.own_sim
                    self.rate_client_2 = None
                elif self.sim_1 is not None and self.sim_2 is None:
                    if self.sim_1.operator == self.sim_1.Operator.travelsim:
                        self.rate_client_1 = self.Rate.ua
                        self.rate_client_2 = self.Rate.world
                    else:
                        self.rate_client_1 = self.Rate.ua
                        self.rate_client_2 = None
                elif self.sim_1 is not None and self.sim_2 is not None:
                    if self.sim_1.operator != self.sim_1.Operator.travelsim and self.sim_2.operator == self.sim_2.Operator.travelsim:
                        self.rate_client_1 = self.Rate.ua
                        self.rate_client_2 = self.Rate.world
                    else:
                        self.rate_client_1 = self.Rate.world
                        self.rate_client_2 = None
                else:
                    self.rate_client_1 = None
                    self.rate_client_2 = self.Rate.world
                if self.owner is None:
                    self.rate_price = 0
                else:
                    if self.owner.provider == self.owner.Provider.dyachuk or \
                            self.owner.provider == self.owner.Provider.card:
                        if self.rate_client_1 == self.Rate.ua:
                            price_1 = 120
                        elif self.rate_client_1 == self.Rate.world:
                            price_1 = 150
                        elif self.rate_client_1 == self.Rate.own_sim:
                            price_1 = 60
                        else:
                            price_1 = 0
                        if self.rate_client_2 == self.Rate.world:
                            price_2 = 150
                        else:
                            price_2 = 0
                        self.rate_price = sum(price_1, price_2)
                    else:
                        if self.rate_client_1 == self.Rate.ua:
                            price_1 = 144
                        elif self.rate_client_1 == self.Rate.world:
                            price_1 = 180
                        elif self.rate_client_1 == self.Rate.own_sim:
                            price_1 = 72
                        else:
                            price_1 = 0
                        if self.rate_client_2 == self.Rate.world:
                            price_2 = 180
                        else:
                            price_2 = 0
                        self.rate_price = price_1 + price_2
        except ValidationError:
            raise ValidationError
        super(Gps, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Бортові Реєстратори (БР)"

    def __str__(self):
        return 'БР №{}'.format(self.number)


class FuelSensor(models.Model):
    serial = models.CharField(max_length=128, verbose_name='Серія')
    number = models.PositiveIntegerField(verbose_name="Номер", help_text='Введіть номер', )
    date_manufacturing = models.DateField(verbose_name='Дата виробництва', null=True, help_text='Оберіть дату',
                                          blank=True)
    gps = models.ForeignKey(Gps, null=True, on_delete=models.CASCADE, verbose_name='БР', related_name='fuel_sensor', )

    class Meta:
        verbose_name_plural = "Датчики Вимірювання Рівня Пального (ДВРП)"

    def __str__(self):
        return '{}-{}'.format(self.serial, self.number)
