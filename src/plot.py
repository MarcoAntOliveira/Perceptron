import pandas as pd
import matplotlib.pyplot as plt
import time

plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        df = pd.read_csv("build/data/train_log_fold1.csv")
        ax.clear()
        ax.plot(df["epoch"], df["bias"], label="Acurácia")
        ax.set_xlabel("Época")
        ax.set_ylabel("Acurácia")
        ax.set_xlim(0,100)
        ax.set_ylim(0, 250)
        ax.set_title("Treinamento do Perceptron")
        ax.legend()
        plt.pause(0.5)
    except Exception as e:
        print("Aguardando dados...", e)
        time.sleep(1)



