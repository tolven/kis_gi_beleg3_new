from django import forms

from kis_pro.fields import UserModelChoiceField
from kis_pro.models import User, Patient, Doctor, Role


class NewDocForms(forms.ModelForm):
    class Meta:
        model = Doctor

        fields = ['title', 'firstname', 'lastname', 'role']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'role': forms.Select(
                choices=Role.objects.all(),
                attrs={
                    'class': 'form-select'
                }
            )
        }


class NewUserForms(forms.ModelForm):
    class Meta:
        model = User

        fields = ['title', 'firstname', 'lastname', 'role']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'role': forms.Select(
                choices=Role.objects.all(),
                attrs={
                    'class': 'form-select'
                }
            )
        }


class NewPatientForms(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ()
