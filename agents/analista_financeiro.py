import os
import json
from groq import Groq

def processar_dados(url, dados_brutos):
    """
    Analisa os dados minerados pelo Worker e extrai inteligência de preços e funil.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("❌ Erro: GROQ_API_KEY não encontrada no ambiente.")
        return

    client = Groq(api_key=api_key)

    # Prompt especializado em detectar estruturas de ofertas de afiliados (ClickBank Style)
    prompt = f"""
    Você é um Especialista em Inteligência de Mercado e Arbitragem de Afiliados.
    Sua tarefa é minerar informações financeiras em um bloco de texto bruto de uma página de vendas.

    DADOS BRUTOS:
    {dados_brutos[:10000]}  # Limite para otimização de contexto

    TAREFAS DE EXTRAÇÃO:
    1. Identifique o NOME REAL do produto.
    2. Encontre o PREÇO INDIVIDUAL (Front-end).
    3. Identifique pacotes (ex: Kit 3 unidades, Kit 6 unidades) e seus respectivos valores totais.
    4. Detecte termos de UPSELL ou Order Bump (ofertas extras no checkout).
    5. Atribua um SCORE de 1 a 5 para o potencial de conversão baseado no preço (Preços mais baixos = Score maior).

    REGRAS:
    - Se o preço não for encontrado, use "None".
    - Responda EXCLUSIVAMENTE em formato JSON puro.

    FORMATO DA RESPOSTA:
    {{
        "produto": "nome do produto",
        "preco": "$0.00",
        "pacotes": ["lista de preços dos kits"],
        "upsells_detectados": ["lista de ofertas extras"],
        "score_conversao": 5,
        "moeda": "USD"
    }}
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Você é um extrator de dados financeiros de alta precisão."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,  # Baixa temperatura para manter a precisão dos dados
            response_format={"type": "json_object"}
        )

        # Processamento da resposta
        analise_json = json.loads(completion.choices[0].message.content)
        
        # Estrutura para salvar no banco de dados local
        resultado = {
            "url": url,
            "analise": analise_json,
            "timestamp": os.path.getmtime('worker.py') # Apenas para referência temporal
        }

        salvar_no_banco(resultado)
        return analise_json

    except Exception as e:
        print(f"❌ Erro na análise da IA para {url}: {e}")
        return None

def salvar_no_banco(dados):
    """
    Armazena o resultado no swarm_database.json para consulta posterior.
    """
    db_file = 'swarm_database.json'
    lista_dados = []

    if os.path.exists(db_file):
        with open(db_file, 'r', encoding='utf-8') as f:
            try:
                lista_dados = json.load(f)
            except:
                lista_dados = []

    lista_dados.append(dados)

    with open(db_file, 'w', encoding='utf-8') as f:
        json.dump(lista_dados, f, indent=4, ensure_ascii=False)