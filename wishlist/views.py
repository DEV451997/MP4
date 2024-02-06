from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import WishlistItem
from products.models import Product

@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist/wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
        if created:
            messages.success(request, f"{product.name} added to your wishlist.")
        else:
            messages.warning(request, f"{product.name} is already in your wishlist.")
    return redirect('product_detail', product_id=product_id)

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, pk=wishlist_item_id, user=request.user)
    product_name = wishlist_item.product.name
    wishlist_item.delete()
    messages.success(request, f"{product_name} removed from your wishlist.")
    return redirect('wishlist')
