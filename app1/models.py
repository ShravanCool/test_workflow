from django.db import models

# Create your models here.

class Model1(models.Model):
    title = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.title
