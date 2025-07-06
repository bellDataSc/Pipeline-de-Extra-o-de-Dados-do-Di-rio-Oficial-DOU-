from bs4 import BeautifulSoup
import os

def extrair_texto(nome_arquivo):
    caminho = os.path.join("data/diarios_html", nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")

    textos = []
    for div in soup.find_all("div", class_="texto-dou"):
        textos.append(div.get_text(strip=True))

    return textos
