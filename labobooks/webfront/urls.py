from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='dashboard'), name='go-to-dashboard'),
    url(r'^dashboard', TemplateView.as_view(template_name="dashboard.html")),
    url(r'^indices', TemplateView.as_view(template_name="indices.html")),
    url(r'^shopping', TemplateView.as_view(template_name="shopping.html")),
    url(r'^stats', TemplateView.as_view(template_name="stats.html")),
    url(r'^private', login_required(TemplateView.as_view(template_name="indices.html"))),
    url(r'^login', TemplateView.as_view(template_name="login.html")),
)