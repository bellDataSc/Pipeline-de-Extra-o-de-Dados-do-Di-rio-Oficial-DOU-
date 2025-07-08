Extract and save to CSV:

from scraper.extract_text import extrair_texto
from scraper.save_to_csv import salvar_csv

textos = extrair_texto('dou_2025-07-01.html')
salvar_csv(textos, '2025-07-01')
