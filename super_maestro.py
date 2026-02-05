import subprocess
import time
import os

# Identidade da Branch conforme sua instrução
BRANCH = "aios-sergio"

def executar_fase(arquivo, descricao):
    print(f"\n{'='*60}")
    print(f"🔥 FASE: {descricao}")
    print(f"{'='*60}")
    try:
        # Usamos o comando python para rodar cada módulo da esteira
        subprocess.run(["python", arquivo], check=True)
        return True
    except Exception as e:
        print(f"❌ Erro na fase {descricao}: {e}")
        return False

def main():
    print(f"\n🤖 INICIANDO SISTEMA INTEGRADO: super_maestro.py")
    print(f"📍 Branch Ativa: {BRANCH}")
    
    tempo_inicio = time.time()

    # Sequência lógica da Fábrica de Agentes
    fases = [
        ("worker.py", "Mineração Profunda de Ofertas"),
        ("seo_swarm_master.py", "Ativação do Enxame de 250 Agentes"),
        ("estrategista_lucro.py", "Análise de ROI e Cruzamento de Dados"),
        ("copywriter_swarm.py", "Geração de Copy Vendedora")
    ]

    for script, desc in fases:
        if not executar_fase(script, desc):
            print(f"\n⚠️ Interrompendo execução devido a erro em: {script}")
            break

    tempo_total = time.time() - tempo_inicio
    print(f"\n{'='*60}")
    print(f"✅ OPERAÇÃO FINALIZADA COM SUCESSO EM {tempo_total:.2f}s")
    print(f"🚀 Todos os dados integrados na branch {BRANCH}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()