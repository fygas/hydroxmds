from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from ...models import Organisation 
from ...admin.organisation import OrganisationAdmin

class ModelAdminTests(TestCase):
    def setup(self):
        self.org = Organisation.objects.create(
            id_code = 'BOG',
            name = 'Bank of Greece',
        )
        self.site = AdminSite()

    def test_modeladmin_str(self):
        self.assertEqual(str(OrganisationAdmin), "<class 'hydro_sdmx.admin.organisation.OrganisationAdmin'>")
