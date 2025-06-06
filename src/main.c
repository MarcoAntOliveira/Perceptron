#include "perceptron.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define FOLDS 5
#define MAX_LINE 1024
#define MAX_EPOCHS 100

int main() {
    srand(time(NULL));
    float fold_accuracies[FOLDS];

    for (int fold = 1; fold <= FOLDS; fold++) {
        char train_file[100], test_file[100], log_file[100];
        snprintf(train_file, sizeof(train_file), "data/iris_nonlinear_fold%d_train.csv", fold);
        snprintf(test_file, sizeof(test_file), "data/iris_nonlinear_fold%d_test.csv", fold);
        snprintf(log_file, sizeof(log_file), "data/train_log_fold%d.csv", fold);

        FILE *train_file_ptr = fopen(train_file, "r");
        if (!train_file_ptr) {
            perror("Erro ao abrir arquivo de treino");
            return 1;
        }

        FILE *log = fopen(log_file, "w");
        if (!log) {
            perror("Erro ao criar arquivo de log");
            return 1;
        }

        // Cabeçalho corrigido para 7 colunas
        fprintf(log, "epoch,accuracy,bias,w1,w2,w3,w4\n");

        float inputs[1000][4];
        int labels[1000];
        int total = 0;

        char line[MAX_LINE];
        fgets(line, sizeof(line), train_file_ptr); // Pular cabeçalho

        while (fgets(line, sizeof(line), train_file_ptr)) {
            sscanf(line, "%f,%f,%f,%f,%d",
                   &inputs[total][0],
                   &inputs[total][1],
                   &inputs[total][2],
                   &inputs[total][3],
                   &labels[total]);
            printf("Entrada: %.2f %.2f %.2f %.2f | Label: %d\n",
                   inputs[total][0], inputs[total][1], inputs[total][2], inputs[total][3], labels[total]);
            total++;
        }
        fclose(train_file_ptr);

        // Inicializar Perceptron
        Perceptron *p = create_perceptron(4, 0.05f);

        for (int epoch = 1; epoch <= MAX_EPOCHS; epoch++) {
            // Treinamento
            for (int i = 0; i < total; i++) {
                train(p, inputs[i], log, labels[i], epoch);
            }

            // Avaliação no conjunto de treino
            int correct = 0;
            for (int i = 0; i < total; i++) {
                int output = activate(p, inputs[i]);
                if (output == labels[i]) correct++;
            }

            float acc = (float) correct / total;

            // Salva no arquivo de log
          fprintf(log, "%d,%.4f,%.4f,%.4f,%.4f,%.4f,%.4f\n",
        epoch, acc, p->bias,
        p->weights[0], p->weights[1], p->weights[2], p->weights[3]);

        }

        fclose(log);

        // Avaliação no conjunto de teste
        FILE *test = fopen(test_file, "r");
        if (!test) {
            perror("Erro ao abrir arquivo de teste");
            return 1;
        }

        int correct = 0, total_test = 0;
        fgets(line, sizeof(line), test); // Pular cabeçalho

        while (fgets(line, sizeof(line), test)) {
            float x[4];
            int y;
            sscanf(line, "%f,%f,%f,%f,%d", &x[0], &x[1], &x[2], &x[3], &y);
            int pred = activate(p, x);
            if (pred == y) correct++;
            total_test++;
        }
        fclose(test);

        float test_acc = (float) correct / total_test;
        printf("Fold %d - Acurácia de teste: %.2f%%\n", fold, test_acc * 100);
        fold_accuracies[fold - 1] = test_acc;

        destroy_perceptron(p);
    }

    // Média dos folds
    float avg_acc = 0.0f;
    for (int i = 0; i < FOLDS; i++) {
        avg_acc += fold_accuracies[i];
    }
    avg_acc /= FOLDS;
    printf("\nAcurácia média dos 5 folds: %.2f%%\n", avg_acc * 100);

    return 0;
}
