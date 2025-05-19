#include "perceptron.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    FILE *file = fopen("../include/data/base_xor.csv", "r");
    if (!file) {
        fprintf(stderr, "Cannot open file base_xor.csv\n");
        return 1;
    }

    char line[1024];  // Suporte para linhas de até 1023 caracteres
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);  // Imprime a linha (inclui o \n se houver)
    }

    fclose(file);

  srand(time(NULL)); // Para aleatoriedade

  Perceptron *p = create_perceptron(2, 0.01f);

  // Exemplo: Treinando para saída 1 com entrada [1.0, 0.0]
  float input[6] = {1.0, 0.0, 2.0, 3.0, 6.0, 9.5};
  train(p, input, 1);

  int result = activate(p, input);
  printf("Resultado: %d\n", result);

  destroy_perceptron(p);
  return 0;
}
