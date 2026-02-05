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
    print("      SISTEMA DE ENXAME DE 250 AGENTES")
    print("="*50)

    # Entrada do Usuário
    produto = input("\n📦 Qual o nome do produto/nicho do Clickbank? ")
    link = input("🔗 Cole o seu link de afiliado (opcional): ")
    
    print(f"\n🧠 Maestro processando estratégia para: {produto}...")
    
    # Definição dos Departamentos do Enxame
    batalhoes = {
        "Dores e Desejos": "Agentes 001-050",
        "Ângulos de Venda": "Agentes 051-100",
        "Copy para Anúncios": "Agentes 101-150",
        "Quebra de Objeções": "Agentes 151-200",
        "Prompts de Imagens": "Agentes 201-250"
    }

    data_slug = datetime.now().strftime("%Y%m%d_%H%M")
    nome_arquivo = f"campanha_{produto.replace(' ', '_').lower()}_{data_slug}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"--- RELATÓRIO DE CAMPANHA MAESTRO V2 ---\n")
        f.write(f"PRODUTO: {produto}\nLINK: {link}\nDATA: {datetime.now()}\n")
        f.write("="*50 + "\n\n")

        for depto, agentes in batalhoes.items():
            print(f"📡 Ativando {agentes} - Especialidade: {depto}...")
            
            prompt = f"""
            Você é um exército de 50 agentes de IA (Grupo {agentes}).
            Seu objetivo é criar 3 ativos de alta conversão para o produto: {produto}.
            Especialidade do grupo: {depto}.
            Link de referência: {link}
            Entregue textos prontos para uso e persuasivos.
            """

            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Você é o Maestro Swarm. Fale em Português do Brasil."},
                        {"role": "user", "content": prompt}
                    ],
                )
                
                resposta = completion.choices[0].message.content
                f.write(f"### {agentes} - {depto} ###\n")
                f.write(resposta + "\n")
                f.write("-" * 50 + "\n\n")
                
            except Exception as e:
                print(f"❌ Erro no {agentes}: {e}")

    print(f"\n✅ SUCESSO! Campanha gerada em: {nome_arquivo}")

if __name__ == "__main__":
    iniciar_maestro()