vetor1 = []
vetor2 = []
for i in range(5):
    v1 = int(input("Digite um numero: " ))
    vetor1.append(v1)
print("#############")
for i in range(5):
    v2 = int(input("Digite um numero"))
    vetor2.append(v2)
vetor3 = []
for i in range(5):
    soma = vetor1[i] + vetor2[i]
    vetor3.append(soma)
print(vetor3)
