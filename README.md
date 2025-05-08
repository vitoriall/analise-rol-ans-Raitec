# 📊 Análise do Rol de Procedimentos da ANS – Projeto Raitec

Este projeto realiza uma análise automatizada do Anexo I do Rol de Procedimentos e Eventos em Saúde publicado pela ANS, com o objetivo de gerar **insights estratégicos** que possam embasar **propostas de melhoria ao governo**.

---

## ⚙️ Etapas do Projeto

- **`web_scraping.py`**  
  Baixa automaticamente o PDF atualizado do site da ANS.

- **`extrair_pdf.py`**  
  Lê o PDF, extrai as tabelas de procedimentos e salva um CSV (`rol_extraido.csv`).

- **`analise_rol_ans.py`**  
  Gera os principais insights do projeto, com visualização gráfica.

---

## 📌 Insights Identificados

### 1. Ausência de dados financeiros (PAC)
Mais de 85% dos procedimentos analisados não possuem valor preenchido para o campo **PAC** (Preço por Ato Completo).  
Isso compromete a **transparência** e **planejamento financeiro** do setor.

📎 Gráfico: `grafico_pac_ausente.png`

---

### 2. Subgrupos mais representados
Mostra os **5 subgrupos** com maior número de procedimentos no rol.

📎 Gráfico: `grafico_subgrupos.png`

---

## 🧠 Propostas de Melhoria

- Tornar obrigatório o preenchimento do campo **PAC** em futuras atualizações.
- Publicar critérios técnicos para definição desses valores.
- Acompanhar a distribuição dos subgrupos para garantir equidade no rol.

---

## 👥 Participantes

- Maria Paula Mesquita Silva Saraiva
- João Victor Jorge Almeida Benevides
- Vitória Lima Albuquerque
- Gustavo Silveira Alcântera

Projeto desenvolvido para o **CASE RAITec 2025.1**.
