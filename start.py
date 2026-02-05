import os
import time
from dotenv import load_dotenv
from groq import Groq

# 1. Carrega as configurações do arquivo .env
load_dotenv()

# 2. Puxa a chave de forma segura
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("❌ ERRO: Chave GROQ_API_KEY não encontrada no arquivo .env")
    exit()

# 3. Inicializa o cliente da Groq
client = Groq(api_key=GROQ_API_KEY)

def main():
    print("🚀 Iniciando Sistema Maestro - Swarm de 250 Agentes")
    print("--------------------------------------------------")
    
    try:
        # 4. Chamada com o modelo mais estável da família Llama 3
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": "Você é o Maestro do Swarm AIOS, focado em alta produtividade."},
                {"role": "user", "content": "Status do sistema? Os 250 agentes estão prontos?"}
            ],
        )
        
        print(f"🤖 RESPOSTA DO MAESTRO: {completion.choices[0].message.content}")
        print("\n✅ Conexão estabelecida com sucesso!")
        
    except Exception as e:
        print(f"⚠️ Ocorreu um erro na execução: {e}")

if __name__ == "__main__":
    main()