from django.db import models
from django.contrib.auth.models import User
from country.models import Country, State, City


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)
# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", related_name="user_address", null=False, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = models.ForeignKey(Country, verbose_name="Country", related_name="user_address", null=False, on_delete=models.CASCADE)
    state = models.ForeignKey(State, verbose_name="State", related_name="user_address", null=False, on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name="City", related_name="user_address", null=False, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    longetude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "address"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
