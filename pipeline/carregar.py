"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""

import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset de clientes.
    
    Args:
        caminho_arquivo: caminho para o CSV
        
    Returns:
        DataFrame com os dados
    """
    # TODO 1: Use pd.read_csv() para carregar o arquivo
    # Dica: df = pd.read_csv(caminho_arquivo)
    
    print("=" * 50)
    print("CARREGAMENTO DOS DADOS")
    print("=" * 50)
    print()
    
    
    df =   pd.read_csv(caminho_arquivo)
    print(f"  Extraídas {len(df)} linhas")
    print()
    return df


def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    
    Args:
        df: DataFrame a ser explorado
    """
    print("=" * 50)
    print("EXPLORAÇÃO DOS DADOS")
    print("=" * 50)
    print()
    
    # TODO 2: Mostre o shape do DataFrame (linhas, colunas)
    # Dica: print(f"Shape: {df.shape}")
    print(f"Linhas (Clientes): {df.shape[0]:,}")
    print(f"Colunas (Atributos): {df.shape[1]}")
    print()
    
    # TODO 3: Mostre os tipos de cada coluna
    # Dica: print(df.dtypes)
    print(f'Os Nomes e os Tipos das colunas são: \n{df.dtypes}')
    print()
    
    # TODO 4: Mostre as 5 primeiras linhas
    # Dica: print(df.head())
    print(f'Os cinco primeiros registros (clientes) são: \n{df.head()}')
    print()
    print("=" * 50)


def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
    
    Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print("-" * 30)
    print("DISTRIBUIÇÃO DO TARGET")
    print("-" * 30)
    
    # TODO 5: Mostre a contagem de cada valor do target
    # Dica: print(df[coluna_target].value_counts())
    print()
    print("CONTAGEM DOS CLIENTES QUE RESPONDERAM À CAMPANHA")
    print()
    print(df['respondeu_campanha'].value_counts())
    print()

    
    
    # TODO 6: Mostre a proporção (percentual) de cada valor
    # Dica: print(df[coluna_target].value_counts(normalize=True))
    print("PROPORÇÃO DOS CLIENTES QUE RESPONDERAM À CAMPANHA (%):")
    print(df['respondeu_campanha'].value_counts(normalize=True))
    print()
    
    print("-" * 30)


# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
