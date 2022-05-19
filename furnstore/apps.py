from django.apps import AppConfig


class FurnstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'furnstore'

    def ready(self):
        import furnstore.signals
