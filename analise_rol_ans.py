# ANÁLISE DO ANEXO I - ROL DE PROCEDIMENTOS DA ANS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do CSV extraído do Anexo I
df = pd.read_csv("rol_extraido.csv")
df.columns = [col.strip() for col in df.columns]  # Limpa nomes de colunas

# ========== INSIGHT 1: Faltam dados financeiros (PAC) ==========
faltando_pac = df['PAC'].isna().sum()
total = len(df)
print(f"[INSIGHT 1] Procedimentos sem valor PAC informado: {faltando_pac}/{total}")

# ========== INSIGHT 2: Top 5 Subgrupos mais representados ==========
subgrupos = df['SUBGRUPO'].value_counts().head(5)
print("\n[INSIGHT 2] Top 5 Subgrupos com mais Procedimentos:")
print(subgrupos)

plt.figure(figsize=(8, 4))
sns.barplot(x=subgrupos.values, y=subgrupos.index, palette="crest")
plt.title("Top 5 Subgrupos com Mais Procedimentos")
plt.xlabel("Quantidade de Procedimentos")
plt.ylabel("Subgrupo")
plt.tight_layout()
plt.savefig("grafico_subgrupos.png")
plt.show()

# ========== INSIGHT 3: Visualização da ausência de PAC ==========
pac_disponivel = df['PAC'].notna().sum()
pac_ausente = df['PAC'].isna().sum()

dados_pac = pd.Series(
    [pac_disponivel, pac_ausente],
    index=['Com PAC informado', 'Sem PAC informado']
)

plt.figure(figsize=(6, 4))
sns.barplot(x=dados_pac.values, y=dados_pac.index, palette="rocket")
plt.title("Preenchimento do Campo PAC (Preço por Ato Completo)")
plt.xlabel("Número de Procedimentos")
plt.ylabel("Situação do Campo PAC")
plt.tight_layout()
plt.savefig("grafico_pac_ausente.png")
plt.show()
