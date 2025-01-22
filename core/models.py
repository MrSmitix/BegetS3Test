from django.db import models


class Picture(models.Model):
    file = models.ImageField()


class Document(models.Model):
    file = models.FileField()
