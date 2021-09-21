from phone_field import PhoneField
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError


class ClientAddress(models.Model):
    index = models.CharField(max_length=5, verbose_name='Пштовий індекс')
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


class ContactProfile(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Прізвище')
    surname = models.CharField(max_length=50, verbose_name="І'мя")
    patronymic = models.CharField(max_length=50, verbose_name='По батькові')
    position = models.CharField(max_length=50, verbose_name='Посада', default='менеджер')
    phone = PhoneField(null=True, verbose_name='№ телефону')
    phone_2 = PhoneField(null=True, blank=True, verbose_name='додатковий № телефону')
    email = models.EmailField(null=True, max_length=254, verbose_name='електронна адреса')

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


class Provider(models.Model):
    name = models.CharField(null=True,
                            max_length=100,
                            verbose_name='Назва',
                            help_text='Введіть повну назву постачальника послуг'
                            )

    class Taxtype:
        taxfree = 'без ПДВ'
        tax = 'з ПДВ'

    TAX_CHOICE = (
        (Taxtype.taxfree, 'без ПДВ'),
        (Taxtype.tax, 'з ПДВ'),
    )
    tax_type = models.CharField(null=True,
                                max_length=100,
                                default=Taxtype.taxfree,
                                choices=TAX_CHOICE,
                                verbose_name='Форма оплати',
                                help_text='Оберіть форму з ПДВ чи без'
                                )

    def __str__(self):
        return '"{}"  /  {}  '.format(
            self.name,
            self.tax_type,

        )

    class Meta:
        verbose_name_plural = "Постачальники послуг для клієнтів"


class ClientLegalDetail(models.Model):
    IPN = models.CharField(null=True,
                           default=123456789012,
                           max_length=12,
                           verbose_name="ІПН",
                           help_text='Введіть ІПН клієнта',
                           validators=[RegexValidator(r'^\d{0,100}$'), MinLengthValidator(10)],
                           blank=True
                           )
    director = models.CharField(null=True,
                                max_length=100,
                                verbose_name='Директор',
                                help_text='Введіть ПІП директора',
                                blank=True
                                )
    IBAN = models.CharField(null=True,
                            default=12345678912345678901234567890,
                            max_length=29,
                            verbose_name="IBAN",
                            help_text='Введіть IBAN клієнта',
                            validators=[RegexValidator(r'^\d{0,100}$'), MinLengthValidator(29)],
                            blank=True
                            )
    bank_account = models.CharField(null=True,
                                    default=1234567890,
                                    max_length=20,
                                    verbose_name="№ р/р",
                                    help_text='Введіть р/р',
                                    validators=[RegexValidator(r'^\d{0,100}$'), ],
                                    blank=True
                                    )
    MFO = models.CharField(null=True,
                           default=12345,
                           max_length=10,
                           verbose_name="IBAN",
                           help_text='Введіть IBAN клієнта',
                           validators=[RegexValidator(r'^\d{0,100}$'), MinLengthValidator(5)],
                           blank=True
                           )
    bank = models.CharField(null=True,
                            max_length=100,
                            verbose_name='Банк',
                            help_text='Введіть назву банку',
                            blank=True
                            )
    legal_address = models.OneToOneField(ClientAddress,
                                         null=True,
                                         on_delete=models.CASCADE,
                                         verbose_name='Юридична адреса',
                                         related_name='client_legal_address',
                                         help_text='Оберіть юридичну адресу клієнта',
                                         blank=True
                                         )

    post_address = models.OneToOneField(ClientAddress,
                                        null=True,
                                        on_delete=models.CASCADE,
                                        verbose_name='Поштова адреса',
                                        related_name='client_post_address',
                                        help_text='Оберіть поштову адресу клієнта, якщо вона не співпадає з юридичною',
                                        blank=True
                                        )

    def __str__(self):
        return 'Реквізити {}'.format(self.IPN)

    class Meta:
        verbose_name_plural = "Реквізити клієнтів"


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
    edrpou = models.CharField(null=True,
                              default=12345678,
                              max_length=8,
                              verbose_name="ЄДРПОУ",
                              help_text='Введіть ЄДРПОУ клієнта',
                              validators=[RegexValidator(r'^\d{0,10}$'), MinLengthValidator(8)],
                              )
    provider = models.ForeignKey(Provider,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Постачальник з АП',
                                 related_name='client_provider')

    contacts = models.ManyToManyField(ContactProfile,
                                      verbose_name='Контактні особи',
                                      related_name='client_field',
                                      )

    class Notification:
        sms = 'SMS'
        viber = 'VIBER'
        email = 'Email'
        medoc = 'M.E.D.O.C.'
        call = 'Дзвінок'

    NOTIFICATION_CHOICE = (
        (Notification.sms, 'SMS'),
        (Notification.viber, 'VIBER'),
        (Notification.email, 'Email'),
        (Notification.medoc, 'M.E.D.O.C.'),
        (Notification.call, 'Дзвінок')
    )

    type_notification_1 = models.CharField(null=True,
                                           max_length=100,
                                           default=Notification.medoc,
                                           choices=NOTIFICATION_CHOICE,
                                           verbose_name='Тип повідомлень 1',
                                           help_text='Оберіть спосіб повідомлення клієнта по рахунках'
                                           )
    notification_contact_1 = models.ForeignKey(ContactProfile,
                                               on_delete=models.CASCADE,
                                               null=True,
                                               default=None,
                                               verbose_name='Контактна особи для повідомлень',
                                               related_name='client_notification_field_1',
                                               help_text='Оберіть контактну особу яку повідомлятимуть по рахунках',
                                               blank=True
                                               )

    type_notification_2 = models.CharField(null=True,
                                           max_length=100,
                                           choices=NOTIFICATION_CHOICE,
                                           verbose_name='Тип повідомлень 2',
                                           help_text='Оберіть спосіб повідомлення клієнта по рахунках',
                                           blank=True
                                           )
    notification_contact_2 = models.ForeignKey(ContactProfile,
                                               on_delete=models.CASCADE,
                                               null=True,
                                               default=None,
                                               verbose_name='Контактна особи для повідомлень',
                                               related_name='client_notification_field_2',
                                               help_text='Оберіть контактну особу, яку повідомлятимуть по рахунках',
                                               blank=True
                                               )
    legal_info = models.OneToOneField(ClientLegalDetail,
                                      on_delete=models.CASCADE,
                                      null=True,
                                      default=None,
                                      verbose_name='Реквізити',
                                      related_name='client_legal_detail',
                                      help_text='Оберіть або створіть реквізити',
                                      blank=True,
                                      )

    def clean(self):
        if self.type_notification_1 != self.Notification.medoc:
            if self.notification_contact_1 is None:
                raise ValidationError(
                    {'notification_contact_1': "Не можливо обратий цей тип повідомленнь 1 не вказавши "
                                               "контактну особу, яку повідомлятимуть по рахунках "
                                               "(особа має бути пов'язана з клієнтом)"})
            elif self.notification_contact_1 not in self.contacts.all():
                raise ValidationError(
                    {'notification_contact_1': "Обрана особа не є контактною і не повязана з клєнтом, "
                                               "оберіть особу яка пов'язана зі списку 'контактні особи'"})
        if self.type_notification_2 != self.Notification.medoc:
            if self.type_notification_2 is not None:
                if self.notification_contact_2 is None:
                    raise ValidationError({'notification_contact_2': "Не можливо обратий тип повідомленнь 2? "
                                                                     "не вказавши контактну особу, "
                                                                     "яку повідомлятимуть по рахунках "
                                                                     "(особа має бути пов'язана з клієнтом)"})
                elif self.notification_contact_2 not in self.contacts.all():
                    raise ValidationError(
                        {'notification_contact_2': "Обрана особа не є контактною і не повязана з клєнтом,"
                                                   "оберіть особу яка пов'язана зі списку 'контактні особи'"})

    def save(self, *args, **kwargs):
        if self.type_notification_1 != self.Notification.medoc:
            if self.notification_contact_1 is None:
                raise ValidationError
        else:
            self.notification_contact_1 = None

        if self.type_notification_2 != self.Notification.medoc:
            if self.type_notification_2 is not None:
                if self.notification_contact_2 is None:
                    raise ValidationError
        else:
            self.notification_contact_2 = None
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return '"{}"  /  {}  '.format(
            self.name,
            self.login,

        )

    class Meta:
        verbose_name_plural = "Клієнти"


class ClientProxyPayment(Client):
    class Meta:
        verbose_name_plural = "Клієнт зведені дані"
        proxy = True
