from django.db import models
from apps.clients.models import Client
# Create your models here.


class Contract(models.Model):
    FORM_CHOICE = (
        ('1', 'Абонплата'),
        ('2', 'Поставки'),
        ('3', 'Обслуговування'),
    )
    form = models.CharField(max_length=1, choices=FORM_CHOICE,verbose_name='Тип договору', help_text='Оберіть тип договору')
    PROVIDER_CHOICE = (
        ('1', 'ТОВ "Системи Контролю Транспорту"'),
        ('2', 'ФОП Шевчук С.І.'),
        ('3', 'ФОП Дячук Л.В.'),
    )
    provider = models.CharField(max_length=1, choices=PROVIDER_CHOICE,verbose_name='Постачальник',
                                help_text='Оберіть постачальника')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупець/Абонент', related_name='contracts')
    number = models.IntegerField(verbose_name='Номер договору', help_text='Введіть номер договору')
    contract_date = models.DateField(verbose_name='Дата заключеня договору', help_text='Оберіть дату')
    STATUS_CHOICE = (
        ('1', 'Створений'),
        ('2', 'Відправлений укрпоштою'),
        ('3', 'Відправлений НП'),
        ('4', 'Відправлений на електронну пошту'),
        ('5', 'В наявності')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name='Статус', help_text='Оберіть статус договору')
    status_date = models.DateField(null=True, verbose_name='Дата статусу(створення/відправки/отримання)', help_text='Оберіть дату')
    contract_image = models.ImageField(upload_to='images/contracts', verbose_name='Скан-копія', blank=True)

    def __str__(self):
        return 'Договір {} №{} від {} між {} та {}'.format(
            self.get_form_display(),
            self.number, self.contract_date,
            self.get_provider_display(),
            self.client,
            self.get_status_display()
        )

    class Meta:
        verbose_name_plural = "Договори"