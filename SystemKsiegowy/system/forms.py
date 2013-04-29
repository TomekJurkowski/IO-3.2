from django.forms import ModelForm
from system.models import BilansOtwarcia, FakturaVAT


class BilansOtwarciaForm(ModelForm):
    class Meta:
        model = BilansOtwarcia

class FakturaVATForm(ModelForm):
    class Meta:
        model = FakturaVAT

