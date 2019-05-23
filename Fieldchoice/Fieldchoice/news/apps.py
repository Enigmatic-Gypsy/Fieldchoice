from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NewsConfig(AppConfig):
    name = 'Fieldchoice.news'
    verbose_name = _("News")
