from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.management.commands import startproject
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.utils.encoding import smart_str
from django.views.generic import TemplateView, FormView, DetailView
import time
from datetime import date

from system.forms import BilansOtwarciaForm, FakturaVATSprzedazyForm, PozycjaFakturyForm, FakturaVATZakupuForm, RegisterForm, EwidencjaVATForm
from system.models import BilansOtwarcia, FakturaVATSprzedazy, FakturaVATZakupu, PozycjaFakturySprzedazy


class StartPageView(TemplateView):
    template_name = "start_page.html"

    def get_context_data(self, **kwargs):
        elements = super(StartPageView, self).get_context_data()
        print(elements)
        print ('view')
        print (elements['view'])
        return elements


class BilansView(FormView):
    template_name = "bilans_form.html"
    form_class = BilansOtwarciaForm

    def form_valid(self, form):
        return HttpResponseRedirect(reverse('StartPage'))

    def get_context_data(self, **kwargs):
        context = super(BilansView, self).get_context_data()
        context['form'] = self.get_form(self.form_class)
        return context


def getFakturaNr():
    nr = 0
    t = smart_str(date.today())
    for f in FakturaVATSprzedazy.objects.all():
        if (smart_str(f.nrFaktury).find(t) >= 0):
            nr += 1

    return t + '/' + str(nr)

class KsiegowanieFakturSprzedazyView(FormView):
    template_name = "faktura_sprzedazy_form.html"
    form_class = FakturaVATSprzedazyForm

    def form_valid(self, form):
        cd = form.cleaned_data
        print(cd)
        f = FakturaVATSprzedazy(user=self.request.user, nrFaktury=getFakturaNr(), dataSprzedazy=cd['data_sprzedazy'], dataWystawienia=cd['data_wystawienia'],
                                sprzedawca_nazwa=cd['sprzedawca_nazwa'], sprzedawca_adres=cd['sprzedawca_adres'], sprzedawca_miasto=cd['sprzedawca_miasto'],
                                sprzedawca_kod=cd['sprzedawca_kod'], sprzedawca_NIP=cd['sprzedawca_NIP'],
                                nabywca_nazwa=cd['nabywca_nazwa'], nabywca_adres=cd['nabywca_adres'], nabywca_miasto=cd['nabywca_miasto'],
                                nabywca_kod=cd['nabywca_kod'], nabywca_NIP=cd['nabywca_NIP'],
                                sposobZaplaty=cd['sposob_zaplaty'], terminZaplaty=cd['termin_zaplaty'], bank=cd['bank'],
                                nrKonta=cd['nr_konta'], uwagi=cd['uwagi'])
        f.save()
        return HttpResponseRedirect(reverse('dodaniePozycjiFakturySprzedazy', kwargs={'id':f.id}))

    def get_context_data(self, **kwargs):
        context = super(KsiegowanieFakturSprzedazyView, self).get_context_data()
        context['form'] = self.get_form(self.form_class)
        context['faktura_nr'] = getFakturaNr()
        return context


class DodaniePozycjiFakturSprzedazyView(FormView):
    template_name = "pozycja_form.html"
    form_class = PozycjaFakturyForm

    def form_valid(self, form):
        cd = form.cleaned_data
        print(cd)
        p = PozycjaFakturySprzedazy(fakturaVAT=FakturaVATSprzedazy.objects.get(id=self.kwargs['id']),
                                    nazwa=cd['nazwa'], PKWiU=cd['PKWiU'], jednostkaMiary=cd['jednostkaMiary'],
                                    ilosc=cd['ilosc'], cena=cd['cena'], VAT=cd['VAT'])
        p.save()
        return HttpResponseRedirect(reverse('dodaniePozycjiFakturySprzedazy', kwargs={'id':self.kwargs['id']}))

    def get_context_data(self, **kwargs):
        context = super(DodaniePozycjiFakturSprzedazyView, self).get_context_data()
        context['form'] = self.get_form(self.form_class)
        context['faktura'] = FakturaVATSprzedazy.objects.get(id=self.kwargs['id']).nrFaktury
        context['pozycje'] = PozycjaFakturySprzedazy.objects.filter(fakturaVAT=FakturaVATSprzedazy.objects.get(id=self.kwargs['id']))
        return context


class KsiegowanieFakturZakupuView(FormView):
    template_name = "faktura_zakupu_form.html"
    form_class = FakturaVATZakupuForm

    def form_valid(self, form):
        cd = form.cleaned_data
        print(cd)
        f = FakturaVATZakupu(user=self.request.user, nrFaktury=cd['nr_faktury'], dataSprzedazy=cd['data_sprzedazy'], dataWystawienia=cd['data_wystawienia'],
                            sprzedawca_nazwa=cd['sprzedawca_nazwa'], sprzedawca_adres=cd['sprzedawca_adres'], sprzedawca_miasto=cd['sprzedawca_miasto'],
                            sprzedawca_kod=cd['sprzedawca_kod'], sprzedawca_NIP=cd['sprzedawca_NIP'],
                            nabywca_nazwa=cd['nabywca_nazwa'], nabywca_adres=cd['nabywca_adres'], nabywca_miasto=cd['nabywca_miasto'],
                            nabywca_kod=cd['nabywca_kod'], nabywca_NIP=cd['nabywca_NIP'],
                            kwota=cd['kwota'], VAT=cd['VAT'],
                            sposobZaplaty=cd['sposob_zaplaty'], terminZaplaty=cd['termin_zaplaty'], bank=cd['bank'],
                            nrKonta=cd['nr_konta'], uwagi=cd['uwagi'])
        f.save()
        return HttpResponseRedirect(reverse('StartPage'))

    def get_context_data(self, **kwargs):
        context = super(KsiegowanieFakturZakupuView, self).get_context_data()
        context['form'] = self.get_form(self.form_class)
        return context

class EwidencjaVATView(FormView):
    template_name = "ewidencjaVAT_form.html"
    form_class = EwidencjaVATForm
    success_url = "/"



class SzczegolyFakturyZakupu(DetailView):
    model = FakturaVATZakupu
    context_object_name = "f"
    template_name = "szczegoly_faktury.html"

    def get_context_data(self, **kwargs):
        context = super(SzczegolyFakturyZakupu, self).get_context_data(**kwargs)
        f = FakturaVATZakupu.objects.get(id=self.kwargs['pk'])
        context['kwota'] = f.kwota
        context['VAT'] = f.VAT
        context['rodzaj'] = 0
        return context


class SzczegolyFakturySprzedazy(DetailView):
    model = FakturaVATSprzedazy
    context_object_name = "f"
    template_name = "szczegoly_faktury.html"

    def get_context_data(self, **kwargs):
        context = super(SzczegolyFakturySprzedazy, self).get_context_data(**kwargs)
        f = FakturaVATSprzedazy.objects.get(id=self.kwargs['pk'])
        context['pozycje'] = PozycjaFakturySprzedazy.objects.filter(fakturaVAT=f)
        context['rodzaj'] = 1
        return context


class KsiegaPRView(TemplateView):
    sprzedaz = FakturaVATSprzedazy.objects.all()
    template_name = "ksiegaPR.html"

    def get_context_data(self, **kwargs):
        context = super(KsiegaPRView, self).get_context_data(**kwargs)
        # f = FakturaVATSprzedazy.objects.get(id=self.kwargs['pk'])
        context['sprzedaz'] = FakturaVATSprzedazy.objects.all()
        context['zakup'] = FakturaVATZakupu.objects.all()
        suma = 0
        for faktura in context['sprzedaz'] :
            suma += faktura.wartosc()
        for faktura in context['zakup'] :
            suma -= faktura.wartosc()
        context['suma'] = suma
        return context


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            user.save()
            if form.cleaned_data['log_on']:
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
                login(request,user)
                template = get_template("start_page.html")
                variables = RequestContext(request,{'user':user})
                output = template.render(variables)
                return HttpResponseRedirect("/")
            else:
                template = get_template("registration/register_success.html")
                variables = RequestContext(request,{'username':form.cleaned_data['username']})
                output = template.render(variables)
                return HttpResponse(output)
    else:
        print ("nie")
        form = RegisterForm()
    template = get_template("registration/register.html")
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)


def logout_page(request):
    print ("logout")
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class EDeklaracjeView(TemplateView):
    template_name = "edeklaracje.html"