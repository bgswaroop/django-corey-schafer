from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Network(models.Model):
    country = CountryField()
    phone_number = PhoneNumberField()
    date_joined = models.DateTimeField(default=timezone.now)
    user_id = models.OneToOneField(to=User, on_delete=models.CASCADE)  # Delete a user deletes the record

    def __str__(self):
        return str(self.user_id)
