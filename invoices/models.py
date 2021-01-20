from django.db import models
from datetime import date
from subscription.models import Subscription


class Invoice(models.Model):

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
    invoice_sum = models.PositiveIntegerField(null=True,
                                                default=0,
                                                verbose_name='сума до сплати',
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


class SubInvoice(Invoice):
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE,
                                     verbose_name='АП',
                                     related_name='invoice'
                                     )
    provider = models.CharField(null=True,
                                max_length=100,
                                verbose_name='Постачальник',
                                help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                blank=True
                                )
    client = models.CharField(null=True,
                              max_length=100,
                              verbose_name='Клієнт',
                              help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                              blank=True
                              )

    def save(self, *args, **kwargs):
        self.provider = self.subscription.client.provider
        self.client = self.subscription.client.name

        super(SubInvoice, self).save(*args, **kwargs)

    def __str__(self):
        return 'РФ №{} від {} '.format(self.number, self.date)

    class Meta:
        verbose_name_plural = "АП рахунки фактури "