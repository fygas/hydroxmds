from . import TestAdminBase

class TestAdminGet(TestAdminBase):
    admin_pages = [
        '/admin/hydro_sdmx/',
        '/admin/hydro_sdmx/agencyscheme/',
    ]

    def test_get_admin(self):
        for page in self.admin_pages:
            resp = self.client.get(page)
            assert resp.status_code == 200
            assert '<!DOCTYPE html'.encode() in resp.content
