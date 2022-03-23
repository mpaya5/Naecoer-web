from django import forms
from captcha.fields import ReCaptchaField

class Formulario(forms.Form):
    name = forms.CharField(
        max_length=100,
        label = 'Nombre',)

    email = forms.EmailField(
        label = 'Correo electrónico',)

    phone = forms.CharField(
        label = 'Teléfono',
        widget=forms.NumberInput,)

    message = forms.CharField(
        label = 'Mensaje',
        widget=forms.Textarea,)
    captcha = ReCaptchaField()
 