from phone_field import PhoneField
 
# Create your models here.
class Client(models.Model):
    PAY_FORM_CHOISE = (
        ('1', 'Безнал'),
        ('2', 'Нал'),
        ('3', 'БК'),
        ('4','Безнал/Нал'),
        ('5','Безнал/БК')
        )
    pay_form = models.CharField(max_length=1, choices=PAY_FORM_CHOISE,
                                help_text='Оберіть форму оплати')
    name = models.CharField(max_length=128, blank=False)
    login = name = models.CharField(max_length=128, blank=False)


class ClientPostAdress(models.Model):
      index = models.IntegerField(help_text='Пштовий індекс', blank=False)
      region = models.CharField(max_length=50,help_text='Область')
      district = models.CharField(max_length=50,help_text='Район')
      city = models.CharField(max_length=50,help_text='Місто', blank=False)
      street = models.CharField(max_length=200,help_text='Вулиця', blank=False)
      house = models.CharField(max_length=50,help_text='Номер будинку', blank=False)
      office = models.CharField(max_length=50,help_text='Номер офісу або квартири')
      client_profile = models.OneToOneField(Client,on_delete=models.CASCADE,
                                     related_name='adress', blank=False)

      def __str__(self):
          return '{} {} {} {} {} {} {}'.format(self.index, self.region, self.district, self.city,
                                    self.street, self.house, self.office, self.client_profile)

    
class ContactProfile(models.Model):
    firstname = models.CharField(max_length=50,help_text='Прізвище')
    surname = models.CharField(max_length=50, blank = False, help_text="І'мя")
    patronymic = models.CharField(max_length=50, help_text='По батькові')
    position = models.CharField(max_length=50, help_text='Посада')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
          return '{} {} {} - {}'.format(self.first_name, self.surname, self.patronymic, self.client)
    
    
class ContactPhone(models.Model):
    phone = PhoneField(help_text='Контактний номер телефону')
    contact_profile = models.ForeignKey(ContactProfile,on_delete=models.CASCADE,
        related_name='phones')

    def __str__(self):
          return '{}. {} - {}'.format(self.id,self.phone,self.contact_profile)


class ContactEmail(models.Model):
      email = models.EmailField(max_length=254,help_text='Контактна електронна адреса')
      contact_profile = models.ForeignKey(ContactProfile,on_delete=models.CASCADE,
            related_name='emails')
      
      def __str__(self):
          return '{}. {} - {}'.format(self.id,self.email,self.contact_profile)

     
      
