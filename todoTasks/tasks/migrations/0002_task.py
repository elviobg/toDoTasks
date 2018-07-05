# Generated by Django 2.0.6 on 2018-07-05 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('final_date', models.DateField(verbose_name='Data final')),
                ('priority', models.CharField(choices=[('A', 'Alta'), ('M', 'Média'), ('B', 'Baixa')], max_length=1, verbose_name='Prioridade')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Category', verbose_name='Categoria')),
            ],
        ),
    ]