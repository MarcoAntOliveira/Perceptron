#include "perceptron.h"

int main() {
  srand(time(NULL)); // Para aleatoriedade

  Perceptron *p = create_perceptron(2, 0.01f);

  // Exemplo: Treinando para saída 1 com entrada [1.0, 0.0]
  float input[2] = {1.0, 0.0};
  train(p, input, 1);

  int result = activate(p, input);
  printf("Resultado: %d\n", result);

  destroy_perceptron(p);
  return 0;
}
