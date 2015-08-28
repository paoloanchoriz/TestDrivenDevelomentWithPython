from django.db import models

class Item(models.Model):
    test = models.TextField(default='')
