import os.path

from django.db import models

from users.models import Users


class UserPost(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    class Meta:
        db_table = 'user_post'
        verbose_name = 'Поста пользователя'
        verbose_name_plural = 'Посты пользователей'

    def __str__(self):
        return self.post_text[:10] + '...'

    def delete(self, *args, **kwargs):
        if self.post_image:
            if os.path.isfile(self.post_image.path):
                os.remove(self.post_image.path)
        super().delete(*args, **kwargs)
