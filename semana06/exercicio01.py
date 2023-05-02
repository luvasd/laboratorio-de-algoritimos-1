zeros = 0
pares = 0
impares = 0

for i in range(10):
    n1 = int(input("Digite um numero: " ))

    if n1 % 2 == 0 and n1 != 0:
        pares += 1

    elif n1 % 2 == 1:
        impares += 1

    elif n1 == 0:
        zeros += 1

print("quantidade de numeros pares são:", pares)
print("quantidade de numeros Impares são:",impares)
print("quantidade de zeros digiteados são:",zeros)
