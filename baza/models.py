from django.db import models

# Create your models here.


class Miejscowosc(models.Model):
    nazwa = models.CharField(max_length=50)
    def __str__(self):
        return str(self.nazwa)

class Adres(models.Model):
    przedrostek = models.CharField(max_length=10, blank=True)
    ulica = models.CharField(max_length=60)
    numer = models.CharField(max_length=30)
    miejscowosc = models.ForeignKey(Miejscowosc)
    def __str__(self):
        return ' '.join((str(self.ulica), str(self.numer), str(self.miejscowosc)))


class Osoba(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        return str(self.imie) + ' ' + str(self.nazwisko)



class Firma(models.Model):
    nazwa = models.CharField(max_length=60, blank=True)
    wlasciciel = models.ForeignKey(Osoba, blank=True, null=True)
    adres = models.ForeignKey(Adres, blank=True, null=True)
#   podstawowy_telefon = models.ForeignKey(Telefon, blank=True, null=True)
    www = models.CharField(max_length=100, blank=True)
    uwagi = models.TextField(blank=True)

class Telefon(models.Model):
    firma = models.ForeignKey(Firma)
    numer = models.CharField(max_length=20)
    rodzaj = models.CharField(max_length=5)
    osoba = models.ForeignKey(Osoba, blank=True, null=True)
    czy_podstawowy = models.BooleanField()









