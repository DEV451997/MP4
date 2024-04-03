from django import forms


class ContactForm(forms.Form):
    """
    A Django form for handling contact information.
    """
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())
