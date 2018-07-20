from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=64, verbose_name='Nome')
  description = models.TextField(verbose_name='Descrição')
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

  class meta:
    verbose_name_plural = 'Categorias'

  def __str__(self):
    return self.name

class Task(models.Model):
  PRIORITY_CHOICES = (
    ('A', 'Alta'),
    ('M', 'Média'),
    ('B', 'Baixa')
  )

  name = models.CharField(max_length=64, verbose_name='Nome')
  description = models.TextField(verbose_name='Descrição', blank=True)
  final_date = models.DateField(verbose_name='Data final')
  priority = models.CharField(max_length=1, verbose_name='Prioridade', choices=PRIORITY_CHOICES)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

  class meta:
    verbose_name_plural = 'Tarefas'

  def __str__(self):
    return self.name