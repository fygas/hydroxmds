from django.contrib import admin
from . import TestAdminBase

class TestAdminGet(TestAdminBase):
    _name = 'hydro_sdmx'

    def _get_admin_app_urls(self):
        return ('/admin/%s' % url.regex.pattern[1:] 
                for url in admin.site.get_urls()
                if url.regex.pattern.startswith('^%s' % self._name) 
        )

    def test_get_admin(self):
        for page in self._get_admin_app_urls():
            resp = self.client.get(page)
            assert resp.status_code == 200
            assert '<!DOCTYPE html'.encode() in resp.content
