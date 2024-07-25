from flask import Flask, render_template, request, redirect,Blueprint,session
import sys
import os

sys.dont_write_bytecode = True
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)
from appbase import *

app = Flask(__name__)
listar_tarefas_bp = Blueprint('listar_tarefas', __name__)


@listar_tarefas_bp.route("/listar-tarefas", methods=["GET"])
def listar_tarefas():
    usuario_logado = session.get('username')
    user = Usuario.objects.get(nome=usuario_logado)
    tarefas = Tarefa.objects.filter(usuario=user).order_by('-id')
    context = {'tarefas': tarefas, 'usuario_logado': usuario_logado}
    return render_template("tarefas/listar-tarefas.html", **context)



@listar_tarefas_bp.route("/listar-htmx", methods=["GET"])
def listar_tarefas_htmx():
    usuario_logado = session.get('username')
    user = Usuario.objects.get(nome=usuario_logado)
    tarefas = Tarefa.objects.filter(usuario=user).order_by('-id')
    context = {'tarefas': tarefas, 'usuario_logado': usuario_logado}
    return render_template("tarefas/listar_htmx.html", **context)


@listar_tarefas_bp.route("/criar-tarefas", methods=["POST"])
def criar_tarefa():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    concluida_f = request.form.get("concluida")
    concluida = True if concluida_f == 'on' else False
    usuario_logado = session.get('username')
    user = Usuario.objects.get(nome=usuario_logado)
    nova_tarefa = Tarefa(usuario=user, titulo=titulo, descricao=descricao, concluida=concluida)
    nova_tarefa.save()
    tarefas = Tarefa.objects.filter(usuario=user)
    return redirect("/listar-htmx")


@listar_tarefas_bp.route("/apagar-htmx/<int:id>", methods=["POST"])
def apagar_htmx(id):
    usuario_logado = session.get('username')
    user = Usuario.objects.get(nome=usuario_logado)
    tarefa = Tarefa.objects.filter(usuario=user,id=id)
    tarefa.delete()
    tarefas = Tarefa.objects.filter(usuario=user).order_by('-id')
    context = {'tarefas': tarefas, 'usuario_logado': usuario_logado}
    return render_template("tarefas/listar_htmx.html", **context)



@listar_tarefas_bp.route("/editar-htmx/<int:id>", methods=["GET","POST"])
def editar_htmx(id):
    usuario_logado = session.get('username')
    user = Usuario.objects.get(nome=usuario_logado)
    tarefa = Tarefa.objects.get(id=id, usuario=user)

    context = {'tarefa': tarefa, 'usuario_logado': usuario_logado}
    return render_template("tarefas/editar.html", **context)


@listar_tarefas_bp.route("/atualizar-htmx/<int:id>", methods=["POST"])
def atualizar_htmx(id):
    usuario_logado = session.get('username')
    user = Usuario.objects.get(nome=usuario_logado)
    tarefa = Tarefa.objects.get(id=id, usuario=user)
    concluida_f = request.form.get("concluida")
    concluida = True if concluida_f == 'on' else False
    tarefa.titulo =  request.form.get("titulo")
    tarefa.descricao =  request.form.get("descricao")
    tarefa.concluida =  concluida
    tarefa.save()
    tarefas = Tarefa.objects.filter(usuario=user).order_by('-id')
    context = {'tarefas': tarefas, 'usuario_logado': usuario_logado}
    return render_template("tarefas/listar_htmx.html", **context)