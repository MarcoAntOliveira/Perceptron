import pandas as pd
import matplotlib.pyplot as plt
import os

# Plotar acurácia de todos os folds
plt.figure(figsize=(10, 6))

for fold in range(1, 6):
    log_path = f"build/data/train_log_fold{fold}.csv"
    df = pd.read_csv(log_path)

    plt.plot(df['epoch'], df['accuracy'], label=f'Fold {fold}')
    # plt.plot(df['epoch'], 1 - df['accuracy'], label=f'Erro - Fold {fold}', linestyle='--')


plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.title('Acurácia por Época - Todos os Folds')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('build/acuracia_treinamento_folds.png')
plt.show()
