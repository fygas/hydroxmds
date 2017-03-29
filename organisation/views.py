from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import OrganisationScheme
from .forms import OrganisationSchemeForm, ExampleForm

class OrganisationSchemeCreate(CreateView):
    form_class = OrganisationSchemeForm
    model = OrganisationScheme


def get_organisation_scheme(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrganisationSchemeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrganisationSchemeForm()

    return render(request, 'organisation/organisationscheme_form.html', {'form': form})

class ExampleView(FormView):
    template_name = 'organisation/example.html'
    form_class = ExampleForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)
