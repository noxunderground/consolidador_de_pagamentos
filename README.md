# 🧾 Consolidador de Pagamentos do MS (.xlsx)

Este script em Python permite consolidar valores pagos pelo Ministério da Saúde com base em uma planilha Excel, agrupando os dados por competência (mês/ano).

---

## ⚙️ Funcionalidades

- Lê uma planilha Excel com cabeçalho na 2ª linha.
- Converte a coluna de datas.
- Agrupa e soma os valores por competência mensal.
- Exporta os dados consolidados para um novo arquivo `consolidado.xlsx`.

---

## 📥 Entrada esperada

O script solicita que o usuário forneça o caminho de um arquivo `.xlsx` que possua, ao menos, as colunas:

- `DATAS`: com datas válidas
- `Valor Pago pelo MS`: com os valores a serem consolidados

---

## 📤 Saída

Gera um arquivo chamado `consolidado.xlsx` no mesmo diretório do script, contendo:

| Competência mês/ano | Valor         |
|---------------------|---------------|
| 01/2024             | 15000.00      |
| 02/2024             | 18000.00      |

---

## ▶️ Como executar

1. Certifique-se de ter o Python 3.x instalado.
2. Instale as dependências com:

```bash
pip install pandas openpyxl
