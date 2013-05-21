from django.conf.urls import patterns, include, url
from system.views import StartPageView, BilansView, KsiegowanieFakturSprzedazyView, KsiegowanieFakturZakupuView,    \
    KsiegaPRView, DodaniePozycjiFakturSprzedazyView, register_page, logout_page,    \
    SzczegolyFakturyZakupu, SzczegolyFakturySprzedazy

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', StartPageView.as_view(), name='StartPage'),
                       url(r'^bilans/$', BilansView.as_view(), name='bilans'),
                       url(r'^ksiegowanie_sprzedazy/$', KsiegowanieFakturSprzedazyView.as_view(), name='ksiegowanieFakturSprzedazy'),
                       url(r'^ksiegowanie_zakupu/$', KsiegowanieFakturZakupuView.as_view(), name='ksiegowanieFakturZakupu'),
                       url(r'^dodaj_pozycje_sprzedazy/(?P<id>\d+)/$', DodaniePozycjiFakturSprzedazyView.as_view(), name='dodaniePozycjiFakturySprzedazy'),
                       # url(r'^dodaj_pozycje_zakupu/(?P<id>\d+)/$', DodaniePozycjiFakturZakupuView.as_view(), name='dodaniePozycjiFakturyZakupu'),

                       url(r'^faktura_sprzedazy/(?P<pk>\d+)/$', SzczegolyFakturySprzedazy.as_view(), name='szczegolyFakturySprzedazy'),
                       url(r'^faktura_zakupu/(?P<pk>\d+)/$', SzczegolyFakturyZakupu.as_view(), name='szczegolyFakturyZakupu'),
                       url(r'^ksiegaPR/$', KsiegaPRView.as_view(), name='ksiegaPR'),



                       url(r'^accounts/login/$','django.contrib.auth.views.login', name='login'),
                       url(r'^accounts/logout/$', logout_page, name='logout'),
                       url(r'^accouts/register/$', register_page, name='register'),

                       url(r'^login/$','django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', logout_page, name='logout'),
                       url(r'^register/$', register_page, name='register'),

                       # url(r'^SystemKsiegowy/', include('SystemKsiegowy.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)

