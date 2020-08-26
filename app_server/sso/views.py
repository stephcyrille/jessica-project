from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

from .forms import LoginForm



# # Create your views here.
# def login(request):
#     template_name = 'registration/login.html'
#     context = {}
#     form = LoginForm(request.POST or None)
#     context['form'] = form
#     if request.POST:
#         if form.is_valid():
#             temp = form.cleaned_data.get("username")
#             print(temp)
#             # user = authenticate(username=username, password=password)
#             if user is not None and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
#     return render(request, template_name, context)

class LoginView(TemplateView):

  template_name = 'registration/login.html'

  def post(self, request, **kwargs):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'registration/login.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)
