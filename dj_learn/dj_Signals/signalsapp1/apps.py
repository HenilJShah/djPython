from django.apps import AppConfig


class Signalsapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signalsapp1'

    def ready(self):
        import signalsapp1.signals