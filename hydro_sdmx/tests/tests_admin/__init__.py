from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from ...models import Organisation

class TestAdminBase(TestCase):

    def setUp(self):
        username = 'test_admin'
        password = User.objects.make_random_password()
        self.user = User.objects.create_superuser(username, 'test_admin@gmail.com', password)
        client = Client()
        client.login(username=username, password=password)
        self.client = client
        self.app_label = Organisation._meta.app_label
        self.factory = RequestFactory()

