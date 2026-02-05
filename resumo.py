import json
import os

def gerar_dashboard():
    db_file = 'swarm_database.json'
    if not os.path.exists(db_file): return

    with open(db_file, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    html_content = """
    <html><body style='font-family: sans-serif; background: #f4f7f6; padding: 20px;'>
    <h1 style='color: #2c3e50;'>🚀 AIOS-SERGIO: Market Intelligence</h1>
    <table border='1' style='border-collapse: collapse; width: 100%; background: white;'>
        <tr style='background: #2c3e50; color: white;'>
            <th style='padding: 10px;'>Produto</th><th style='padding: 10px;'>Preço</th>
            <th style='padding: 10px;'>Potencial</th><th style='padding: 10px;'>Link</th>
        </tr>
    """

    for item in dados:
        analise = item.get('analise', {})
        html_content += f"""
        <tr>
            <td style='padding: 10px;'>{analise.get('produto', 'N/A')}</td>
            <td style='padding: 10px;'>{analise.get('preco', 'N/A')}</td>
            <td style='padding: 10px;'>⭐⭐⭐⭐⭐</td>
            <td style='padding: 10px;'><a href='{item.get('url')}'>Ver Site</a></td>
        </tr>
        """
    
    html_content += "</table></body></html>"
    
    with open("dashboard_resultado.html", "w", encoding='utf-8') as f:
        f.write(html_content)
    
    print("\n✅ DASHBOARD HTML GERADO: abra 'dashboard_resultado.html' no seu navegador!")

if __name__ == "__main__":
    gerar_dashboard()