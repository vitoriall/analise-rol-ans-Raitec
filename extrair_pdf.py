import pdfplumber
import pandas as pd

tabelas_encontradas = []

with pdfplumber.open("anexo1.pdf") as pdf:
    for i, pagina in enumerate(pdf.pages):
        tabela = pagina.extract_table()
        if tabela:
            df = pd.DataFrame(tabela[1:], columns=tabela[0])
            tabelas_encontradas.append(df)

# Junta tudo que foi extraído
if tabelas_encontradas:
    df_final = pd.concat(tabelas_encontradas, ignore_index=True)
    df_final.to_csv("rol_extraido.csv", index=False)
    print("Tabela salva em 'rol_extraido.csv'")
else:
    print("Nenhuma tabela foi encontrada no PDF.")
