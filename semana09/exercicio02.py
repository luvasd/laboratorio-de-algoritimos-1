def lerValores(vetor):
    for valorr in range(10):
        valorr = int(input("Digite valores distintos: " ))
        vetor.append(valorr)
    return vetor
        

def mostrarValores(vetor):
    i = 1
    while (i < len(vetor)):
        print(vetor[i])
        i += 2

def main():
    vetor = []
    vetor = lerValores(vetor)
    mostrarValores(vetor)

main()
