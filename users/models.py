from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
        verbose_name='Користувач'
    )

    phone = PhoneField(null=True, verbose_name='Робочий номер телефону співробітника')

    phone_2 = PhoneField(null=True, verbose_name='Персональний номер телефону співробітника')

    email = models.EmailField(null=True, max_length=254, verbose_name='Персональна електронна адреса')

    birthday = models.DateField(null=True, blank=True,
                                verbose_name='Дата народження')
    position = models.CharField(max_length=50,
                                verbose_name='Посада')
    avatar = models.ImageField(upload_to='images/users',
                               verbose_name='Зображення')

    def get_avatar(self):
        if not self.avatar:
            return 'image/CKT'
        return self.avatar.url

    # метод, для создания фейкового поля таблицы в режиме read only
    def avatar_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % self.get_avatar())

    avatar_tag.short_description = 'Фото'

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
        return '{}'.format(self.user.last_name, )

