from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=64, verbose_name='Nome')
  description = models.TextField(verbose_name='Descrição')
