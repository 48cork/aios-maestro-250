import os
from dotenv import load_dotenv
from groq import Groq

# 1. Configurações Iniciais
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Definição dos Batalhões (Fatiamento dos 250 Agentes)
BATALHOES = {
    "001-050": "Especialistas em Curiosidade (Atração no Pinterest/TikTok)",
    "051-100": "Engenheiros de Comparação (Ted vs. Projetos Comuns)",
    "101-150": "Copywriters de Anúncios Diretos (Foco em Clique)",
    "151-200": "Especialistas em Quebra de Objeção (Iniciantes/Ferramentas)",
    "201-250": "Geradores de Prompts Visuais (Imagens de Móveis de Luxo)"
}

def executar_swarm_ted():
    print("🪓 INICIANDO OPERAÇÃO: TED'S WOODWORKING SWARM")
    print(f"{'='*50}")

    for faixa, especialidade in BATALHOES.items():
        print(f"\n🚀 Ativando Agentes {faixa}: {especialidade}...")
        
        try:
            prompt = f"""
            Você está operando como os Agentes {faixa}, parte de um enxame de 250 IAs.
            Seu objetivo é vender o produto Ted's Woodworking (Clickbank).
            Sua especialidade hoje: {especialidade}.
            Gere 3 exemplos de alta conversão focados especificamente na sua área.
            """

            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é uma célula de inteligência do Swarm AIOS Sergio."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            
            print(f"🤖 RESPOSTA DOS AGENTES {faixa}:")
            print(completion.choices[0].message.content)
            print("-" * 30)

        except Exception as e:
            print(f"⚠️ Erro no Batalhão {faixa}: {e}")

if __name__ == "__main__":
    executar_swarm_ted()