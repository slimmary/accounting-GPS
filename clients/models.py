from phone_field import PhoneField
from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator


class ContactProfile(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Прізвище')
    surname = models.CharField(max_length=50, verbose_name="І'мя")
    patronymic = models.CharField(max_length=50, verbose_name='По батькові')
    position = models.CharField(max_length=50, verbose_name='Посада')
    phone = PhoneField(null=True, verbose_name='Контактний номер телефону')
    phone_2 = PhoneField(null=True, blank=True, verbose_name='додатковий контактний номер телефону')
    email = models.EmailField(null=True, max_length=254, verbose_name='Контактна електронна адреса')

    def __str__(self):
        return '{} {} {}  - посада: {}, телефон: {}, email: {}  '.format(
            self.firstname,
            self.surname,
            self.patronymic,
            self.position,
            self.phone,
            self.email
        )

    class Meta:
        verbose_name_plural = "Контактні особи клієнтів"


class ClientPostAddress(models.Model):
    index = models.IntegerField(verbose_name='Пштовий індекс')
    region = models.CharField(max_length=50, verbose_name='Область')
    district = models.CharField(max_length=50, verbose_name='Район', blank=True)
    city = models.CharField(max_length=50, verbose_name='Місто')
    street = models.CharField(max_length=200, verbose_name='Вулиця')
    house = models.CharField(max_length=50, verbose_name='Номер будинку')
    office = models.CharField(max_length=50, verbose_name='Номер офісу або квартири')

    def __str__(self):
        return 'Індекс: {}, Область: {}, Район: {}, Місто: {}, Вулиця: {}, Будинок №: {}, Офіс/квартира №: {}'.format(
            self.index,
            self.region,
            self.district,
            self.city,
            self.street,
            self.house,
            self.office)

    class Meta:
        verbose_name_plural = "Поштові адреси"


class Client(models.Model):
    day_start = models.DateField(null=True,
                                 verbose_name='Дата початку роботи',
                                 help_text='Оберіть дату',
                                 blank=False
                                 )
    name = models.CharField(max_length=128,
                            verbose_name='Назва клієнта',
                            blank=False
                            )
    login = models.CharField(max_length=128,
                             verbose_name="Ім'я користувача (login)",
                             blank=False
                             )
    STATUS_FORM_CHOICE = (
        ('1', 'активний'),
        ('2', 'видалений')
    )
    status = models.CharField(null=True,
                              max_length=1,
                              default='активний',
                              choices=STATUS_FORM_CHOICE,
                              verbose_name='Статус',
                              help_text='Оберіть статус клієнта'
                              )
    edrpou = models.PositiveIntegerField(null=True,
                                         default=00000000,
                                         max_length=8,
                                         verbose_name="ЄДРПОУ",
                                         help_text='Введіть ЄДРПОУ клієнта',
                                         validators=[RegexValidator(r'^\d{0,10}$'), MinLengthValidator(8)],
                                         )
    IPN = models.CharField(null=True,
                           default=00000000,
                           max_length=12,
                           verbose_name="ІПН",
                           help_text='Введіть ІПН клієнта',
                           validators=[RegexValidator(r'^\d{0,10}$'),MinLengthValidator(10)],
                           blank=True
                           )
    director = models.CharField(null=True,
                                max_length=100,
                                verbose_name='Директор',
                                help_text='Введіть ПІП директора',
                                blank=True
                                )
    IBAN = models.CharField(null=True,
                            default=00000000,
                            max_length=29,
                            verbose_name="IBAN",
                            help_text='Введіть IBAN клієнта',
                            validators=[RegexValidator(r'^\d{0,10}$'),MinLengthValidator(29)],
                            blank=True
                            )
    contacts = models.ManyToManyField(ContactProfile,
                                      verbose_name='Контактні особи',
                                      related_name='client_field'
                                      )
    address = models.OneToOneField(ClientPostAddress,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   verbose_name='Поштова адреса',
                                   related_name='client'
                                   )

    class Provider:
        ckt = 'ТОВ "Системи Контролю Транспорту"'
        shevchuk = 'ФОП Шевчук С.І.'
        demchenko = 'ФОП Демченко К.В.'
        dyachuk = 'ФОП Дячук Л.В.'
        card = 'БК/ІНШЕ'

    PROVIDER_CHOICE = (
        (Provider.ckt, 'ТОВ "Системи Контролю Транспорту"'),
        (Provider.shevchuk, 'ФОП Шевчук С.І.'),
        (Provider.dyachuk, 'ФОП Демченко К.В.'),
        (Provider.demchenko, 'ФОП Дячук Л.В.'),
        (Provider.card, 'БК/ІНШЕ')
    )
    provider = models.CharField(null=True,
                                max_length=100,
                                default=Provider.shevchuk,
                                choices=PROVIDER_CHOICE,
                                verbose_name='Постачальник з абонплати',
                                help_text='Оберіть постачальника з абонплати'
                                )

    def __str__(self):
        return '"{}"  /  логін: {}  '.format(
            self.name,
            self.login,

        )

    class Meta:
        verbose_name_plural = "Клієнти"
