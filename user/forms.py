from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(
        label="user",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-group"
            }
        )
    )
    password=forms.CharField(
        label="password",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-group"
            }
        )
    )