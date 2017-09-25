from django.conf.urls import url
from accountapp.views import SignupView


urlpatterns = [
    url(r"^signup/$", SignupView.as_view(), name="account_signup"),
]
