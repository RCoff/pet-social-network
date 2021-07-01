from django import forms
from django.contrib.auth.forms import AuthenticationForm

from data.models import AnimalModel, PetProfile


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=140)
    # email = forms.EmailField(max_length=140)
    password = forms.CharField(max_length=140, widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})


class AddAPetForm(forms.ModelForm):
    class Meta:
        model = AnimalModel
        fields = ('animal_type', 'animal_name', 'animal_breed', 'age_years', 'birth_date')
        widgets = {
            'animal_type': forms.Select(attrs={'class': 'form-select'}),
            'animal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'animal_breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age_years': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'})
        }


class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ('profile_image', 'profile_description')
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'profile_description': forms.Textarea(attrs={'class': 'form-control',
                                                         'style': 'height: auto !important;',
                                                         'rows': '3'})
        }
