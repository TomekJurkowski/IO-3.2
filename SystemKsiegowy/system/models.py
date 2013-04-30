from django.core.exceptions import ValidationError
from django.db import models


class BilansOtwarcia(models.Model):
    """
    Bilans Otwracia skladajacy sie z Aktyw (trwalych i obrotowych) oraz
    Pasyw (dlugo- i krotkoterminowych).
    """
    # aktywaTrwale
    wartosciNiematerialneIPrawne = models.IntegerField(default=0)
    grunty = models.IntegerField(default=0)
    budynkiIBudowle = models.IntegerField(default=0)
    maszynyIUrzadzenia = models.IntegerField(default=0)
    inwestycjeRozpoczete = models.IntegerField(default=0)
    dlugoterminowePapieryWartosciowe = models.IntegerField(default=0)
    pozostalyMajatekTrwaly = models.IntegerField(default=0)
    # aktywaObrotowe
    naleznosciIRoszczenia = models.IntegerField(default=0)
    zapasy = models.IntegerField(default=0)
    srodkiPieniezne = models.IntegerField(default=0)
    pozostalyMajatekObrotowy = models.IntegerField(default=0)
    # pasywaDlugoterminowe
    funduszeWlasne = models.IntegerField(default=0)
    zobowiazaniaDlugoterminowe = models.IntegerField(default=0)
    # pasywaKrotkoterminowe
    zobowiazaniaKrotkoterminowe = models.IntegerField(default=0)
    kredytyIPozyczkiKrotkoterminowe = models.IntegerField(default=0)
    pozostalePasywa = models.IntegerField(default=0)

    def getSumaAktyw(self):
        return (self.wartosciNiematerialneIPrawne + self.grunty + self.budynkiIBudowle + self.maszynyIUrzadzenia
                + self.inwestycjeRozpoczete + self.dlugoterminowePapieryWartosciowe + self.pozostalyMajatekTrwaly)

    def getSumaPasyw(self):
        return (self.funduszeWlasne + self.zobowiazaniaDlugoterminowe + self.zobowiazaniaKrotkoterminowe
                + self.kredytyIPozyczkiKrotkoterminowe + self.pozostalePasywa)

    def __unicode__(self):
        return 'Bilans otwarcia o sumie aktyw = %d zl i sumie pasyw = %d zl.' % (self.getSumaAktyw(), self.getSumaPasyw())


class Osoba(models.Model):
    """
    Osoba reprezentuje osobe fizyczna (wtedy w miejscu nazwy pojawic powinno sie imie i nazwisko)
    lub osobe prawna (firme, przedsiebiorstwo, itp.).
    """
    nazwa = models.CharField(max_length=80)
    adres = models.CharField(max_length=100)
    miasto = models.CharField(max_length=50)
    kod = models.CharField(max_length=5)
    NIP = models.CharField(max_length=10)

    def clean_fields(self, exclude=None):
        if self.nazwa == '' or self.nazwa == None:
            raise ValidationError(u'Podaj nazwe (imie i nazwisko w pzypadku osoby fizycznej).')
        if self.adres == '' or self.adres == None:
            raise ValidationError(u'Podaj adres.')
        if self.miasto == '' or self.miasto== None:
            raise ValidationError(u'Podaj miejscowosc.')
        if self.kod == '' or self.kod == None:
            raise ValidationError(u'Podaj kod pocztowy (5 cyfr).')
        if not (self.kod.isdigit()) or (len(self.kod) != 5):
            raise ValidationError(u'Kod Pocztowy powinien skladac sie z 5 cyfr.')
        if self.NIP == '' or self.NIP == None:
            raise ValidationError(u'Podaj NIP (10 cyfr).')
        if not (self.NIP.isdigit()) or (len(self.NIP) != 5):
            raise ValidationError(u'NIP powinien skladac sie z 10 cyfr.')

    def __unicode__(self):
        return '%s' % self.nazwa


class FakturaVAT(models.Model):
    """
    Faktura VAT.
    """
    nrFaktury = models.CharField(max_length=15)
    dataSprzedazy = models.DateField()
    dataWystawienia = models.DateField()
    sprzedawca = Osoba()
    nabywca = Osoba()
    sposobZaplaty = models.CharField(max_length=25)
    terminZaplaty = models.DateField()
    uwagi = models.TextField()

    def clean_fields(self, exclude=None):
        pass

    def __unicode__(self):
        return 'Faktura VAT nr %s' % self.nrFaktury


class PozycjaFaktury(models.Model):
    """
    Pojedyncza pozycja faktury VAT.
    """
    fakturaVAT = models.ForeignKey(FakturaVAT)
    nazwa = models.CharField(max_length=60)
    PKWiU = models.CharField(max_length=20)
    jednostkaMiary = models.CharField(max_length=15)
    ilosc = models.PositiveIntegerField()
    cena = models.FloatField()
    VAT = models.PositiveIntegerField()

    def clean_fields(self, exclude=None):
        pass

    def __unicode__(self):
        return 'Pozycja faktury VAT o numerze %s. Nazwa pozycji: %s ' % (self.fakturaVAT.nrFaktury, self.nazwa)

