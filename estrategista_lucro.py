import json
import os

def carregar_dados_clickbank():
    try:
        with open('swarm_database.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        return []

def carregar_keywords():
    try:
        if os.path.exists('seo_full_report.txt'):
            with open('seo_full_report.txt', 'r', encoding='utf-8') as f:
                return f.readlines()
        return []
    except:
        return []

def gerar_plano_de_guerra():
    print("\n⚔️ AGENTE ESTRATEGISTA-MOR ATIVADO")
    print("📊 Analisando estrutura aninhada de 250 agentes...")

    dados_brutos = carregar_dados_clickbank()
    keywords = carregar_keywords()

    print(f"\n🚀 ESTRATÉGIA FINAL (Branch: aios-sergio):")
    print("-" * 60)

    for item in dados_brutos:
        # Mergulhando na estrutura que você enviou: item -> analise -> produto/preco
        analise = item.get('analise', {})
        nome_prod = analise.get('produto', 'Desconhecido')
        p_raw = str(analise.get('preco', '0'))

        # Se o preço for "None" ou "0", ignoramos para não sujar o relatório
        if p_raw == "None" or p_raw == "0":
            print(f"⚠️ Produto {nome_prod} ignorado: Sem preço detectado.")
            continue

        try:
            # Limpeza para casos como $3.275 (transforma em 3275.0 ou 3.27)
            # Aqui vamos apenas remover o $ e converter
            p_limpo = p_raw.replace('$', '').replace(',', '').strip()
            preco_venda = float(p_limpo)
        except:
            preco_venda = 0.0

        if preco_venda > 0:
            comissao = preco_venda * 0.75
            print(f"📦 PRODUTO: {nome_prod.upper()}")
            print(f"💰 Valor Detectado: ${preco_venda:.2f} | Comissão Est.: ${comissao:.2f}")
            
            print(f"🎯 ÂNGULOS DE SEO (SWARM):")
            if keywords:
                # Pega 3 palavras aleatórias do seu enxame de 250
                import random
                amostra = random.sample(keywords, min(3, len(keywords)))
                for kw in amostra:
                    texto = kw.split("extraiu:")[-1].strip() if "extraiu:" in kw else kw.strip()
                    print(f"   ✅ {texto[:70]}...")
            print("-" * 60)

if __name__ == "__main__":
    gerar_plano_de_guerra()