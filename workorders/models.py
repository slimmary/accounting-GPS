from django.db import models
from vehicle.models import Vehicle
from products.models import Equipment, Service, Gps, FuelSensor


class Completed_service_works(models.Model):
    car = models.ForeignKey(Vehicle,
                            on_delete=models.CASCADE,
                            verbose_name='ТЗ',
                            related_name='service_works'
                            )
    type_service = models.ForeignKey(Service,
                                     on_delete=models.CASCADE,
                                     verbose_name='виконані роботи',
                                     related_name='completed_service_works'
                                     )
    used_equipment = models.ForeignKey(Equipment,
                                       on_delete=models.CASCADE,
                                       verbose_name='використане обладнання',
                                       related_name='used_equipment'
                                       )

    gps = models.ForeignKey(Gps,
                            on_delete=models.CASCADE,
                            verbose_name='БР',
                            related_name='gps_service_works',
                            )

    fuel_sensor = models.ForeignKey(FuelSensor,
                                    on_delete=models.CASCADE,
                                    verbose_name='ДВРП',
                                    related_name='fuel_sensor_service_works',
                                    )

    class Payer:
        client = 'Клієнт'
        ckt = 'СКТ'
        executor = 'монтажник'
        manufacturer = 'виробник'

    PAYER_CHOICE = (
        (Payer.client, 'Клієнт'),
        (Payer.ckt, 'ЛайСКТфсел'),
        (Payer.executor, 'Тревел-монтажник'),
        (Payer.manufacturer, 'виробник-сім'),
    )
    payer = models.CharField(max_length=100,
                             default=Payer.client,
                             choices=PAYER_CHOICE,
                             verbose_name='Оператор',
                             help_text='Оберіть оператора'
                             )
