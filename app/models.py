from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    technologies = models.TextField(max_length=300)
    img_1 = models.ImageField(upload_to="images\project")
    img_2 = models.ImageField(upload_to="images\project")
    purl = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class Contactme(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    company = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500)
    def register(self):
        self.save()
    def __str__(self):
        return self.name
