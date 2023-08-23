from django import forms
from apps.config.models import GrowConfig

class ConfigForm(forms.Form):
    class Meta:
        model = GrowConfig
        exclude = ['lastUpdate']
        widgets = {
            "watering": forms.CheckboxInput(
               attrs={
                   "class": "form-control"
                }
            )
            ,
            "stageType": forms.Select(
                attrs={
                    "class": "form-control"
                }
            )
        }
