from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('clubs'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I3MyOCLGmmNHSHidP9I79taTX4uHT6Hdapmi4Qcsy6QQTkPwI0x1Sj5WvO2HmkTmwW1Xo9nsTjLcQB7DuDkyqYq00twcrrchR',
        'client_secret': 'test clent secret',
    }

    return render(request, template, context)
