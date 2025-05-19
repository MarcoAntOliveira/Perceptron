# from sklearn.model_selection import cross_val_score, StratifiedGroupKFold
# import pandas as pd

# pd.set_option('display.max_columns', 64)
# pd.set_option('display.max_rows', 64)
# arquivo = pd.read_csv('archive5/Data_train_reduced.csv')

# y = arquivo["Instant.Liking"]
# x = arquivo.drop('Instant.Liking', axis = 1)
# kfold = StratifiedGroupKFold(n_splits=5)

# # Passe os grupos no cross_val_score
# resultado = cross_val_score(modelo, x, y, cv=kfold, groups=groups)
# resultado.mean()

import numpy as np
from sklearn.model_selection import KFold
import json

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
kf = KFold(n_splits=2)

folds = []

for i, (train_index, test_index) in enumerate(kf.split(X)):
    fold = {
        "fold": i + 1,
        "train_indices": train_index.tolist(),
        "test_indices": test_index.tolist()
    }
    folds.append(fold)

# Salvar em arquivo JSON
with open("folds.json", "w") as f:
    json.dump(folds, f, indent=4)
