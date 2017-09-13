from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    user = None

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        auth = authenticate(email=email,password=password)
        if not auth:
            raise forms.ValidationError("Check your password!")
        else:
            self.user = auth

        return cleaned_data