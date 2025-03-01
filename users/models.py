import os

from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    avatar = models.ImageField(upload_to='static/images/user_avatar', null=True, blank=True, verbose_name='Аватар')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def delete(self, *args, **kwargs):
        if self.avatar:
            if os.path.isfile(self.avatar.path):
                os.remove(self.avatar.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Users.objects.get(pk=self.pk)
                if old_instance.avatar and old_instance.avatar != self.avatar:
                    if os.path.isfile(old_instance.avatar.path):
                        os.remove(old_instance.avatar.path)
            except Users.DoesNotExist:
                pass
        super().save(*args, **kwargs)