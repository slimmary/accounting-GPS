from django.db import models
from django.core.validators import RegexValidator
from vehicle.models import Vehicle


class Gps(models.Model):
    number = models.CharField(verbose_name='Номер', help_text='Введіть номер', max_length=6,
                              validators=[RegexValidator(r'^\d{0,10}$')])
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, verbose_name='Транспортний засіб',
                                   related_name='gps')

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
    operator = models.CharField(max_length=100, default=Operator.kiyvstar, choices=OPERATOR_CHOICE,
                                verbose_name='Оператор',
                                help_text='Оберіть оператора')
    number = models.CharField(verbose_name='Номер БР', help_text='Введіть номер', max_length=11,
                              validators=[RegexValidator(r'^\d{0,11}$')])
    account_number = models.CharField(verbose_name='Рахунок', help_text='Введіть номер рахунку',
                                      max_length=5, validators=[RegexValidator(r'^\d{0,10}$')])
    date_receive = models.DateField(verbose_name='Дата отримання', help_text='Оберіть дату')
    rate_sim = models.FloatField(max_length=5, null=True, verbose_name='Тариф оператора грн/міс', help_text='Введіть суму', blank=True)
    packet_volume = models.PositiveIntegerField(null=True, verbose_name="Об'єм пакетних даних Мб/міс",
                                                help_text='Введіть кількість', blank=True)
    rate_volume = models.FloatField(max_length=5, null=True, verbose_name='Тариф за 1Мб поза пакетом', help_text='Введіть суму',
                                    blank=True)
    gps = models.ForeignKey(Gps, null=True, on_delete=models.CASCADE, verbose_name='БР', related_name='sim', blank=True)

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

    rate_client = models.CharField(max_length=100, choices=RATE_CHOICE, verbose_name='Тариф',
                                   help_text='Оберіть тариф для клієнта', )
    # @property
    # def get_client_provider(self):
    #     provider = self.gps.vehicle.client.provider
    #     return provider
    # rate_price = models.CharField(max_length=100, default=price, verbose_name='Вартість',
    #                              help_text='Змініть вартість')

    INSTALLER_CHOICE = (
        ('1', 'Герус В.'),
        ('2', 'Манін В.'),
        ('3', 'Ігнатенко М.'),
    )
    installer = models.CharField(max_length=1, choices=INSTALLER_CHOICE, verbose_name='Монтажник',
                                 help_text='Оберіть монтажника, якому видано сім', blank=True)
    date_given = models.DateField(verbose_name='Дата видачі монтажнику сім', help_text='Оберіть дату', blank=True)

    class Meta:
        verbose_name_plural = "Сім-картки"

    def __str__(self):
        return '{} {} {}'.format(self.get_operator_display(), self.number, self.rate_client)


class FuelSensor(models.Model):
    serial = models.CharField(max_length=128, verbose_name='Серія')
    number = models.PositiveIntegerField(verbose_name="Номер", help_text='Введіть номер', )
    date_manufacturing = models.DateField(verbose_name='Дата виробництва', help_text='Оберіть дату', blank=True)
    gps = models.ForeignKey(Gps, null=True, on_delete=models.CASCADE, verbose_name='БР', related_name='fuel_sensor',
                            blank=True)

    class Meta:
        verbose_name_plural = "Датчики Вимірювання Рівня Пального (ДВРП)"

    def __str__(self):
        return '{}-{}'.format(self.serial, self.number)
