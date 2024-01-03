from django.apps import AppConfig


class MymailroomConfig(AppConfig):
    name = 'mymailroom'

    def ready(self):
        import mymailroom.signals
