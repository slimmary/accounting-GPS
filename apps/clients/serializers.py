from rest_framework import serializers
from .models import Client, ClientPostAdress, ContactProfile, ContactPhone, ContactEmail 



class ClientPostAdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientPostAdress
        fields = ('id', 'index', 'region', 'district',
                  'city', 'street', 'house', 'office', 'client_profile' )

class ClientPostAdressBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientPostAdress
        fields = ('id', 'index', 'region', 'district',
                  'city', 'street', 'house', 'office' )

        
class ContactPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactPhone
        fields = ('id', 'phone', 'contact_profile' )

class ContactPhoneBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactPhone
        fields = ('id', 'phone')


        
class ContactEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactEmail
        fields = ('id', 'email', 'contact_profile' )

class ContactEmaiBrieflSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactEmail
        fields = ('id', 'email')


                
class ContactProfileBriefSerializer(serializers.ModelSerializer):
    emails = ContactEmaiBrieflSerializer
    phones = ContactPhoneBriefSerializer
    class Meta:
        model = ContactProfile
        fields = ('id', 'firstname', 'surname', 'patronymic',
                  'position', 'phones', 'emails')
        
class ContactProfileSerializer(serializers.ModelSerializer):
    emails = ContactEmaiBrieflSerializer
    phones = ContactPhoneBriefSerializer
    class Meta:
        model = ContactProfile
        fields = ('id', 'firstname', 'surname', 'patronymic',
                  'position', 'phones', 'emails', 'client_field')

        
class ClientSerializer(serializers.ModelSerializer):
    adress = ClientPostAdressBriefSerializer
    contacts = ContactProfileBriefSerializer
    class Meta:
        model = Client
        fields = ('id', 'name', 'pay_form', 'login',
                  'adress', 'contacts')        
    
    
