from django import forms
from django.forms import TextInput

from produse.models import PPetrolier, PCuratenie, PConsumabil


class PPetrolierForm(forms.ModelForm):
    class Meta:
        model = PPetrolier
        fields = "__all__"

        widgets = {
            "denumire":TextInput(attrs={'placeholder': 'Introduceti denumirea produsului', 'class':'form-control'}),
            "brand":TextInput(attrs={'placeholder': 'Introduceti brand-ul produsului', 'class':'form-control'}),
            "model":TextInput(attrs={'placeholder': 'Introduceti modelul produsului', 'class':'form-control'}),
            "informatii":TextInput(attrs={'placeholder': 'Introduceti informatiile produsului', 'class':'form-control'}),
            "tipul":TextInput(attrs={'placeholder': 'Introduceti tipul produsului', 'class':'form-control'}),

        }

class PCuratenieForm(forms.ModelForm):
    class Meta:
        model = PCuratenie
        fields = "__all__"

        widgets = {
            "denumire":TextInput(attrs={'placeholder': 'Introduceti denumirea produsului', 'class':'form-control'}),
            "brand":TextInput(attrs={'placeholder': 'Introduceti brand-ul produsului', 'class':'form-control'}),
            "model":TextInput(attrs={'placeholder': 'Introduceti modelul produsului', 'class':'form-control'}),
            "informatii":TextInput(attrs={'placeholder': 'Introduceti informatiile produsului', 'class':'form-control'}),
            "tipul":TextInput(attrs={'placeholder': 'Introduceti tipul produsului', 'class':'form-control'}),

        }


class PConsumabilForm(forms.ModelForm):
    class Meta:
        model = PConsumabil
        fields = "__all__"

        widgets = {
            "denumire":TextInput(attrs={'placeholder': 'Introduceti denumirea produsului', 'class':'form-control'}),
            "brand":TextInput(attrs={'placeholder': 'Introduceti brand-ul produsului', 'class':'form-control'}),
            "model":TextInput(attrs={'placeholder': 'Introduceti modelul produsului', 'class':'form-control'}),
            "informatii":TextInput(attrs={'placeholder': 'Introduceti informatiile produsului', 'class':'form-control'}),
            "tipul":TextInput(attrs={'placeholder': 'Introduceti tipul produsului', 'class':'form-control'}),

        }