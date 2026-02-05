import json
import os

def gerar_relatorio():
    db_file = os.path.join('..', 'swarm_database.json')
    
    print("\n" + "="*80)
    print("🚀 DASHBOARD INTELIGENTE - BRANCH: aios-sergio")
    print("="*80)

    if not os.path.exists(db_file):
        print("❌ Database não encontrada.")
        return

    with open(db_file, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    print(f"{'PRODUTO':<20} | {'PREÇO':<10} | {'PROMESSA PRINCIPAL':<40}")
    print("-" * 80)

    for item in dados:
        if "analise" in item:
            analise = item['analise']
            nome = analise.get('Nome do Produto', 'N/A')[:20]
            preco = analise.get('Preço Principal', 'N/A')[:10]
            promessa = analise.get('Principal benefício/promessa', 'N/A')[:40]
            print(f"{nome:<20} | {preco:<10} | {promessa:<40}")

    print("-" * 80)
    print(f"📈 Total de Inteligência acumulada: {len(dados)} itens")
    print("="*80 + "\n")

if __name__ == "__main__":
    gerar_relatorio()