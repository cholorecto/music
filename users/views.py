from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import login, logout

from .forms import LoginForm


class UserLogin(TemplateView):
    """ User login account
    """
    template_name = 'auth/login.html'

    def get(self, *args, **kwargs):
        """ Displays the login form
        """
        form = LoginForm()
        return render(self.request, self.template_name, {'form':form})

    def post(self, *args, **kwargs):
        """ submits the data
        """
        form = LoginForm(self.request.POST)
        if form.is_valid():
            login(self.request, form.user)
            return redirect('Dashboard')

        return render(self.request, self.template_name, {'form':form})


class Dashboard(TemplateView):
    """ Displays the dashboard page
    """
    template_name = 'dashboard.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class UserLogout(View):
    """ Logout the user account
    """
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('UserLogin')
