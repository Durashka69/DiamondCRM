from django.db import models
from django.contrib.auth import get_user_model

from profiles.choices import RANGS

from clans.models import Clan


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="profile"
    )
    profile_photo = models.ImageField(
        upload_to="images/profile_photos", 
        blank=True, null=True
    )
    rang = models.CharField(
        max_length=50,
        choices=RANGS,
        verbose_name='Ранг',
        default='Первый ранг'
    )
    clan = models.ForeignKey(
        Clan,
        on_delete=models.CASCADE,
        related_name='profiles',
        verbose_name='Клан',
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
