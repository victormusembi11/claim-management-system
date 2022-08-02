from django.views.generic import CreateView

from ..forms import UserRegistrationForm


class RegistrationView(CreateView):

    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = 'registration/login'
