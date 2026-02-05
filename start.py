import subprocess
import os
import time

def rodar_swarm_total():
    os.environ["GROQ_API_KEY"] = "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"
    venv_python = os.path.join(".venv", "Scripts", "python.exe")
    if not os.path.exists(venv_python): venv_python = "python"

    print("\n" + "█"*60)
    print("🚀 AIOS-SERGIO: SISTEMA AUTÔNOMO DE INTELIGÊNCIA DE MERCADO")
    print("█"*60)

    # 1. TREND-HUNTER
    print("\n📡 [1/4] TREND-HUNTER: Caçando novidades...")
    subprocess.run([venv_python, "trend_hunter.py"])
    
    # 2. SPY-AD
    print("\n🕵️ [2/4] SPY-AD: Espionando criativos...")
    subprocess.run([venv_python, "spy_ad.py"])
    
    # 3. WORKER (MINERAÇÃO)
    print("\n💰 [3/4] WORKER: Minerando preços na página de vendas...")
    if os.path.exists("swarm_database.json"): os.remove("swarm_database.json")
    subprocess.run([venv_python, "worker.py"])
    
    # 4. FUNNEL-BREAKER
    print("\n⚔️ [4/4] FUNNEL-BREAKER: Mapeando upsells escondidos...")
    subprocess.run([venv_python, "funnel_breaker.py"])
    
    # RELATÓRIO FINAL CONSOLIDADO
    print("\n" + "█"*60)
    print("📊 GERANDO RELATÓRIO 360 GRAUS...")
    print("█"*60)
    time.sleep(1)
    subprocess.run([venv_python, "resumo.py"])

if __name__ == "__main__":
    rodar_swarm_total()