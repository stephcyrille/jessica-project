from django.conf.urls import url, include
from django.contrib import admin
from simple_sso.sso_server.server import Server
from .views import LoginView, LogoutView

test_server = Server()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/login/$', LoginView.as_view(), name="login"),
    url(r'^auth/logout/$', LogoutView.as_view(), name="logout"),
]

urlpatterns += [
    url(r'^server/', include(test_server.get_urls())),
]
