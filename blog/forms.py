from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=3)
    name = forms.CharField(min_length=3)
    lastname = forms.CharField(min_length=3)
    password_conf = forms.CharField(min_length=3)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.DecimalField()