from flask import Blueprint, render_template, request, jsonify
from .classifier import classify_email

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email_content = request.form.get("email")

        if not email_content:
            return jsonify({"error": "Por favor, insira o conteúdo do email."}), 400

        # Classificar o email
        categoria = classify_email(email_content)

        # Resposta básica simulada
        resposta = "Seu email foi classificado como produtivo!" if categoria == "Produtivo" else "Seu email não requer ação imediata."

        return jsonify({
            "categoria": categoria,
            "resposta": resposta
        })

    return render_template("index.html")
