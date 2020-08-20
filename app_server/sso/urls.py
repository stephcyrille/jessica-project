from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from simple_sso.sso_server.server import Server


test_server = Server()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cache/clearcache/', include('clearcache.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', TemplateView.as_view(template_name='home.html'), name='home'),
]

urlpatterns += [
    url(r'^server/', include(test_server.get_urls())),
]
