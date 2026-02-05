import requests
import random

def fetch_content(url):
    # Lista de identidades para rotacionar e evitar bloqueios
    identidades = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
    ]

    headers = {
        "User-Agent": random.choice(identidades),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    
    try:
        session = requests.Session()
        # allow_redirects é essencial para links da Clickbank
        response = session.get(url, headers=headers, timeout=15, allow_redirects=True)
        
        if response.status_code == 200:
            return response.text
        else:
            print(f"⚠️ Erro de Status {response.status_code} para {url}")
            return None
    except Exception as e:
        print(f"❌ Erro de conexão no motor: {e}")
        return None