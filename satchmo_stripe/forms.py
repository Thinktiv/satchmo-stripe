import logging
from django import forms
from django.utils.translation import ugettext as _

from payment.forms import SimplePayShipForm

from satchmo_store.contact.models import Contact
from satchmo_store.shop.models import Cart
from models import StripeToken

from signals_ahoy.signals import form_presave, form_postsave

log = logging.getLogger('payment.stripe.forms')

class StripePayShipForm(SimplePayShipForm):
    stripe_token = forms.CharField(max_length=50, widget=forms.HiddenInput({"value": ""}))
    #credit_number = forms.CharField(required=False)
    display_cc = forms.CharField(max_length=4)

    def __init__(self, request, paymentmodule, *args, **kwargs):
        super(StripePayShipForm, self).__init__(request, paymentmodule, *args, **kwargs)

        self.tempCart = Cart.objects.from_request(request)
        self.the_token = None

        try:
            self.tempContact = Contact.objects.from_request(request)
        except Contact.DoesNotExist:
            self.tempContact = None
        
    def clean_stripe_token(self):
        if len(self.cleaned_data['stripe_token']) == 0:
            raise forms.ValidationError(_('Invalid Stripe Token'))
        return self.cleaned_data['stripe_token']

    def save(self, request, cart, contact, payment_module, data=None):
        form_presave.send(StripePayShipForm, form=self)
        if data is None:
            data = self.cleaned_data
        assert(data)
        super(StripePayShipForm, self).save(request, cart, contact, payment_module, data=data)

        if self.orderpayment:
            op = self.orderpayment.capture
            token = StripeToken(
                orderpayment=op,
                payment_token=data['stripe_token'],
                display_cc=data['display_cc']
            )
            token.save()
            self.the_token = token
        form_postsave.send(StripePayShipForm, form=self)
