from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from system.forms import BilansOtwarciaForm, FakturaVATForm, PozycjaFakturyForm
from system.models import BilansOtwarcia
from django.core.urlresolvers import reverse
from django.shortcuts import render


class StartPageView(TemplateView):
    template_name = "start_page.html"

    def get_context_data(self, **kwargs):
        elements = super(StartPageView, self).get_context_data()
        print 'view'
        print elements['view']
        return elements


class BilansView(TemplateView):
    template_name = "bilans_form.html"
    form_class = BilansOtwarciaForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,  self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('StartPage'))

        return render(request, self.template_name, {'form': form})


class KsiegowanieFakturView(TemplateView):
    template_name = "faktura_form.html"
    form_class = FakturaVATForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,  self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('StartPage'))

        return render(request, self.template_name, {'form': form})


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
