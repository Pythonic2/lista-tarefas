# lista-tarefas

# Para rodar com Docker:
    # 1 -  docker-compose build
    # 2 -  docker-compose up

# Rodar sem docker:
    - No modulo controllers há um main.py, execute-o, lembre-se da env de host do postgres

# Urls:
    # 1 - '/' Url de login
    # 2 - '/register' Url para cadastrar novo usuario
    # 1 - '/logout' Url para deslogar

# Envs:
    POSTGRES_DB
    POSTGRES_USER
    POSTGRES_PASSWORD
    SECRET_KEY
    HOST - se rodar no docker, tente 'db', para local, localhost

