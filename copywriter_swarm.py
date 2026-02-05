import json
import os
from groq import Groq

# Mantendo a identidade da branch
BRANCH_NAME = "aios-sergio"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def carregar_melhor_oportunidade():
    try:
        with open('swarm_database.json', 'r', encoding='utf-8') as f:
            produtos = json.load(f)
            # Pegamos o primeiro da lista como exemplo (ex: Prostadine)
            return produtos[0]
    except:
        return None

def gerar_copy_vendedora(produto, preco):
    print(f"\n✍️ AGENTE COPYWRITER GERANDO ANÚNCIO PARA: {produto}")
    
    prompt = f"""
    Você é um copywriter especialista em Direct Response e Google Ads.
    Produto: {produto}
    Preço: {preco}
    Tarefa: Escreva um anúncio de alta conversão.
    - 3 Títulos (máx 30 caracteres cada)
    - 2 Descrições (máx 90 caracteres cada)
    - 1 Gatilho mental de urgência.
    Responda em Português do Brasil.
    """
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar copy: {e}"

def main():
    print(f"\n🚀 ATIVANDO CICLO DE COPYWRITING - {BRANCH_NAME}")
    
    dados = carregar_melhor_oportunidade()
    if not dados:
        print("❌ Nenhum produto encontrado no banco de dados.")
        return

    # Extraindo nome e preço (tratando a estrutura aninhada se necessário)
    nome = dados.get('analise', {}).get('produto') or dados.get('produto')
    preco = dados.get('analise', {}).get('preco') or dados.get('preco')

    copy = gerar_copy_vendedora(nome, preco)
    
    print("\n" + "="*50)
    print(f"📄 RELATÓRIO DE ANÚNCIO FINAL")
    print("="*50)
    print(copy)
    print("="*50)

    # Salva o anúncio final
    with open('anuncio_final.txt', 'w', encoding='utf-8') as f:
        f.write(copy)
    print("\n✅ Anúncio salvo em 'anuncio_final.txt'!")

if __name__ == "__main__":
    main()