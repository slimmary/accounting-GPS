from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
        verbose_name='Користувач'
    )

    phone = PhoneField(null=True, verbose_name='Номер телефону співробітника')

    birthday = models.DateField(null=True, blank=True,
                                verbose_name='Дата народження')
    position = models.CharField(max_length=50,
                                verbose_name='Посада')
    avatar = models.ImageField(upload_to='images/users',
                               verbose_name='Зображення')

    date_start_work = models.DateField(null=True, blank=True,
                                       verbose_name='Дата прийому на роботу')
    STATUS_FORM_CHOICE = (
        ('1', 'на випробному терміні'),
        ('2', 'прийнятий')
    )
    status = models.CharField(max_length=1, choices=STATUS_FORM_CHOICE, help_text='Оберіть статус')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return '{} - {} - {} | Контактний телефон: {} | Дата народження: {} '.format(self.user, self.position, self.get_status_display(), self.phone, self.birthday,  )

    class Meta:
        verbose_name_plural = "Користувачі (співробітники)"
