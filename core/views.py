from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name: str = 'home.html'


class AboutView(TemplateView):

    template_name: str = 'about.html'