import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

# 1. Configurações Iniciais
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def iniciar_maestro():
    print("\n" + "="*50)
    print("        🚀 AIOS SERGIO - MAESTRO V2.0 🚀")
    print("      ESPECIALISTA EM PINTEREST & ORGÂNICO")
    print("="*50)

    # Entrada do Usuário
    produto = input("\n📦 Qual o nome do produto/nicho? ")
    link = input("🔗 Cole o seu link de afiliado: ")
    
    print(f"\n🧠 Maestro orquestrando estratégia de Pinterest para: {produto}...")
    
    # Batalhões reconfigurados para fugir dos banimentos do Facebook
    batalhoes = {
        "SEO e Palavras-Chave": "Agentes 001-050",
        "Títulos Magnéticos (Pins)": "Agentes 051-100",
        "Descrições Persuasivas (Rich Pins)": "Agentes 101-150",
        "Roteiros para Ideia Pins (Vídeo)": "Agentes 151-200",
        "Prompts de Imagem Lifestyle": "Agentes 201-250"
    }

    data_slug = datetime.now().strftime("%Y%m%d_%H%M")
    nome_arquivo = f"pinterest_{produto.replace(' ', '_').lower()}_{data_slug}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"--- RELATÓRIO PINTEREST MAESTRO V2 ---\n")
        f.write(f"PRODUTO: {produto}\nLINK: {link}\nDATA: {datetime.now()}\n")
        f.write("="*50 + "\n\n")

        for depto, agentes in batalhoes.items():
            print(f"📡 Ativando {agentes} - Especialidade: {depto}...")
            
            # Prompt otimizado para Pinterest (Pede prompts de imagem em Inglês)
            prompt = f"""
            Você é um exército de 50 agentes (Grupo {agentes}).
            Objetivo: Criar 3 ativos para PINTEREST para o produto: {produto}.
            Especialidade: {depto}.
            Link: {link}
            
            IMPORTANTE: 
            - Se for gerar Prompts de Imagem, escreva-os em INGLÊS para melhor qualidade.
            - Foque em conteúdo que evite termos sensíveis (não use promessas milagrosas).
            - Use linguagem de 'estilo de vida' e 'solução de problemas'.
            """

            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Você é o Maestro do Swarm Sergio Farias. Entregue conteúdo pronto para Pinterest."},
                        {"role": "user", "content": prompt}
                    ],
                )
                
                resposta = completion.choices[0].message.content
                f.write(f"### {agentes} - {depto} ###\n")
                f.write(resposta + "\n")
                f.write("-" * 50 + "\n\n")
                
            except Exception as e:
                print(f"❌ Erro no {agentes}: {e}")

    print(f"\n✅ SUCESSO! Estratégia Pinterest gerada: {nome_arquivo}")

if __name__ == "__main__":
    iniciar_maestro()