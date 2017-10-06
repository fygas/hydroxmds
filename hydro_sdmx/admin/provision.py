from .base import MaintainableArtefactAdmin

class DataProvisionAgreementAdmin(MaintainableArtefactAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]['fields'] = (
            ('id_code', 'name'), 
            ('agency', 'version'),
            ('data_provider', 'data_provider_scheme'),
            'structure_usage'
        ) 
        return fieldsets 
