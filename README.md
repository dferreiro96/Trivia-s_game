# Trivia Game / Juego de Trivia

A Python CLI trivia game with a dictionary of questions and answers. The program asks questions, keeps score, and shows the total at the end.

Un juego de trivia en Python con un diccionario de preguntas y respuestas. El programa hace preguntas, lleva la puntuación y muestra el total al final.

## Features / Funcionalidades

- Dictionary of 10 questions and answers / Diccionario con 10 preguntas y respuestas
- Random question order with `random.shuffle()` / Orden aleatorio de preguntas con `random.shuffle()`
- Validates answers case-insensitively / Valida respuestas sin distinguir mayúsculas/minúsculas
- Keeps track of correct answers / Lleva la cuenta de respuestas correctas
- Shows total score at the end / Muestra la puntuación total al final
- Option to play again / Opción de jugar de nuevo
- Allows early exit with "salir" / Permite salir antes con "salir"

## Requirements / Requisitos

- Python 3

## What I Learned / Lo que Aprendí

- Using dictionaries to store questions and answers / Usar diccionarios para guardar preguntas y respuestas

- Using random.shuffle() to randomize the order / Usar random.shuffle() para aleatorizar el orden

- Using enumerate() to number the questions / Usar enumerate() para numerar las preguntas

- Validating answers with .lower().strip() / Validar respuestas con .lower().strip()

- Tracking score with a counter / Llevar la puntuación con un contador

- Using flags to control loops / Usar banderas para controlar bucles

## Author / Autor

[dferreiro96]

## How to Run / Cómo Ejecutar

```bash
python trivia.py