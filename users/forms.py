from django import forms
#from django.contrib.auth import authenticate, login,

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def auth(self, *args, **kwargs):
        import pdb;pdb.set_trace()