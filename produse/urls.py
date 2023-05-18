from django.urls import path

from produse import views

urlpatterns = [
    path('', views.ProduseTemplateView.as_view(), name="categorii")
]