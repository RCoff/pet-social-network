from django import forms
from django.contrib.auth.forms import AuthenticationForm

from data.models import AnimalModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=140)
    # email = forms.EmailField(max_length=140)
    password = forms.CharField(max_length=140, widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})


class AddAPetForm(forms.ModelForm):
    class Meta:
        model = AnimalModel
        fields = ('animal_type', 'animal_name', 'age_years', 'birth_date')
        widgets = {
            'animal_type': forms.Select(attrs={'class': 'form-select'}),
            'animal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age_years': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'})
        }
