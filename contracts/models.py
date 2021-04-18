from django.db import models
from clients.models import Client
from datetime import date
from projects.models import Project
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class AbstractContract(models.Model):
    number = models.IntegerField(verbose_name='Номер №',
                                 help_text='Введіть номер'
                                 )
    contract_date = models.DateField(default=date.today(),
                                     verbose_name='Дата заключеня',
                                     help_text='Оберіть дату'
                                     )

    class StatusChoice:
        created = 'Створений'
        send_post = 'Відправлений укрпоштою'
        send_NP = 'Відправлений НП'
        send_email = 'Відправлений на електронну пошту'
        in_stock = 'В наявності'

    STATUS_CHOICE = (
        (StatusChoice.created, 'Створений'),
        (StatusChoice.send_post, 'Відправлений укрпоштою'),
        (StatusChoice.send_NP, 'Відправлений НП'),
        (StatusChoice.send_email, 'Відправлений на електронну пошту'),
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
    contract_image = models.ImageField(upload_to='images/contracts',
                                       verbose_name='Скан-копія',
                                       blank=True)

    class Meta:
        abstract = True


class Contract(AbstractContract):
    class TypeChoice:
        project = 'поставки'
        service = 'сервісного обслуговування'
        subscription = 'абонентського обслуговування'

    TYPE_CHOICE = (
        (TypeChoice.project, 'поставки'),
        (TypeChoice.service, 'сервісного обслуговування'),
        (TypeChoice.subscription, 'абонентського обслуговування'),
    )

    type = models.CharField(max_length=100,
                            default=TypeChoice.project,
                            choices=TYPE_CHOICE,
                            verbose_name='Тип договору',
                            help_text='Оберіть тип', blank=True)

    class ProviderChoice:
        ckt = 'ТОВ "Системи Контролю Транспорту"'
        shevchuk = 'ФОП Шевчук С.І.'
        dyachuk = 'ФОП Дячук Л.В.'
        demidenko = 'ФОП Демченко К.Б.'

    PROVIDER_CHOICE = (
        (ProviderChoice.ckt, 'ТОВ "Системи Контролю Транспорту"'),
        (ProviderChoice.shevchuk, 'ФОП Шевчук С.І.'),
        (ProviderChoice.dyachuk, 'ФОП Дячук Л.В.'),
        (ProviderChoice.demidenko, 'ФОП Демченко К.Б.'),
    )
    provider = models.CharField(max_length=100, choices=PROVIDER_CHOICE, verbose_name='Постачальник',
                                default=ProviderChoice.ckt,
                                help_text='Оберіть постачальника', blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупець/Абонент',
                               related_name='contracts_all')
    contract_project_to = models.OneToOneField(Project,
                                               null=True,
                                               on_delete=models.CASCADE,
                                               verbose_name='Проект',
                                               related_name='project_contract',
                                               blank=True
                                               )

    def clean(self):
        if self.contract_project_to:
            if self.type != self.TypeChoice.project:
                raise ValidationError("до проекту не можливо додати договір, який не є договором поставки")

    def save(self, *args, **kwargs):
        if self.type == self.TypeChoice.project:
            if self.status == self.StatusChoice.in_stock:
                self.contract_project_to.date_receipt_contract = self.status_date

        super(Contract, self).save(*args, **kwargs)
        Project.save(self.contract_project_to, *args, **kwargs)

    def __str__(self):
        return 'Договір {} №{} від {} між {} та {} {}'.format(
            self.type,
            self.number,
            self.contract_date,
            self.provider,
            self.client,
            self.get_status_display(),
        )

    class Meta:
        verbose_name_plural = "Договори"


class Additions(AbstractContract):
    add_project_to = models.OneToOneField(Project,
                                          null=True,
                                          on_delete=models.CASCADE,
                                          verbose_name='Проект',
                                          related_name='project_add_contract',
                                          blank=True
                                          )

    contract_to = models.ForeignKey(Contract,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Основний договір до якого створено ДУ',
                                    related_name='additions',
                                    blank=True)

    def save(self, *args, **kwargs):
        if self.add_project_to is not None:
            if self.status == self.StatusChoice.in_stock:
                self.add_project_to.date_receipt_contract = self.status_date

        super(Additions, self).save(*args, **kwargs)
        Project.save(self.add_project_to, *args, **kwargs)
    #
    # def clean(self):
    #     if self.add_project_to:
    #         if self.contract_to.type != self.contract_to.TypeChoice.project:
    #             raise ValidationError("до проекту не можливо додати ДУ, яка не відноситься до договору поставки")

    def __str__(self):
        return '№{} від {}'.format(self.number, self.contract_date)

    class Meta:
        verbose_name_plural = "Додаткові Угоди"
