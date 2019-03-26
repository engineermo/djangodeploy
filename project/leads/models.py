from django.db import models
from django.core.validators import RegexValidator



# Create your models here.
class Lead(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    address_line = models.CharField(max_length=150)
    address_line2 = models.CharField(blank=True, null=True, max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    zip = models.CharField(
    max_length=10,
    null=True,
    blank=True,
    help_text="Zipcode",
    validators=[RegexValidator(
        regex=r'^(^[0-9]{5}(?:-[0-9]{4})?$|^$)',
        message=(u'Must be valid zipcode in formats 12345 or 12345-1234'),
    )],
)
    message = models.CharField(blank=True, null=True, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

