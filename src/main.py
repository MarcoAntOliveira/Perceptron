import pandas as pd
import matplotlib.pyplot as plt

log = pd.read_csv("build/data/train_log_fold1.csv")  # ou qualquer fold

plt.figure(figsize=(10,6))
plt.plot(log['epoch'], log['w1'], label='w1')
plt.plot(log['epoch'], log['w2'], label='w2')
plt.plot(log['epoch'], log['w3'], label='w3')
plt.plot(log['epoch'], log['w4'], label='w4')
plt.plot(log['epoch'], log['bias'], label='bias', linestyle='--')

plt.xlabel('Época')
plt.ylabel('Valor')
plt.title('Evolução dos pesos e bias ao longo do tempo')
plt.legend()
plt.grid()
plt.show()
