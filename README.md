# 🚀 AIOS-SERGIO: Esteira de Produção Massiva com 250 Agentes

Este projeto implementa uma infraestrutura completa de **Inteligência Artificial Swarm (Enxame)** para mineração, análise e copywriting de ofertas do ClickBank. O sistema é capaz de processar 250 análises simultâneas em menos de 190 segundos.

## 🧠 Arquitetura do Sistema (A Fábrica de ROI)

O ecossistema está dividido em módulos especializados que se comunicam através de um banco de dados JSON centralizado:

1.  **`worker.py` (O Minerador):** Utiliza *DrissionPage* e *Llama 3.3* para furar iFrames de checkouts e extrair preços e nomes reais de produtos.
2.  **`seo_swarm_master.py` (O Enxame):** Orquestra **250 Agentes de SEO** simultâneos que mineram palavras-chave de fundo de funil e estimam CPC.
3.  **`estrategista_lucro.py` (O General):** Realiza o cruzamento de dados, calcula comissões (padrão 75%) e define os melhores ângulos de ataque.
4.  **`copywriter_swarm.py` (O Vendedor):** Gera scripts de anúncios e copies de alta conversão baseados nos dados reais extraídos.

## 🛠️ Como Operar o Sistema

Para rodar a esteira completa com um único comando, utilize o script maestro:

```powershell
python super_maestro.py