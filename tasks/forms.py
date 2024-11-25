from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import CustomUser

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirme su contraseña")

    class Meta:
        model = CustomUser
        fields = ['nombre_de_usuario', 'correo_electronico', 'edad', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data

class UserLoginForm(AuthenticationForm):
    pass

class UserPasswordChangeForm(PasswordChangeForm):
    pass
