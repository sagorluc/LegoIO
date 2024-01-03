from django.apps import AppConfig


class ViewTrackerConfig(AppConfig):
    name = 'viewtracker'

    def ready(self):
        import viewtracker.signals

