from django.db import models

# Create your models here.


class Ticket(models.Model):
    class Status(models.TextChoices):
        NEW = "new"
        OLD = "old"

    status = models.CharField(choices=Status.choices, max_length=10)
    price = models.IntegerField()
    name = models.CharField(max_length=100, null=True, blank=True)
