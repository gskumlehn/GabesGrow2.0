from django import forms
from apps.config.models import GrowConfig

class ConfigForm(forms.ModelForm):
    class Meta:
        model = GrowConfig
        exclude = ['lastUpdate']
        widgets = {
            "watering": forms.CheckboxInput(
               attrs={
                   "class": "form-control"
                }
            ),
            "stageType": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "lastUpdate": forms.DateTimeField(
                attrs={
                    "class": "form-control",
                    "hidden": True
                }
            )
        }
