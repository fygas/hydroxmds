from .base import MaintainableArtefactAdmin

class ProvisionAgreementAdmin(MaintainableArtefactAdmin):
    fieldsets = [ 
        ('Identification', {
            'fields': (
                ('id_code', 'agency', 'version'),
                ('data_provider', 'data_provider_scheme'),
                'structure_usage',
                'uri',
            ),
            'classes': ('collapse',)
        }),
        ('Duration', {
            'fields': (
                ('valid_from', 'valid_to'), 
            ),
            'classes': ('collapse',)
        }),
    ] 
