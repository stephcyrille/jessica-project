from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from simple_sso.sso_server.server import Server
from .views import LoginView, LogoutView

test_server = Server()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/login/$', LoginView.as_view(), name="login"),
    url(r'^auth/logout/$', LogoutView.as_view(), name="logout"),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
]

urlpatterns += [
    url(r'^server/', include(test_server.get_urls())),
]
