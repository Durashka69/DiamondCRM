from django.apps import AppConfig


class ClansConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "clans"
    verbose_name: str = 'Кланы'

    def ready(self) -> None:
        import clans.signals
