from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestAdminBase(TestCase):

    def setUp(self):
        username = 'test_admin'
        password = User.objects.make_random_password()
        User.objects.create_superuser(username, 'test_admin@gmail.com', password)
        client = Client()
        client.login(username=username, password=password)
        self.client = client
