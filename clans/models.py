from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Clan(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название клана'
    )
    description = models.TextField(
        verbose_name='Описание клана'
    )
    date_joined = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    @property
    def total_profiles(self):
        return self.profiles.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клан'
        verbose_name_plural = 'Кланы'
