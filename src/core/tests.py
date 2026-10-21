from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def setUp(self):
        self.password = "un-password-seguro-2026"
        self.user = get_user_model().objects.create_user(
            username="usuario",
            password=self.password,
        )

    def test_get_displays_login_form(self):
        response = self.client.get(reverse("core:login"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')
        self.assertContains(response, "core/login.css")

    def test_invalid_credentials_display_error(self):
        response = self.client.post(
            reverse("core:login"),
            {"username": self.user.username, "password": "incorrecta"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Usuario o contraseña incorrectos.")
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_valid_credentials_log_user_in_and_redirect_home(self):
        response = self.client.post(
            reverse("core:login"),
            {"username": self.user.username, "password": self.password},
        )

        self.assertRedirects(response, reverse("core:home"))
        self.assertEqual(
            self.client.session["_auth_user_id"],
            str(self.user.pk),
        )

    def test_valid_credentials_show_success_message(self):
        response = self.client.post(
            reverse("core:login"),
            {"username": self.user.username, "password": self.password},
            follow=True,
        )

        self.assertContains(response, "Acceso correcto")


class NavbarAuthStateTests(TestCase):
    def setUp(self):
        self.password = "un-password-seguro-2026"
        self.user = get_user_model().objects.create_user(
            username="usuario",
            password=self.password,
        )

    def test_anonymous_user_sees_links_and_access(self):
        response = self.client.get(reverse("core:home"))

        self.assertContains(response, '<a href="#servicios">Servicios</a>', count=3)
        self.assertContains(response, reverse("core:login"))
        self.assertNotContains(response, 'class="nav-user"')

    def test_authenticated_user_sees_username_instead_of_links(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse("core:home"))
        content = response.content.decode()

        self.assertContains(response, '<span class="nav-user">usuario</span>', count=2)
        # Solo queda el enlace del footer; el navbar ya no muestra los enlaces
        self.assertEqual(content.count('<a href="#servicios">Servicios</a>'), 1)
        self.assertNotContains(response, reverse("core:login"))
