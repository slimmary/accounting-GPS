from django.db import models
from datetime import date
from subscription.models import Subscription
from projects.models import Project


class Invoice(models.Model):
    number = models.PositiveIntegerField(null=True,
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
    status_payment = models.CharField(default=Status_payment.not_paid,
                                      choices=PAYMENT_CHOICE,
                                      max_length=100,
                                      verbose_name='Статус оплати',
                                      help_text='Оберіть статус оплати',
                                      blank=True
                                      )
    sum_payment = models.PositiveIntegerField(null=True,
                                              default=0,
                                              verbose_name='сума оплати',
                                              help_text='Ведіть суму, якщо оплата часткова',
                                              blank=True
                                              )
    date_payment = models.DateField(null=True,
                                    verbose_name='Дата оплати',
                                    help_text='Заповниться автоматично',
                                    blank=True
                                    )

    def save(self, *args, **kwargs):
        if self.status_payment == self.Status_payment.paid:
            self.sum_payment = self.invoice_sum
        super(Invoice, self).save(*args, **kwargs)


class SubInvoice(Invoice):
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE,
                                     verbose_name='АП',
                                     related_name='sub_invoice'
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


class ProjectInvoice(Invoice):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                verbose_name='Проект',
                                related_name='project_invoice'
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
        self.provider = self.project.client.provider
        self.client = self.project.client.name

        super(ProjectInvoice, self).save(*args, **kwargs)

    def __str__(self):
        return 'РФ №{} від {} '.format(self.number, self.date)

    class Meta:
        verbose_name_plural = "Проекти рахунки фактури "


class ProjectInvoiceTaxfree(Invoice):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                verbose_name='Проект',
                                related_name='project_invoice_taxfree'
                                )

    def __str__(self):
        return 'KO №{} від {} '.format(self.number, self.date)

    class Meta:
        verbose_name_plural = "Касові Ордера (КО)"
