import os
import json
from groq import Groq

def quebrar_funil():
    print("\n⚔️ AGENTE FUNNEL-BREAKER ATIVADO")
    print("🎯 Mapeando ofertas escondidas e upsells...")

    api_key = os.environ.get("GROQ_API_KEY")
    client = Groq(api_key=api_key)

    # Simulação de captura de fluxos de checkout detectados pelo Worker
    dados_fluxo = """
    Página Inicial: $69 (1 unidade)
    Link detectado: /checkout-offer-2 (Preço sugerido: $177 - 3 unidades)
    Link detectado: /one-time-offer (Suplemento extra: $39)
    """

    prompt = f"""
    Com base nos dados de fluxo abaixo, desenhe a estrutura do funil de vendas.
    Identifique o Front-end e os possíveis Upsells.
    DADOS:
    {dados_fluxo}
    Responda apenas JSON:
    {{"funil": {{"front_end": "$00", "upsells": ["preço1", "preço2"]}}, "lucro_potencial_maximo": "$000"}}
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        res = json.loads(completion.choices[0].message.content)
        
        with open("funnel_report.json", "w", encoding='utf-8') as f:
            json.dump(res, f, indent=4, ensure_ascii=False)
        
        print("✅ Mapa de funil gerado com sucesso!")
    except Exception as e:
        print(f"❌ Erro no Funnel-Breaker: {e}")

if __name__ == "__main__":
    quebrar_funil()