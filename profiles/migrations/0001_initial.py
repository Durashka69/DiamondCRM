# Generated by Django 4.1.1 on 2022-10-04 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Guild",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание гильдии")),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Основатель гильдии",
                    ),
                ),
            ],
            options={
                "verbose_name": "Гильдия",
                "verbose_name_plural": "Гильдии",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "profile_photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/profile_photos"
                    ),
                ),
                (
                    "rang",
                    models.CharField(
                        choices=[
                            ("GAYNIN", "Генин"),
                            ("CHUNIN", "Чунин"),
                            ("JONIN", "Джоунин"),
                            ("ELITE_JONIN", "Элитный Джоунин"),
                            ("ANBU_JONIN", "Анбу"),
                            ("AKATSUKI_MEMBER", "Акацуки"),
                            ("LEGENDARY_SANIN", "Легендарный Санин"),
                            ("KAGE", "Каге"),
                        ],
                        max_length=50,
                        verbose_name="Ранг",
                    ),
                ),
                (
                    "guild",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="profile",
                        to="profiles.guild",
                        verbose_name="Гильдия",
                    ),
                ),
            ],
            options={
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профили",
            },
        ),
    ]