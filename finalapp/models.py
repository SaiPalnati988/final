from django.db import models

class CustomerDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile_number = models.BigIntegerField()
    serial_number = models.IntegerField()
    unique_id = models.IntegerField()
    password = models.CharField(max_length=10)
    re_enter_password = models.CharField(max_length=10)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)


# Create your models here.
