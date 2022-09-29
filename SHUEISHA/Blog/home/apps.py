from django.apps import AppConfig
from django import signals

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals