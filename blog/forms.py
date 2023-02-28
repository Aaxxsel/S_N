from django.forms import forms


class UserForm(forms.Form):
    email = forms.EmailField()
    password = forms.DecimalField(min_value=3, max_value=200)
    name = forms.CharField()


