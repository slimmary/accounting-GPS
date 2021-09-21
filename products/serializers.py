from rest_framework import serializers
from .models import Equipment, Service, Sim, Gps, FuelSensor
from django.utils.html import format_html

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class EquipmentBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('name', 'price_taxfree', 'price_tax')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'price_taxfree', 'price_tax', 'salary_installer')


class SimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sim
        fields = '__all__'


class SimBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sim
        fields = ('operator', 'number', 'installer', 'date_given', )


class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields = '__all__'


class GpsBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields = ('number', 'vehicle',)


class FuelSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelSensor
        fields = '__all__'


class FuelSensorBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelSensor
        fields = ('type', 'serial','number', 'vehicle')


class ProductsLinkSerializer(serializers.Serializer):
    equipments = format_html("<a href='../../products/equipments/'>Комплектуючі</a>")
    services = format_html("<a href='../../products/servises/'>Послуги</a>")
    sim = format_html("<a href='../../products/sims/'>Сім-картки</a>")
    gps = format_html("<a href='../../products/gpss/'>Бортові Реєстратори (БР)</a>")
    fuelsensors = format_html("<a href='../../products/fuelsensors/'>Датчики Вимірювання Рівня Пального (ДВРП)</a>")
