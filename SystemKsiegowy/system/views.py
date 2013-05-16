from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.views.generic import TemplateView

from system.forms import BilansOtwarciaForm, FakturaVATForm, PozycjaFakturyForm, RegisterForm
from system.models import BilansOtwarcia


class StartPageView(TemplateView):
    template_name = "start_page.html"

    def get_context_data(self, **kwargs):
        elements = super(StartPageView, self).get_context_data()
        print ('view')
        print (elements['view'])
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
