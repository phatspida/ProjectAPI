from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.name} Contact'
