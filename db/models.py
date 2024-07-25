from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    password = models.CharField(max_length=128, default='1234')  # O tamanho é suficiente para armazenar hashes

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

class Tarefa(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    concluida = models.BooleanField(default=False)
    criacao = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.concluida and self.data_conclusao is None:
            self.data_conclusao = timezone.now().date()
        elif not self.concluida:
            self.data_conclusao = None
        super().save(*args, **kwargs)
