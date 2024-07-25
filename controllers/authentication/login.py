from flask import Flask, render_template, request, redirect,Blueprint, session
import sys
import os

sys.dont_write_bytecode = True
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)
from appbase import *

app = Flask(__name__)
auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        usuario = Usuario.objects.filter(nome=username).first()
        if usuario and usuario.check_password(password):
            # Armazenar informações do usuário na sessão
            session['username'] = username
            return redirect('/listar-tarefas')
        else:
            return "Usuário ou senha inválidos"
    return render_template("authentication/login.html")


@auth_bp.route("/logout")
def logout():
    session.pop('username', None)
    return redirect('/')