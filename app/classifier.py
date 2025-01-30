from groq import Groq
import os

# Configurar a API Key da Groq
client = Groq(api_key="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")


#Classifica o texto como 'Produtivo' ou 'Improdutivo' e gera uma resposta automática.

def classify_and_generate_response(text):
   
    prompt = f"""
    Você é um assistente que classifica emails como 'Produtivo' ou 'Improdutivo' e gera uma resposta automática.
    
    Texto do email:
    {text}

    Saída esperada:
    - Categoria: (Produtivo ou Improdutivo)
    - Resposta sugerida: (Uma mensagem automática educada baseada na categoria com até 50 palavras)\n\n
    
    Retorne os valores no seguinte formato:
    Categoria: <categoria>
    Resposta: <resposta gerada>
    IMPORTANTE: Sempre forneça tanto a categoria quanto a resposta, sem exceção.
    Se for Produtivo, gere uma resposta curta e direta.
    """

    response = client.chat.completions.create(
        model="llama-3.2-3b-preview",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150
    )

    print("Resposta bruta da IA:", response.choices[0].message.content)
    output = response.choices[0].message.content.strip().split("\n")

     # Garantir que temos pelo menos duas linhas válidas
    if len(output) < 2:
        return {"category": output[0].split(":")[-1].strip(), "response": "Erro: resposta não gerada pela IA."}

    category = output[0].split(":")[-1].strip()
    generated_response = output[1].split(":")[-1].strip()

    # Remover espaços extras no início da resposta
    generated_response = generated_response.lstrip()

    # Limitar tamanho da resposta para evitar estouro de tokens
    if len(generated_response.split()) > 50:
        generated_response = " ".join(generated_response.split()[:50]) + "..."

    return {"category": category, "response": generated_response}
