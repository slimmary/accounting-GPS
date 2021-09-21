from django.db import models
from clients.models import Client, Provider
from datetime import date


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

    provider = models.ForeignKey(Provider,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Постачальник',
                                 related_name='contract_provider')

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупець/Абонент',
                               related_name='contracts_all')

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

    contract_to = models.ForeignKey(Contract,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Основний договір до якого створено ДУ',
                                    related_name='additions',
                                    blank=True)

    def __str__(self):
        return '№{} від {}'.format(self.number, self.contract_date)

    class Meta:
        verbose_name_plural = "Додаткові Угоди"
