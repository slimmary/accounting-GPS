from django.db import models
from datetime import date
from clients.models import Client
from products.models import Gps
from django.core.exceptions import ValidationError


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

    if quarter == 'Перший':
        first_month = 'січень'
        second_month = 'лютий'
        third_mont = 'березень'
    elif quarter == 'Другий':
        first_month = 'квітень'
        second_month = 'травень'
        third_mont = 'червень'
    if quarter == 'Третій':
        first_month = 'липень'
        second_month = 'серпень'
        third_mont = 'вересень'
    else:
        first_month = 'жовтень'
        second_month = 'листопад'
        third_mont = 'грудень'

    rate_ua = models.CharField(null=True,
                               max_length=100,
                               verbose_name="Ураїна",
                               help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                               blank=True
                               )

    rate_world = models.CharField(null=True,
                                  max_length=100,
                                  verbose_name="Світ",
                                  help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                  blank=True
                                  )
    rate_ua_world = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name="Україна+Світ",
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )
    rate_pause = models.CharField(null=True,
                                  max_length=100,
                                  verbose_name="Пауза",
                                  help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                  blank=True
                                  )

    rate_own_sim = models.CharField(null=True,
                                    max_length=100,
                                    verbose_name="Власна Сім",
                                    help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                    blank=True
                                    )
    price = models.IntegerField(null=True,
                                default=0,
                                verbose_name="Вартість грн/міс",
                                help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                blank=True
                                )

    class Status_payment:
        paid = 'Сплачено'
        not_paid = 'НЕ сплачено'
        partially_paid = 'Частково сплачено'

    PAYMENT_CHOICE = (
        (Status_payment.paid, 'Сплачено'),
        (Status_payment.not_paid, 'НЕ сплачено'),
        (Status_payment.partially_paid, 'Частково сплачено'),
    )
    status = models.CharField(max_length=100,
                              default=Status_payment.not_paid,
                              choices=PAYMENT_CHOICE,
                              verbose_name='Статус оплати',
                              help_text='Оберіть статус оплати',
                              blank=True
                              )
    activation = models.BooleanField(default=False, verbose_name="Статус активації", )

    activation_sum = models.IntegerField(null=True,
                                         default=0,
                                         verbose_name="Сума активації",
                                         help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                         blank=True
                                         )

    def save(self, *args, **kwargs):
        all_gps = self.client.gps.all()

        def get_rate_ua(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client=i.Rate.ua).count()

        self.rate_ua = get_rate_ua(all_gps)

        def get_world(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client=i.Rate.world).count()

        self.rate_world = get_world(all_gps)

        def get_ua_world(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client=i.Rate.ua_world).count()

        self.rate_ua_world = get_ua_world(all_gps)

        def get_pause(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client=i.Rate.pause).count()

        self.rate_pause = get_pause(all_gps)

        def get_own_sim(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client=i.Rate.own_sim).count()

        self.rate_own_sim = get_own_sim(all_gps)

        def get_activation_sum(all_gps):
            if self.activation is True:
                quantity = all_gps.count()
                return quantity * 20
            else:
                return 0

        self.activation_sum = get_activation_sum(all_gps)

        def get_price(all_gps):
            return sum((gps.rate_price for gps in all_gps), self.activation_sum)

        self.price = get_price(all_gps)

        super(Subscription, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {} року'.format(self.get_quarter_display(), self.year)

    class Meta:
        verbose_name_plural = "АП звітність "


class Letters(models.Model):
    date = models.DateField(null=True,
                            verbose_name='Дата листа',
                            help_text='Оберіть дату'
                            )
    client = models.ForeignKey(Client,
                               null=True,
                               on_delete=models.CASCADE,
                               max_length=100,
                               verbose_name='Покупець/Абонент',
                               help_text='Оберіть клієнта від якого реєструється звернення',
                               blank=True
                               )

    class Action:
        delete = 'Видалення'
        change = 'Зміна тарифу'

    ACTION_CHOICE = (
        (Action.delete, 'Видалення'),
        (Action.change, 'Зміна тарифу'),
    )

    action = models.CharField(max_length=100,
                              choices=ACTION_CHOICE,
                              verbose_name='Дія',
                              help_text='Оберіть дію')

    gps = models.ForeignKey(Gps,
                            on_delete=models.CASCADE,
                            verbose_name='БР',
                            related_name='letters',
                            default=None,
                            help_text='Оберіть реєстратор для зміни'
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

    gps_rate = models.CharField(null=True,
                                max_length=100,
                                verbose_name='з тарифу',
                                help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                blank=True)

    new_rate = models.CharField(null=True,
                                max_length=100,
                                choices=RATE_CHOICE,
                                verbose_name='на тариф',
                                help_text='Оберіть тариф на який змінюється',
                                blank=True)

    def clean(self):
        if self.gps.owner != self.client:
            raise ValidationError('Реєстратор не належить клієнту, ці данні не будуть збережені, оберіть реєстратор, '
                                  'який належить клієнту')

    def save(self, *args, **kwargs):
        try:
            self.gps.owner = self.client
            if self.action == self.Action.change:
                self.gps_rate = self.gps.rate_client
                self.gps.rate_client = self.new_rate
            else:
                self.gps_rate = None
                self.new_rate = None
                self.gps.rate_client = None
                self.gps.owner = None
                self.gps.vehicle = None
                self.gps__fuel_sensor = None
                self.gps.rate_price = 0
        except IndexError:
            raise ValidationError('Реєстратор не належить клієнту, ці данні не будуть збережені, оберіть реєстратор, '
                                  'який належить клієнту')
        super(Letters, self).save(*args, **kwargs)
        Gps.save(self.gps, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Звернення/листи"
