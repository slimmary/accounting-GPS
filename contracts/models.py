from django.db import models
from clients.models import Client


class Contract(models.Model):
    class TypeChoice:
        project = 'поставки'
        service = 'сервісного обслуговування'
        subscription = 'абонентського обслуговування'

    TYPE_CHOICE = (
        (TypeChoice.project, 'поставки'),
        (TypeChoice.service, 'сервісного обслуговування'),
        (TypeChoice.subscription, 'абонентського обслуговування'),
    )

    type = models.CharField(max_length=100, choices=TYPE_CHOICE, verbose_name='Тип договору',
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
    provider = models.CharField(max_length=100, choices=PROVIDER_CHOICE, verbose_name='Постачальник',default=ProviderChoice.ckt,
                                help_text='Оберіть постачальника', blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупець/Абонент',
                               related_name='contracts')
    number = models.IntegerField(verbose_name='Номер договору', help_text='Введіть номер договору')
    contract_date = models.DateField(verbose_name='Дата заключеня договору', help_text='Оберіть дату')

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
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, verbose_name='Статус',
                              help_text='Оберіть статус договору', default=StatusChoice.created)
    status_date = models.DateField(null=True, verbose_name='Дата зміни статусу',
                                   help_text='Оберіть дату')
    contract_image = models.ImageField(upload_to='images/contracts', verbose_name='Скан-копія', blank=True)

    def __str__(self):
        return 'Договір {} №{} від {} між {} та {} {}'.format(
            self.type,
            self.number,
            self.contract_date,
            self.provider,
            self.client,
            self.get_status_display()
        )

    class Meta:
        verbose_name_plural = "Договори"


class Additions(models.Model):
    contract_to = models.ForeignKey(Contract,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Основний договір до якого створено ДУ',
                                    related_name='additions',
                                    blank=True)

    number = models.IntegerField(verbose_name='Номер ДУ',)
    date = models.DateField(verbose_name='Дата заключеня ДУ',)

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
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, verbose_name='Статус',
                              help_text='Оберіть статус договору', default=StatusChoice.created)
    status_date = models.DateField(null=True, verbose_name='Дата зміни статусу',
                                   help_text='Оберіть дату')
    contract_supp_image = models.ImageField(upload_to='images/contracts', verbose_name='Скан-копія', blank=True)

    def __str__(self):
        return '№{} від {}'.format(self.number, self.date)

    class Meta:
        verbose_name_plural = "Додаткові Угоди"
