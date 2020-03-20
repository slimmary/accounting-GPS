from django.db import models
import datetime
from clients.models import Client
from products.models import Gps


class Subscription(models.Model):
    QUARTER_CHOICE = (
        ('1', 'Перший'),
        ('2', 'Другий'),
        ('3', 'Третій'),
        ('4', 'Четвертий')
    )
    quarter = models.CharField(max_length=1, choices=QUARTER_CHOICE, verbose_name='Квартал',
                                help_text='Оберіть оператора')
    year = datetime.datetime.now().year
    client = models.OneToOneField(Client, on_delete=models.CASCADE, verbose_name='Платник',
                               related_name='subscription')
    PROVIDER_CHOICE = (
        ('1', 'ТОВ "Системи Контролю Транспорту"'),
        ('2', 'ФОП Шевчук С.І.'),
        ('3', 'ФОП Дячук Л.В.'),
        ('4', 'БК/ІНШЕ')
    )
    provider = models.CharField(null=True, max_length=1, choices=PROVIDER_CHOICE, verbose_name='Постачальник',
                                help_text='Оберіть постачальника')

    def __str__(self):
        return '{} {} року'.format(self.get_quarter_display(), self.year)

    class Meta:
        verbose_name_plural = "АП звітність "


class Letters(models.Model):
    date = models.DateField(null=True, verbose_name='Дата листа', help_text='Оберіть дату')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупець/Абонент',
                               related_name='letters')
    ACTION_CHOICE = (
        ('1', 'Видалення'),
        ('2', 'Зміна тарифу'),
    )
    action = models.CharField(max_length=1, choices=ACTION_CHOICE, verbose_name='Дія',
                              help_text='Оберіть дію')
    gps = models.ForeignKey(Gps, null=True, on_delete=models.CASCADE, verbose_name='БР', related_name='letters')

    RATE_CHOICE = (
        ('1', 'Україна'),
        ('2', 'Світ'),
        ('3', 'Пауза'),
        ('4', 'Власна сім'),
    )
    old_rate = models.CharField(null=True, max_length=1, choices=RATE_CHOICE, verbose_name='з тарифу',
                                help_text='Оберіть тариф який змінюється', blank=True)
    new_rate = models.CharField(null=True, max_length=1, choices=RATE_CHOICE, verbose_name='на тариф',
                                help_text='Оберіть тариф на який змінюється', blank=True)

    class Meta:
        verbose_name_plural = "Звернення/листи"