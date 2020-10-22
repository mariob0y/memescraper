from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'post'

    def ready(self):
        from post import scrap
        scrap.start()
