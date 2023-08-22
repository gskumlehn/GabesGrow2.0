from django import forms
from apps.stage.models import StageType

class ConfigForm(forms.Form):
    watering=forms.CheckboxInput(
        label="auto-watering",
        attrs={
            "class": "form-control"
        }
    )

    stageType=forms.CharField(
        label="type"
        choices=StageType.choices,
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control"
            }
        )
    )

