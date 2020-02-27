from phone_field import PhoneField
from django.db import models


# Create your models here.
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
    PAY_FORM_CHOICE = (
        ('1', 'Безнал'),
        ('2', 'Нал'),
        ('3', 'БК'),
        ('4', 'Безнал/Нал'),
        ('5', 'Безнал/БК')
    )
    pay_form = models.CharField(max_length=1, choices=PAY_FORM_CHOICE, verbose_name='форма оплати',
                                help_text='Оберіть форму оплати')
    name = models.CharField(max_length=128, verbose_name='Назва', blank=False)
    login = models.CharField(max_length=128, verbose_name="Ім'я користувача", blank=False)
    STATUS_FORM_CHOICE = (
        ('1', 'активний'),
        ('2', 'видалений')
    )
    status = models.CharField(null=True, max_length=1, choices=STATUS_FORM_CHOICE, verbose_name='Статус', help_text='Оберіть статус клієнта')
    contacts = models.ManyToManyField(ContactProfile, verbose_name='Контактні особи', related_name='client_field')
    address = models.OneToOneField(ClientPostAddress, null=True, on_delete=models.CASCADE, verbose_name='Поштова адреса', related_name='client')

    def __str__(self):
        return '"{}"  |  логін: {}  | статус: {} | форма оплати: {}'.format(
            self.name,
            self.login,
            self.get_status_display(),
            self.get_pay_form_display(),

        )

    class Meta:
        verbose_name_plural = "Клієнти"