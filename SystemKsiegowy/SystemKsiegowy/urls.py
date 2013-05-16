from django.conf.urls import patterns, include, url
from system.views import StartPageView, BilansView, KsiegowanieFakturView, KsiegaPRView, DodaniePozycjiFakturView, register_page, logout_page

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', StartPageView.as_view(), name='StartPage'),
                       url(r'^bilans/$', BilansView.as_view(), name='bilans'),
                       url(r'^ksiegowanie/$', KsiegowanieFakturView.as_view(), name='ksiegowanieFaktur'),
                       url(r'^pozycja/$', DodaniePozycjiFakturView.as_view(), name='dodaniePozycjiFaktury'),
                       url(r'^ksiegaPR/$', KsiegaPRView.as_view(), name='ksiegaPR'),



                       url(r'^accounts/login/$','django.contrib.auth.views.login', name='login'),
                       url(r'^accounts/logout/$', logout_page, name='logout'),
                       url(r'^accouts/register/$', register_page, name='register'),

                       # url(r'^SystemKsiegowy/', include('SystemKsiegowy.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
)

