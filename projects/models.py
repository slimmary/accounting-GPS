from django.db import models
from datetime import date
from clients.models import Client
from contracts.models import Contract, Additions
from django.core.exceptions import ValidationError


class Project(models.Model):
    number = models.PositiveIntegerField(null=True,
                                         verbose_name='№',
                                         help_text='Номер проекту',
                                         blank=True
                                         )

    class StatusProject:
        finished = 'Завершено'
        not_finished = 'НЕ завершено'

    STATUS_CHOICE = (
        (StatusProject.finished, 'Завершено'),
        (StatusProject.not_finished, 'НЕ завершено'),
    )
    project_status = models.CharField(max_length=100,
                                      default=StatusProject.not_finished,
                                      choices=STATUS_CHOICE,
                                      verbose_name='Статус проекту',
                                      help_text='Оберіть статус проекту',
                                      blank=True
                                      )
    date_start = models.DateField(default=date.today(),
                                  verbose_name='Дата створення проекту',
                                  )
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='клієнт',
                               related_name='project'
                               )
    amount_gps = models.PositiveIntegerField(null=True,
                                             verbose_name='кіл-ть СКТ',
                                             help_text='введіть кількість',
                                             blank=True
                                             )
    amount_fuel_sensor = models.PositiveIntegerField(null=True,
                                                     verbose_name='кіл-ть ДВРП',
                                                     help_text='введіть кількість',
                                                     blank=True
                                                     )
    add_costs = models.PositiveIntegerField(null=True,
                                            verbose_name='дод. витрати грн',
                                            help_text='введіть суму',
                                            blank=True
                                            )
    sum = models.PositiveIntegerField(null=True,
                                      verbose_name='загальна сума проекту',
                                      help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                      blank=True
                                      )

    class PayForm:
        taxfree = 'КО'
        invoice = 'РФ'

    PAY_CHOICE = (
        (PayForm.taxfree, 'КО'),
        (PayForm.invoice, 'РФ'),
    )
    pay_form = models.CharField(max_length=100,
                                default=PayForm.taxfree,
                                choices=PAY_CHOICE,
                                verbose_name='Форма оплати',
                                help_text='Оберіть форму оплати',
                                blank=True
                                )

    payment_status = models.CharField(null=True,
                                      max_length=100,
                                      verbose_name='Статус оплати',
                                      help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                      blank=True
                                      )
    date_payment = models.CharField(null=True,
                                    max_length=100,
                                    verbose_name='Дата оплати',
                                    help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                    blank=True
                                    )
    sum_payment = models.PositiveIntegerField(null=True,
                                              verbose_name='Сума оплати',
                                              help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                              blank=True
                                              )
    contract = models.OneToOneField(Contract, null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Договір до даного проекту',
                                    related_name='project_to_contract',
                                    blank=True)
    additions = models.OneToOneField(Additions, null=True,
                                     on_delete=models.CASCADE,
                                     verbose_name='ДУ до даного проекту',
                                     related_name='project_to_additions',
                                     blank=True)
    date_receipt_contract = models.DateField(null=True,
                                             verbose_name='Дата отримання договору',
                                             help_text='Введіть дату',
                                             blank=True
                                             )
    date_raceipt_sale_invoice = models.DateField(null=True,
                                                 verbose_name='Дата отримання видаткової накладної',
                                                 help_text='Введіть дату',
                                                 blank=True
                                                 )

    class ExecutionStatus:
        finished = 'Виконано'
        not_executed = 'НЕ виконано'
        partly_executed = 'Частково виконано'

    EXECUTION_CHOICE = (
        (ExecutionStatus.finished, 'Виконано'),
        (ExecutionStatus.not_executed, 'НЕ виконано'),
        (ExecutionStatus.partly_executed, 'Частково виконано'),
    )
    execution_status = models.CharField(max_length=100,
                                        default=ExecutionStatus.not_executed,
                                        choices=EXECUTION_CHOICE,
                                        verbose_name='Статус виконання робіт',
                                        help_text='Оберіть статус',
                                        blank=True
                                        )
    notes = models.CharField(max_length=100,
                             verbose_name='Приміки',
                             blank=True
                             )

    def clean(self):
        if self.contract is not None:
            if self.contract.type != self.contract.TypeChoice.project:
                raise ValidationError("до проекту не можливо додати договір, який не є договором поставки")
        else:
            if self.additions is not None:
                if self.additions.contract_to.type != self.additions.contract_to.TypeChoice.project:
                    raise ValidationError("до проекту не можливо додати ДУ, яка не відноситься до договору поставки")

    def save(self, *args, **kwargs):
        if self.contract is not None:
            if self.contract.status == self.contract.StatusChoice.in_stock:
                self.date_receipt_contract = self.contract.status_date
        else:
            if self.additions is not None:
                if self.additions.status == self.additions.StatusChoice.in_stock:
                    self.date_receipt_contract = self.additions.status_date

        if self.pay_form == self.PayForm.invoice:
            self.sum = self.amount_gps * 4200 + self.amount_fuel_sensor * 3240 + self.add_costs
            if self.project_invoice == None:
                pass
            else:
                self.payment_status = self.project_invoice.status_payment
                self.sum_payment = self.project_invoice.sum_payment
                self.date_payment = self.project_invoice.date_payment

        else:
            self.sum = self.amount_gps * 3500 + self.amount_fuel_sensor * 2700 + self.add_costs
            if self.project_invoice_taxfree is None:
                self.payment_status = self.project_invoice_taxfree.status_payment
                self.sum_payment = self.project_invoice_taxfree.sum_payment
                self.date_payment = self.project_invoice_taxfree.date_payment

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return 'Проект №{} від {} '.format(self.number, self.date_start)

    class Meta:
        verbose_name_plural = "Проекти"
