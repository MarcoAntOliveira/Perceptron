#include  "perceptron.h"
// Inicializa o Perceptron
Perceptron* create_perceptron(int num_inputs, float learning_rate) {
    Perceptron *p = (Perceptron*) malloc(sizeof(Perceptron));
    p->num_inputs = num_inputs;
    p->learning_rate = learning_rate;
    p->bias = 1.0;

    // Aloca e inicializa pesos com valores aleatórios entre -1 e 1
    p->weights = (float*) malloc((num_inputs + 1) * sizeof(float));
    for (int i = 0; i <= num_inputs; i++) {
        p->weights[i] = ((float) rand() / RAND_MAX) * 2.0f - 1.0f;
    }

    return p;
}

// Função de ativação (degrau)
int activate(Perceptron *p, float *inputs) {
    float sum = 0.0;

    for (int i = 0; i < p->num_inputs; i++) {
        sum += inputs[i] * p->weights[i];
    }

    // Adiciona o bias diretamente
    sum += p->bias;

    return (sum > 0) ? 1 : 0;
}


// Treina o perceptron com uma amostra
void train(Perceptron *p, float *inputs,  FILE *log_file, int desired_output, int epoch) {
    int guess = activate(p, inputs);
    int error = desired_output - guess;

    if (error != 0) {
        for (int i = 0; i < p->num_inputs; i++) {
            p->weights[i] += p->learning_rate * error * inputs[i];
        }
        // Atualiza o bias diretamente
        p->bias += p->learning_rate * error;
    }
   fprintf(log_file, "%d,%d\n", epoch, error);
}

void evaluate(Perceptron *p, const char *test_path) {
    FILE *test_file = fopen(test_path, "r");
    if (!test_file) {
        perror("Erro ao abrir base de teste");
        return;
    }

    char line[1024];
    int correct = 0, total = 0;

    // Ignora o cabeçalho
    fgets(line, sizeof(line), test_file);

    while (fgets(line, sizeof(line), test_file)) {
        float inputs[4];
        int label;

        if (sscanf(line, "%f,%f,%f,%f,%d",
                   &inputs[0], &inputs[1], &inputs[2], &inputs[3], &label) == 5) {
            int prediction = activate(p, inputs);
            if (prediction == label)
                correct++;
            total++;
        }
    }

    fclose(test_file);

    float accuracy = 100.0f * correct / total;
    printf("Acurácia no teste: %.2f%% (%d corretos de %d)\n", accuracy, correct, total);
}


// Libera a memória do perceptron
void destroy_perceptron(Perceptron *p) {
    free(p->weights);
    free(p);
}





