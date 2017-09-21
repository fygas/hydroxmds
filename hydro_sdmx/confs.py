"""
Settings for HYDRO_SDMX are all namespaced in the HYDRO_SDMX setting.
For example your project's `settings.py` file might look like this:

HYDRO_SDMX = {
    'DEFAULT_LENGTHS': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    )
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    )
}

This module provides the `api_setting` object, that is used to access
HYDRO_SDMX settings, checking for user settings first, then falling
back to the defaults.
"""

from django.conf import settings
from django.test.signals import setting_changed

DEFAULTS = {
    # Base API policies
    'DEFAULT_CHARVAR_LENGTHS': {
        'max_length': 255,
    }
}

REMOVED_SETTINGS = ()


class APISettings(object):
    """
    A settings object, that allows API settings to be accessed as properties.
    For example:

        from rest_framework.settings import api_settings
        print(api_settings.DEFAULT_RENDERER_CLASSES)

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.
    """
    def __init__(self, user_settings=None, defaults=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'HYDRO_SDMX', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val

    def __check_user_settings(self, user_settings):
        SETTINGS_DOC = "https://django-hydro-sdmx-readthedocs.io/en/stable/api/settings"
        for setting in REMOVED_SETTINGS:
            if setting in user_settings:
                raise RuntimeError("The '%s' setting has been removed. Please refer to '%s' for available settings." % (setting, SETTINGS_DOC))
        return user_settings


api_settings = APISettings(None, DEFAULTS)


def reload_api_settings(*args, **kwargs):
    global api_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'REST_FRAMEWORK':
        api_settings = APISettings(value, DEFAULTS)


setting_changed.connect(reload_api_settings)
