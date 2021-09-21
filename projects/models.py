from django.db import models
from datetime import date
from clients.models import Client, Provider
from contracts.models import Contract, Additions
from django.core.exceptions import ObjectDoesNotExist, ValidationError


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
                                  verbose_name='Дата створення',
                                  )
    date_finish = models.DateField(null=True,
                                   verbose_name='Дата завершення',
                                   blank=True
                                   )
    provider = models.ForeignKey(Provider,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Постачальник',
                                 help_text='Оберіть постачальника',
                                 related_name='project',
                                 )
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='клієнт',
                               related_name='project'
                               )
    amount_gps = models.PositiveIntegerField(null=True,
                                             default=0,
                                             verbose_name='кіл-ть СКТ',
                                             help_text='введіть кількість',
                                             blank=True
                                             )
    amount_fuel_sensor = models.PositiveIntegerField(null=True,
                                                     default=0,
                                                     verbose_name='кіл-ть ДВРП',
                                                     help_text='введіть кількість',
                                                     blank=True
                                                     )
    add_costs = models.PositiveIntegerField(null=True,
                                            default=0,
                                            verbose_name='дод. витрати грн',
                                            help_text='введіть суму',
                                            blank=True
                                            )
    sum = models.PositiveIntegerField(null=True,
                                      verbose_name='загальна сума проекту',
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

    contract_project_to = models.OneToOneField(Contract,
                                               null=True,
                                               on_delete=models.CASCADE,
                                               verbose_name='Договір',
                                               related_name='project_contract',
                                               blank=True
                                               )
    addition = models.OneToOneField(Additions,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Дод.угода',
                                    related_name='project_additions',
                                    blank=True
                                    )

    def clean(self):
        if self.date_finish and self.project_status != self.StatusProject.finished:
            raise ValidationError({'date_finish': "не можна обрати дату завершення, якщо проект ще не завершений"})
        if self.addition:
            if self.addition.contract_to.type != self.addition.contract_to.TypeChoice.project:
                raise ValidationError(
                    {'addition': "до проекту не можливо ДУ, який має відношення до договору поставки"})
        elif self.contract_project_to:
            if self.contract_project_to.type != self.contract_project_to.TypeChoice.project:
                raise ValidationError({'contract_project_to': "до проекту не можливо договір, який не є договором "
                                                              "поставки"})

    def save(self, *args, **kwargs):
        if self.list_project_works is not None:
            wo = self.list_project_works.all()
            wo_amount_gps = 0
            wo_amount_fuel_sensor = 0
            for i in wo:
                wo_amount_gps += i.count_gps
                wo_amount_fuel_sensor += i.count_fuel
            if self.amount_gps == wo_amount_gps and self.amount_fuel_sensor == wo_amount_fuel_sensor:
                self.execution_status = self.ExecutionStatus.finished
            elif self.amount_gps > wo_amount_gps > 0 or self.amount_fuel_sensor > wo_amount_fuel_sensor > 0:
                self.execution_status = self.ExecutionStatus.partly_executed
        if self.execution_status == self.ExecutionStatus.finished:
            if self.provider.tax_type == self.provider.Taxtype.taxfree:
                check = 0
                for invoice in self.project_invoice.all():
                    if invoice.status_payment != invoice.Status_payment.paid:
                        check += 1
                if check == 0:
                    self.project_status = self.StatusProject.finished
            else:
                check = 0
                for invoice in self.project_invoice.all():
                    if invoice.status_payment != invoice.Status_payment.paid or invoice.saleinvoice is None\
                            or invoice.saleinvoice.status != invoice.saleinvoice.StatusChoice.in_stock:
                        check += 1

                if check == 0 and self.addition and self.addition.status == self.addition.StatusChoice.in_stock:
                    self.project_status = self.StatusProject.finished

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return 'Проект №{} від {} '.format(self.number, self.date_start)

    class Meta:
        verbose_name_plural = "Проекти"
