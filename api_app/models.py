from django.db import models

# Create your models here.

class Name(models.Model):
    """This class represents the loglist model."""
    name = models.TextField()

    def __str__(self):
        return self.name