from django.contrib import admin
from django.urls import reverse
from django.contrib.admin import AdminSite
from ...models import Organisation, OrganisationScheme, Codelist, ConceptScheme, DataStructure
from ...admin import OrganisationAdmin, OrganisationSchemeAdmin, CodelistAdmin, ConceptSchemeAdmin, DataStructureAdmin

from .. import data
from . import TestAdminBase 

class TestAdmin(TestAdminBase):
    def setUp(self):
        super().setUp()
        self.admin_site = AdminSite()

    def _get_admin_app_urls(self):
        return ('/admin/%s' % url.regex.pattern[1:] 
                for url in admin.site.get_urls()
                if url.regex.pattern.startswith('^%s' % self.app_label) 
        )

    def test_get_admin(self):
        for page in self._get_admin_app_urls():
            resp = self.client.get(page)
            assert resp.status_code == 200
            assert '<!DOCTYPE html'.encode() in resp.content

    def Test_put_organisation(self):
        admin_inst = OrganisationAdmin(Organisation, self.admin_site)
        request = reverse('admin:%s_organisation_add' % self.app_label)
        request_obj = self.factory.get(request)
        request_obj.user = self.user
        form = admin_inst.get_form(request_obj)(data.organisation)
        formsets = admin_inst.get_formsets_with_inlines(request_obj)
        self.assertEqual(form.is_valid(), True)
        for form in formsets:
            self.assertEqual(form[0](data.organisation).is_valid(), True)

        self.client.post(request, data.organisation)
        request = 'admin:%s_organisation_changelist' % self.app_label
        response = self.client.get(reverse(request))
        self.assertEqual(response.context['cl'].result_count, 1)

    def Test_put_organisationscheme(self):
        self.Test_put_organisation()
        admin_inst = OrganisationSchemeAdmin(OrganisationScheme, self.admin_site)
        request = reverse('admin:%s_organisationscheme_add' % self.app_label)
        form = admin_inst.get_form(request)(data.organisation_scheme)
        self.assertEqual(form.is_valid(), True, form.errors)
        self.client.post(request, data.organisation_scheme)
        request = reverse('admin:%s_organisationscheme_changelist' % self.app_label)
        response = self.client.get(request)
        self.assertEqual(response.context['cl'].result_count, 1)

    def Test_put_codelist(self):
        self.Test_put_organisationscheme()
        admin_inst = CodelistAdmin(Codelist, self.admin_site)
        request = reverse('admin:%s_codelist_add' % self.app_label)
        form = admin_inst.get_form(request)(data.codelist)
        self.assertEqual(form.is_valid(), True, form.errors)
        self.client.post(request, data.codelist)
        request = reverse('admin:%s_codelist_changelist' % self.app_label)
        response = self.client.get(request)
        self.assertEqual(response.context['cl'].result_count, 1)

    def Test_put_conceptscheme(self):
        self.Test_put_codelist()
        admin_inst = ConceptSchemeAdmin(ConceptScheme, self.admin_site)
        request = reverse('admin:%s_conceptscheme_add' % self.app_label)
        form = admin_inst.get_form(request)(data.codelist)
        self.assertEqual(form.is_valid(), True, form.errors)
        self.client.post(request, data.conceptscheme)
        request = reverse('admin:%s_conceptscheme_changelist' % self.app_label)
        response = self.client.get(request)
        self.assertEqual(response.context['cl'].result_count, 1)
    
    def Test_put_datastructure(self):
        self.Test_put_conceptscheme()
        admin_inst = DataStructureAdmin(DataStructure, self.admin_site)
        request = reverse('admin:%s_datastructure_add' % self.app_label)
        form = admin_inst.get_form(request)(data.datastructure)
        self.assertEqual(form.is_valid(), True, form.errors)
        # request = reverse('admin:%s_datastructure_add' % self.app_label)
        # request_obj = self.factory.get(request)
        # request_obj.user = self.user
        # formsets = admin_inst.get_formsets_with_inlines(request_obj)
        # for i, formset in enumerate(formsets):
        #     boundform = formset[0].form(data.datastructure_comps[i])
        #
        #     self.assertEqual(boundform.is_valid(), True, boundform.errors)
        self.client.post(request, data.datastructure)
        request = reverse('admin:%s_datastructure_changelist' % self.app_label)
        response = self.client.get(request)
        self.assertEqual(response.context['cl'].result_count, 1)

    def test_put(self):
        self.Test_put_datastructure()
