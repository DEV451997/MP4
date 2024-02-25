from django.contrib import admin
from .models import Product, Category


# Admin configuration for the Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


# Admin configuration for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register the models with their respective admin configurations
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
