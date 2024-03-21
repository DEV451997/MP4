from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView
from django.contrib import messages

from .forms import ContactForm


# A view for handling the contact form submission.
class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")

# Handle the valid form submission.
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        if form.is_valid():
            messages.success(self.request, 'Successfully sent message!')

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        # Send an email notification
     #   send_mail(
     #       subject="Received contact form submission",
     #       message=full_message,
     #       from_email=settings.DEFAULT_FROM_EMAIL,
     #       recipient_list=[settings.NOTIFY_EMAIL],
     #   )
        return super(ContactView, self).form_valid(form)
