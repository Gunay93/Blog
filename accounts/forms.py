from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Username', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Username"
    }))
    password = forms.CharField(max_length=255, label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Password"
    }))

    class Meta:
        model = User
        fields = ['username', 'password1']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password is wrong!')
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label='Username', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Username"
    }))
    first_name = forms.CharField(max_length=255, label='First name', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "First name"
    }))
    last_name = forms.CharField(max_length=255, label='Last Name', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Last Name"
    }))
    email = forms.EmailField(max_length=255, label='Email', widget=forms.EmailInput(attrs={
        "class": "form-control", "placeholder": "Email"
    }))
    password1 = forms.CharField(max_length=255, label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Password"
    }))
    password2 = forms.CharField(max_length=255, label='PasswordConfirm', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Password Confirm"
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords not equals!')
        return super(RegisterForm, self).clean()
