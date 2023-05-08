from django.urls import path

from contact import views

urlpatterns = [
    path('', views.ContactTemplateView.as_view(), name="contact")
]