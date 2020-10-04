from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
import pyotp
from .forms import LoginForm
from encrypted_login.models import AuthChecker
from .lib.code_generator import generateCode
from .lib.code_encrypt_decrypt import encrypt_message, decrypt_message


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
        # TODO Check code hashedv there
        auth_checker = AuthChecker.objects.filter(status="wait").first()
        if authtoken == auth_checker.q_code:
            if not auth_checker.is_expired():
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                context = {
                "auth_message" : "Votre OTP a expiré"
            }
            return render(request, template_name, context)
        else:
            context = {
                "auth_message" : "Mauvais OTP"
            }
            return render(request, template_name, context)
    user = request.user
    code = generateCode(6)
    #  Put each authchecke reauest to close
    old_auth_checkers = AuthChecker.objects.filter(user=request.user, status="wait")
    for a in old_auth_checkers:
        a.status = "close"
        a.save()
    auth_checker = AuthChecker(user=user, q_code=code)
    auth_checker.save()
    encrypted_code = encrypt_message(code, settings.OTP_SECRET_KEY)
    print(encrypted_code)
    context = {
        "hash_code" : encrypted_code
    }
    return render(request, template_name, context)