from django.apps import AppConfig


class EoxNoticesConfig(AppConfig):
    name = "plugins.eox_notices"
    verbose_name = "EoX Notices"

    def ready(self):

        import eox_notices.signals  # noqa: F401
