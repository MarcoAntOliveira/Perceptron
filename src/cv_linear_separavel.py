import pandas as pd
from sklearn.model_selection import KFold

# Carregar a base de dados linearmente separável
df = pd.read_csv("data/base_linear_separavel.csv")

# Separar X e y
X = df[["x1", "x2"]].values
y = df["label"].values

# Criar KFold com 5 divisões
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Criar lista para armazenar os dados de cada fold
folds_data = []

# Gerar os folds e armazenar os dados de treino/teste
for fold_num, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
    train_data = df.iloc[train_idx]
    test_data = df.iloc[test_idx]

    # Salvar cada fold em CSV
    train_path = f"data/fold{fold_num}_train.csv"
    test_path = f"data/fold{fold_num}_test.csv"

    train_data.to_csv(train_path, index=False)
    test_data.to_csv(test_path, index=False)

fold_num  # Último número de fold para verificação
