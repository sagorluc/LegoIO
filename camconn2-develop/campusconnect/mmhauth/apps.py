from django.apps import AppConfig


class AuthMmhConfig(AppConfig):
    name = 'mmhauth'

    def ready(self):
        import mmhauth.signals
