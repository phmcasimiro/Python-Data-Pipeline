"""
Pipeline - Etapa 3: Treinar Modelo
"""

import time
from xml.parsers.expat import model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def preparar_dados(df, coluna_target='respondeu_campanha'):
    """
    Separa features (X) e target (y).
    
    Args:
        df: DataFrame completo
        coluna_target: nome da coluna target
        
    Returns:
        X (features), y (target)
    """
    
    # TODO 1: Crie X removendo a coluna target e cliente_id do DataFrame
    # Dica: X = df.drop(columns=[coluna_target, 'cliente_id'])
    
    # TODO 2: Crie y extraindo apenas a coluna target
    # Dica: y = df[coluna_target]
    
    X = df.drop(columns=['respondeu_campanha', 'cliente_id'])
    y = df['respondeu_campanha']
    
    print("=" * 50)
    print("CONFERIR FEATURES E TARGET")
    print("=" * 50)
    
    print(f"Features (X): {X.shape[0]} linhas x {X.shape[1]} colunas")
    # shape[0] = número de linhas, shape[1] = número de colunas
    print(f"Target (y): {y.shape[0]} valores")
    print()
    
    print("Primeiras linhas de X:")
    print(X.head()) # head() = mostra primeiras 5 linhas
    print()

    print("Primeiros valores de y:")
    print(y.head())
    print()
    
    return X, y


def dividir_treino_teste(X, y, tamanho_teste=0.2, random_state=42):
    """
    Divide os dados em treino e teste.
    
    Args:
        X: features
        y: target
        tamanho_teste: proporção para teste (0.2 = 20%)
        random_state: semente para reprodutibilidade
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    
    # TODO 3: Use train_test_split para dividir os dados
    # Dica: X_train, X_test, y_train, y_test = train_test_split(
    #           X, y, test_size=tamanho_teste, random_state=random_state
    #       )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=tamanho_teste, random_state=random_state
    )    
    
    # Mostrar tamanhos
    if X_train is not None:
        print(f"Dados de treino: {len(X_train)} registros")
        print(f"Dados de teste: {len(X_test)} registros")
    
    return X_train, X_test, y_train, y_test


def treinar_modelo(X_train, y_train):
    """
    Criar e treina um RandomForestClassifier.
    
    Args:
        X_train: features de treino
        y_train: target de treino
        
    Returns:
        Modelo treinado
    """
    
    print("Criando e Treinando modelo...")
    
    # TODO 4: Crie e treine o modelo RandomForestClassifier
    # Passo 1: Criar o modelo
    # Dica: modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    
    modelo = RandomForestClassifier(
    n_estimators=100,  # número de árvores de decisão no ensemble
    random_state=42,   # semente para reprodutibilidade (sempre mesmo resultado)
    max_depth=10       # profundidade máxima de cada árvore (evita overfitting)
                                )
    print(modelo) # imprime os parâmetros configurados do modelo
    print()
    
    # Passo 2: Treinar o modelo (se foi criado)
    # Dica: modelo.fit(X_train, y_train)
    
    if modelo is not None:
    # TODO 5: Treine o modelo usando .fit()
        inicio = time.time() # time.time() = retorna timestamp atual em segundos
        modelo.fit(X_train, y_train) # fit() = treina o modelo usando X (features) e y (target)
        fim = time.time()
        print(f"✅ Treinamento concluído em {fim - inicio:.2f} segundos!") # calcula tempo decorrido e formata com 2 casas decimais
        print()
    
    return modelo


def salvar_modelo(modelo, caminho='models/modelo_campanha.pkl'):
    """
    Salva o modelo treinado em disco.
    
    Args:
        modelo: modelo treinado
        caminho: onde salvar
    """
    joblib.dump(modelo, caminho)
    print(f"Modelo salvo em: {caminho}")


# Teste local
if __name__ == "__main__":
    # Carregar dados
    df = pd.read_csv("data/clientes_campanha.csv")
    
    # Preparar
    X, y = preparar_dados(df)
    
    if X is None or y is None:
        print("ERRO: Complete os TODOs 1 e 2!")
    else:
        # Dividir
        X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)
        
        if X_train is None:
            print("ERRO: Complete o TODO 3!")
        else:
            # Treinar
            modelo = treinar_modelo(X_train, y_train)
            
            if modelo is None:
                print("ERRO: Complete os TODOs 4 e 5!")
            else:
                salvar_modelo(modelo)
