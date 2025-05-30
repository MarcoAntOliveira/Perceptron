import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

# Carregar a base Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

df = pd.DataFrame(X, columns=feature_names)
df["label"] = y

# Linearmente separável: apenas as classes 0 e 1 (setosa e versicolor)
linear_df = df[df["label"].isin([0, 1])].reset_index(drop=True)

# Não linearmente separável:apenas as classes 1, 2 (versicolor e virginica)
nonlinear_df = df[df["label"].isin([1, 2])].reset_index(drop=True)

# Função para salvar folds em CSV
def save_kfolds(df, prefix, n_splits=5):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    X = df[feature_names].values
    y = df["label"].values

    for fold_num, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
        train_data = df.iloc[train_idx]
        test_data = df.iloc[test_idx]

        train_path = f"build/data/{prefix}_fold{fold_num}_train.csv"
        test_path = f"build/data/{prefix}_fold{fold_num}_test.csv"

        train_data.to_csv(train_path, index=False)
        test_data.to_csv(test_path, index=False)

# Salvar os conjuntos
save_kfolds(linear_df, "iris_linear")
save_kfolds(nonlinear_df, "iris_nonlinear")

print("Conjuntos 'iris_linear' (classes 0 e 1) e 'iris_nonlinear' (classes 1, 2) salvos em 5 folds cada.")
