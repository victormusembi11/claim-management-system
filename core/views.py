from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):

    def get(self, request):
        return render(request, 'home.html', content_type='text/html')


class AboutView(TemplateView):

    def get(self, request):
        return render(request, 'about.html', content_type='text/html')
