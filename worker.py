import json
import os
import time
from DrissionPage import ChromiumPage, ChromiumOptions
from groq import Groq

# Configuração da Branch personalizada
BRANCH_NAME = "aios-sergio"

# Inicializa o cérebro (Groq/Llama)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extrair_dados_com_ia(html_sujo):
    """Usa o Llama 3.3 para identificar nome e preço no meio do código HTML"""
    try:
        prompt = f"""
        Analise o HTML abaixo e extraia APENAS o nome do produto e o preço principal.
        Responda estritamente no formato JSON: {{"produto": "nome", "preco": "valor"}}
        HTML: {html_sujo[:2000]}
        """
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1, # Temperatura baixa para ser preciso
            response_format={ "type": "json_object" }
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        print(f"⚠️ Erro na IA: {e}")
        return {"produto": "Desconhecido", "preco": "0.00"}

def minerar_oferta(url):
    print(f"\n🕵️ Agente de Mineração entrando em: {url}")
    
    # Configurações para não ser detectado
    co = ChromiumOptions().set_paths(local_port=9222)
    co.set_argument('--headless') # Roda em segundo plano para escalar
    page = ChromiumPage(co)
    
    try:
        page.get(url)
        time.sleep(5) # Espera renderização profunda
        
        # Tenta pegar o texto de áreas críticas (iFrames e Checkouts)
        corpo_texto = page.html
        
        # Chama a IA para limpar o dado
        dados = extrair_dados_com_ia(corpo_texto)
        dados['url'] = url
        
        print(f"✅ Dados Extraídos: {dados['produto']} | {dados['preco']}")
        return dados
    except Exception as e:
        print(f"❌ Falha ao acessar {url}: {e}")
        return {"produto": "Falha", "preco": "0.00", "url": url}
    finally:
        page.quit()

def salvar_no_banco(novos_dados):
    db_path = 'swarm_database.json'
    banco = []
    
    if os.path.exists(db_path):
        with open(db_path, 'r', encoding='utf-8') as f:
            try:
                banco = json.load(f)
            except:
                banco = []
    
    banco.append(novos_dados)
    
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(banco, f, indent=4, ensure_ascii=False)
    print(f"💾 Banco de Dados '{db_path}' atualizado!")

if __name__ == "__main__":
    # Teste de fogo com o alvo principal
    alvo = "https://prostadine.com/"
    resultado = minerar_oferta(alvo)
    salvar_no_banco(resultado)