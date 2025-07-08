import pandas as pd
import os
from datetime import date

def salvar_csv(textos, data=date.today().strftime('%Y-%m-%d')):
    df = pd.DataFrame(textos, columns=["conteudo"])
    output_path = f"data/diarios_csv/dou_{data}.csv"
    df.to_csv(output_path, index=False)
    print(f" CSV salvo em {output_path}")
