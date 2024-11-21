"""Dada uma lista de palavras, escreva um programa que solicite ao usuário uma lista de frutas e mostre:

- a lista original
- a lista ordenada
- a lista na ordem inversa
Caso o usuário digite sair, pare de solicitar dados.
"""

import os
os.system("clear || clls")

lista_frutas = []

print("===solicitando dados===")

while True:
    fruta = input("digite sua fruta: ")
    if fruta.lower() == "sair":
        break
    else:
        lista_frutas.append(fruta)
def ordenada():
    lista_ordenada = sorted(lista_frutas)
    return lista_ordenada


print("ordenando...")

print(lista_ordenada)

print("resultado")

print("lista original")
print(lista_frutas)

print(lista_ordenada)
lista_inversa = sorted(lista_frutas, reverse = True)
print("lista inversa...")
print(lista_inversa)

