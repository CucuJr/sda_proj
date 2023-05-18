from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class CategoriiTemplateView(TemplateView):
    template_name = 'categorii/petroliere.html'
