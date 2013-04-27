from django.views.generic import TemplateView


class StartPageView(TemplateView):
    template_name = "start_page.html"

    def get_context_data(self, **kwargs):
        elements = super(StartPageView, self).get_context_data()
        print 'view'
        print elements['view']
        return elements


class BilansView(TemplateView):
    template_name = "start_page.html"


class KsiegowanieFakturView(TemplateView):
    template_name = "start_page.html"


class KsiegaPRView(TemplateView):
    template_name = "start_page.html"