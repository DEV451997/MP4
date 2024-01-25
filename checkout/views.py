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
        'stripe_public_key': 'pk_test_51OcTbAA6y8PzZ2kYcvGJHqinyjc9Lyxr2fd1yPU3Fr4zeERuDVQHjUw4YV2M0hbOerHI9WV4qlxM8w0Aus11l6bV00HQmf17MV',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)