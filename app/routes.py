import time
from flask import Blueprint, request, render_template, jsonify
from app.classifier import classify_and_generate_response
import os
import PyPDF2

main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf'}

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file):
    filename = file.filename
    if filename.endswith('.txt'):
        return file.read().decode('utf-8')
    elif filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    else:
        raise ValueError("Formato de arquivo não suportado")


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/classify', methods=['POST'])
def classify():
    # Priorizar o texto enviado diretamente
    if "email_text" in request.form and request.form["email_text"].strip():
        email_text = request.form["email_text"]
        result = classify_and_generate_response(email_text)
        return jsonify(result)

    # Verificar se há um arquivo enviado
    if "file" in request.files:
        file = request.files["file"]
        if file and is_allowed_file(file.filename):
            try:
                file.seek(0)  # Garante que a leitura começa do início do arquivo
                text = extract_text_from_file(file)  # Extrai texto do arquivo
                result = classify_and_generate_response(text)  # Classifica o texto
                return jsonify(result)
            except Exception as e:
                return jsonify({"error": f"Erro ao processar o arquivo: {str(e)}"}), 400
        else:
            return jsonify({"error": "Arquivo não suportado ou inválido."}), 400

    # Caso nenhuma das condições seja atendida
    return jsonify({"error": "Nenhum dado enviado."}), 400
