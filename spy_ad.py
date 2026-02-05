import os
import json
from groq import Groq

def espiar_anuncios():
    print("\n🕵️ AGENTE SPY-AD ATIVADO")
    print("📡 Analisando criativos e promessas de mercado...")

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("❌ Erro: GROQ_API_KEY não configurada.")
        return
        
    client = Groq(api_key=api_key)

    # Dados simulados de alta conversão para o relatório
    dados_anuncios = "Promessa: Perda de peso rápida com café matinal. Headline: Wake up and burn."

    prompt = f"Analise este anúncio e resuma a estratégia em JSON: {dados_anuncios}"

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        print("✅ Relatório de anúncios gerado!")
    except Exception as e:
        print(f"❌ Erro no Spy-Ad: {e}")

if __name__ == "__main__":
    espiar_anuncios()