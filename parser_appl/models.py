from django.db import models

class MybookModel(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.title


class RezkaModel(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name