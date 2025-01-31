from groq import Groq
import os

# Configurar a API Key da Groq
client = Groq(api_key="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")



# Função para classificar um email como 'Produtivo' ou 'Improdutivo' e gerar uma resposta automática.
def classify_and_generate_response(text):
   
    #Prompt fornecido para a API IA
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

    #Chama a API para fornecer a resposta
    response = client.chat.completions.create(
        model="llama-3.2-3b-preview", #Modelo da IA
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150
    )

    # Exibe a resposta bruta da IA no console para depuração.
    print("Resposta bruta da IA:", response.choices[0].message.content)

    # Divide a resposta da IA em linhas para facilitar a extração dos dados.
    output = response.choices[0].message.content.strip().split("\n")

    # Garantir que temos pelo menos duas linhas válidas
    if len(output) < 2:
        return {"category": output[0].split(":")[-1].strip(), "response": "Erro: resposta não gerada pela IA."}

    # Extração da categoria e resposta a partir do texto formatado.
    category = output[0].split(":")[-1].strip()
    generated_response = output[1].split(":")[-1].strip()

    # Remover espaços extras no início da resposta
    generated_response = generated_response.lstrip()

    # Limitar tamanho da resposta para evitar estouro de tokens
    if len(generated_response.split()) > 50:
        generated_response = " ".join(generated_response.split()[:50]) + "..."

    return {"category": category, "response": generated_response}
