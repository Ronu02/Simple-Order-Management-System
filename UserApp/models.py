from django.db import models


class orderDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(max_length=100, null=True, blank=True)
    Amount = models.IntegerField(max_length=100, null=True, blank=True)
    Status = models.CharField(max_length=200, null=True, blank=True)
    CreatedAt = models.CharField(max_length=100, null=True, blank=True)
    UpdatedAt = models.CharField(max_length=100, null=True, blank=True)


class SignupDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Repeat_password = models.CharField(max_length=50, null=True, blank=True)