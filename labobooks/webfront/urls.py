from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf.urls import url

from webfront import views


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^welcome/?$',
        TemplateView.as_view(template_name="welcome.html"), name='welcome'),
    url(r'^about/?$',
        TemplateView.as_view(template_name="labobooks_about.html"), name='about'),
    url(r'^terms/?$',
        TemplateView.as_view(template_name="labobooks_terms.html"), name='terms'),
    url(r'^privacy/?$',
        TemplateView.as_view(template_name="labobooks_privacy.html"), name='privacy'),
    url(r'^login/?$', RedirectView.as_view(pattern_name='account_login')),

    url(
        r'^organizations/new/?$', views.OrganizationView.as_view(), name='organization_new'
    ),
    url(
        r'^(?P<organization_slug>[\w_-]+)/dashboard/?$',
        login_required(TemplateView.as_view(template_name="dashboard.html")),
        name='dashboard'
    ),
    url(
        r'^(?P<organization_slug>[\w_-]+)/indices/?$',
        login_required(TemplateView.as_view(template_name="indices.html")),
        name='indices'
    ),
    url(
        r'^(?P<organization_slug>[\w_-]+)/shopping/?$',
        login_required(TemplateView.as_view(template_name="shopping.html")),
        name='shopping'
    ),
    url(
        r'^(?P<organization_slug>[\w_-]+)/stats/?$',
        login_required(TemplateView.as_view(template_name="stats.html")),
        name='stats'
    ),
    url(
        r'^(?P<organization_slug>[\w_-]+)/$',
        RedirectView.as_view(pattern_name='dashboard'),
        name='organization_home'
    ),
]
