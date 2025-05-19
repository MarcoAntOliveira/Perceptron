import numpy as np
import pandas as pd
import os

# Diretório para salvar os arquivos
output_dir = "data"

# 1. Gerar base linearmente separável
np.random.seed(0)
class0 = np.random.randn(50, 2) * 0.5 + np.array([1, 1])
class1 = np.random.randn(50, 2) * 0.5 + np.array([4, 4])
X_linear = np.vstack((class0, class1))
y_linear = np.array([0]*50 + [1]*50).reshape(-1, 1)
data_linear = np.hstack((X_linear, y_linear))

# 2. Base XOR (não linearmente separável)
X_xor = np.array([[0,0],[0,1],[1,0],[1,1]])
y_xor = np.array([0,1,1,0]).reshape(-1, 1)
data_xor = np.hstack((X_xor, y_xor))


pd.DataFrame(data_linear, columns=["x1", "x2", "label"]).to_csv( "base_linear_separavel.csv", index=False)
pd.DataFrame(data_xor, columns=["x1", "x2", "label"]).to_csv( "base_xor.csv", index=False)


