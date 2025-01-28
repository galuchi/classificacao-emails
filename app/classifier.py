import re
import nltk
from nltk.corpus import stopwords

# Baixar recursos necessários do NLTK
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

# Configuração inicial
STOPWORDS = set(stopwords.words('portuguese'))  # Configurado para português
LEMMA = nltk.WordNetLemmatizer()

def preprocess_text(text):
    """
    Realiza o pré-processamento básico do texto.
    
    - Remove caracteres especiais e números.
    - Converte para minúsculas.
    - Tokeniza o texto.
    - Remove stopwords e aplica lematização.
    
    Args:
        text (str): Texto a ser pré-processado.
    
    Returns:
        str: Texto pré-processado.
    """
    if not text or not isinstance(text, str):
        raise ValueError("O texto de entrada deve ser uma string válida.")

    # Remoção de caracteres especiais e números
    text = re.sub(r"[^a-zA-Záéíóúãõç\s]", "", text)
    text = text.lower()

    # Tokenização
    tokens = nltk.word_tokenize(text)

    # Remoção de stopwords e lematização
    processed_tokens = [
        LEMMA.lemmatize(word) for word in tokens if word not in STOPWORDS
    ]

    return " ".join(processed_tokens)


def classify_email(text, default_category="Improdutivo"):
    """
    Classifica o email como 'Produtivo' ou 'Improdutivo'.
    
    Args:
        text (str): Texto do email a ser classificado.
        default_category (str): Categoria padrão caso nenhuma palavra-chave seja encontrada.
    
    Returns:
        str: Categoria do email ('Produtivo' ou 'Improdutivo').
    """
    if not text or not isinstance(text, str):
        raise ValueError("O texto de entrada deve ser uma string válida.")

    # Palavras-chave para cada categoria
    productive_keywords = ["atualização", "pedido", "urgente", "suporte", "dúvida", "atendimento"]
    unproductive_keywords = ["obrigado", "parabéns", "feliz", "natal", "páscoa"]

    # Pré-processar o texto
    text = preprocess_text(text)

    # Verifica palavras-chave
    if any(word in text for word in productive_keywords):
        return "Produtivo"
    elif any(word in text for word in unproductive_keywords):
        return "Improdutivo"
    else:
        return default_category  # Categoria padrão
