from django.db import models
from clients.models import Client


class Vehicle(models.Model):
    TYPE_VEHICLE_CHOICE = (
        ('1', 'Тягач'),
        ('2', 'Легкове авто'),
        ('3', 'Мікроавтобус'),
        ('4', 'Екскаватор'),
        ('5', 'Навантажувач'),
        ('6', 'Трактор'),
        ('7', 'Оприскувач'),
        ('8', 'Комбайн'),
        ('9', 'Асфальтоукладник'),
        ('10', 'Фреза'),
        ('11', 'Каток'),
        ('12', 'Інше'),

    )
    type = models.CharField(max_length=1, choices=TYPE_VEHICLE_CHOICE, verbose_name='Тип ТЗ',
                            help_text='Оберіть тип Транспортного Засобу', blank=True)
    make = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name="Модель", blank=True)
    number = models.CharField(max_length=50, verbose_name=' Ідентифікатор (держ.номер)')
    owner = models.ForeignKey(Client,
                              null=True,
                              on_delete=models.CASCADE,
                              verbose_name='Власник',
                              related_name='vehicle',
                              blank=True
                              )

    class Rate:
        ua = 'Україна'
        world = 'Світ'
        pause = 'Пауза'
        own_sim = 'Власна сім'
        personal = 'Персональний'

    RATE_CHOICE = (
        (Rate.ua, 'Україна'),
        (Rate.world, 'Світ'),
        (Rate.pause, 'Пауза'),
        (Rate.own_sim, 'Власна сім'),
        (Rate.personal, 'Персональний')
    )

    rate_client = models.CharField(null=True,
                                   choices=RATE_CHOICE,
                                   max_length=100,
                                   verbose_name='Тариф',
                                   help_text='Тариф заповниться автоматично нічого не потрібно вводити',
                                   blank=True
                                   )

    rate_price = models.IntegerField(null=True,
                                     default=0,
                                     verbose_name='Вартість грн/міс',
                                     help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                     blank=True
                                     )

    def save(self, *args, **kwargs):
        if self.owner is None:
            self.rate_client = 0
        else:
            gps = self.gps if hasattr(self, 'gps') else None
            if gps:
                if self.rate_client == self.Rate.pause:
                    if self.owner.provider.tax_type == self.owner.provider.Taxtype.taxfree:
                        self.rate_price = 30
                    else:
                        self.rate_price = 36
                else:
                    if self.rate_client != self.Rate.personal:
                        if self.gps.sim_1 is None and self.gps.sim_2 is None:
                            self.rate_client = self.Rate.own_sim
                            if self.owner.provider.tax_type == self.owner.provider.Taxtype.taxfree:
                                self.rate_price = 60
                            else:
                                self.rate_price = 72
                        else:
                            if self.gps.sim_2 is None:
                                if self.owner.provider.tax_type == self.owner.provider.Taxtype.taxfree:
                                    if self.gps.sim_1.operator == self.gps.sim_1.Operator.travelsim or self.gps.sim_1.operator == self.gps.sim_1.Operator.goodline:
                                        self.rate_client = self.Rate.world
                                        self.rate_price = 270
                                    else:
                                        self.rate_client = self.Rate.ua
                                        self.rate_price = 120
                                else:
                                    if self.gps.sim_1.operator == self.gps.sim_1.Operator.travelsim or self.gps.sim_1.operator == self.gps.sim_1.Operator.goodline:
                                        self.rate_client = self.Rate.world
                                        self.rate_price = 324
                                    else:
                                        self.rate_client = self.Rate.ua
                                        self.rate_price = 144
                            else:
                                self.rate_client = self.Rate.world
                                if self.owner.provider.tax_type == self.owner.provider.Taxtype.taxfree:
                                    self.rate_price = 270
                                else:
                                    self.rate_price = 324
            else:
                self.rate_client = '-'
                self.rate_price = 0
        super(Vehicle, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {} {} держ.номер {} '.format(
            self.get_type_display(),
            self.make,
            self.model,
            self.number,
            self.owner,
        )

    class Meta:
        verbose_name_plural = "Транспортні засоби"
