dentro = 0

fora = 0

for nu1 in range(10):
    
    nu1 = int(input("Digite um numero: " ))
    
    if nu1 >= 10 and nu1 <= 20:
        dentro += 1

    else:    
        fora += 1

print("Quantidade de numeros do intervalo de 10 e 20 são: ", dentro)
print("Quantidade de numeros fora do intervalo de 10 e 20:", fora)


