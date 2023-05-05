# inicializa o contador de números entre 30 e 90
contador = 0

# coleta os dez números
for i in range(10):
    numero = int(input(f"Informe o número {i+1}: "))

    # verifica se o número está entre 30 e 90
    if numero >= 30 and numero <= 90:
        contador += 1

# exibe o resultado na tela
print(f"Existem {contador} números entre 30 e 90.")
