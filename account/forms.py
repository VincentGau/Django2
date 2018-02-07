from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length='100',
                               error_messages={'required': 'username is required.'},
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'username'
                                   }
                               )
                               )
    password = forms.CharField(error_messages={'required': 'password is required'},
                               widget=forms.PasswordInput(
                                   attrs={
                                       'placeholder': 'password'
                                   }
                               ))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Login failed, please try again')
        if not user.is_active:
            raise forms.ValidationError('User is not active, please contact administrator.')
        return self.cleaned_data
