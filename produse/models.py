from django.db import models


class PPetrolier(models.Model):

    denumire = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    informatii = models.TextField(max_length=100)
    tipul = models.CharField(max_length=20)
    profil = models.ImageField(upload_to="images/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.denumire}"


class PCuratenie(models.Model):

    denumire = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    informatii = models.TextField(max_length=100)
    tipul = models.CharField(max_length=20)
    profil = models.ImageField(upload_to="images/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.denumire}"


class PConsumabil(models.Model):

    denumire = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    informatii = models.TextField(max_length=100)
    tipul = models.CharField(max_length=20)
    profil = models.ImageField(upload_to="images/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.denumire}"