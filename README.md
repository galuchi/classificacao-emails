## Contexto do Projeto

Estou criando uma **solução digital para uma grande empresa** do setor financeiro que lida com um **alto volume de emails diariamente**. Esses emails podem ser mensagens solicitando um status atual sobre uma requisição em andamento, compartilhando algum arquivo ou até mesmo mensagens improdutivas, como desejo de feliz natal ou perguntas não relevantes. 

O **objetivo é automatizar a leitura e classificação desses emails** e sugerir classificações e respostas automáticas de acordo com o teor de cada email recebido, **liberando tempo da equipe** para que não seja mais necessário ter uma pessoa fazendo esse trabalho manualmente.

## Objetivo do Projeto Simplificado

Desenvolver uma aplicação web simples que utilize inteligência artificial para:

1. **Classificar** emails em categorias predefinidas.
2. **Sugerir respostas automáticas** baseadas na classificação realizada.

**Categorias de Classificação**

- **Produtivo:** Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
- **Improdutivo:** Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).

## Comandos para a execucar a aplicação localmente

1. Em seu terminal, clone este repositório em uma pasta desejada
   ```sh
   git clone https://github.com/galuchi/classificacao-emails.git
   cd classificacao-emails
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv env
   source env/bin/activate  # No Linux 
   env\Scripts\activate     # No Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
   A instalação pode demorar um pouco, então relaxe, pegue um cafézinho...

4. Execute a aplicação:
   ```sh
   python run.py
   ```
5. Acesse a aplicação em: [http://127.0.0.1:5000]

