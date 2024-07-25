#!/bin/sh

# Espera pelo banco de dados estar disponível
echo "Esperando pelo banco de dados..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Banco de dados pronto."

# Executa as migrações e outros comandos
python manage.py makemigrations
python manage.py migrate

# Inicia o servidor Django
exec "$@"
