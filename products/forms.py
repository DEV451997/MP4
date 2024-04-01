from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


# Form for the Product model
class ProductForm(forms.ModelForm):
    """
    Form for the Product model.
    """

    class Meta:
        model = Product
        fields = '__all__'
    # Customizing the 'image' field with a clearable file input widget
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def clean_rating(self):
        """
        Custom cleaning method for the 'rating' field.

        This method ensures that the rating falls within the range of 1 to 5.

        Returns:
            int: The cleaned rating value.

        Raises:
            forms.ValidationError:
            If the rating is outside the range of 1 to 5.
        """
        # Custom cleaning method for the 'rating' field
        rating = self.cleaned_data.get('rating')

        # Ensure the rating is within the range of 1 to 5
        if rating is not None and (rating < 1 or rating > 5):
            raise forms.ValidationError('Rating must be between 1 and 5.')

        return rating

    def clean_price(self):
        """
        Custom cleaning method for the 'price' field.

        This method ensures that the price is greater than or equal to 0.01.

        Returns:
            float: The cleaned price value.

        Raises:
            forms.ValidationError:
            If the price is less than 0.01.
        """
        price = self.cleaned_data.get('price')

        if price is not None and price <= 0.00:
            raise forms.ValidationError('Price must be at least 0.01.')

        return price
