from django.db import models

from .abstract import VersionableArtefact
from .registration import MetaStructure 

from ..settings import api_maxlen_settings as maxlengths
from ..validators import re_validators, clean_validators 

class MaintainableArtefact(VersionableArtefact):
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE,
                               validators=[re_validators['IDType']])
    agency = models.ForeignKey('Organisation', on_delete=models.CASCADE) 
    is_final = models.BooleanField(default=False)
    name = models.CharField(max_length=maxlengths.NAME)
    registrations = models.ManyToManyField(MetaStructure)

    class Meta(VersionableArtefact.Meta):
        abstract = True
        unique_together = ('id_code', 'agency', 'version')
        indexes = [
            models.Index(fields=['id_code']),
            models.Index(fields=['name']),
            models.Index(fields=['agency']),
            models.Index(fields=['id_code', 'version']),
            models.Index(fields=['id_code','agency', 'version']),
        ]

    def __str__(self):
        return '%s:%s:%s:%s' % (self.id_code, self.agency, self.version, self.name)

    def clean(self):
        # Make sure that final structures cannot be modified
        created = not bool(self.pk)
        if not created and self.is_final:
            raise clean_validators[self.__class__.__name__] 

    def save(self, *args, **kwargs):
        if not kwargs.get('registration'):
            created = not bool(self.pk)
            action = 'Append' if created else 'Replace'
            from ..utils.permissions import get_current_user
            created_by = get_current_user().contact
            print(created_by)
            print(type(created_by))
            registration = MetaStructure(created_by=created_by, action=action, interactive=True)
            registration.save()
            kwargs['registration'] = registration 
            print(kwargs['registration'])
        self.full_clean()
        registration = kwargs.pop('registration')
        super().save(*args, **kwargs)
        self.registrations.add(registration)

    def delete(self):
        action = 'Delete'
        from ..utils.permissions import get_current_user
        created_by = get_current_user().contact
        MetaStructure(created_by=created_by, action=action).save()
        super().delete()
