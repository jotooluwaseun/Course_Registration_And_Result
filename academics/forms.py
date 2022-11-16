from django import forms
# from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
        error_messages = {
            'username': {
                'unique': 'Email already exists',
            },
        }

        placeholder = {
            'first_name': {
                'placeholder': 'First Name',
            }
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name',
            'class': 'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name',
            'class': 'form-control',

        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email Address',
            'class': 'form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Create Password',
            'class': 'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'class': 'form-control',
        })


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matric_no', 'dob', 'gender', 'department', 'entry_date', 'graduated_date']
