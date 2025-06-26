import pandas as pd
import os

# Loop até o usuário fornecer um caminho de arquivo válido
while True:
    caminho_arquivo = input("Digite o caminho do arquivo .xlsx (ou arraste o arquivo aqui e pressione Enter): ").strip()
    
    if not os.path.isfile(caminho_arquivo):
        print(f"❌ Arquivo não encontrado: {caminho_arquivo}\nTente novamente.\n")
        continue
    
    try:
        df = pd.read_excel(caminho_arquivo, header=1)
        break  # Sai do loop se a leitura for bem-sucedida
    except Exception as e:
        print(f"⚠️ Erro ao ler o arquivo: {e}\nTente novamente.\n")

# Garantir que a coluna 'DATAS' é datetime
df['DATAS'] = pd.to_datetime(df['DATAS'], errors='coerce')

# Criar coluna de competência
df['Competência mês/ano'] = df['DATAS'].dt.strftime('%m/%Y')

# Agrupar e somar os valores por competência
df_consolidado = (
    df.groupby('Competência mês/ano')['Valor Pago pelo MS']
    .sum()
    .reset_index(name='Valor')
)

# Criar coluna de data real para ordenação
df_consolidado['Data referência'] = pd.to_datetime(df_consolidado['Competência mês/ano'], format='%m/%Y')

# Ordenar e remover coluna auxiliar
df_consolidado = df_consolidado.sort_values('Data referência').drop('Data referência', axis=1)

# Adicionar linha de total
total = df_consolidado['Valor'].sum()
df_consolidado.loc[len(df_consolidado)] = ['Total Geral', total]

# Exibir resultado
print(df_consolidado)

# Salvar para Excel
df_consolidado.to_excel('consolidado.xlsx', index=False)
