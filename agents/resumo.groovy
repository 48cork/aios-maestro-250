import json
import os

db_path = 'swarm_database.json'

if os.path.exists(db_path):
    with open(db_path, 'r', encoding='utf-8') as f:
        try:
            dados = json.load(f)
            print(f"\n📊 RELATÓRIO DO SWARM ({len(dados)} registros)\n" + "="*40)
            for i in dados:
                url = i.get("url", "N/A")
                analise = i.get("analise", {})
                print(f"🔗 URL: {url}")
                print(f"📦 PRODUTO: {analise.get('produto', 'N/A')}")
                print(f"💰 PREÇO: {analise.get('preco', 'N/A')}")
                print(f"💡 PROMESSA: {analise.get('promessa', 'N/A')[:100]}...")
                print("-" * 40)
        except Exception as e:
            print(f"❌ Erro ao ler banco: {e}")
else:
    print("⚠️ O arquivo swarm_database.json ainda não existe.")