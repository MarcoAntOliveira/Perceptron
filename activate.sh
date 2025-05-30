#!/bin/bash

# Parar se houver qualquer erro
set -e
rm build/data/*.csv

echo "==> Etapa 5: Verificando ambiente virtual 'amb1'"
if [ ! -d "amb1" ]; then
    echo "--> Ambiente 'amb1' não encontrado. Criando ambiente virtual..."
    python3 -m venv amb1
    echo "--> Ambiente 'amb1' criado com sucesso."

    echo "--> instalando os pacotes via pip"
    pip3 install -r requisitos.txt
fi

echo "==> Ativando ambiente virtual 'amb1'"
source amb1/bin/activate

python3 src/cv_linear_separavel.py
echo "==> Etapa 1: Criando/Entrando na pasta build"
mkdir -p build
cd build

echo "==> Etapa 2: Executando CMake"
cmake ..

echo "==> Etapa 3: Compilando com make"
make
./perceptron

echo "==> Etapa 4: Voltando para o diretório raiz"
cd ..


echo "==> Etapa 6: Executando código Python com perceptron"
python3 src/main.py
python3 src/plot.py


echo "==> Execução finalizada com sucesso."

