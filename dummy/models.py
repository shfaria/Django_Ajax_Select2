from django.db import models

# Create your models here.
class Dum(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Dim(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    dum = models.ForeignKey(Dum, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        