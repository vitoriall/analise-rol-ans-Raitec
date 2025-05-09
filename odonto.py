import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do CSV e padronização das colunas
df = pd.read_csv("~/Downloads/rol_extraido.csv")
df.columns = [col.strip().upper() for col in df.columns]

# Filtro para o grupo "CABEÇA E PESCOÇO"
grupo = "CABEÇA E PESCOÇO"
df_cabeca = df[df['GRUPO'] == grupo]

# Contagens
dados_cobertura = {
    'OD (Odontológica)': df_cabeca['OD'].notna().sum(),
    'AMB (Ambulatorial)': df_cabeca['AMB'].notna().sum(),
    'HCO (Hospitalar c/ Cirurgia)': df_cabeca['HCO'].notna().sum(),
    'HSO (Hospitalar s/ Obstetrícia)': df_cabeca['HSO'].notna().sum(),
    'REF (Plano Referência)': df_cabeca['REF'].notna().sum()
}

# Cálculo de apenas OD
apenas_od = df_cabeca[
    df_cabeca['OD'].notna() &
    df_cabeca['AMB'].isna() &
    df_cabeca['HCO'].isna() &
    df_cabeca['HSO'].isna() &
    df_cabeca['REF'].isna()
].shape[0]

# Adiciona ao dicionário
dados_cobertura['Apenas OD'] = apenas_od

# Plot - gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(dados_cobertura.keys(), dados_cobertura.values(), color='steelblue')
plt.title("Cobertura de Procedimentos - Grupo 'CABEÇA E PESCOÇO'")
plt.ylabel("Quantidade de Procedimentos")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

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
