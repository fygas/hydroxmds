from django import forms

from .models.registration import MetaStructure 

from .constants import ACTIONS

class MetaStructureRegistrationForm(forms.ModelForm):
    action = forms.ChoiceField(choices=ACTIONS)

    def save(self, *args, **kwargs):
        commit = kwargs.pop('commit', False)
        new_obs = super().save(*args, **kwargs, commit=False)
        from .utils.permissions import get_current_user
        created_by = get_current_user()
        new_obs.registration = MetaStructure(created_by=created_by, action=self.action) 
        return new_obs.save(commit=commit)
