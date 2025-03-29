import os.path

from django.db import models
from django.utils import timezone

from users.models import Users


class UserPost(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'user_post'
        verbose_name = 'Поста пользователя'
        verbose_name_plural = 'Посты пользователей'

    def __str__(self):
        return self.post_text[:10] + '...'

    def save(self, *args, **kwargs):
        if not self.id:  # Только при создании
            self.created_at = timezone.now().replace(tzinfo=None)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.post_image:
            if os.path.isfile(self.post_image.path):
                os.remove(self.post_image.path)
        super().delete(*args, **kwargs)
