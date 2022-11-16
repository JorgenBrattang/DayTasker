from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
