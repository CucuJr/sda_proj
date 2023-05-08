from django.urls import path

from home import views

urlpatterns = [
    path('', views.ContactTemplateview.as_view(), name="contact")
]