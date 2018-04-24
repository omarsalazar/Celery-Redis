from django.apps import AppConfig


class ExamplappConfig(AppConfig):
    name = 'examplapp'

    def ready(self):
        try:
            import examplapp.signals
        except ImportError as e:
            print(e)
            print('no pudo importarse signals')
