from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=25)
