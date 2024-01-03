from django.apps import AppConfig


class CandidateProfileConfig(AppConfig):
    name = 'prof_candidate'

    def ready(self):
        import prof_candidate.signals

