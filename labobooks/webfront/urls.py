from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='dashboard'), name='go-to-dashboard'),
    url(r'^dashboard', login_required(TemplateView.as_view(template_name="dashboard.html"))),
)
