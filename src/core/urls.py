from django.contrib.auth.views import LogoutView
from django.urls import path

from core.views import (
    CustomLoginView,
    # LogoutDoneView,
    # ejercicio_4,
    home,
    # te_saludo,
)

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    # path("login/", login_view, name="login"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    # path("logout/done/", LogoutDoneView.as_view(), name="logout_done"),
    # path("te-saludo/", te_saludo, name="te_saludo"),
    # path("ejercicio-4/", ejercicio_4, name="ejercicio_4"),
]
