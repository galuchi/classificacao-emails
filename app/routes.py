from flask import Flask, Blueprint, request, render_template, jsonify
from app.classifier import classify_email
import os
import PyPDF2

main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf'}  # Tipos de arquivo suportados

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file):
    """
    Extrai texto de um arquivo .txt ou .pdf.
    """
    filename = file.filename
    if filename.endswith('.txt'):
        return file.read().decode('utf-8')  # Lê conteúdo de arquivos .txt
    elif filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        return text
    else:
        raise ValueError("Formato de arquivo não suportado")





@main.route('/')
def home():
    return render_template('index.html')


@main.route('/classify', methods=['POST'])
def classify():
    # Priorizar o texto enviado diretamente
    if 'email_text' in request.form and request.form['email_text'].strip():
        email_text = request.form['email_text']
        category = classify_email(email_text)
        response = (
            "Obrigado por entrar em contato. Nossa equipe esta analisando sua solicitacao."
            if category == "Produtivo"
            else "Agradecemos a mensagem! Caso precise de ajuda, nos avise."
    )

        # Retorna os resultados em JSON (pode ser adaptado para exibição no HTML)
        return jsonify({
            'category': category,
            'response': response
        })

    # Verificar se há um arquivo enviado
    if 'file' in request.files:
        file = request.files['file']
        if file and is_allowed_file(file.filename):
            try:
                text = extract_text_from_file(file)  # Extrai texto do arquivo
                category = classify_email(text)  # Classifica o texto
                response = (
                    "Obrigado por entrar em contato. Nossa equipe esta analisando sua solicitacao."
                    if category == "Produtivo"
                    else "Agradecemos a mensagem! Caso precise de ajuda, nos avise."
                )

                 # Retorna os resultados em JSON (pode ser adaptado para exibição no HTML)
                return jsonify({
                    'category': category,
                    'response': response
                })

            except Exception as e:
                return jsonify({'error': f'Erro ao processar o arquivo: {str(e)}'}), 400
        else:
            return jsonify({'error': 'Arquivo nao suportado ou invalido.'}), 400

    # Caso nenhuma das condições seja atendida
    return jsonify({'error': 'Nenhum dado enviado.'}), 400
