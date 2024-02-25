from django.apps import AppConfig


# AppConfig for the 'checkout' app
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
