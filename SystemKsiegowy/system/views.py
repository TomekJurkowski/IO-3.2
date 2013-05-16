from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.utils.encoding import smart_str
from django.views.generic import TemplateView, FormView
import time
from datetime import date

from system.forms import BilansOtwarciaForm, FakturaVATForm, PozycjaFakturyForm, RegisterForm
from system.models import BilansOtwarcia, FakturaVAT


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
    for f in FakturaVAT.objects.all():
        if (smart_str(f.nrFaktury).find(t) >= 0):
            nr += 1

    return t + '/' + str(nr)

class KsiegowanieFakturView(FormView):
    template_name = "faktura_form.html"
    form_class = FakturaVATForm

    def form_valid(self, form):
        cd = form.cleaned_data
        print(cd)
        f = FakturaVAT(nrFaktury=getFakturaNr(), dataSprzedazy=cd['data_sprzedazy'], dataWystawienia=cd['data_wystawienia'],
                       sprzedawca_nazwa=cd['sprzedawca_nazwa'], sprzedawca_adres=cd['sprzedawca_adres'], sprzedawca_miasto=cd['sprzedawca_miasto'],
                       sprzedawca_kod=cd['sprzedawca_kod'], sprzedawca_NIP=cd['sprzedawca_NIP'],
                       nabywca_nazwa=cd['nabywca_nazwa'], nabywca_adres=cd['nabywca_adres'], nabywca_miasto=cd['nabywca_miasto'],
                       nabywca_kod=cd['nabywca_kod'], nabywca_NIP=cd['nabywca_NIP'],
                       sposobZaplaty=cd['sposob_zaplaty'], terminZaplaty=cd['termin_zaplaty'], bank=cd['bank'],
                       nrKonta=cd['nr_konta'], uwagi=cd['uwagi'])
        print(f)
        f.save()
        print("FAKTURY:")
        for f in FakturaVAT.objects.all():
            print (f)
        return HttpResponseRedirect(reverse('StartPage'))

    def get_context_data(self, **kwargs):
        context = super(KsiegowanieFakturView, self).get_context_data()
        context['form'] = self.get_form(self.form_class)
        context['faktura_nr'] = getFakturaNr()
        return context


class DodaniePozycjiFakturView(TemplateView):
    template_name = "pozycja_form.html"
    form_class = PozycjaFakturyForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,  self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('StartPage'))

        return render(request, self.template_name, {'form': form})


class KsiegaPRView(TemplateView):
    template_name = "start_page.html"


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
                template = get_template("main_page.html")
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
