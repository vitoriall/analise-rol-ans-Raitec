import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do CSV e padronização das colunas
df = pd.read_csv("rol_extraido.csv")
df.columns = [col.strip().upper() for col in df.columns]

# Filtro para o grupo "CABEÇA E PESCOÇO"
grupo = "CABEÇA E PESCOÇO"
df_cabeca = df[df['GRUPO'] == grupo]

# Contagens de coberturas
dados_cobertura = {
    'OD (Odontológica)': df_cabeca['OD'].notna().sum(),
    'AMB (Ambulatorial)': df_cabeca['AMB'].notna().sum(),
    'HCO (Hospitalar c/ Cirurgia)': df_cabeca['HCO'].notna().sum(),
    'HSO (Hospitalar s/ Obstetrícia)': df_cabeca['HSO'].notna().sum(),
    'REF (Plano Referência)': df_cabeca['REF'].notna().sum()
}

# Cálculo de procedimentos que têm apenas cobertura OD
apenas_od = df_cabeca[
    df_cabeca['OD'].notna() &
    df_cabeca['AMB'].isna() &
    df_cabeca['HCO'].isna() &
    df_cabeca['HSO'].isna() &
    df_cabeca['REF'].isna()
].shape[0]

# Adiciona "Apenas OD" ao dicionário
dados_cobertura['Apenas OD'] = apenas_od

# Plot - gráfico de cobertura de procedimentos
plt.figure(figsize=(10, 6))
plt.bar(dados_cobertura.keys(), dados_cobertura.values(), color='steelblue')
plt.title("Cobertura de Procedimentos - Grupo 'CABEÇA E PESCOÇO'")
plt.ylabel("Quantidade de Procedimentos")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("grafico_cobertura_cabeca_pescoco.png")
plt.close()
