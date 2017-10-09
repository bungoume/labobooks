from django.forms import ModelForm

from core.models import Organization


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'id_slug']
