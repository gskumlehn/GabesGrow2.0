from django import forms
from apps.stage.models import StageType

class ConfigForm(forms.Form):
    watering=forms.BooleanField(
        label="auto-watering",
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    stageType=forms.CharField(
        label="type",
        widget=forms.Select(
            choices=StageType.choices,
            attrs={
                "class": "form-control"
            }
        )
    )

