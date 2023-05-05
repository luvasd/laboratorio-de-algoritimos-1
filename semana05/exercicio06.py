# inicializa o contador de pessoas com idade maior ou igual a 18 anos
contador = 0

# coleta as idades das dez pessoas
for i in range(10):
    idade = int(input(f"Informe a idade da pessoa {i+1}: "))

    # verifica se a pessoa tem idade maior ou igual a 18 anos
    if idade >= 18:
        contador += 1

# exibe o resultado na tela
print(f"Existem {contador} pessoas com idade maior ou igual a 18 anos.")
