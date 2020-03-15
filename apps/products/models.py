from django.db import models
from django.core.validators import RegexValidator
from apps.clients.models import Client
from apps.vehicle.models import Vehicle


class Gps(models.Model):
    number = models.CharField(verbose_name='Номер', help_text='Введіть номер', max_length=6,
                              validators=[RegexValidator(r'^\d{0,10}$')])
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Транспортний засіб',
                               related_name='gps')

    class Meta:
        verbose_name_plural = "Реєстратори"

    def __str__(self):
        return 'БР №{}'.format(self.number)


class Sim(models.Model):

    OPERATOR_CHOICE = (
        ('1', 'Київстар'),
        ('2', 'Лайфсел'),
        ('3', 'Тревел-сім'),
    )
    operator = models.CharField(max_length=1, choices=OPERATOR_CHOICE, verbose_name='Оператор',
                                help_text='Оберіть оператора')
    number = models.CharField(verbose_name='Номер', help_text='Введіть номер', max_length=11,
                              validators=[RegexValidator(r'^\d{0,11}$')])
    account_number = models.CharField(verbose_name='Рахунок', help_text='Введіть номер рахунку',
                                      max_length=5, validators=[RegexValidator(r'^\d{0,10}$')])
    date_receive = models.DateField(verbose_name='Дата отримання', help_text='Оберіть дату')
    rate = models.FloatField(max_length=5, verbose_name='Тариф грн/міс', help_text='Введіть суму', blank=True)
    packet_volume = models.PositiveIntegerField(verbose_name="Об'єм пакетних даних Мб/міс",
                                        help_text='Введіть кількість', blank=True)
    rate_volume = models.FloatField(max_length=5, verbose_name='Тариф за 1Мб поза пакетом', help_text='Введіть суму',blank=True)
    gps = models.ForeignKey(Gps, null=True, on_delete=models.CASCADE, verbose_name='БР', related_name='sim', blank=True)
    RATE_CHOICE = (
        ('1', 'Україна'),
        ('2', 'Світ'),
        ('3', 'Пауза'),
    )

    rate_client = models.CharField(max_length=1, choices=RATE_CHOICE, verbose_name='Тариф',
                                help_text='Оберіть тариф для клієнта', default='1')
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