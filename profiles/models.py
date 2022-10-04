from django.db import models
from django.contrib.auth import get_user_model

from profiles.choices import RANGS


User = get_user_model()


class Guild(models.Model):
    creator = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Основатель гильдии'
    )
    title = models.CharField(
        max_length=255, 
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name='Описание гильдии'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Гильдия"
        verbose_name_plural = "Гильдии"


class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True, 
        related_name="profile"
    )
    profile_photo = models.ImageField(
        upload_to="images/profile_photos", 
        blank=True, null=True
    )
    rang = models.CharField(
        max_length=50,
        choices=RANGS,
        verbose_name='Ранг'
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        related_name='profile',
        verbose_name='Гильдия',
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
