from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    organizer = models.CharField(max_length=100, null=True)
    money = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='BRL')
    parcial = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='BRL')
    place = models.CharField(max_length=100, null=True)
    invitations = models.IntegerField()
    date = models.DateField(null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    description = models.CharField(max_length=250, null=True)

    tag = models.ForeignKey(Tag, null=False, on_delete=models.CASCADE, related_name="tags", related_query_name="tag")

    def __str__(self):
        return self.name

class Payers(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Activities(models.Model):
    name = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
