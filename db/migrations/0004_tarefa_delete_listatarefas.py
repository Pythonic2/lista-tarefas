# Generated by Django 5.0.7 on 2024-07-24 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_usuario_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=50)),
                ('concluida', models.BooleanField(default=False)),
                ('criacao', models.DateField(auto_now_add=True)),
                ('data_conclusao', models.DateField(default='None')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='ListaTarefas',
        ),
    ]
