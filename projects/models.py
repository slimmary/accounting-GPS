from django.db import models
from datetime import date
from clients.models import Client
from django.core.exceptions import ObjectDoesNotExist


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
                                      help_text='Поле заповниться автоматично, вводити нічого не потрібно',
                                      blank=True
                                      )

    date_receipt_contract = models.DateField(null=True,
                                             verbose_name='Дата отримання договору',
                                             help_text='Введіть дату',
                                             blank=True
                                             )
    date_receipt_sale_invoice = models.DateField(null=True,
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

    def save(self, *args, **kwargs):
        if self.work_orders is not None:
            wo = self.work_orders.all()
            wo_amount_gps = 0
            wo_amount_fuel_sensor = 0
            for i in wo:
                wo_amount_gps += i.amount_gps
                wo_amount_fuel_sensor += i.amount_fuel_sensor
            if self.amount_gps == wo_amount_gps and self.amount_fuel_sensor == wo_amount_fuel_sensor:
                self.execution_status = self.ExecutionStatus.finished
            elif self.amount_gps > wo_amount_gps > 0 or self.amount_fuel_sensor > wo_amount_fuel_sensor > 0:
                self.execution_status = self.ExecutionStatus.partly_executed
        try:
            if self.project_contract is not None:
                if self.project_contract.status == self.project_contract.StatusChoice.in_stock:
                    self.date_receipt_contract = self.project_contract.status_date
            else:
                if self.project_add_contract is not None:
                    if self.project_add_contract.status == self.project_add_contract.StatusChoice.in_stock:
                        self.date_receipt_contract = self.project_add_contract.status_date
        except ObjectDoesNotExist:
            pass

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return 'Проект №{} від {} '.format(self.number, self.date_start)

    class Meta:
        verbose_name_plural = "Проекти"
