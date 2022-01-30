from django import forms

from kis_pro.fields import UserModelChoiceField
from kis_pro.models import User, Patient, Doctor, Role, Cases


class DateInput(forms.DateInput):
    input_type = 'date'


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

    def __init__(self, *args, **kwargs):
        super(NewDocForms, self).__init__(*args, **kwargs)
        self.fields['title'].required = False


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

    def __init__(self, *args, **kwargs):
        super(NewUserForms, self).__init__(*args, **kwargs)
        self.fields['title'].required = False


class NewPatientForms(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['attending_doctor']

        fields = ['title', 'firstname', 'lastname', 'birthdate']
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

            'birthdate': DateInput(
                attrs={
                    'class': 'input-group date'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(NewPatientForms, self).__init__(*args, **kwargs)
        self.fields['title'].required = False


class NewCaseForms(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ['timestamp', 'doctor']
        exclude = ['patient']
        widgets = {
            'timestamp': DateInput(
                attrs={
                    'class': 'input-group date'
                }
            )
        }
