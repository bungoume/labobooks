from account.forms import SignupForm as DefaultSignupForm
from account.views import SignupView as DefaultSignupView


class SignupForm(DefaultSignupForm):
    field_order = ['username', 'email', 'password', 'password_confirm']


class SignupView(DefaultSignupView):
    form_class = SignupForm
