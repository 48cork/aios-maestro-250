import asyncio
import os
from groq import Groq
import time

# Limite para não estourar a API gratuita da Groq (ajuste conforme seu plano)
# Para 250 agentes, vamos processar de 5 em 5 para manter a estabilidade
MAX_CONCURRENT_TASKS = 5 
semaforo = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

async def agente_seo_brain(id_agente, nicho):
    async with semaforo:
        try:
            # Cada agente foca em um ângulo diferente
            prompt = f"Como especialista em SEO para o nicho {nicho}, sugira UMA palavra-chave de fundo de funil e uma estimativa de CPC. Seja curto."
            
            # Chamada assíncrona para a IA (executada dentro do loop)
            # Nota: Usamos run_in_executor para não travar o loop com a biblioteca Groq que é síncrona
            loop = asyncio.get_event_loop()
            completion = await loop.run_in_executor(None, lambda: client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=50
            ))
            
            resposta = completion.choices[0].message.content.strip()
            print(f"🧠 Agente #{id_agente} extraiu: {resposta[:50]}...")
            return f"Agente_{id_agente}: {resposta}"
        except Exception as e:
            return f"Agente_{id_agente}: Erro -> {e}"

async def main():
    nicho_alvo = "Saúde Prostática (Suplementos)"
    print(f"\n🔥 ATIVANDO ENXAME CEREBRAL: 250 Agentes analisando {nicho_alvo}")
    inicio = time.time()

    tarefas = [agente_seo_brain(i, nicho_alvo) for i in range(250)]
    resultados = await asyncio.gather(*tarefas)

    fim = time.time()
    print(f"\n✅ ENXAME FINALIZOU A ANÁLISE!")
    print(f"⏱️ Tempo total: {fim - inicio:.2f}s para 250 análises de IA.")
    
    # Salva o resultado para você ver a "fábrica" de ideias
    with open("seo_full_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(resultados))

if __name__ == "__main__":
    asyncio.run(main())