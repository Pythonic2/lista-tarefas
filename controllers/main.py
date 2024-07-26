# app.py
from flask import Flask
from authentication.register import register_bp
from authentication.login import auth_bp
from tarefas.listar_tarefas import listar_tarefas_bp

def create_app():
    app = Flask(__name__)

    app.secret_key = 'sua_chave_secreta_aqui'

    # Registrar blueprints
    app.register_blueprint(register_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(listar_tarefas_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
