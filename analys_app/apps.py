from django.apps import AppConfig


class AnalysAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analys_app'

    def ready(self):
        import analys_app.signals