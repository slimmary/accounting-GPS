from django.db import models
from datetime import date
from projects.models import Project
from workorders.models import WorkOrder
from subscription.models import Subscription


class Invoices(models.Model):
    number = models.PositiveIntegerField(null=True,
                                         default=0,
                                         verbose_name='№',
                                         help_text='Номер',
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

    class Meta:
        abstract = True


class Invoice(Invoices):
    work_order = models.OneToOneField(WorkOrder,
                                      null=True,
                                      on_delete=models.CASCADE,
                                      verbose_name='ЗН',
                                      related_name='invoice_workorder',
                                      blank=True)

    class Meta:
        verbose_name_plural = "рахунки на послуги"


class SubInvoice(Invoices):
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
        db_table = 'subinvoice'
        verbose_name_plural = "АП рахунки фактури "


class ProjectInvoice(Invoices):
    project_to = models.OneToOneField(Project,
                                      null=True,
                                      on_delete=models.CASCADE,
                                      verbose_name='РФ/КО',
                                      related_name='project_invoice',
                                      blank=True
                                      )

    class PayForm:
        taxfree = 'КО'
        tax = 'РФ'

    PAY_CHOICE = (
        (PayForm.taxfree, 'КО'),
        (PayForm.tax, 'РФ'),
    )
    pay_form = models.CharField(max_length=100,
                                default=PayForm.taxfree,
                                choices=PAY_CHOICE,
                                verbose_name='РФ/КО',
                                help_text='Оберіть форму оплати',
                                blank=True
                                )

    # client = models.CharField(null=True,
    #                           max_length=100,
    #                           verbose_name='Клієнт',
    #                           help_text='Поле заповниться автоматично, вводити нічого не потрібно',
    #                           blank=True
    #                           )
    #
    # def save(self, *args, **kwargs):
    #     if self.project_invoice is not None:
    #         self.client = self.project_invoice.client
    #     super(ProjectInvoice, self).save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if self.status_payment == self.Status_payment.paid:
            self.sum_payment = self.invoice_sum
        else:
            if self.sum_payment== 0:
                self.status_payment = self.Status_payment.not_paid
            else:
                self.status_payment = self.Status_payment.partially_paid

        super(ProjectInvoice, self).save(*args, **kwargs)

    def __str__(self):
        return '{} №{} від {} '.format(self.pay_form, self.number, self.date)

    class Meta:
        db_table = 'projectinvoice'
        verbose_name_plural = "Проекти рахунки фактури та касові ордери "
