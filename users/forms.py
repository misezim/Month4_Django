from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from .models import CustomUser

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    phone_number = forms.CharField(required=True, label='Phone')
    experience = forms.IntegerField(required=True, label='Experience')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')

    education = forms.CharField(required=True, max_length=255, label='Education')
    last_job = forms.CharField(required=False, max_length=255, label='Last Job')
    projects = forms.CharField(required=False, label='Projects')
    programming_languages = forms.CharField(required=True,label='Programming Languages')
    awards = forms.CharField(required=False, label='Awards')
    address = forms.CharField(required=True, label='Address')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender',
            'experience',
            'education',
            'last_job',
            'projects',
            'programming_languages',
            'awards',
            'phone_number',
            'address',
        )

    def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.phone_number = self.cleaned_data['phone_number']
            user.experience = self.cleaned_data['experience']
            user.gender = self.cleaned_data['gender']
            user.education = self.cleaned_data['education']
            user.last_job = self.cleaned_data['last_job']
            user.projects = self.cleaned_data['projects']
            user.programming_languages = self.cleaned_data['programming_languages']
            user.awards = self.cleaned_data['awards']
            user.address = self.cleaned_data['address']

            if commit:
                    user.save()
            return user