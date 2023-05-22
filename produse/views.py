from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from produse.forms import PPetrolierForm
from produse.models import PPetrolier


class PPetrolierCreateView(CreateView):
    template_name = "categorii/create_ppetroliere.html"
    model = PPetrolier
    form_class = PPetrolierForm
    success_url = reverse_lazy("list-ppetroliere")


class PPetrolierListView(ListView):
    template_name = "categorii/list_ppetroliere.html"
    model = PPetrolier
    context_object_name = "all_ppetroliere"