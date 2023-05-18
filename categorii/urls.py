from django.urls import path

from categorii import views

urlpatterns = [
    path('', views.CategoriiTemplateView.as_view(), name="categorii")
]