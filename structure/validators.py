import re
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator

patterns = {
    'NestedIDType': "[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*",
    'TwoLevelIDType': "[A-Za-z0-9_@$\-]+\.[A-Za-z0-9_@$\-]+",
    'IDType': "^[A-Za-z0-9_@$\-]+$",
    'NCNameIDType': "[A-Za-z][A-Za-z0-9_\-]*",
    'NestedNCNameIDType': "[A-Za-z][A-Za-z0-9_\-]*(\.[A-Za-z][A-Za-z0-9_\-]*)*",
    'SingleNCNameIDType': "[A-Za-z][A-Za-z0-9_\-]*",
    'VersionType': "[0-9]+(\.[0-9]+)*",
}

re_validators = {
    key: RegexValidator(
            re.compile(value), 
            _('Enter a value of type %s that has pattern "(%s)"') %  \
                (key, value), 
            'invalid_pattern'
         ) 
    for key, value in patterns.items()
}
