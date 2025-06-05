import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

# Carrega o dataset Iris do sklearn
iris = datasets.load_iris()
X = iris.data  # características (comprimento e largura das pétalas e sépalas)
y = iris.target  # rótulos (0 = setosa, 1 = versicolor, 2 = virginica)
feature_names = iris.feature_names
target_names = iris.target_names

# Criação do DataFrame para facilitar manipulação
df = pd.DataFrame(X, columns=feature_names)
df["label"] = y

# Criação de subconjunto linearmente separável (classes 0 e 1)
linear_df = df[df["label"].isin([0, 1])].reset_index(drop=True)

# Criação de subconjunto não linearmente separável (classes 1 e 2)
nonlinear_df = df[df["label"].isin([1, 2])].reset_index(drop=True)

# Função para salvar os folds de treino e teste como CSVs
def save_kfolds(df, prefix, n_splits=5):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    X = df[feature_names].values
    y = df["label"].values

    for fold_num, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
        train_data = df.iloc[train_idx]
        test_data = df.iloc[test_idx]

        # Salva arquivos de treino e teste
        train_path = f"build/data/{prefix}_fold{fold_num}_train.csv"
        test_path = f"build/data/{prefix}_fold{fold_num}_test.csv"
        train_data.to_csv(train_path, index=False)
        test_data.to_csv(test_path, index=False)

# Gera os folds para os dois conjuntos (linear e não-linear)
save_kfolds(linear_df, "iris_linear")
save_kfolds(nonlinear_df, "iris_nonlinear")

print("Conjuntos 'iris_linear' (classes 0 e 1) e 'iris_nonlinear' (classes 1, 2) salvos em 5 folds cada.")
