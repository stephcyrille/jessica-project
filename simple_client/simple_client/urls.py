from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from simple_sso.sso_client.client import Client
from django.views.generic.base import TemplateView

test_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = [
    url(r'^admin/clearcache/', include('clearcache.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^client/', include(test_client.get_urls())),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', TemplateView.as_view(template_name='home.html'), name='home'),
]
