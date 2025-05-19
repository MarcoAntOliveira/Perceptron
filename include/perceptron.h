#ifndef perceptron_h
#define perceptron_h


#include <stdio.h>
#include <stdlib.h>
#include <time.h>


//struct para guardar as caracteristicas da rede
typedef struct {
  int num_inputs;
  float *weights;
  float learning_rate;
  float bias;
} Perceptron;

// Inicializa o Perceptron
Perceptron* create_perceptron(int num_inputs, float learning_rate);

// Função de ativação (degrau)
int activate(Perceptron *p, float *inputs);


// Treina o perceptron com uma amostra
void train(Perceptron *p, float *inputs, int desired_output);

// Libera a memória do perceptron
void destroy_perceptron(Perceptron *p);

#endif
