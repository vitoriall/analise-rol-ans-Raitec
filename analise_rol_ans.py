# ANÁLISE DO ANEXO I - ROL DE PROCEDIMENTOS DA ANS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do CSV extraído do Anexo I
df = pd.read_csv("rol_extraido.csv")
df.columns = [col.strip() for col in df.columns]  # Limpa nomes de colunas

# Salva as 5 primeiras linhas como .csv e .html para visualização externa
df.head().to_csv("preview_tabela.csv", index=False)
df.head().to_html("preview_tabela.html", index=False)

# ========== GRÁFICO 1: Top 5 Subgrupos mais representados ==========
subgrupos = df['SUBGRUPO'].value_counts().head(5)
print("\n[GRÁFICO 1] Top 5 Subgrupos com mais Procedimentos:")
print(subgrupos)

plt.figure(figsize=(8, 4))
sns.barplot(x=subgrupos.values, y=subgrupos.index, palette="crest")
plt.title("Top 5 Subgrupos com Mais Procedimentos")
plt.xlabel("Quantidade de Procedimentos")
plt.ylabel("Subgrupo")
plt.tight_layout()
plt.savefig("grafico_subgrupos_top5.png")
plt.show()

# ========== GRÁFICO 2: Associação entre PAC e DUT ==========
df['tem_PAC'] = df['PAC'].notna()
df['tem_DUT'] = df['DUT'].notna()
df['PAC_DUT'] = df['tem_PAC'].astype(str) + "/" + df['tem_DUT'].astype(str)

combinacoes = df['PAC_DUT'].value_counts()
combinacoes.index = combinacoes.index.map({
    'True/True': 'Tem PAC e DUT',
    'True/False': 'Só PAC',
    'False/True': 'Só DUT',
    'False/False': 'Nenhum'
})

plt.figure(figsize=(6, 4))
sns.barplot(x=combinacoes.values, y=combinacoes.index, palette="magma")
plt.title("Distribuição de Procedimentos com PAC e DUT")
plt.xlabel("Quantidade")
plt.ylabel("Classificação")
plt.tight_layout()
plt.savefig("grafico_pac_dut_associacao.png")
plt.show()

# ========== GRÁFICO 3: Odontologia vs Outras Áreas ==========
odonto = df['GRUPO'].str.contains("ODONTOL", case=False, na=False)
odonto_contagem = pd.Series({
    'Odontologia': odonto.sum(),
    'Outras áreas': (~odonto).sum()
})

plt.figure(figsize=(6, 4))
sns.barplot(x=odonto_contagem.values, y=odonto_contagem.index, palette="viridis")
plt.title("Distribuição de Procedimentos Odontológicos vs Outras Áreas")
plt.xlabel("Quantidade de Procedimentos")
plt.tight_layout()
plt.savefig("grafico_odontologia_vs_outras.png")
plt.show()
