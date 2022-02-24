from django.apps import AppConfig


class InvescofilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invescofiles'
    def ready(self):
        import invescofiles.signals
