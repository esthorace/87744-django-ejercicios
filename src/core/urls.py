from django.urls import path

from core.views import ejercicio_4, home, login_view, te_saludo

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("te-saludo/", te_saludo, name="te_saludo"),
    path("ejercicio-4/", ejercicio_4, name="ejercicio_4"),
]
