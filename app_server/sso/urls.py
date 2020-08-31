from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from qr_code import urls as qr_code_urls
from simple_sso.sso_server.server import Server
from .views import LoginView, LogoutView, qr_login

test_server = Server()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/login/$', LoginView.as_view(), name="login"),
    url(r'^auth/login/qr/login/$', login_required(qr_login), name="qr_login"),
    url(r'^auth/logout/$', LogoutView.as_view(), name="logout"),
    url(r'^qr_code/', include(qr_code_urls, namespace='qr_code')),
]

urlpatterns += [
    url(r'^server/', include(test_server.get_urls())),
]
