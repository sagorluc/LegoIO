from django.apps import AppConfig


class SuperAdminConfig(AppConfig):
    name = 'superadmin'

    def ready(self):
        import superadmin.signals

