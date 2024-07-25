from flask import Flask, render_template, request, redirect, Blueprint
import sys
import os

sys.dont_write_bytecode = True
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)
from appbase import *

app = Flask(__name__)
register_bp = Blueprint('register', __name__)

@register_bp.route("/register", methods=["GET"])
def register():
    
    return render_template("authentication/register.html")

@register_bp.route("/save", methods=["POST"])
def save():
    if request.method == 'POST':
        username = request.form.get("username")
        password = make_password(request.form.get("password"))
        usuario = Usuario(nome=username, password=password)
        usuario.save()
        return redirect("/")
    return render_template("authentication/register.html")