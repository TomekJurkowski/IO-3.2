from django.forms import ModelForm, DateInput
from system.models import BilansOtwarcia, FakturaVATSprzedazy
from django import forms
from django.utils.encoding import smart_str

class BilansOtwarciaForm(ModelForm):
    class Meta:
        model = BilansOtwarcia


SPOSOBY_PLATNOSCI = [
    ('przelew', 'przelew'),
    ('gotowka', 'gotowka'),
    ('karta', 'karta'),
    ('platnosc elektroniczna', 'platnosc elektroniczna')
]

class FakturaVATSprzedazyForm(forms.Form):

    data_sprzedazy = forms.DateField(label='Data sprzedazy:', widget=DateInput)
    data_wystawienia = forms.DateField(label='Data wystawienia:', widget=DateInput)

    sprzedawca_nazwa = forms.CharField(label='Nazwa sprzedawcy:', max_length=80)
    sprzedawca_adres = forms.CharField(label='Adres:', max_length=100)
    sprzedawca_miasto = forms.CharField(label='Miasto:', max_length=50)
    sprzedawca_kod = forms.CharField(label='Kod pocztowy:', help_text='Kod pocztowy powinien byc ciagiem 5 cyfr', max_length=5)
    sprzedawca_NIP = forms.CharField(label='NIP sprzedawcy:', help_text='Nr NIP powinien byc ciagiem 10 cyfr', max_length=10)

    nabywca_nazwa = forms.CharField(label='Nazwa nabywcy:', max_length=80)
    nabywca_adres = forms.CharField(label='Adres:', max_length=100)
    nabywca_miasto = forms.CharField(label='Miasto:', max_length=50)
    nabywca_kod = forms.CharField(label='Kod pocztowy:', help_text='Kod pocztowy powinien byc ciagiem 5 cyfr', max_length=5)
    nabywca_NIP = forms.CharField(label='NIP nabywcy:', help_text='Nr NIP powinien byc ciagiem 10 cyfr', max_length=10)

    sposob_zaplaty = forms.ChoiceField(label='Sposob zaplaty:', widget=forms.Select(), choices=SPOSOBY_PLATNOSCI)
    termin_zaplaty = forms.DateField(label='Termin zaplaty:', widget=DateInput)
    bank = forms.CharField(label='Bank:', max_length=70, required=False)
    nr_konta = forms.CharField(label='Numer konta:', max_length=32, required=False)
    uwagi = forms.CharField(label='Uwagi:', help_text='Tu wpisz dodatkowe informacje, uwagi - pole nieobowiazkowe', widget=forms.Textarea, required=False)

    def clean(self):
        cleaned_data = super(FakturaVATSprzedazyForm, self).clean()

        ds = cleaned_data.get("data_sprzedazy", None)
        dw = cleaned_data.get("data_wystawienia", None)
        tz = cleaned_data.get("termin_zaplaty", None)
        if ds and dw:
            if ds > dw:
                self._errors['data_sprzedazy'] = self.error_class([u'Data sprzedazy nie moze byc pozniejsza od daty wystawienia.'])
                self._errors['data_wystawienia'] = self.error_class([u'Data wystawienia nie moze byc wczesniejsza od daty sprzedazy.'])
        if tz and dw:
            if tz > dw:
                self._errors['termin_zaplaty'] = self.error_class([u'Termin zaplaty nie moze byc pozniejszy od daty wystawienia.'])
                self._errors['data_wystawienia'] = self.error_class([u'Data wystawienia nie moze byc wczesniejsza od terminu zaplaty.'])

        sk = cleaned_data.get("sprzedawca_kod", None)
        if sk:
            if len(sk) != 5:
                self._errors['sprzedawca_kod'] = self.error_class([u'Kod pocztowy powinien skladac sie z 5 cyfr.'])
        nk = cleaned_data.get("nabywca_kod", None)
        if nk:
            if len(nk) != 5:
                self._errors['nabywca_kod'] = self.error_class([u'Kod pocztowy powinien skladac sie z 5 cyfr.'])
        sn = cleaned_data.get("sprzedawca_NIP", None)
        if sn:
            if len(sn) != 10:
                self._errors['sprzedawca_NIP'] = self.error_class([u'Kod pocztowy powinien skladac sie z 10 cyfr.'])
        nn = cleaned_data.get("nabywca_NIP", None)
        if nn:
            if len(nn) != 10:
                self._errors['nabywca_NIP'] = self.error_class([u'Kod pocztowy powinien skladac sie z 10 cyfr.'])

        sz = cleaned_data.get("sposob_zaplaty", None)
        b = cleaned_data.get("bank", None)
        nr = cleaned_data.get("nr_konta", None)
        if sz == 'przelew':
            if not b or b == '' :
                self._errors['bank'] = self.error_class([u'Dla przelewu musi byc zdefiniowany bank.'])
            if not nr or nr == '' :
                self._errors['nr_konta'] = self.error_class([u'Dla przelewu musi byc zdefiniowany nr konta bankowego.'])
            else:
                if not nr.isdigit():
                    self._errors['nr_konta'] = self.error_class([u'Nr konta bankowego powinno skladac sie z samych cyfr.'])
        else:
            if b and b != '':
                self._errors['bank'] = self.error_class([u'To pole musi byc zdefiniowane tylko dla sposobu zaplaty - przelew.'])
            if nr and nr != '':
                self._errors['nr_konta'] = self.error_class([u'To pole musi byc zdefiniowane tylko dla sposobu zaplaty - przelew.'])

        return cleaned_data


JEDNOSTKI_MIARY = [
    ('szt.', 'szt.'),
    ('kg', 'kg'),
    ('litr', 'litr')
]

class PozycjaFakturyForm(forms.Form):
    nazwa = forms.CharField(label='Nazwa pozycji:', max_length=80)
    PKWiU = forms.CharField(label='PKWiU', max_length=20)
    jednostkaMiary = forms.ChoiceField(label='Jednostka miary', widget=forms.Select(), choices=JEDNOSTKI_MIARY)
    ilosc = forms.IntegerField(label='Ilosc')
    cena = forms.FloatField(label='cena')
    VAT = forms.IntegerField(label='VAT')

    def clean(self):
        cleaned_data = super(PozycjaFakturyForm, self).clean()
        i = cleaned_data.get("ilosc", None)
        c = cleaned_data.get("cena", None)
        v = cleaned_data.get("VAT", None)
        if i <= 0:
            self._errors['ilosc'] = self.error_class([u'Ilosc powinna byc wartoscia dodatnia.'])
        if c <= 0:
            self._errors['cena'] = self.error_class([u'Cena powinna byc wartoscia dodatnia.'])
        if v <= 0 or v >= 100:
            self._errors['VAT'] = self.error_class([u'Wartosc pola VAT powinna byc z zakresu (0, 100).'])

        return cleaned_data


class FakturaVATZakupuForm(forms.Form):

    nr_faktury = forms.CharField(label='Numer faktury:', max_length=40)
    data_sprzedazy = forms.DateField(label='Data sprzedazy:', widget=DateInput)
    data_wystawienia = forms.DateField(label='Data wystawienia:', widget=DateInput)

    sprzedawca_nazwa = forms.CharField(label='Nazwa sprzedawcy:', max_length=80)
    sprzedawca_adres = forms.CharField(label='Adres:', max_length=100)
    sprzedawca_miasto = forms.CharField(label='Miasto:', max_length=50)
    sprzedawca_kod = forms.CharField(label='Kod pocztowy:', help_text='Kod pocztowy powinien byc ciagiem 5 cyfr', max_length=5)
    sprzedawca_NIP = forms.CharField(label='NIP sprzedawcy:', help_text='Nr NIP powinien byc ciagiem 10 cyfr', max_length=10)

    nabywca_nazwa = forms.CharField(label='Nazwa nabywcy:', max_length=80)
    nabywca_adres = forms.CharField(label='Adres:', max_length=100)
    nabywca_miasto = forms.CharField(label='Miasto:', max_length=50)
    nabywca_kod = forms.CharField(label='Kod pocztowy:', help_text='Kod pocztowy powinien byc ciagiem 5 cyfr', max_length=5)
    nabywca_NIP = forms.CharField(label='NIP nabywcy:', help_text='Nr NIP powinien byc ciagiem 10 cyfr', max_length=10)

    sposob_zaplaty = forms.ChoiceField(label='Sposob zaplaty:', widget=forms.Select(), choices=SPOSOBY_PLATNOSCI)
    termin_zaplaty = forms.DateField(label='Termin zaplaty:', widget=DateInput)
    bank = forms.CharField(label='Bank:', max_length=70, required=False)
    nr_konta = forms.CharField(label='Numer konta:', max_length=32, required=False)
    uwagi = forms.CharField(label='Uwagi:', help_text='Tu wpisz dodatkowe informacje, uwagi - pole nieobowiazkowe', widget=forms.Textarea, required=False)

    def clean(self):
        cleaned_data = super(FakturaVATZakupuForm, self).clean()

        ds = cleaned_data.get("data_sprzedazy", None)
        dw = cleaned_data.get("data_wystawienia", None)
        tz = cleaned_data.get("termin_zaplaty", None)
        if ds and dw:
            if ds > dw:
                self._errors['data_sprzedazy'] = self.error_class([u'Data sprzedazy nie moze byc pozniejsza od daty wystawienia.'])
                self._errors['data_wystawienia'] = self.error_class([u'Data wystawienia nie moze byc wczesniejsza od daty sprzedazy.'])
        if tz and dw:
            if tz > dw:
                self._errors['termin_zaplaty'] = self.error_class([u'Termin zaplaty nie moze byc pozniejszy od daty wystawienia.'])
                self._errors['data_wystawienia'] = self.error_class([u'Data wystawienia nie moze byc wczesniejsza od terminu zaplaty.'])

        sk = cleaned_data.get("sprzedawca_kod", None)
        if sk:
            if len(sk) != 5:
                self._errors['sprzedawca_kod'] = self.error_class([u'Kod pocztowy powinien skladac sie z 5 cyfr.'])
        nk = cleaned_data.get("nabywca_kod", None)
        if nk:
            if len(nk) != 5:
                self._errors['nabywca_kod'] = self.error_class([u'Kod pocztowy powinien skladac sie z 5 cyfr.'])
        sn = cleaned_data.get("sprzedawca_NIP", None)
        if sn:
            if len(sn) != 10:
                self._errors['sprzedawca_NIP'] = self.error_class([u'Kod pocztowy powinien skladac sie z 10 cyfr.'])
        nn = cleaned_data.get("nabywca_NIP", None)
        if nn:
            if len(nn) != 10:
                self._errors['nabywca_NIP'] = self.error_class([u'Kod pocztowy powinien skladac sie z 10 cyfr.'])

        sz = cleaned_data.get("sposob_zaplaty", None)
        b = cleaned_data.get("bank", None)
        nr = cleaned_data.get("nr_konta", None)
        if sz == 'przelew':
            if not b or b == '' :
                self._errors['bank'] = self.error_class([u'Dla przelewu musi byc zdefiniowany bank.'])
            if not nr or nr == '' :
                self._errors['nr_konta'] = self.error_class([u'Dla przelewu musi byc zdefiniowany nr konta bankowego.'])
            else:
                if not nr.isdigit():
                    self._errors['nr_konta'] = self.error_class([u'Nr konta bankowego powinno skladac sie z samych cyfr.'])
        else:
            if b and b != '':
                self._errors['bank'] = self.error_class([u'To pole musi byc zdefiniowane tylko dla sposobu zaplaty - przelew.'])
            if nr and nr != '':
                self._errors['nr_konta'] = self.error_class([u'To pole musi byc zdefiniowane tylko dla sposobu zaplaty - przelew.'])

        return cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Haslo:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtorz haslo:",widget=forms.PasswordInput())
    log_on = forms.BooleanField(label="Logowanie po rejestracji:",required=False)
