import pandas as pd
from sklearn.model_selection import KFold

# Carregar a base XOR (não linearmente separável)
df_xor = pd.read_csv("base_xor.csv")

# Separar X e y
X_xor = df_xor[["x1", "x2"]].values
y_xor = df_xor["label"].values

# Criar KFold com 2 divisões (4 amostras só permitem 2 splits)
kf_xor = KFold(n_splits=5, shuffle=True, random_state=42)

# Gerar os folds e salvar
for fold_num, (train_idx, test_idx) in enumerate(kf_xor.split(X_xor), start=1):
    train_data_xor = df_xor.iloc[train_idx]
    test_data_xor = df_xor.iloc[test_idx]

    # Salvar os folds em CSV
    train_path_xor = f"xor_fold{fold_num}_train.csv"
    test_path_xor = f"xor_fold{fold_num}_test.csv"

    train_data_xor.to_csv(train_path_xor, index=False)
    test_data_xor.to_csv(test_path_xor, index=False)

fold_num  # Último fold da base XOR para verificação
