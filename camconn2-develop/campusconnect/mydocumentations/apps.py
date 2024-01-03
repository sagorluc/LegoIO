from django.apps import AppConfig


class MyDocsConfig(AppConfig):
    name = 'mydocumentations'

    def ready(self):
        import mydocumentations.signals

