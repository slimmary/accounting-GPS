from django.db import models
from datetime import date
from clients.models import Client
from products.models import Gps


class Subscription(models.Model):
    date_init = date.today()
    if date_init.month == 3:
        quarter_choice = 'Другий'
    elif date_init.month == 6:
        quarter_choice = 'Третій'
    elif date_init.month == 9:
        quarter_choice = 'Четвертий'
    elif date_init.month == 12:
        quarter_choice = 'Перший'
    else:
        quarter_choice = 'Оберіть квартал в ручну'

    class Quarter:
        first = 'Перший'
        second = 'Другий'
        third = 'Третій'
        fourth = 'Четвертий'

    QUARTER_CHOICE = (
        (Quarter.first, 'Перший'),
        (Quarter.second, 'Другий'),
        (Quarter.third, 'Третій'),
        (Quarter.fourth, 'Четвертий')
    )
    quarter = models.CharField(max_length=100, default=quarter_choice, choices=QUARTER_CHOICE, verbose_name='Квартал')
    year = date.today().year
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Платник', related_name='subscription')

    def __str__(self):
        return '{} {} року'.format(self.get_quarter_display(), self.year)

    class Meta:
        verbose_name_plural = "АП звітність "


class Letters(models.Model):
    date = models.DateField(null=True, verbose_name='Дата листа', help_text='Оберіть дату')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупець/Абонент',
                               related_name='letters')

    class Action:
        delete = 'Видалення'
        change = 'Зміна тарифу'

    ACTION_CHOICE = (
        (Action.delete, 'Видалення'),
        (Action.change, 'Зміна тарифу'),
    )
    action = models.CharField(max_length=1, choices=ACTION_CHOICE, verbose_name='Дія',
                              help_text='Оберіть дію')
    gps = models.ManyToManyField(Gps, verbose_name='БР', related_name='letters')

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
    old_rate = models.CharField(null=True, max_length=1, choices=RATE_CHOICE, verbose_name='з тарифу',
                                help_text='Оберіть тариф який змінюється', blank=True)
    new_rate = models.CharField(null=True, max_length=1, choices=RATE_CHOICE, verbose_name='на тариф',
                                help_text='Оберіть тариф на який змінюється', blank=True)

    class Meta:
        verbose_name_plural = "Звернення/листи"
