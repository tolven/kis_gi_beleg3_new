from django import forms

from kis_pro.fields import UserModelChoiceField
from kis_pro.models import User, Patient, Doctor, Role, Cases, TNM


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


class NewTNMForms(forms.ModelForm):
    class Meta:
        model = TNM
        fields = ['nodes', 'tumor', 'metastases', 'report_text']
        exclude = ['case']
        tumors = {
            ('TX', 'TX'),
            ('T0', 'T0'),
            ('Tis', 'Tis'),
            ('T1', 'T1'),
            ('T2', 'T2'),
            ('T3', 'T3'),
            ('T4', 'T4')
        }
        nodes = {
            ('NX', 'NX'),
            ('N0', 'N0'),
            ('N1', 'N1'),
            ('N2', 'N2'),
            ('N3', 'N3')
        }
        metas = {
            ('M0', 'M0'),
            ('M1', 'M1')
        }
        widgets = {
            'nodes': forms.Select(
                choices=nodes
            ),
            'tumor': forms.Select(
                choices=tumors
            ),
            'metastases': forms.Select(
                choices=metas
            )
        }

