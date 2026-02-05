import subprocess
import time

def executar_fase(nome, comando):
    print(f"\n--- INICIANDO FASE: {nome} ---")
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        return True
    except:
        print(f"❌ Erro na fase {nome}")
        return False

def main():
    print("🔥 ATIVANDO CICLO DE 250 AGENTES - ESTILO ALLAN")
    
    # 1. Mineração
    if executar_fase("ESPECIALISTA CLICKBANK", "python start.py"):
        time.sleep(2)
        
        # 2. SEO Swarm (Os 250 agentes)
        if executar_fase("SEO SWARM (250 AGENTES)", "python seo_swarm_master.py"):
            time.sleep(2)
            
            # 3. Estrategista
            executar_fase("ESTRATEGISTA DE LUCRO", "python estrategista_lucro.py")

if __name__ == "__main__":
    main()