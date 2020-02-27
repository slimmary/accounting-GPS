from phone_field import PhoneField
from django.db import models


# Create your models here.
class ContactProfile(models.Model):
    firstname = models.CharField(max_length=50, help_text='Прізвище')
    surname = models.CharField(max_length=50, help_text="І'мя")
    patronymic = models.CharField(max_length=50, help_text='По батькові')
    position = models.CharField(max_length=50, help_text='Посада')
    phone = PhoneField(null=True, help_text='Контактний номер телефону')
    phone_2 = PhoneField(null=True, blank=True, help_text='додатковий контактний номер телефону')
    email = models.EmailField(null=True, max_length=254, help_text='Контактна електронна адреса')

    def __str__(self):
        return '{} {} {} '.format(self.firstname, self.surname, self.patronymic)


class ClientPostAddress(models.Model):
    index = models.IntegerField(help_text='Пштовий індекс')
    region = models.CharField(max_length=50, help_text='Область')
    district = models.CharField(max_length=50, help_text='Район', blank=True)
    city = models.CharField(max_length=50, help_text='Місто')
    street = models.CharField(max_length=200, help_text='Вулиця')
    house = models.CharField(max_length=50, help_text='Номер будинку')
    office = models.CharField(max_length=50, help_text='Номер офісу або квартири')

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.index, self.region, self.district, self.city,
                                             self.street, self.house, self.office)


class Client(models.Model):
    PAY_FORM_CHOICE = (
        ('1', 'Безнал'),
        ('2', 'Нал'),
        ('3', 'БК'),
        ('4', 'Безнал/Нал'),
        ('5', 'Безнал/БК')
    )
    pay_form = models.CharField(max_length=1, choices=PAY_FORM_CHOICE,
                                help_text='Оберіть форму оплати')
    name = models.CharField(max_length=128, blank=False)
    login = models.CharField(max_length=128, blank=False)
    STATUS_FORM_CHOICE = (
        ('1', 'активний'),
        ('2', 'видалений')
    )
    status = models.CharField(null=True, max_length=1, choices=STATUS_FORM_CHOICE, help_text='Оберіть статус клієнта')
    contacts = models.ManyToManyField(ContactProfile, related_name='client_field')
    address = models.OneToOneField(ClientPostAddress, null=True, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return '{} {} {} {}'.format(self.pay_form, self.name, self.login, self.status)
