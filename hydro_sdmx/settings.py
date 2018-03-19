"""
Settings for HYDRO_SDMX are all namespaced in the HYDRO_SDMX setting.
For example your project's `settings.py` file might look like this:

HYDRO_SDMX = {
    'DEFAULT_LENGTHS': {
        'id_code': 64,
        'name': 128
    },
}

This module provides the `api_setting` object, that is used to access
HYDRO_SDMX settings, checking for user settings first, then falling
back to the defaults.
"""
import os.path

from django.conf import settings
from django.test.signals import setting_changed

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULTS = {
    'HYDRO_SDMX': {
        'SDMXMLSCHEMA': os.path.join(MODULE_DIR, 'schemas', 'xml', 'SDMXMessage.xsd')
    },
    'HYDRO_SDMX_MAXLENGTHS': {
        'ID_CODE': 63,
        'NAME': 255,
        'VERSION': 15,
        'MAX_LENGTH': 255,
        'ANNOTATION_TITLE': 127,
        'ANNOTATION_TYPE': 63,
        'DEPARTMENT': 31,
        'ROLE': 31,
        'TELEPHONE': 31,
        'X400': 63,
        'DATA_TYPE': 63,
        'TIME_PERIOD': 63,
        'MEAS_DIM_VALUE': 255,
        'OBS_VALUE': 255,
        'DIMENSION_TYPE': 15,
        'METADATA_TARGET_COMPONENTS': 63, 
        'TOKENS': 15,
        'VALUE_MAP': 127,
        'PERIODICITY': 63,
        'OFFSET': 63,
        'TOLERANCE': 63,
        'LANG': 63
    }
}

REMOVED_SETTINGS = {
    'HYDRO_SDMX': (),
    'HYDRO_SDMX_MAXLENGTHS': ()
} 

class APISettings(object):
    """
    A settings object, that allows API settings to be accessed as properties.
    For example:

        from hydro_sdmx.settings import api_settings
        print(api_settings.DEFAULT_CHARVAR_LENGTHS)

    """
    def __init__(self, setting, user_settings=None, defaults=None):
        self._setting = self.__check_setting(setting)
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS[setting]

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, self._setting, {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid %s setting: '%s'" % (self._setting, attr))

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val

    def __check_setting(self, setting):
        if setting not in ['HYDRO_SDMX', 'HYDRO_SDMX_MAXLENGTHS']:
            raise RuntimeError("The '%s' global setting is not allowed.  Please choose one of the following '%s'" % (setting, ['HYDRO_SDMX', 'HYDRO_SDMX_MAXLENGTHS']))
        return setting

    def __check_user_settings(self, user_settings):
        SETTINGS_DOC = "https://django-hydro-sdmx-readthedocs.io/en/stable/api/settings"
        for setting in REMOVED_SETTINGS[self._setting]:
            if setting in user_settings:
                raise RuntimeError("The '%s' setting of '%s' settings has been removed. Please refer to '%s' for available settings." % (setting, self._setting, SETTINGS_DOC))
        return user_settings


api_settings = APISettings('HYDRO_SDMX', None, DEFAULTS['HYDRO_SDMX'])
api_maxlen_settings = APISettings('HYDRO_SDMX_MAXLENGTHS', None, DEFAULTS['HYDRO_SDMX_MAXLENGTHS'])

def reload_api_settings(*args, **kwargs):
    global api_settings
    global api_maxlen_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'HYDRO_SDMX':
        api_settings = APISettings(setting, value, DEFAULTS[setting])
    elif setting == 'HYDRO_SDMX_MAXLENGTHS':
        api_maxlen_settings = APISettings(setting, value, DEFAULTS[setting])

setting_changed.connect(reload_api_settings)
