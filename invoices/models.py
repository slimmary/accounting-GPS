from django.db import models
from projects.models import Project
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
                                              help_text='Ведіть суму',
                                              blank=True
                                              )
    date_payment = models.DateField(null=True,
                                    verbose_name='Дата оплати',
                                    help_text='Оберіть дату оплати',
                                    blank=True
                                    )

    class Meta:
        abstract = True


class ServiceInvoice(Invoices):
    def __str__(self):
        return 'РФ №{} від {} '.format(self.number, self.date)

    class Meta:
        verbose_name_plural = "рахунки на послуги"


class SubInvoice(Invoices):
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
    subscription = models.ForeignKey(Subscription,
                                     null=True,
                                     on_delete=models.CASCADE,
                                     verbose_name='РФ',
                                     related_name='sub_invoice',
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
        verbose_name_plural = "АП рахунки фактури"


class SaleInvoice(models.Model):
    number = models.PositiveIntegerField(null=True,
                                         default=0,
                                         verbose_name='№',
                                         help_text='Номер',
                                         )
    date = models.DateField(null=True,
                            verbose_name='Дата створення',
                            help_text='Оберіть дату'
                            )

    class StatusChoice:
        created = 'Створено'
        in_stock = 'В наявності'

    STATUS_CHOICE = (
        (StatusChoice.created, 'Створено'),
        (StatusChoice.in_stock, 'В наявності')
    )
    status = models.CharField(max_length=100,
                              choices=STATUS_CHOICE,
                              verbose_name='Статус',
                              help_text='Оберіть статус договору',
                              default=StatusChoice.created
                              )
    status_date = models.DateField(null=True,
                                   verbose_name='Дата зміни статусу',
                                   help_text='Оберіть дату',
                                   blank=True
                                   )

    def __str__(self):
        return 'ВН №{} від {} '.format(self.number, self.date)

    class Meta:
        verbose_name_plural = "Видаткові Накладні до проектів"


class ProjectInvoice(Invoices):
    pay_form = models.CharField(null=True,
                                max_length=100,
                                verbose_name='Форма оплати',
                                help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                blank=True
                                )

    client = models.CharField(null=True,
                              max_length=100,
                              verbose_name='Клієнт',
                              help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                              blank=True
                              )
    project = models.ForeignKey(Project,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='Проект',
                                related_name='project_invoice',
                                blank=True
                                )
    saleinvoice = models.OneToOneField(SaleInvoice,
                                       null=True,
                                       on_delete=models.CASCADE,
                                       verbose_name='ВН',
                                       related_name='project_invoice',
                                       blank=True)

    def save(self, *args, **kwargs):
        if self.project is not None:
            if self.project.provider.tax_type == self.project.provider.Taxtype.taxfree:
                self.pay_form = 'КО'
            else:
                self.pay_form = 'РФ'
        self.client = self.project.client.name
        if self.status_payment == self.Status_payment.paid:
            self.sum_payment = self.invoice_sum
        else:
            if self.sum_payment == 0:
                self.status_payment = self.Status_payment.not_paid
            elif self.sum_payment == self.invoice_sum:
                self.status_payment = self.Status_payment.paid
            else:
                self.status_payment = self.Status_payment.partially_paid

        super(ProjectInvoice, self).save(*args, **kwargs)

    def __str__(self):
        return '{} №{} від {} '.format(self.pay_form, self.number, self.date)

    class Meta:
        db_table = 'projectinvoice'
        verbose_name_plural = "рахунки фактури та касові ордери проекти"
