from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NsXN4DzuN2kx3sFDOfQnA0l2eszQNcr2NgTxw4ohC2mfrU5PTwdZJy5eAFZMXg6SBTLUODM0K02DD3SDCMeN3YT00cXH6O5up',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
