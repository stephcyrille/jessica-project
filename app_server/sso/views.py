from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
import pyotp
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
        return HttpResponseRedirect('qr/login/')
        # return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    message = ""
    if user is None:
        message = "Mauvais informations d'authentification"

    context = {
        "message" : message
    }
    return render(request, self.template_name, context)


class LogoutView(TemplateView):

  template_name = 'registration/login.html'

  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)


# Create your views here.
def qr_login(request):
    template_name = 'registration/login_confirmation.html'
    if request.method == "POST":
        authtoken = request.POST.get('authtoken', False)
        base32secret = settings.OTP_SECRET_KEY
        totp = pyotp.TOTP(base32secret)
        if totp.verify(authtoken) == True:
            return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
        else:
            context = {
                "auth_message" : "Mauvais OTP ou OTP expiré"
            }
            return render(request, template_name, context)
    authUri = pyotp.totp.TOTP(settings.OTP_SECRET_KEY).provisioning_uri(issuer_name="Jess 2FA Server")
    print(authUri)
    context = {
        "hash_code" : authUri
    }
    return render(request, template_name, context)
