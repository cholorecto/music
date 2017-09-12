from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import logout

from .forms import LoginForm


class UserLogin(TemplateView):
    """ User login account
    """
    template_name = 'auth/login.html'

    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, self.template_name, {'form':form})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        form.auth()
        return redirect('UserLogin')