import random

# Função de ativação: degrau
def step_function(x):
    return 1 if x >= 0 else 0

# Função para treinar o perceptron
def treinar_perceptron(entradas, saidas_esperadas, taxa_aprendizado, epocas):
    # Inicializa pesos e viés com valores aleatórios pequenos
    pesos = [random.uniform(-1, 1) for _ in range(len(entradas[0]))]
    bias = random.uniform(-1, 1)

    for epoca in range(epocas):
        erro_total = 0
        for i in range(len(entradas)):
            soma = sum([entradas[i][j] * pesos[j] for j in range(len(pesos))]) + bias
            saida_prevista = step_function(soma)
            erro = saidas_esperadas[i] - saida_prevista

            # Atualiza pesos e viés
            for j in range(len(pesos)):
                pesos[j] += taxa_aprendizado * erro * entradas[i][j]
            bias += taxa_aprendizado * erro

            erro_total += abs(erro)

        print(f"Época {epoca+1}: erro total = {erro_total}")
        if erro_total == 0:
            break

    return pesos, bias

# Função para usar o perceptron treinado
def prever(x, pesos, bias):
    soma = sum([x[i] * pesos[i] for i in range(len(pesos))]) + bias
    return step_function(soma)

# Dados de entrada (problema OR)
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
saidas = [0, 1, 1, 1]

# Parâmetros
taxa_aprendizado = 0.1
epocas = 20

# Treina o perceptron
pesos_finais, bias_final = treinar_perceptron(entradas, saidas, taxa_aprendizado, epocas)

# Testa o perceptron treinado
print("\nResultados após o treinamento:")
for entrada in entradas:
    resultado = prever(entrada, pesos_finais, bias_final)
    print(f"Entrada: {entrada} → Saída prevista: {resultado}")
