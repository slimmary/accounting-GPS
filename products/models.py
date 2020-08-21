from django.db import models
from django.core.validators import RegexValidator
from vehicle.models import Vehicle
from clients.models import Client


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
        ua_world = 'Україна+Світ'
        pause = 'Пауза'
        own_sim = 'Власна сім'

    RATE_CHOICE = (
        (Rate.ua, 'Україна'),
        (Rate.world, 'Світ'),
        (Rate.ua_world, 'Україна+Світ'),
        (Rate.pause, 'Пауза'),
        (Rate.own_sim, 'Власна сім'),
    )

    rate_client = models.CharField(null=True,
                                   max_length=100,
                                   default=Rate.ua,
                                   choices=RATE_CHOICE,
                                   verbose_name='Тариф',
                                   help_text='Оберіть тариф для клієнта',
                                   blank=True
                                   )

    rate_price = models.IntegerField(null=True,
                                     default=0,
                                     verbose_name='Вартість грн/міс',
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )

    def save(self, *args, **kwargs):
        if self.owner is None:
            self.rate_price = 0
        else:
            if self.owner.provider == self.owner.Provider.dyachuk or \
                    self.owner.provider == self.owner.Provider.card:
                if self.rate_client == self.Rate.ua:
                    self.rate_price = 120
                elif self.rate_client == self.Rate.world:
                    self.rate_price = 150
                elif self.rate_client == self.Rate.ua_world:
                    self.rate_price = 270
                elif self.rate_client == self.Rate.pause:
                    self.rate_price = 30
                elif self.rate_client == self.Rate.own_sim:
                    self.rate_price = 60
                else:
                    self.rate_price = 0
            else:
                if self.rate_client == self.Rate.ua:
                    self.rate_price = 144
                elif self.rate_client == self.Rate.world:
                    self.rate_price = 180
                elif self.rate_client == self.Rate.ua_world:
                    self.rate_price = 324
                elif self.rate_client == self.Rate.pause:
                    self.rate_price = 36
                elif self.rate_client == self.Rate.own_sim:
                    self.rate_price = 72
                else:
                    self.rate_price = 0

        super(Gps, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Бортові Реєстратори (БР)"

    def __str__(self):
        return 'БР №{}'.format(self.number)


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
    gps = models.ForeignKey(Gps,
                            null=True,
                            on_delete=models.CASCADE,
                            verbose_name='БР',
                            related_name='sim',
                            blank=True
                            )

    INSTALLER_CHOICE = (
        ('1', 'Герус В.'),
        ('2', 'Манін В.'),
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


class FuelSensor(models.Model):
    serial = models.CharField(max_length=128, verbose_name='Серія')
    number = models.PositiveIntegerField(verbose_name="Номер", help_text='Введіть номер', )
    date_manufacturing = models.DateField(verbose_name='Дата виробництва', help_text='Оберіть дату', blank=True)
    gps = models.ForeignKey(Gps, null=True, on_delete=models.CASCADE, verbose_name='БР', related_name='fuel_sensor', )

    class Meta:
        verbose_name_plural = "Датчики Вимірювання Рівня Пального (ДВРП)"

    def __str__(self):
        return '{}-{}'.format(self.serial, self.number)
