cmake_minimum_required(VERSION 3.10)
project(perceptron_project C)

set(CMAKE_C_STANDARD 99)

add_executable(perceptron
    src/main.c
    src/perceptron.c
)

target_include_directories(perceptron PRIVATE include)
