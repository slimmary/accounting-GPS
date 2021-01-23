from django.db import models
from phone_field import PhoneField
from datetime import date


class Staff(models.Model):
    lastname = models.CharField(max_length=50, verbose_name='Прізвище')
    name = models.CharField(max_length=50, verbose_name="І'мя")
    position = models.CharField(max_length=50, verbose_name='Посада')
    birthday = models.DateField(verbose_name='Дата народженя')
    day_start = models.DateField(verbose_name='Дата початку робти')
    phone_1 = PhoneField(null=True, verbose_name='робочий № телефону')
    phone_2 = PhoneField(null=True, verbose_name='персональний № телефону', blank=True)
    email_1 = models.EmailField(null=True, max_length=254, verbose_name='робоча електронна адреса')
    email_2 = models.EmailField(null=True, max_length=254, verbose_name='персональна електронна адреса', blank=True)

    def __str__(self):
        return '{} {}'.format(self.lastname, self.name)

    class Meta:
        verbose_name_plural = "Співробітники"
