from flask import Flask

def create_app():
    """
    Cria e configura a aplicação Flask.

    Returns:
        app (Flask): Instância do aplicativo Flask configurado.
    """
    app = Flask(__name__)  # Inicializa a aplicação Flask

    # Importa e registra as rotas do aplicativo
    from .routes import main
    app.register_blueprint(main)

    return app  # Retorna a instância configurada do Flask
