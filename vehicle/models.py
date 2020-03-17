from django.db import models
from clients.models import Client
# Create your models here.


class Vehicle(models.Model):
    TYPE_VEHICLE_CHOICE = (
        ('1', 'Тягач'),
        ('2', 'Легкове авто'),
        ('3', 'Мікроавтобус'),
        ('4', 'Екскаватор'),
        ('5', 'Навантажувач'),
        ('6', 'Трактор'),
        ('7', 'Оприскувач'),
        ('8', 'Комбайн'),
        ('9', 'Асфальтоукладник'),
        ('10', 'Фреза'),
        ('11', 'Каток'),
        ('12', 'Інше'),

    )
    type = models.CharField(max_length=1, choices=TYPE_VEHICLE_CHOICE, verbose_name='Тип ТЗ',
                            help_text='Оберіть тип Транспортного Засобу')
    make = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name="Модель", blank=True)
    number = models.CharField(max_length=50, verbose_name=' Ідентифікатор (держ.номер)')
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Власник', related_name='vehicle')

    def __str__(self):
        return '{} {} {} держ.номер {} '.format(
            self.get_type_display(),
            self.make,
            self.model,
            self.number,
            self.owner,
        )

    class Meta:
        verbose_name_plural = "Транспортні засоби"


