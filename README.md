# 📊 Análise do Rol de Procedimentos da ANS – Projeto Raitec

Este projeto realiza uma análise automatizada do Anexo I do Rol de Procedimentos e Eventos em Saúde da ANS, com o objetivo de gerar insights estratégicos para embasar propostas de melhoria regulatória.

---

## ⚙️ Etapas do Projeto

1. **`web_scraping.py`**  
   Faz o download automático do PDF oficial mais recente da ANS.

2. **`extrair_pdf.py`**  
   Extrai tabelas estruturadas do PDF e salva como `rol_extraido.csv`.

3. **`analise_rol_ans.py`**  
   Realiza análise exploratória e gera gráficos com base nos dados extraídos.

---

## 🔍 Análises Realizadas

### 📊 Gráfico 1: Top 5 Subgrupos com Mais Procedimentos
- Mostra as áreas com maior número de procedimentos listados no rol.
- **Insight**: Forte concentração em subgrupos laboratoriais e técnicos pode indicar prioridade da ANS em exames diagnósticos.

📎 `grafico_subgrupos_top5.png`

---

### 🔗 Gráfico 2: Associação entre PAC e DUT
- Classifica os procedimentos conforme possuem ou não marcações de Alta Complexidade (PAC) e Diretriz de Utilização (DUT).
- **Insight**: Nem todos os procedimentos de alta complexidade exigem critérios adicionais de regulação, e vice-versa.

📎 `grafico_pac_dut_associacao.png`

---

### 🦷 Gráfico 3: Odontologia vs Outras Áreas
- Compara o número de procedimentos odontológicos com os demais.
- **Insight**: Verifica se a odontologia está proporcionalmente representada no rol atual.

📎 `grafico_odontologia_vs_outras.png`

---

## 📎 Arquivos Gerados

- `preview_tabela.csv`: 5 primeiras linhas da base extraída
- `rol_extraido.csv`: todos os dados extraídos do PDF
- `grafico_subgrupos_top5.png`
- `grafico_pac_dut_associacao.png`
- `grafico_odontologia_vs_outras.png`

---

## 👥 Participantes

- Maria Paula Mesquita Silva Saraiva
- João Victor Jorge Almeida Benevides
- Vitória Lima Albuquerque
- Gustavo Silveira Alcântera

Projeto desenvolvido para o **CASE RAITec 2025.1**.
