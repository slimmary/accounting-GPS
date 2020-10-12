from django.db import models
from datetime import date
from clients.models import Client
from products.models import Gps
from django.core.exceptions import ValidationError
from django.utils import timezone


class Subscription(models.Model):
    date_init = models.DateField(null=True,
                                 verbose_name='Дата створення',
                                 help_text='Дата заповниться автоматично',
                                 auto_now_add=True,
                                 )

    year = models.CharField(verbose_name='Рік',
                            help_text='Заповниться автоматично',
                            max_length=10,
                            null=True,
                            blank=True,
                            )

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
    quarter = models.CharField(max_length=100,
                               default=Quarter.first,
                               choices=QUARTER_CHOICE,
                               verbose_name='Квартал'
                               )

    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Платник',
                               related_name='subscription'
                               )

    first_month = '1 міс'
    second_month = '2 міс'
    third_month = '3 міс'

    price_quarter = models.PositiveIntegerField(null=True,
                                                default=0,
                                                verbose_name="нараховано",
                                                help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                                blank=True
                                                )

    sum_payment = models.PositiveIntegerField(null=True,
                                              default=0,
                                              verbose_name="сплачено",
                                              help_text='Введть суму, що сплатив клієнт',
                                              blank=True
                                              )
    sum_to_pay = models.IntegerField(null=True,
                                     default=0,
                                     verbose_name="залишок",
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
    date_payment = models.DateField(null=True,
                                    verbose_name='Дата оплати',
                                    help_text='Заповниться автоматично',
                                    blank=True
                                    )
    activation = models.BooleanField(default=False, verbose_name="активація", )

    activation_sum = models.PositiveIntegerField(null=True,
                                                 default=0,
                                                 verbose_name="Сума активації",
                                                 help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                                 blank=True
                                                 )

    rate_ua_1m = models.CharField(null=True,
                                  max_length=100,
                                  verbose_name="{} - Укр".format(first_month),
                                  help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                  blank=True
                                  )

    rate_world_1m = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name="{} - Св".format(first_month),
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )

    rate_pause_1m = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name="{} - П".format(first_month),
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )
    rate_own_sim_1m = models.CharField(null=True,
                                       max_length=100,
                                       verbose_name="{} - ВС".format(first_month),
                                       help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                       blank=True
                                       )
    all_1m = models.CharField(null=True,
                              max_length=100,
                              verbose_name="{} - БР".format(first_month),
                              help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                              blank=True
                              )
    rate_ua_2m = models.CharField(null=True,
                                  max_length=100,
                                  verbose_name="{} - Укр".format(second_month),
                                  help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                  blank=True
                                  )

    rate_world_2m = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name="{} - Св".format(second_month),
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )

    rate_pause_2m = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name="{} - П".format(second_month),
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )
    rate_own_sim_2m = models.CharField(null=True,
                                       max_length=100,
                                       verbose_name="{} - ВС".format(second_month),
                                       help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                       blank=True
                                       )
    all_2m = models.CharField(null=True,
                              max_length=100,
                              verbose_name="{} - БР".format(second_month),
                              help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                              blank=True
                              )

    rate_ua_3m = models.CharField(null=True,
                                  max_length=100,
                                  verbose_name="{} - Укр".format(third_month),
                                  help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                  blank=True
                                  )
    rate_world_3m = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name="{} - Св".format(third_month),
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )

    rate_pause_3m = models.CharField(null=True,
                                     max_length=100,
                                     verbose_name="{} - П".format(third_month),
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )

    rate_own_sim_3m = models.CharField(null=True,
                                       max_length=100,
                                       verbose_name="{} - ВС".format(third_month),
                                       help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                       blank=True
                                       )
    all_3m = models.CharField(null=True,
                              max_length=100,
                              verbose_name="{} - БР".format(third_month),
                              help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                              blank=True
                              )

    price_1m = models.PositiveIntegerField(null=True,
                                           default=0,
                                           verbose_name="грн/{}".format(first_month),
                                           help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                           blank=True
                                           )
    price_2m = models.PositiveIntegerField(null=True,
                                           default=0,
                                           verbose_name="грн/{}".format(second_month),
                                           help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                           blank=True
                                           )
    price_3m = models.PositiveIntegerField(null=True,
                                           default=0,
                                           verbose_name="грн/{}".format(third_month),
                                           help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                           blank=True
                                           )

    def save(self, *args, **kwargs):
        if self.date_init is None:
            self.date_init = date.today()
        self.year = self.date_init.year
        if self.date_init.month == 3:
            self.quarter = 'Другий'
        elif self.date_init.month == 6:
            self.quarter = 'Третій'
        elif self.date_init.month == 9:
            self.quarter = 'Четвертий'
        elif self.date_init.month == 12:
            self.quarter = 'Перший'
        else:
            self.quarter = self.quarter

        all_gps = self.client.gps.all()

        m1 = date(self.date_init.year, (self.date_init.month + 1), 15)
        m2 = date(self.date_init.year, (self.date_init.month + 2), 15)
        m3 = date(self.date_init.year, (self.date_init.month + 3), 15)

        date_save = date.today()  # date of saving

        def get_rate_ua(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client_1=i.Rate.ua).count()

        def get_world(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client_1=i.Rate.world).count() + all_gps.filter(
                    rate_client_2=i.Rate.world).count()

        def get_pause(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client_1=i.Rate.pause).count()

        def get_own_sim(all_gps):
            for i in all_gps:
                return all_gps.filter(rate_client_1=i.Rate.own_sim).count()

        def get_price(all_gps):
            return sum((gps.rate_price for gps in all_gps))

        if m1 > date_save >= self.date_init:  # if date saving is between date of init and date_init + 15 days -
            # updating all months and prices
            self.all_1m = all_gps.count()
            self.all_2m = all_gps.count()
            self.all_3m = all_gps.count()

            self.rate_ua_1m = get_rate_ua(all_gps)
            self.rate_ua_2m = get_rate_ua(all_gps)
            self.rate_ua_3m = get_rate_ua(all_gps)

            self.rate_world_1m = get_world(all_gps)
            self.rate_world_2m = get_world(all_gps)
            self.rate_world_3m = get_world(all_gps)

            self.rate_pause_1m = get_pause(all_gps)
            self.rate_pause_2m = get_pause(all_gps)
            self.rate_pause_3m = get_pause(all_gps)

            self.rate_own_sim_1m = get_own_sim(all_gps)
            self.rate_own_sim_2m = get_own_sim(all_gps)
            self.rate_own_sim_3m = get_own_sim(all_gps)

            self.price_1m = get_price(all_gps)
            self.price_2m = get_price(all_gps)
            self.price_3m = get_price(all_gps)

        elif m1 < date_save < m2:  # if date saving is between 15.1month and 15.2month - updating 2d and 3th
            # months and prices
            self.all_2m = all_gps.count()
            self.all_3m = all_gps.count()

            self.rate_ua_2m = get_rate_ua(all_gps)
            self.rate_ua_3m = get_rate_ua(all_gps)

            self.rate_world_2m = get_world(all_gps)
            self.rate_world_2m = get_world(all_gps)

            self.rate_pause_2m = get_pause(all_gps)
            self.rate_pause_3m = get_pause(all_gps)

            self.rate_own_sim_2m = get_own_sim(all_gps)
            self.rate_own_sim_3m = get_own_sim(all_gps)

            self.price_2m = get_price(all_gps)
            self.price_3m = get_price(all_gps)

        elif m2 < date_save < m3:  # if date saving is between 15.2month and 15.3month - updating 3th
            # months and prices
            self.all_3m = all_gps.count()

            self.rate_ua_3m = get_rate_ua(all_gps)

            self.rate_world_2m = get_world(all_gps)

            self.rate_pause_3m = get_pause(all_gps)

            self.rate_own_sim_3m = get_own_sim(all_gps)

            self.price_3m = get_price(all_gps)
        else:
            pass

        def get_activation_sum(all_gps):
            if self.activation is True:
                quantity = all_gps.count()
                return quantity * 20 * 3
            else:
                return 0

        self.activation_sum = get_activation_sum(all_gps)
        if self.sum_payment == 0:
            if self.status == 'Сплачено':
                self.date_payment = date.today()
                self.sum_payment = self.price_quarter
            else:
                self.status = 'НЕ сплачено'
        elif self.price_quarter > self.sum_payment > 0:
            if self.status == 'Сплачено':
                self.date_payment = date.today()
                self.sum_payment = self.price_quarter
            else:
                self.status = 'Частково сплачено'
        elif self.sum_payment >= self.price_quarter:  # if user enter the sum, status will change
            self.status = 'Сплачено'
            self.date_payment = date.today()

        self.price_quarter = self.price_1m + self.price_2m + self.price_3m + self.activation_sum
        self.sum_to_pay = self.price_quarter - self.sum_payment

        super(Subscription, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {} квартал {} року'.format(self.client.name, self.get_quarter_display(), self.year)

    class Meta:
        verbose_name_plural = "АП звітність "


class Invoice(models.Model):
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE,
                                     verbose_name='АП',
                                     related_name='invoice'
                                     )
    client = models.CharField(null=True,
                              max_length=100,
                              verbose_name='Клієнт',
                              help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                              blank=True
                              )
    number = models.CharField(null=True,
                              max_length=100,
                              verbose_name='№',
                              help_text='Номер РФ',
                              blank=True
                              )
    date = models.DateField(null=True,
                            verbose_name='Дата створення',
                            help_text='Оберіть дату'
                            )

    def save(self, *args, **kwargs):
        self.client = self.subscription.client.name

        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):
        return 'РФ №{} від {} '.format(self.number, self.date)

    class Meta:
        verbose_name_plural = "АП рахунки фактури "


class Letters(models.Model):
    date_letter = models.DateField(null=True,
                                   verbose_name='Дата листа',
                                   help_text='Оберіть дату'
                                   )
    client = models.ForeignKey(Client,
                               null=True,
                               on_delete=models.CASCADE,
                               max_length=100,
                               related_name='letters',
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
        except ValidationError:
            raise ValidationError('Реєстратор не належить клієнту, ці данні не будуть збережені, оберіть реєстратор, '
                                  'який належить клієнту')
        super(Letters, self).save(*args, **kwargs)
        Gps.save(self.gps, *args, **kwargs)

    class Meta:
        verbose_name_plural = "Звернення/листи"
