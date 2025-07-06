import requests
from bs4 import BeautifulSoup
from datetime import date

def baixar_html_data(data=date.today().strftime('%Y-%m-%d')):
    url = f"https://www.in.gov.br/leiturajornal?data={data}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"data/diarios_html/dou_{data}.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ Página {data} salva.")
    else:
        print(f"❌ Erro ao baixar página: {response.status_code}")
