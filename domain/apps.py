from django.apps import AppConfig

from django.core.signals import request_finished


class DomainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'domain'


    # def ready(self):
    #     from domain.utils import update_allowed_domains_cache
    #     update_allowed_domains_cache()
