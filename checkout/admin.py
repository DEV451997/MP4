from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin for OrderLineItem within OrderAdmin.

    This class defines the inline
    admin configuration for the OrderLineItem model
    to be displayed within the OrderAdmin page in the Django admin interface.

    Attributes:
        model: The model associated with the inline admin (OrderLineItem).
        readonly_fields:
        The fields in the inline admin that should be read-only.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Main admin configuration for the Order model.

    This class defines the main admin configuration for the Order model in the
    Django admin interface.
    It specifies the fields to be displayed, their read-only
    status, list display settings, ordering, and inline admin configuration for
    related models.

    Attributes:
        inlines: The inline admin classes,
        associated with the main admin (OrderLineItemAdminInline).
        readonly_fields: The fields in the main admin that should be read-only.
        fields: The fields to be displayed in the main admin.
        list_display: The fields to be displayed,
        in the list view of the main admin.
        ordering: The ordering of records in the main admin.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
