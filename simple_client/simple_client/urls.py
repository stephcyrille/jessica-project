from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from simple_sso.sso_client.client import Client
from .views import login


test_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='home/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^client/', include(test_client.get_urls())),
    url(r'^home/$', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
    url(r'^login/$', login, name='login'),
]
