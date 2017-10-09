from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from core import models
from webfront import forms


def home(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    if not request.user.org_memberships.exists():
        return redirect('organization_new')
    main_org = request.user.org_memberships.last()
    return redirect('dashboard', organization_slug=main_org.id_slug)


def organization_new(request):
    form = forms.OrganizationForm()
    return render(request, 'organization/new.html', {'form': form})


class OrganizationView(FormView):
    template_name = 'organization/new.html'
    form_class = forms.OrganizationForm
    model = models.Organization


    def form_valid(self, form):
        # import pdb;pdb.set_trace()
        form.save()
        form.instance.members.through.objects.create(
            organization=form.instance, user=self.request.user, role='owner')
        return redirect('dashboard', organization_slug=form.instance.id_slug)
