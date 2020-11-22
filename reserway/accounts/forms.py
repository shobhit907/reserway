from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import BookingAgent

class ExtendedUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={ 'required':True}),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(attrs={'required':True}),

        }

    def save(self,commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']

        if commit:
            user.save()
        return user 

class BookingAgentForm(ModelForm):
    class Meta:
        model=BookingAgent
        fields=('credit_card','address')