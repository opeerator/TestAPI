from django.db import models

# Create your models here.

class Name(models.Model):
    """This class represents the loglist model."""
    name = models.TextField(null=True, default="Not defined in message")

    def __str__(self):
        self.name;