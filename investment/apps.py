from django.apps import AppConfig


class InvestmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'investment'

    def ready(self):
        from investment import task_starter
        task_starter.start()
