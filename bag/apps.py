# Importing the AppConfig class from the django.apps module
from django.apps import AppConfig


# Creating a configuration class for the 'bag' app
class BagConfig(AppConfig):
    """
    Configuration class for the 'bag' app.

    This class defines configuration options for the 'bag' app, such as the
    default auto field for models.

    Attributes:
        default_auto_field (str):
        The name of the default auto field for models.
        name (str): The name of the app ('bag').
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
