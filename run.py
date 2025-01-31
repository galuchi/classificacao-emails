import os
from app import create_app

# Cria a instância do aplicativo Flask
app = create_app()

#Inicia o servidor Flask, definindo a porta automaticamente com base na variável de ambiente.
if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  # Executa o app Flask na porta definida
