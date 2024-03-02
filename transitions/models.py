from django.db import models
from ckeditor.fields import RichTextField

class Hakkimda(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

class Haber(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

class SonBagislar(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

class SSS(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()

class Iletisim(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = RichTextField()
class Uyelik(models.Model):
    name=models.CharField(max_length=100)
    content = RichTextField()