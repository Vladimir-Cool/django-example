from django.apps import AppConfig


class ExCrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ex_crm'
    # Имя приложения для админки
    verbose_name = 'CRM_Base'
