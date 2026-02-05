import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

# 1. Carrega as chaves do .env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Define a estratégia de fatiamento dos 250 agentes
BATALHOES = {
    "001-050": "Especialistas em Curiosidade (Atração no Pinterest/TikTok)",
    "051-100": "Engenheiros de Comparação (Ted vs. Projetos Comuns)",
    "101-150": "Copywriters de Anúncios Diretos (Foco em Clique)",
    "151-200": "Especialistas em Quebra de Objeção (Iniciantes/Ferramentas)",
    "201-250": "Geradores de Prompts Visuais (Imagens de Móveis de Luxo)"
}

def executar_swarm_ted():
    # Define o nome do arquivo de saída
    nome_arquivo = "output_ted_woodworking.txt"
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    print(f"🪓 OPERAÇÃO INICIADA - Gravando em {nome_arquivo}")
    
    # 3. Abre/Cria o arquivo de texto para salvar a produção
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"--- RELATÓRIO DO MAESTRO - SWARM 250 AGENTES ---\n")
        f.write(f"PRODUTO: Ted's Woodworking | DATA: {data_atual}\n")
        f.write("="*50 + "\n\n")

        # 4. Loop que percorre cada batalhão
        for faixa, especialidade in BATALHOES.items():
            print(f"🚀 Ativando Batalhão {faixa}...")
            
            try:
                # O Maestro dá a ordem específica para cada grupo
                prompt = f"Gere 3 estratégias de alta conversão para o Ted's Woodworking como se você fosse 50 agentes focados em: {especialidade}."

                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Você é o Maestro do Swarm Sergio Farias. Entregue conteúdo pronto para copiar e colar."},
                        {"role": "user", "content": prompt}
                    ],
                )
                
                resposta = completion.choices[0].message.content
                
                # Escreve os resultados no arquivo TXT
                f.write(f"### BATALHÃO {faixa}: {especialidade} ###\n")
                f.write(resposta + "\n")
                f.write("-" * 50 + "\n\n")
                
            except Exception as e:
                f.write(f"⚠️ Erro no Batalhão {faixa}: {e}\n")

    print(f"\n✅ SUCESSO! O arquivo '{nome_arquivo}' foi gerado.")

if __name__ == "__main__":
    executar_swarm_ted()